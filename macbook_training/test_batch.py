from ultralytics import YOLO
import cv2

# 1. Load your CUSTOM trained model (make sure train3 matches your latest successful run!)
model = YOLO('runs/detect/train3/weights/best.pt')

# 2. Add the filters here to fix the wall engravings and double-boxes
# YOLO will automatically find and process all images inside
results = model('test_images', conf=0.6, iou=0.5, agnostic_nms=True)

# Loop through the results (one by one)
for result in results:
    # Extract the image with the bounding boxes
    annotated_image = result.plot()

    # Display the current image
    cv2.imshow("Batch YOLO Test", annotated_image)

    # Wait for you to press a key.
    # Pressing 'q' will quit the whole program.
    # Pressing literally any other key will move to the next photo!
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break

# Clean up and close the window when the loop finishes
cv2.destroyAllWindows()