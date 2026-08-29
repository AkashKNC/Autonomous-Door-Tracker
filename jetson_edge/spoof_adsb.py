from pymavlink import mavutil
import time

master = mavutil.mavlink_connection('udp:127.0.0.1:14540')
master.wait_heartbeat()
print("Spoofing ADSB Traffic across the antimeridian...")

try:
    while True:
        master.mav.adsb_vehicle_send(
            12345, # ICAO address
            160000000, # lat: 16.0 degrees (x1E7)
            -1799990000, # lon: -179.999 degrees (x1E7)
            0, # altitude type
            10000, # altitude (mm)
            0, # heading (cdeg)
            0, 0, # horizontal/vertical velocity
            b"GHOST", # callsign (MUST BE A BYTE STRING)
            2, # emitter type
            1, # time since last communication
            65535, # flags
            17 # squawk
        )
        time.sleep(1)
except KeyboardInterrupt:
    pass
