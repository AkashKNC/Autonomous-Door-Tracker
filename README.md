# Autonomous Edge-AI Quadcopter

An autonomous drone platform engineered to detect and classify physical door states (open, closed, ajar) in real-time. This project integrates custom hardware power distribution with a closed-loop computer vision pipeline deployed directly on edge hardware.

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