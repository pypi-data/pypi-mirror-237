// Copyright 2020-2023 Andrew D. Straw.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// http://www.apache.org/licenses/LICENSE-2.0> or the MIT license <LICENSE-MIT
// or http://opensource.org/licenses/MIT>, at your option. This file may not be
// copied, modified, or distributed except according to those terms.

use std::fmt::{Debug, Formatter};

use crate::*;

use chrono::Utc;

pub trait Source {}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Triggerbox;
impl Source for Triggerbox {}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct HostClock;
impl Source for HostClock {}

/// A type that represents a timestamp but is serialized to an f64.
// TODO: rename from 'Local' because actually the f64 stamp is UTC.
#[derive(Clone, PartialEq, Eq)]
pub struct FlydraFloatTimestampLocal<S> {
    value_f64: NotNan<f64>,
    source: std::marker::PhantomData<S>,
}

impl<S> Debug for FlydraFloatTimestampLocal<S> {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::result::Result<(), std::fmt::Error> {
        let dt: chrono::DateTime<Utc> = self.into();
        write!(f, "FlydraFloatTimestampLocal {{ {dt:?} }}")
    }
}

impl<S, TZ: chrono::TimeZone> From<&chrono::DateTime<TZ>> for FlydraFloatTimestampLocal<S> {
    fn from(orig: &chrono::DateTime<TZ>) -> Self {
        FlydraFloatTimestampLocal::from_dt(orig)
    }
}

impl<S, TZ: chrono::TimeZone> From<chrono::DateTime<TZ>> for FlydraFloatTimestampLocal<S> {
    fn from(val: chrono::DateTime<TZ>) -> FlydraFloatTimestampLocal<S> {
        FlydraFloatTimestampLocal::from_dt(&val)
    }
}

impl<'a, S> From<&'a FlydraFloatTimestampLocal<S>> for chrono::DateTime<Utc> {
    fn from(orig: &'a FlydraFloatTimestampLocal<S>) -> chrono::DateTime<Utc> {
        datetime_conversion::f64_to_datetime(orig.value_f64.into_inner())
    }
}

impl<S> From<FlydraFloatTimestampLocal<S>> for chrono::DateTime<Utc> {
    fn from(orig: FlydraFloatTimestampLocal<S>) -> chrono::DateTime<Utc> {
        datetime_conversion::f64_to_datetime(orig.value_f64.into_inner())
    }
}

assert_impl_all!(FlydraFloatTimestampLocal<Triggerbox>: PartialEq);

impl<S> FlydraFloatTimestampLocal<S> {
    pub fn from_dt<TZ: chrono::TimeZone>(dt: &chrono::DateTime<TZ>) -> Self {
        let value_f64 = datetime_conversion::datetime_to_f64(dt);
        let value_f64 = value_f64.try_into().unwrap();
        let source = std::marker::PhantomData;
        Self { value_f64, source }
    }

    pub fn from_f64(value_f64: f64) -> Self {
        assert!(
            !value_f64.is_nan(),
            "cannot convert NaN to FlydraFloatTimestampLocal"
        );
        Self::from_notnan_f64(value_f64.try_into().unwrap())
    }

    pub fn from_notnan_f64(value_f64: NotNan<f64>) -> Self {
        let source = std::marker::PhantomData;
        Self { value_f64, source }
    }

    #[inline(always)]
    pub fn as_f64(&self) -> f64 {
        self.value_f64.into()
    }
}

/// Compute the trigger time for a particular frame.
///
/// Requires both a clock model (general for all cameras) and a frame offset
/// (which maps the particular frame numbers for a given camera into a
/// synchronized frame number).
#[inline]
pub fn get_start_ts(
    clock_model: Option<&ClockModel>,
    frame_offset: Option<u64>,
    frame: usize,
) -> Option<FlydraFloatTimestampLocal<Triggerbox>> {
    let frame: u64 = frame.try_into().unwrap();
    if let Some(frame_offset) = frame_offset {
        if let Some(cm) = clock_model {
            let ts: f64 = ((frame - frame_offset) as f64) * cm.gain + cm.offset;
            let ts = FlydraFloatTimestampLocal::<Triggerbox>::from_f64(ts);
            return Some(ts);
        }
    }
    None
}

#[test]
#[should_panic]
fn test_nan_handling() {
    let _ts = FlydraFloatTimestampLocal::<Triggerbox>::from_f64(std::f64::NAN);
}

/// Ensure that conversion with particular floating point representation remains
/// fixed. This is important for backwards compatibility of saved data.
#[test]
fn ensure_conversion() {
    use chrono::{DateTime, Utc};
    let t1 = DateTime::<Utc>::from_naive_utc_and_offset(
        chrono::NaiveDateTime::from_timestamp_opt(60, 123_456_789).unwrap(),
        Utc,
    );
    let t2 = FlydraFloatTimestampLocal::<HostClock>::from(t1);
    let t3 = t2.value_f64.into_inner();
    assert!((t3 - 60.123456789).abs() < 1e-10);
}
