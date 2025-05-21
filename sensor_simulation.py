import numpy as np
import cv2

def get_camera_frame():
    # Simulated camera feed (replace with actual camera)
    return np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)

def get_lidar_data():
    # Simulated lidar 2D data (angle, distance)
    angles = np.linspace(0, 2*np.pi, 360)
    distances = 10 * np.random.rand(360)
    return np.stack((angles, distances), axis=-1)

