from ultralytics import YOLO

model = YOLO("yolov8n-obb.pt") 

results = model.track(
    source="./video/crossroad.mp4", show=True, persist=True, show_labels=False, show_conf=False
) 