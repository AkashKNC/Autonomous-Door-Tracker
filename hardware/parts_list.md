# Hardware Bill of Materials (BOM)

**Core Autonomous Platform**
* Holybro X500 Quadcopter Frame
* Pixhawk 6C Flight Controller (Center-of-Gravity mounted)
* NVIDIA Jetson Orin Nano (Forward-mounted for edge inference)
* Holybro PM02 Analog Power Module (JST-GH telemetry)
* High-Capacity LiPo Battery (Rear-mounted for CoG counterweight)

**Vision System & Sensors**
* Arducam Mini 12.3MP HQ Camera (IMX477 1/2.3" Sensor, M12 Mount) - Interfaced directly with the Jetson board for real-time vision processing

**Custom Power Distribution Grid**
* MATEKSYS 12S Pro BEC (Dedicated 12V step-down for Jetson)
* 1000µF Electrolytic Capacitor (Anti-brownout and ESC voltage spike protection)
* Bussmann Inline Fuse Holder with 5A Fuse (Series integration for overcurrent protection)
* XT60 Connectors and custom-cut silicon wiring

**Custom Mezzanine Mounting Deck**
* 1.5mm ABS Plastic Sheet (Cut to 50x50mm for electrical isolation)
* M3 Nylon Hex Standoffs (15mm) and Nylon Nuts
* 3M VHB Double-Sided Tape (Vibration damping)