from ultralytics import YOLO
import json
import torch

device = 0 if torch.cuda.is_available() else "cpu"

model_path = "/home/duypd/Fall-Detection/Utils/runs/detect/train/weights/best.pt"
model = YOLO(model_path)

results = model.val(device=device)

print("🎯 Kết quả đánh giá:")
print(results)

metrics = results.results_dict if hasattr(results, "results_dict") else results
with open("val_metrics.json", "w") as f:
    json.dump(metrics, f, indent=2, ensure_ascii=False)

print("📁 Đã lưu kết quả vào val_metrics.json")
