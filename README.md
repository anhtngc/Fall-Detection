# Fall Detection Using YOLOv9 on Raspberry Pi 5
## 1️⃣ Abstract:
This project aims to develop a real-time fall detection system using a deep learning model. It is *based on a previously published study that achieved an mAP@0.5 of 98.1% using the YOLOv9 model*. However, we have re-trained and fine-tuned the model by adjusting parameters and using an updated dataset, achieving an improved final training **accuracy of 99%**.

Following this, the system is developed on an embedded platform using the Raspberry Pi 5 combined with a USB Webcam to ensure flexibility, low cost, and ease of practical deployment. When a fall is detected, the system instantly sends alerts to users through messaging platforms, significantly reducing response time and enabling timely assistance in emergency situations.

This solution is designed for deployment in various environments such as homes with elderly or children, unsupervised areas, construction sites, and hazardous zones, aiming to enhance safety and minimize risks caused by falls.
![image](https://github.com/user-attachments/assets/f10733df-e778-44fb-ac25-17ce1212ce8e)

### Key Features:
- YOLOv9-based deep learning model for fall detection
- Fine-tuned and optimized model for higher training accuracy
- Raspberry Pi 5 embedded deployment with USB Webcam
- Real-time processing and alerting
- Low latency for fast response
Suitable for elderly, children, construction, hazardous zones.

## 2️⃣ Technologies Used:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)   
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)   
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)   
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)   
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/-Raspberry_Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-%23F9A825.svg?style=for-the-badge&logo=googlecolab&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)	
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

## 3️⃣ Dataset:
This project reuses three widely adopted open-source [dataset](#references) for fall detection, comprising a total of 17,661 images:
- Train set: 10,596 images
- Valid set: 3,532 images
- Test set: 3,533 images

While the original study simplified the task into a single-class binary classification (FallDown only), our approach restructures it into a two-class problem: FallDown and Not_Fallen.

To enhance the model's ability to distinguish between dangerous falls and normal daily activities, we added around **6,000 Not_Fallen images** from the CAUCAFall dataset. Each frame is labeled accordingly (class 0 for FallDown, class 1 for Not_Fallen). This design reduces overfitting, improves overall accuracy, and minimizes false positives in real-world deployments such as homes, hospitals, and construction sites. Our new labeled datasets: [click here](https://www.kaggle.com/datasets/loyalp/dataset-fall-detection)
![image](https://github.com/user-attachments/assets/e99bd5a6-f3e4-4912-a6b6-ed94c029e6d9)

## 4️⃣ Results:
1. Model Training:
   Achieved high detection performance with a final mAP@0.5 of 99% after re-training and optimizing the YOLOv9 model.
   ![image](https://github.com/user-attachments/assets/3ec144e4-bad8-457d-89e6-eb38d30dd29c)
3. Deployment on Raspberry Pi 5:
   *(On-going — system integration and testing in progress)*
   
## References:
[Roboflow Fall Detection Computer Vision Project](https://universe.roboflow.com/roboflow-universe-projects/fall-detection-ca3o8)   
[Kaggle Fall Detection Dataset](https://www.kaggle.com/datasets/uttejkumarkandagatla/fall-detection-dataset)    
[Dataset for human fall recognition in an uncontrolled environment](https://doi.org/10.1016/j.dib.2022.108610)    
[FD-YOLO: A YOLO Network Optimized for Fall Detection](https://doi.org/10.3390/app15010453)    
