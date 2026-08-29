from ultralytics import YOLO
import cv2

# Load your custom model
model = YOLO('runs/detect/train3/weights/best.pt')

# Open the default Mac webcam (0)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Run inference with your optimized filters
    results = model(frame, conf=0.6, iou=0.5, agnostic_nms=True)
    
    # Plot the boxes and display the video feed
    annotated_frame = results[0].plot()
    cv2.imshow("Drone Vision: Live Feed", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()