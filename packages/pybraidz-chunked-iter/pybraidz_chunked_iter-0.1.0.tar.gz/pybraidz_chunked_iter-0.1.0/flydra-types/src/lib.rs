// Copyright 2020-2023 Andrew D. Straw.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// http://www.apache.org/licenses/LICENSE-2.0> or the MIT license <LICENSE-MIT
// or http://opensource.org/licenses/MIT>, at your option. This file may not be
// copied, modified, or distributed except according to those terms.

#[macro_use]
extern crate bitflags;
#[macro_use]
extern crate static_assertions;

use ordered_float::NotNan;
use rust_cam_bui_types::{ClockModel, RecordingPath};

use serde::{Deserialize, Deserializer, Serialize};

use bui_backend_types::AccessToken;
use withkey::WithKey;

pub const DEFAULT_MODEL_SERVER_ADDR: &str = "0.0.0.0:8397";

// These are the filenames saved during recording. --------------------
//
// Any changes to these names, including additions and removes, should update
// BraidMetadataSchemaTag.
pub const BRAID_SCHEMA: u16 = 3; // BraidMetadataSchemaTag

// CSV files. (These may also exist as .csv.gz)
pub const KALMAN_ESTIMATES_CSV_FNAME: &str = "kalman_estimates.csv";
pub const DATA_ASSOCIATE_CSV_FNAME: &str = "data_association.csv";
pub const DATA2D_DISTORTED_CSV_FNAME: &str = "data2d_distorted.csv";
pub const CAM_INFO_CSV_FNAME: &str = "cam_info.csv";
pub const TRIGGER_CLOCK_INFO_CSV_FNAME: &str = "trigger_clock_info.csv";
pub const EXPERIMENT_INFO_CSV_FNAME: &str = "experiment_info.csv";
pub const TEXTLOG_CSV_FNAME: &str = "textlog.csv";

// Other files
pub const CALIBRATION_XML_FNAME: &str = "calibration.xml";
pub const BRAID_METADATA_YML_FNAME: &str = "braid_metadata.yml";
pub const README_MD_FNAME: &str = "README.md";
pub const IMAGES_DIRNAME: &str = "images";
pub const CAM_SETTINGS_DIRNAME: &str = "cam_settings";
pub const FEATURE_DETECT_SETTINGS_DIRNAME: &str = "feature_detect_settings";
pub const RECONSTRUCT_LATENCY_HLOG_FNAME: &str = "reconstruct_latency_usec.hlog";
pub const REPROJECTION_DIST_HLOG_FNAME: &str = "reprojection_distance_100x_pixels.hlog";

// Ideas for future:
//
// Make tracking model and parameters "pluggable" so that other models - with
// different structure - can be easily used.
//
// **statistics cache for data2d_distorted** We could keep a statistics cache as
// we write a braidz file for things like num found points, average and maximum
// values etc. This could be periodically flushed to disk and recomputed anytime
// but would eliminate most needs to iterate over the entire dataset at read
// time.
//
// **statistics cache for kalman_estimates** Same as above but 3D.
//
// Cache the camera pixel sizes. Currently this can be found if images are saved
// or if the a camera calibration is present. The images in theory are always
// there but this is not currently implemented in the strand-cam "flydratrax"
// mode. Even when that is fixed, to simply read the image size that way will
// require parsing an entire image parser.
//
// Replace `TrackingParams.initial_position_std_meters` and
// `TrackingParams.initial_vel_std_meters_per_sec` with a scaled version of the
// process covariance matrix Q. According to this ([p.
// 18](https://www.robots.ox.ac.uk/~ian/Teaching/Estimation/LectureNotes2.pdf)),
// this approach is common with a scale factor of 10.
// --------------------------------------------------------------------

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct CamInfoRow {
    // changes to this should update BraidMetadataSchemaTag
    pub camn: CamNum,
    pub cam_id: String,
    // pub hostname: String,
}

