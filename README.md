# Autonomous Edge-AI Quadcopter

**Onboard visual perception for autonomous navigation using NVIDIA Jetson Orin Nano, YOLOv8, OpenCV, and a Pixhawk-based quadcopter platform.**

This project explores how a quadcopter can use onboard edge AI to identify physical door states and determine whether an opening is potentially traversable during autonomous navigation.

The system combines a custom power and hardware architecture with a computer-vision pipeline trained off-device and deployed to an NVIDIA Jetson Orin Nano for real-time camera inference. The current implementation detects and classifies doors as open, closed, or ajar, providing a perception layer that can later be integrated with flight-control and path-planning logic.

## System Architecture

The platform separates flight control from onboard AI perception. A Pixhawk 6C manages the quadcopter's flight-control functions, while an NVIDIA Jetson Orin Nano serves as the companion computer for real-time visual perception.

The current perception pipeline works as follows:

1. **Model Training** — Door-state images are prepared and used to train a custom YOLOv8 model off-device.
2. **Edge Deployment** — The trained model is transferred to the Jetson Orin Nano.
3. **Live Perception** — A camera feed is processed with OpenCV and passed to the model for real-time inference.
4. **Door-State Classification** — The system identifies doors and classifies their state as open, closed, or ajar.
5. **Navigation Integration — Planned** — Perception results will ultimately be provided to navigation and flight-control logic so the aircraft can determine whether an opening is traversable and respond autonomously.

The hardware is supported by a custom electrically isolated power-distribution architecture designed to safely power the flight controller, Jetson companion computer, and supporting electronics from the aircraft's LiPo power system.

```mermaid
flowchart LR
    A[Training Dataset] --> B[YOLOv8 Model Training]
    B --> C[Trained Model]
    C --> D[NVIDIA Jetson Orin Nano]
    E[Onboard Camera] --> D
    D --> F[Door Detection & State Classification]
    F --> G[Traversability Decision]
    G -. Future Integration .-> H[Navigation / Path Planning]
    H -. Future Integration .-> I[Pixhawk 6C Flight Control]
```

## Current Project Status

| Capability | Status |
|---|---|
| Custom door-state model training | ✅ Implemented |
| NVIDIA Jetson Orin Nano deployment | ✅ Implemented |
| Live camera inference with OpenCV | ✅ Implemented |
| Open / closed / ajar door classification | ✅ Implemented |
| Quadcopter hardware and power integration | 🔧 In Progress |
| Perception-to-navigation interface | 📋 Planned |
| Autonomous path planning | 📋 Planned |
| Closed-loop autonomous flight through traversable openings | 📋 Planned |

## Validation & Results

The perception pipeline has been validated progressively from offline model testing to live edge deployment.

### 1. Offline Image Validation
The custom YOLOv8 model was evaluated against a separate set of test images to verify door detection and state classification before deployment. Inference testing used a 0.60 confidence threshold, 0.50 IoU threshold, and class-agnostic non-maximum suppression to reduce duplicate detections and false positives.

### 2. Live Camera Validation
The trained model was then connected to a live OpenCV camera feed to verify continuous frame-by-frame inference under real-world viewing conditions rather than static images alone.

### 3. NVIDIA Jetson Edge Deployment
The perception model was deployed to the NVIDIA Jetson Orin Nano as a TensorRT inference engine. The Jetson pipeline:

- Captures video from a MIPI CSI camera at 1280×720 resolution
- Performs GPU-accelerated inference directly on the edge device
- Detects and classifies doors as **open**, **closed**, or **partially open**
- Displays annotated detections from the live camera stream

This validated the core perception pipeline required for the next phase of the project: connecting visual door-state information to navigation and flight-control logic.

### Current Validation Scope

The current prototype demonstrates that the complete perception path can operate from:

**camera → Jetson → TensorRT inference → door detection → door-state classification**

Navigation decisions and autonomous flight responses have not yet been integrated and remain planned work.

### Example Detections

| Open Door | Closed Door | Partially Open Door |
|---|---|---|
| ![](results/open_door.jpg) | ![](results/closed_door.jpg) | ![](results/partially_open_door.jpg) |

## Repository Structure

* `/architecture`: System flowcharts and power routing diagrams.
* `/hardware`: Mezzanine deck specifications and component lists.
* `/macbook_training`: Local AI training scripts and validation code.
* `/jetson_edge`: Inference scripts and real-time camera handlers.
