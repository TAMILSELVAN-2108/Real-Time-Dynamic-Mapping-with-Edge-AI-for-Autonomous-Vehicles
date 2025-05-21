import torch
from torchvision import models, transforms
from PIL import Image
import cv2

class EdgeAI:
    def __init__(self):
        self.model = models.mobilenet_v2(pretrained=True)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

    def detect_objects(self, frame):
        img = self.transform(frame).unsqueeze(0)
        with torch.no_grad():
            outputs = self.model(img)
        return outputs.argmax().item()  # returns class index
