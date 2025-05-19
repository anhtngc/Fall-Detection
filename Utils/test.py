from ultralytics import YOLO
import json
import torch

device = 0 if torch.cuda.is_available() else "cpu"
print(f"🚀 Sử dụng thiết bị: {'GPU' if device == 0 else 'CPU'}")

model_path = "/home/duypd/Fall-Detection/weights_old/weights_not_fall/best.pt"
yaml_path = "/home/duypd/Fall-Detection/my_custom.yaml"

model = YOLO(model_path)

results = model.val(data=yaml_path, split='test', device=device)

metrics = results.results_dict if hasattr(results, "results_dict") else results
for k, v in metrics.items():
    print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")

with open("test_metrics.json", "w") as f:
    json.dump(metrics, f, indent=2, ensure_ascii=False)
print("📁 Đã lưu kết quả vào test_metrics.json")
