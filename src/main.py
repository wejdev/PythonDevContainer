import torch
import cv2

print("✅ PyTorch CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("🧠 GPU:", torch.cuda.get_device_name(0))

img = cv2.imread("sample.jpg")
if img is None:
    print("⚠️ sample.jpg not found — skipping OpenCV display test.")
else:
    print("📷 Image loaded with shape:", img.shape)
