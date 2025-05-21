import numpy as np
import matplotlib.pyplot as plt

class GridMap:
    def __init__(self, size=100, resolution=1.0):
        self.size = size
        self.map = np.zeros((size, size))
        self.resolution = resolution

    def update(self, lidar_data):
        self.map.fill(0)  # Reset
        for angle, dist in lidar_data:
            x = int((self.size // 2) + dist * np.cos(angle) / self.resolution)
            y = int((self.size // 2) + dist * np.sin(angle) / self.resolution)
            if 0 <= x < self.size and 0 <= y < self.size:
                self.map[y, x] = 1

    def show(self):
        plt.imshow(self.map, cmap='gray')
        plt.title('Dynamic Map')
        plt.pause(0.01)
