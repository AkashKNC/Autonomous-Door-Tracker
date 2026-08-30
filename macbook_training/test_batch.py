from ultralytics import YOLO

# 1. Load your CUSTOM trained model
model = YOLO('runs/detect/trainPrime/weights/best.pt')

# 2. Run inference and SAVE the results directly to your folder
# By setting save=True, YOLO does all the work automatically without cv2
results = model(
    'test_images', 
    conf=0.6, 
    iou=0.5, 
    agnostic_nms=True, 
    save=True, 
    project='tested_images_output', 
    name='run_1'
)

print("Batch complete! Check the 'tested_images_output/run_1' folder for the images.")