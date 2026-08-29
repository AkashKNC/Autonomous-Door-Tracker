from pymavlink import mavutil
import time

# 1. Connect to the SITL drone
print("Connecting to SITL...")
master = mavutil.mavlink_connection('udp:127.0.0.1:14540')
master.wait_heartbeat()
print("Connected!")

# 2. Define the broken MAVLink parameters
target_system = master.target_system
target_component = master.target_component
frame = mavutil.mavlink.MAV_FRAME_BODY_NED

# Bitmask: We want to IGNORE velocity and acceleration. (0 means use, 1 means ignore)
# Bits 3-5 are velocity. Bits 6-8 are acceleration.
# 0b0000000111111000 in binary = 0x01F8 in hex. 
ignore_velocity_and_accel_mask = 0x01F8 

# 3. Fire the message
print("Sending SET_POSITION_TARGET_LOCAL_NED (Body Frame, Position Only)...")
master.mav.set_position_target_local_ned_send(
    0,  # time_boot_ms
    target_system,
    target_component,
    frame,
    ignore_velocity_and_accel_mask,
    5.0, 0.0, 0.0,  # X, Y, Z (Move 5 meters forward)
    0.0, 0.0, 0.0,  # VX, VY, VZ (Ignored)
    0.0, 0.0, 0.0,  # AFX, AFY, AFZ (Ignored)
    0.0, 0.0          # Yaw, Yaw_rate
)
print("Message sent!")
