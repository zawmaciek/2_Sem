import os
import cv2
from tqdm import tqdm

for root, dirs, files in os.walk("PhoneRealDataset", topdown=False):
    for name in tqdm(files):
        if name.endswith('.mp4'):
            file_path = os.path.join(root, name)
            vidcap = cv2.VideoCapture(file_path)
            success, image = vidcap.read()
            count = 0
            while success:
                cv2.imwrite(os.path.join(root, f"{name.strip('.mp4')}{count}.jpg"), image)  # save frame as JPEG file
                success, image = vidcap.read()
                count += 1
