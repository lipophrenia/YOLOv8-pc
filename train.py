from ultralytics import YOLO

DATASET = './datasets/VisDrone/VisDrone.yaml'
BATCH_SIZE = 16 # Размер батча. Больше - быстрее, но кушает видеопамять
EPOCHS = 100 # Количество эпох обучения

SAVE_ROOT = './save/VisDrone'
SAVE_NAME = 'run'

model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml')  # build a new model from YAML
# model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

results = model.train(
    data=DATASET,
    batch=BATCH_SIZE,
    epochs=EPOCHS,
    imgsz=640,
    project = SAVE_ROOT,
    name=SAVE_NAME
)