#[allow(non_snake_case)]
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct KalmanEstimatesRow {
    // changes to this struct should update BraidMetadataSchemaTag
    pub obj_id: u32,
    pub frame: SyncFno,
    /// The timestamp when the trigger pulse fired.
    ///
    /// Note that calculating this live in braid requires that the clock model
    /// has established itself. Thus, the initial frames immediately after
    /// synchronization will not have a timestamp.
    #[serde(with = "crate::timestamp_opt_f64")]
    pub timestamp: Option<FlydraFloatTimestampLocal<Triggerbox>>,
    pub x: f64,
    pub y: f64,
    pub z: f64,
    pub xvel: f64,
    pub yvel: f64,
    pub zvel: f64,
    pub P00: f64,
    pub P01: f64,
    pub P02: f64,
    pub P11: f64,
    pub P12: f64,
    pub P22: f64,
    pub P33: f64,
    pub P44: f64,
    pub P55: f64,
}
impl WithKey<SyncFno> for KalmanEstimatesRow {
    fn key(&self) -> SyncFno {
        self.frame
    }
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub struct FlydraRawUdpPoint {
    pub x0_abs: f64,
    pub y0_abs: f64,
    pub area: f64,
    pub maybe_slope_eccentricty: Option<(f64, f64)>,
    pub cur_val: u8,
    pub mean_val: f64,
    pub sumsqf_val: f64,
}

/// The original camera name from the driver.
#[derive(Debug, PartialEq, Clone, Serialize, Deserialize, Eq, PartialOrd, Ord)]
pub struct RawCamName(String);

impl RawCamName {
    pub fn new(s: String) -> Self {
        RawCamName(s)
    }
    pub fn to_ros(&self) -> RosCamName {
        let ros_name: String = self.0.replace('-', "_");
        let ros_name: String = ros_name.replace(' ', "_");
        RosCamName::new(ros_name)
    }
    pub fn as_str(&self) -> &str {
        &self.0
    }
}

/// Name that works as a ROS node name (i.e. no '-' or ' ' chars).
#[derive(Debug, PartialEq, Clone, Serialize, Deserialize, Eq, PartialOrd, Ord)]
pub struct RosCamName(String);

impl RosCamName {
    pub fn new(s: String) -> Self {
        RosCamName(s)
    }
    pub fn as_str(&self) -> &str {
        &self.0
    }
}

impl std::fmt::Display for RosCamName {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> Result<(), std::fmt::Error> {
        write!(f, "{}", self.0)
    }
}

pub const REMOTE_CAMERA_INFO_PATH: &str = "remote_camera_info/";

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub enum StartSoftwareFrameRateLimit {
    /// Set the frame_rate limit at a given frame rate.
    Enable(f64),
    /// Disable the frame_rate limit.
    Disabled,
    /// Do not change the frame rate limit.
    NoChange,
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub struct RemoteCameraInfoResponse {
    pub camdata_addr: String,
    pub config: BraidCameraConfig,
    pub force_camera_sync_mode: bool,
    pub software_limit_framerate: StartSoftwareFrameRateLimit,
}

pub const DEFAULT_ACQUISITION_DURATION_ALLOWED_IMPRECISION_MSEC: Option<f64> = Some(5.0);

fn return_false() -> bool {
    false
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
#[serde(deny_unknown_fields)]
pub struct BraidCameraConfig {
    /// The name of the camera (e.g. "Basler-22005677")
    pub name: String,
    /// Filename of vendor-specific camera settings file.
    pub camera_settings_filename: Option<std::path::PathBuf>,
    /// The pixel format to use.
    pub pixel_format: Option<String>,
    /// Configuration for detecting points.
    #[serde(default = "flydra_pt_detect_cfg::default_absdiff")]
    pub point_detection_config: flydra_feature_detector_types::ImPtDetectCfg,
    /// Whether to raise the priority of the grab thread.
    #[serde(default = "return_false")]
    pub raise_grab_thread_priority: bool,
    /// Which backend to use. Currently supported: "pylon"
    #[serde(default)]
    pub start_backend: StartCameraBackend,
    pub acquisition_duration_allowed_imprecision_msec: Option<f64>,
}

#[derive(Deserialize, Serialize, Debug, Clone, PartialEq, Eq)]
#[serde(rename_all = "lowercase")]
pub enum StartCameraBackend {
    /// Do not start a camera locally. Rather, wait for a remote camera to connect.
    Remote,
    /// Start a Pylon camera locally using `strand-cam-pylon` program.
    Pylon,
    /// Start a Vimba camera locally using `strand-cam-vimba` program.
    Vimba,
}

impl Default for StartCameraBackend {
    fn default() -> StartCameraBackend {
        StartCameraBackend::Pylon
    }
}

impl StartCameraBackend {
    pub fn strand_cam_exe_name(&self) -> Option<&str> {
        match self {
            StartCameraBackend::Remote => None,
            StartCameraBackend::Pylon => Some("strand-cam-pylon"),
            StartCameraBackend::Vimba => Some("strand-cam-vimba"),
        }
    }
}

impl BraidCameraConfig {
    pub fn default_absdiff_config(name: String) -> Self {
        Self {
            name,
            camera_settings_filename: None,
            pixel_format: None,
            point_detection_config: flydra_pt_detect_cfg::default_absdiff(),
            raise_grab_thread_priority: false,
            start_backend: Default::default(),
            acquisition_duration_allowed_imprecision_msec:
                DEFAULT_ACQUISITION_DURATION_ALLOWED_IMPRECISION_MSEC,
        }
    }
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub struct PerCamSaveData {
    pub current_image_png: PngImageData,
    pub cam_settings_data: Option<UpdateCamSettings>,
    pub feature_detect_settings: Option<UpdateFeatureDetectSettings>,
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub struct RegisterNewCamera {
    /// The name of the camera as returned by the camera
    pub orig_cam_name: RawCamName,
    /// The name of the camera used in ROS (e.g. with '-' converted to '_').
    pub ros_cam_name: RosCamName,
    /// Location of the camera control HTTP server.
    pub http_camserver_info: Option<CamHttpServerInfo>,
    /// The camera settings.
    pub cam_settings_data: Option<UpdateCamSettings>,
    /// The current image.
    pub current_image_png: PngImageData,
}

#[derive(Debug, PartialEq, Eq, Clone, Serialize, Deserialize)]
pub struct UpdateImage {
    /// The current image.
    pub current_image_png: PngImageData,
}

#[derive(PartialEq, Eq, Clone, Serialize, Deserialize)]
pub struct PngImageData {
    pub data: Vec<u8>,
}

impl From<Vec<u8>> for PngImageData {
    fn from(data: Vec<u8>) -> Self {
        Self { data }
    }
}

impl PngImageData {
    pub fn as_slice(&self) -> &[u8] {
        self.data.as_slice()
    }
}

impl std::fmt::Debug for PngImageData {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "PngImageData{{..}}",)
    }
}

#[derive(Debug, PartialEq, Eq, Clone, Serialize, Deserialize)]
pub struct UpdateCamSettings {
    /// The current camera settings
    pub current_cam_settings_buf: String,
    /// The filename extension for the camera settings
    pub current_cam_settings_extension: String,
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub struct UpdateFeatureDetectSettings {
    /// The current feature detection settings.
    pub current_feature_detect_settings: flydra_feature_detector_types::ImPtDetectCfg,
}

#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
pub enum ConnectedCameraSyncState {
    /// No known reference to other cameras
    Unsynchronized,
    /// This `u64` is frame0, the offset to go from camera frame to sync frame.
    Synchronized(u64),
}

impl ConnectedCameraSyncState {
    pub fn is_synchronized(&self) -> bool {
        match self {
            ConnectedCameraSyncState::Unsynchronized => false,
            ConnectedCameraSyncState::Synchronized(_) => true,
        }
    }
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub struct HttpApiShared {
    pub fake_sync: bool,
    pub clock_model_copy: Option<ClockModel>,
    pub csv_tables_dirname: Option<RecordingPath>,
    // This is "fake" because it only signals if each of the connected computers
    // is recording MKVs.
    pub fake_mp4_recording_path: Option<RecordingPath>,
    pub post_trigger_buffer_size: usize,
    pub calibration_filename: Option<String>,
    pub connected_cameras: Vec<CamInfo>, // TODO: make this a BTreeMap?
    pub model_server_addr: Option<std::net::SocketAddr>,
    pub flydra_app_name: String,
    pub all_expected_cameras_are_synced: bool,
}

#[derive(Debug, PartialEq, Eq, Clone, Serialize, Deserialize, Default)]
pub struct RecentStats {
    pub total_frames_collected: usize,
    pub frames_collected: usize,
    pub points_detected: usize,
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub enum CamHttpServerInfo {
    /// No server is present (e.g. prerecorded data).
    NoServer,
    /// A server is available.
    Server(BuiServerInfo),
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub struct BuiServerInfo {
    /// The address of the camera control HTTP server.
    addr: std::net::SocketAddr,
    /// The token for initial connection to the camera control HTTP server.
    token: AccessToken,
    resolved_addr: String,
}

impl BuiServerInfo {
    #[cfg(feature = "with-dns")]
    pub fn new(addr: std::net::SocketAddr, token: AccessToken) -> Self {
        let resolved_addr = if addr.ip().is_unspecified() {
            format!("{}:{}", dns_lookup::get_hostname().unwrap(), addr.port())
        } else {
            format!("{}", addr)
        };
        Self {
            addr,
            token,
            resolved_addr,
        }
    }

    #[cfg(feature = "with-dns")]
    pub fn parse_url_with_token(url: &str) -> Result<Self, FlydraTypesError> {
        let stripped = url
            .strip_prefix("http://")
            .ok_or(FlydraTypesError::UrlParseError)?;
        let first_slash = stripped.find('/');
        let (addr_str, token) = if let Some(slash_idx) = first_slash {
            let path = &stripped[slash_idx..];
            if path.len() == 1 {
                (&stripped[..slash_idx], AccessToken::NoToken)
            } else {
                let token_str = path[1..]
                    .strip_prefix("?token=")
                    .ok_or(FlydraTypesError::UrlParseError)?;
                (
                    &stripped[..slash_idx],
                    AccessToken::PreSharedToken(token_str.to_string()),
                )
            }
        } else {
            (stripped, AccessToken::NoToken)
        };
        let addr = std::net::ToSocketAddrs::to_socket_addrs(addr_str)?
            .next()
            .ok_or(FlydraTypesError::UrlParseError)?;
        Ok(Self::new(addr, token))
    }

    pub fn guess_base_url_with_token(&self) -> String {
        match self.token {
            AccessToken::NoToken => format!("http://{}/", self.resolved_addr),
            AccessToken::PreSharedToken(ref tok) => {
                format!("http://{}/?token={}", self.resolved_addr, tok)
            }
        }
    }

    pub fn base_url(&self) -> String {
        format!("http://{}", self.addr)
    }

    pub fn token(&self) -> &AccessToken {
        &self.token
    }
}

#[cfg(feature = "with-dns")]
#[test]
fn test_bui_server_info() {
    for addr_str in &[
        "127.0.0.1:1234",
        // Ideally, we would also test unspecified addresses here.
        // "0.0.0.0:222"
    ] {
        let addr1 = std::net::ToSocketAddrs::to_socket_addrs(addr_str)
            .unwrap()
            .next()
            .unwrap();
        let bsi1 = BuiServerInfo::new(addr1, AccessToken::PreSharedToken("token1".into()));

        let url1 = bsi1.guess_base_url_with_token();
        let test1 = BuiServerInfo::parse_url_with_token(&url1).unwrap();
        let url2 = test1.guess_base_url_with_token();
        assert_eq!(url1, url2);
    }
}

#[derive(Debug, Serialize, Deserialize)]
pub struct TextlogRow {
    // changes to this struct should update BraidMetadataSchemaTag
    pub mainbrain_timestamp: f64,
    pub cam_id: String,
    pub host_timestamp: f64,
    pub message: String,
}

/// Tracking parameters
///
/// The terminology used is as defined at [the Wikipedia page on the Kalman
/// filter](https://en.wikipedia.org/wiki/Kalman_filter).
///
/// The state estimated is a six component vector with position and velocity
/// **x** = \<x, y, z, x', y', z'\>. The motion model is a constant velocity
/// model with noise term, (see
/// [description](https://webee.technion.ac.il/people/shimkin/Estimation09/ch8_target.pdf)).
///
/// The state covariance matrix **P** is initialized with the value (α is
/// defined in the field [TrackingParams::initial_position_std_meters] and β is
/// defined in the field [TrackingParams::initial_vel_std_meters_per_sec]:<br/>
/// **P**<sub>initial</sub> = [[α<sup>2</sup>, 0, 0, 0, 0, 0],<br/>
/// [0, α<sup>2</sup>, 0, 0, 0, 0],<br/>
/// [0, 0, α<sup>2</sup>, 0, 0, 0],<br/>
/// [0, 0, 0, β<sup>2</sup>, 0, 0],<br/>
/// [0, 0, 0, 0, β<sup>2</sup>, 0],<br/>
/// [0, 0, 0, 0, 0, β<sup>2</sup>]]
///
/// The covariance of the state process update **Q**(τ) is defined as a function
/// of τ, the time interval from the previous update):<br/>
/// **Q**(τ) = [TrackingParams::motion_noise_scale] [[τ<sup>3</sup>/3, 0, 0, τ<sup>2</sup>/2, 0,
/// 0],<br/>
/// [0, τ<sup>3</sup>/3, 0, 0, τ<sup>2</sup>/2, 0],<br/>
/// [0, 0, τ<sup>3</sup>/3, 0, 0, τ<sup>2</sup>/2],<br/>
/// [τ<sup>2</sup>/2, 0, 0, τ, 0, 0],<br/>
/// [0, τ<sup>2</sup>/2, 0, 0, τ, 0],<br/>
/// [0, 0, τ<sup>2</sup>/2, 0, 0, τ]]
///
/// Note that this form of the state process update covariance has the property
/// that 2**Q**(τ) = **Q**(2τ). In other words, two successive additions of this
/// covariance will have an identical effect to a single addtion for twice the
/// time interval.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct TrackingParams {
    /// This is used to scale the state noise covariance matrix **Q** as
    /// described at the struct-level (Kalman filter parameter).
    pub motion_noise_scale: f64,
    /// This is α in the above formula used to build the position terms in the
    /// initial estimate covariance matrix **P** as described at the
    /// struct-level (Kalman filter parameter).
    pub initial_position_std_meters: f64,
    /// This is β in the above formula used to build the velocity terms in the
    /// initial estimate covariance matrix **P** as described at the
    /// struct-level (Kalman filter parameter).
    pub initial_vel_std_meters_per_sec: f64,
    /// The observation noise covariance matrix **R** (Kalman filter
    /// parameter).
    pub ekf_observation_covariance_pixels: f64,
    /// This sets a minimum threshold for using an obervation to update an
    /// object being tracked (data association parameter).
    pub accept_observation_min_likelihood: f64,
    /// This is used to compute the maximum allowable covariance before an
    /// object is "killed" and no longer tracked.
    pub max_position_std_meters: f32,
    /// These are the hypothesis testing parameters used to "birth" a new new
    /// object and start tracking it.
    ///
    /// This is `None` if 2D (flat-3d) tracking.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub hypothesis_test_params: Option<HypothesisTestParams>,
    /// This is the minimum number of observations before object becomes
    /// visible.
    #[serde(default = "default_num_observations_to_visibility")]
    pub num_observations_to_visibility: u8,
    /// Parameters defining mini arena configuration.
    ///
    /// This is MiniArenaConfig::NoMiniArena if no mini arena is in use.
    #[serde(skip_serializing_if = "MiniArenaConfig::is_none", default)]
    pub mini_arena_config: MiniArenaConfig,
}

pub struct MiniArenaLocator {
    /// The index number of the mini arena. None if the point is not in a mini arena.
    my_idx: Option<u8>,
}

impl MiniArenaLocator {
    pub fn from_mini_arena_idx(val: u8) -> Self {
        Self { my_idx: Some(val) }
    }

    pub fn new_none() -> Self {
        Self { my_idx: None }
    }

    /// Return the index number of the mini arena. None if the point is not in a
    /// mini arena.
    pub fn idx(&self) -> Option<u8> {
        self.my_idx
    }
}

/// Configuration defining potential mini arenas.
#[derive(Debug, Clone, Serialize, Deserialize, Default, PartialEq)]
#[serde(tag = "type")]
pub enum MiniArenaConfig {
    /// No mini arena is in use.
    #[default]
    NoMiniArena,
    /// A 2D grid arranged along the X and Y axes.
    XYGrid(XYGridConfig),
}

impl MiniArenaConfig {
    pub fn is_none(&self) -> bool {
        self == &Self::NoMiniArena
    }

    pub fn get_arena_index(&self, coords: &nalgebra::Point3<MyFloat>) -> MiniArenaLocator {
        match self {
            Self::NoMiniArena => MiniArenaLocator::from_mini_arena_idx(0),
            Self::XYGrid(xy_grid_config) => xy_grid_config.get_arena_index(coords),
        }
    }

    pub fn iter_locators(&self) -> impl Iterator<Item = MiniArenaLocator> {
        let res = match self {
            Self::NoMiniArena => vec![MiniArenaLocator::from_mini_arena_idx(0)],
            Self::XYGrid(xy_grid_config) => {
                let sz = xy_grid_config.x_centers.0.len() * xy_grid_config.y_centers.0.len();
                (0..sz)
                    .map(|idx| MiniArenaLocator::from_mini_arena_idx(idx.try_into().unwrap()))
                    .collect()
            }
        };
        res.into_iter()
    }

    pub fn len(&self) -> usize {
        match self {
            Self::NoMiniArena => 1,
            Self::XYGrid(xy_grid_config) => {
                xy_grid_config.x_centers.0.len() * xy_grid_config.y_centers.0.len()
            }
        }
    }

    pub fn is_empty(&self) -> bool {
        self.len() == 0
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
struct Sorted(Vec<f64>);

impl Sorted {
    fn new(vals: &[f64]) -> Self {
        assert!(!vals.is_empty());
        let mut vals: Vec<NotNan<f64>> = vals.iter().map(|v| NotNan::new(*v).unwrap()).collect();
        vals.sort();
        let vals = vals.iter().map(|v| v.into_inner()).collect();
        Sorted(vals)
    }
    fn dist_and_argmin(&self, x: f64) -> (f64, usize) {
        let mut best_dist = std::f64::INFINITY;
        let mut prev_dist = std::f64::INFINITY;
        let mut best_idx = 0;
        for (i, selfi) in self.0.iter().enumerate() {
            let dist = (selfi - x).abs();
            if dist < best_dist {
                best_dist = dist;
                best_idx = i;
            }
            if dist > prev_dist {
                // short circuit end of loop
                break;
            }
            prev_dist = dist
        }
        (best_dist, best_idx)
    }
}

#[test]
fn test_sorted() {
    let x = Sorted::new(&[1.0, 2.0, 1.0]);

    assert_eq!(x.0, vec![1.0, 1.0, 2.0]);
    assert_eq!(x.dist_and_argmin(1.1).1, 0);

    let x = Sorted::new(&[1.0, 2.0, 1.0, 3.0, 4.0]);
    assert_eq!(x.dist_and_argmin(2.1).1, 2);

    assert_eq!(x.dist_and_argmin(1.9).1, 2);
}

/// Parameters defining a 2D grid of mini arenas arranged along X and Y axes.
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct XYGridConfig {
    x_centers: Sorted,
    y_centers: Sorted,
    radius: f64,
}

impl XYGridConfig {
    pub fn new(x: &[f64], y: &[f64], radius: f64) -> Self {
        Self {
            x_centers: Sorted::new(x),
            y_centers: Sorted::new(y),
            radius,
        }
    }

    pub fn iter_centers(&self) -> impl Iterator<Item = (f64, f64)> {
        XYGridIter {
            col_centers: self.x_centers.0.clone(),
            row_centers: self.y_centers.0.clone(),
            next_idx: 0,
        }
    }

    pub fn get_arena_index(&self, coords: &nalgebra::Point3<MyFloat>) -> MiniArenaLocator {
        if coords.z != 0.0 {
            return MiniArenaLocator::new_none();
        }
        let obj_x = coords.x;
        let obj_y = coords.y;

        let (dist_x, idx_x) = self.x_centers.dist_and_argmin(obj_x);
        let (dist_y, idx_y) = self.y_centers.dist_and_argmin(obj_y);

        let dist = (dist_x * dist_x + dist_y * dist_y).sqrt();
        if dist <= self.radius {
            let idx = (idx_y * self.x_centers.0.len() + idx_x).try_into().unwrap();
            MiniArenaLocator::from_mini_arena_idx(idx)
        } else {
            MiniArenaLocator::new_none()
        }
    }
}

struct XYGridIter {
    row_centers: Vec<f64>,
    col_centers: Vec<f64>,
    next_idx: usize,
}

impl Iterator for XYGridIter {
    type Item = (f64, f64);
    fn next(&mut self) -> Option<Self::Item> {
        let (row_idx, col_idx) = num_integer::div_rem(self.next_idx, self.col_centers.len());
        if row_idx >= self.row_centers.len() {
            None
        } else {
            let result = (self.col_centers[col_idx], self.row_centers[row_idx]);
            self.next_idx += 1;
            Some(result)
        }
    }
}

fn default_num_observations_to_visibility() -> u8 {
    // This number should suppress spurious trajectory births but not wait too
    // long before notifying listeners.
    3
}

pub type MyFloat = f64;

pub fn default_tracking_params_full_3d() -> TrackingParams {
    TrackingParams {
        motion_noise_scale: 0.1,
        initial_position_std_meters: 0.1,
        initial_vel_std_meters_per_sec: 1.0,
        accept_observation_min_likelihood: 1e-8,
        ekf_observation_covariance_pixels: 1.0,
        max_position_std_meters: 0.01212,
        hypothesis_test_params: Some(make_hypothesis_test_full3d_default()),
        num_observations_to_visibility: default_num_observations_to_visibility(),
        mini_arena_config: MiniArenaConfig::NoMiniArena,
    }
}

pub fn default_tracking_params_flat_3d() -> TrackingParams {
    TrackingParams {
        motion_noise_scale: 0.0005,
        initial_position_std_meters: 0.001,
        initial_vel_std_meters_per_sec: 0.02,
        accept_observation_min_likelihood: 0.00001,
        ekf_observation_covariance_pixels: 1.0,
        max_position_std_meters: 0.003,
        hypothesis_test_params: None,
        num_observations_to_visibility: 10,
        mini_arena_config: MiniArenaConfig::NoMiniArena,
    }
}

/// Hypothesis testing parameters.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HypothesisTestParams {
    pub minimum_number_of_cameras: u8,
    pub hypothesis_test_max_acceptable_error: f64,
    pub minimum_pixel_abs_zscore: f64,
}

pub fn make_hypothesis_test_full3d_default() -> HypothesisTestParams {
    HypothesisTestParams {
        minimum_number_of_cameras: 2,
        hypothesis_test_max_acceptable_error: 5.0,
        minimum_pixel_abs_zscore: 0.0,
    }
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub struct CamInfo {
    pub name: RosCamName,
    pub state: ConnectedCameraSyncState,
    pub http_camserver_info: CamHttpServerInfo,
    pub recent_stats: RecentStats,
}

/// Messages to the mainbrain
#[derive(Clone, Debug, Serialize, Deserialize)]
pub enum HttpApiCallback {
    /// Called from strand-cam to register a camera
    NewCamera(RegisterNewCamera),
    /// Called from strand-cam to update the current image
    UpdateCurrentImage(PerCam<UpdateImage>),
    /// Called from strand-cam to update the current camera settings (e.g.
    /// exposure time)
    UpdateCamSettings(PerCam<UpdateCamSettings>),
    /// Called from strand-cam to update the current feature detection settings
    /// (e.g. threshold different)
    UpdateFeatureDetectSettings(PerCam<UpdateFeatureDetectSettings>),
    /// Start or stop recording data (.braid directory with csv tables for later
    /// .braidz file)
    DoRecordCsvTables(bool),
    /// Start or stop recording MKV videos for all cameras
    DoRecordMp4Files(bool),
    /// set uuid in the experiment_info table
    SetExperimentUuid(String),
    /// Set the number of frames to buffer in each camera
    SetPostTriggerBufferSize(usize),
    /// Initiate MKV recording using post trigger
    PostTriggerMp4Recording,
}

#[derive(Debug, PartialEq, Eq, Clone, Serialize, Deserialize)]
pub struct PerCam<T> {
    /// The name of the camera used in ROS (e.g. with '-' converted to '_').
    pub ros_cam_name: RosCamName,
    pub inner: T,
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub struct FlydraRawUdpPacket {
    pub cam_name: String,
    /// frame timestamp of trigger pulse start (or None if cannot be determined)
    #[serde(with = "crate::timestamp_opt_f64")]
    pub timestamp: Option<FlydraFloatTimestampLocal<Triggerbox>>,
    /// frame timestamp of camnode program sampling system clock
    #[serde(with = "crate::timestamp_f64")]
    pub cam_received_time: FlydraFloatTimestampLocal<HostClock>,
    /// timestamp from the camera
    pub device_timestamp: Option<std::num::NonZeroU64>,
    /// frame number from the camera
    pub block_id: Option<std::num::NonZeroU64>,
    pub framenumber: i32,
    pub n_frames_skipped: u32,
    /// this will always be 0.0 for flydra1 custom serialized packets
    pub done_camnode_processing: f64,
    /// this will always be 0.0 for flydra1 custom serialized packets
    pub preprocess_stamp: f64,
    /// this will always be 0 for flydra1 custom serialized packets
    pub image_processing_steps: ImageProcessingSteps,
    pub points: Vec<FlydraRawUdpPoint>,
}

mod synced_frame;
pub use synced_frame::SyncFno;

mod cam_num;
pub use cam_num::CamNum;

mod timestamp;
pub use crate::timestamp::{
    get_start_ts, FlydraFloatTimestampLocal, HostClock, Source, Triggerbox,
};

pub mod timestamp_f64;
pub mod timestamp_opt_f64;

#[cfg(feature = "with-tokio-codec")]
mod tokio_cbor;
#[cfg(feature = "with-tokio-codec")]
pub use crate::tokio_cbor::CborPacketCodec;

#[derive(thiserror::Error, Debug)]
pub enum FlydraTypesError {
    #[error("CBOR data")]
    CborDataError,
    #[error("serde error")]
    SerdeError,
    #[error("unexpected hypothesis testing parameters")]
    UnexpectedHypothesisTestingParameters,
    #[error("input too long")]
    InputTooLong,
    #[error("long string not implemented")]
    LongStringNotImplemented,
    #[error("{0}")]
    IoError(#[from] std::io::Error),
    #[error("{0}")]
    Utf8Error(#[from] std::str::Utf8Error),
    #[error("URL parse error")]
    UrlParseError,
}

#[derive(Deserialize, Serialize, Debug)]
pub struct AddrInfoUnixDomainSocket {
    pub filename: String,
}

#[derive(Deserialize, Serialize, Debug, Clone)]
pub struct AddrInfoIP {
    inner: std::net::SocketAddr,
}

impl AddrInfoIP {
    pub fn from_socket_addr(src: &std::net::SocketAddr) -> Self {
        Self { inner: *src }
    }
    pub fn to_socket_addr(&self) -> std::net::SocketAddr {
        self.inner
    }
    pub fn ip(&self) -> std::net::IpAddr {
        self.inner.ip()
    }
    pub fn port(&self) -> u16 {
        self.inner.port()
    }
}

#[derive(Debug)]
pub enum RealtimePointsDestAddr {
    UnixDomainSocket(AddrInfoUnixDomainSocket),
    IpAddr(AddrInfoIP),
}

impl RealtimePointsDestAddr {
    pub fn into_string(self) -> String {
        match self {
            RealtimePointsDestAddr::UnixDomainSocket(uds) => format!("file://{}", uds.filename),
            RealtimePointsDestAddr::IpAddr(ip) => format!("http://{}:{}", ip.ip(), ip.port()),
        }
    }
}

#[derive(Debug, Clone)]
pub struct MainbrainBuiLocation(pub BuiServerInfo);

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq)]
pub struct TriggerClockInfoRow {
    // changes to this should update BraidMetadataSchemaTag
    #[serde(with = "crate::timestamp_f64")]
    pub start_timestamp: FlydraFloatTimestampLocal<HostClock>,
    pub framecount: i64,
    /// Fraction of full framecount is tcnt/255
    pub tcnt: u8,
    #[serde(with = "crate::timestamp_f64")]
    pub stop_timestamp: FlydraFloatTimestampLocal<HostClock>,
}

#[derive(Deserialize, Serialize, Debug, Clone)]
pub struct StaticMainbrainInfo {
    pub name: String,
    pub version: String,
}

bitflags! {
    #[derive(Serialize, Deserialize)]
    pub struct ImageProcessingSteps: u8 {
        const BGINIT    = 0b00000001;
        const BGSTARTUP = 0b00000010;
        const BGCLEARED = 0b00000100;
        const BGUPDATE  = 0b00001000;
        const BGNORMAL  = 0b00010000;
    }
}

/// TriggerboxV1 configuration
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct TriggerboxConfig {
    pub device_fname: String,
    pub framerate: f32,
    #[serde(default = "default_query_dt")]
    pub query_dt: std::time::Duration,
    pub max_triggerbox_measurement_error: Option<std::time::Duration>,
}

impl std::default::Default for TriggerboxConfig {
    fn default() -> Self {
        Self {
            device_fname: "/dev/trig1".to_string(),
            framerate: 100.0,
            query_dt: default_query_dt(),
            // Make a relatively long default so that cameras will synchronize
            // even with relatively long delays. Users can always specify
            // tighter precision within a config file.
            max_triggerbox_measurement_error: Some(std::time::Duration::from_millis(20)),
        }
    }
}

const fn default_query_dt() -> std::time::Duration {
    std::time::Duration::from_millis(1500)
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct FakeSyncConfig {
    pub framerate: f64,
}

impl Default for FakeSyncConfig {
    fn default() -> Self {
        Self { framerate: 95.0 }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
#[serde(tag = "trigger_type")]
pub enum TriggerType {
    TriggerboxV1(TriggerboxConfig),
    FakeSync(FakeSyncConfig),
}

impl Default for TriggerType {
    fn default() -> Self {
        TriggerType::FakeSync(FakeSyncConfig::default())
    }
}

/// Feature detection data in raw camera coordinates.
///
/// Because these are in raw camera coordinates (and thus have not been
/// undistorted with any lens distortion model), they are called "distorted".
///
/// Note that in `.braidz` files, subsequent rows on disk are not in general
/// monotonically increasing in frame number.
///
/// See the "Details about how data are processed online and saved for later
/// analysis" section in the "3D Tracking in Braid" chapter of the [User's
/// Guide](https://strawlab.github.io/strand-braid/) for a description of why
/// these cannot be relied upon in `.braidz` files to be monotonic.
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Data2dDistortedRow {
    // changes to this should update BraidMetadataSchemaTag
    // should be kept in sync with Data2dDistortedRowF32
    pub camn: CamNum,
    pub frame: i64,
    /// This is the trigger timestamp (if available).
    #[serde(with = "crate::timestamp_opt_f64")]
    pub timestamp: Option<FlydraFloatTimestampLocal<Triggerbox>>,
    #[serde(with = "crate::timestamp_f64")]
    pub cam_received_timestamp: FlydraFloatTimestampLocal<HostClock>,
    /// timestamp from the camera
    pub device_timestamp: Option<std::num::NonZeroU64>,
    /// frame number from the camera
    pub block_id: Option<std::num::NonZeroU64>,
    #[serde(deserialize_with = "invalid_nan")]
    pub x: f64,
    #[serde(deserialize_with = "invalid_nan")]
    pub y: f64,
    #[serde(deserialize_with = "invalid_nan")]
    pub area: f64,
    #[serde(deserialize_with = "invalid_nan")]
    pub slope: f64,
    #[serde(deserialize_with = "invalid_nan")]
    pub eccentricity: f64,
    pub frame_pt_idx: u8,
    pub cur_val: u8,
    #[serde(deserialize_with = "invalid_nan")]
    pub mean_val: f64,
    #[serde(deserialize_with = "invalid_nan")]
    pub sumsqf_val: f64,
}

/// Lower precision version of [Data2dDistortedRow] for saving to disk.
// Note that this matches the precision specified in the old flydra Python
// module `flydra_core.data_descriptions.Info2D`.
#[derive(Debug, Serialize)]
pub struct Data2dDistortedRowF32 {
    // changes to this should update BraidMetadataSchemaTag
    pub camn: CamNum,
    pub frame: i64,
    /// This is the trigger timestamp (if available).
    #[serde(with = "crate::timestamp_opt_f64")]
    pub timestamp: Option<FlydraFloatTimestampLocal<Triggerbox>>,
    #[serde(with = "crate::timestamp_f64")]
    pub cam_received_timestamp: FlydraFloatTimestampLocal<HostClock>,
    /// timestamp from the camera
    pub device_timestamp: Option<std::num::NonZeroU64>,
    /// frame number from the camera
    pub block_id: Option<std::num::NonZeroU64>,
    pub x: f32,
    pub y: f32,
    pub area: f32,
    pub slope: f32,
    pub eccentricity: f32,
    pub frame_pt_idx: u8,
    pub cur_val: u8,
    pub mean_val: f32,
    pub sumsqf_val: f32,
}

impl From<Data2dDistortedRow> for Data2dDistortedRowF32 {
    fn from(orig: Data2dDistortedRow) -> Self {
        Self {
            camn: orig.camn,
            frame: orig.frame,
            timestamp: orig.timestamp,
            cam_received_timestamp: orig.cam_received_timestamp,
            device_timestamp: orig.device_timestamp,
            block_id: orig.block_id,
            x: orig.x as f32,
            y: orig.y as f32,
            area: orig.area as f32,
            slope: orig.slope as f32,
            eccentricity: orig.eccentricity as f32,
            frame_pt_idx: orig.frame_pt_idx,
            cur_val: orig.cur_val,
            mean_val: orig.mean_val as f32,
            sumsqf_val: orig.sumsqf_val as f32,
        }
    }
}

impl WithKey<i64> for Data2dDistortedRow {
    fn key(&self) -> i64 {
        self.frame
    }
}

fn invalid_nan<'de, D>(de: D) -> Result<f64, D::Error>
where
    D: Deserializer<'de>,
{
    f64::deserialize(de).or(
        // TODO: should match on DeserializeError with empty field only,
        // otherwise, return error. The way this is written, anything
        // will return a nan.
        Ok(std::f64::NAN),
    )
}

pub const BRAID_EVENTS_URL_PATH: &str = "braid-events";
pub const BRAID_EVENT_NAME: &str = "braid";
