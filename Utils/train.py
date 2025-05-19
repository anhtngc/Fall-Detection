from ultralytics import YOLO
import os
import cv2
import matplotlib.pyplot as plt
import random
import torch

model = YOLO("/home/duypd/Fall-Detection/yolov9m.pt")

# Huấn luyện mô hình với dữ liệu fall detection
model.train(
    data="/home/duypd/Fall-Detection/my_custom.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    optimizer="SGD",  
    dropout=0.3,
    lr0=0.001,
    device=0    
)