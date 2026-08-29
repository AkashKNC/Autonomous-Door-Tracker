from ultralytics import YOLO

# Load the base nano model
model = YOLO('yolov8n.pt')

# Train the model on your custom dataset
# Paste the relative path you just copied inside the quotes below!
# It should look something like 'Drone-Vision-Test-1/data.yaml'
results = model.train(data='door_dataset_v9/data.yaml', epochs=100, imgsz=640, device = 'mps')

#source door_env/bin/activate - activates the virtual environment for this project
#python filename.py - activates the python script