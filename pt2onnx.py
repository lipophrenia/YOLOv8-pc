from ultralytics import YOLO
import shutil

# MODEL_NAME = 'yolov8n.pt'
MODEL_NAME = 'visdrone100'
MODEL_PATH = './train_result'
MODEL = f'{MODEL_PATH}/{MODEL_NAME}.pt'

EXPORT_PATH = './onnx_export'

model = YOLO(MODEL)
success = model.export(format="onnx", opset=12, simplify=True, imgsz=(480,640))
assert success

shutil.move(f"{MODEL_PATH}/{MODEL_NAME}.onnx", f"{EXPORT_PATH}/{MODEL_NAME}.onnx")