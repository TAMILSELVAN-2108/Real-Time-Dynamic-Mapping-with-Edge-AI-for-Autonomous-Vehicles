import time
from sensor_simulation import get_camera_frame, get_lidar_data
from edge_ai_model import EdgeAI
from map_builder import GridMap
import matplotlib.pyplot as plt

def main():
    edge_ai = EdgeAI()
    grid_map = GridMap()

    plt.ion()

    for _ in range(100):  # Simulate 100 cycles
        frame = get_camera_frame()
        lidar_data = get_lidar_data()

        detected_class = edge_ai.detect_objects(frame)
        print(f"Detected Object Class ID: {detected_class}")

        grid_map.update(lidar_data)
        grid_map.show()

        time.sleep(0.1)

if __name__ == "__main__":
    main()
