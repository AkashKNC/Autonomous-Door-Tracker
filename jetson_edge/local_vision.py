import cv2
import os
from ultralytics import YOLO

def get_jetson_gstreamer_pipeline(capture_width=1280, capture_height=720, framerate=30):
    """Safely opens MIPI camera at standard HD resolution and passes it cleanly without squashing."""
    return (
        f"nvarguscamerasrc ! "
        f"video/x-raw(memory:NVMM), width=(int){capture_width}, height=(int){capture_height}, format=(string)NV12, framerate=(fraction){framerate}/1 ! "
        f"nvvidconv flip-method=0 ! "
        f"video/x-raw, format=(string)BGRx ! "
        f"videoconvert ! "
        f"video/x-raw, format=(string)BGR ! appsink drop=true sync=false"
    )

def main():
    print("Loading TensorRT engine...")
    # Load your custom door model
    model = YOLO("custom_doors.engine", task="detect")
    
    pipeline_string = get_jetson_gstreamer_pipeline()
    cap = cv2.VideoCapture(pipeline_string, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("Error: Could not open MIPI CSI camera.")
        return

    print("Camera active. Displaying on local Jetson monitor...")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run the AI on the GPU
        results = model(frame, device=0, verbose=False, conf=0.60)
       
        results[0].names = {0: "closed door", 1: "open door", 2: "partially open door"}
 
        # Draw the bounding boxes
        annotated_frame = results[0].plot()

        # Pop open the video window
        cv2.imshow("F450 Drone Target Tracking", annotated_frame)

        # Press 'q' on the physical keyboard to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Camera released cleanly.")

if __name__ == "__main__":
    main()
