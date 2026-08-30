# Autonomous Edge-AI Quadcopter

**Onboard visual perception for autonomous navigation using NVIDIA Jetson Orin Nano, YOLOv8, OpenCV, and a Pixhawk-based quadcopter platform.**

This project explores how a quadcopter can use onboard edge AI to identify physical door states and determine whether an opening is potentially traversable during autonomous navigation.

The system combines a custom power and hardware architecture with a computer-vision pipeline trained off-device and deployed to an NVIDIA Jetson Orin Nano for real-time camera inference. The current implementation detects and classifies doors as open, closed, or ajar, providing a perception layer that can later be integrated with flight-control and path-planning logic.

**Hardware Architecture**
* Holybro X500 Quadcopter Frame with a Pixhawk 6C Flight Controller
* NVIDIA Jetson Orin Nano for edge inference
* Custom-fabricated electrically isolated mezzanine deck
* Distributed capacitance power grid with inline circuit protection

**Software & AI Pipeline**
* PyTorch & YOLOv8 for custom door-state model training
* OpenCV for live camera feed processing
* Iterative edge-deployment and validation directly on the Jetson hardware

**Repository Structure**
* `/architecture`: System flowcharts and power routing diagrams.
* `/hardware`: Mezzanine deck specifications and component lists.
* `/macbook_training`: Local AI training scripts and validation code.
* `/jetson_edge`: Inference scripts and real-time camera handlers.
