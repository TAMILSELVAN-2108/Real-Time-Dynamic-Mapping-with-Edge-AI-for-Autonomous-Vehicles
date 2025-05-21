# Real-Time-Dynamic-Mapping-with-Edge-AI-for-Autonomous-Vehicles
A system that leverages Edge AI to process sensor data in real time, enabling autonomous vehicles to dynamically build and update maps for safe and efficient navigation.
This project showcases a real-time dynamic mapping system for autonomous vehicles using Edge AI, simulated sensors (camera + LiDAR), and a responsive voice-enabled GUI. The system continuously updates its map and identifies objects using lightweight AI models optimized for edge deployment.

🔍 Key Features
Edge AI Object Detection:
Uses MobileNetV2 to identify real-time camera input with ultra-low latency.

Simulated Sensor Fusion:
Integrates mock LiDAR and camera streams to emulate real-world driving conditions.

Dynamic Map Builder:
Generates and updates a 2D grid map using sensor data to visualize the environment dynamically.

Voice-Controlled Assistant:
Voice interaction powered by speech recognition and text-to-speech to control and query the system.

User-Friendly GUI:
Real-time status updates, object detection display, and voice command interface using tkinter.

🗂️ Project Structure
File	Description
main.py	Runs the core pipeline: object detection and map updates
main1.py	Launches the GUI with voice assistant and dynamic updates
edge_ai_model.py	AI model for object classification (MobileNetV2)
sensor_simulation.py	Generates fake camera and LiDAR data
map_builder.py	Constructs and updates a visual 2D map
AI_chatbot.py	Standalone voice assistant script
assistant_gui.py	GUI with voice control and real-time status display

🖥️ How It Works
Simulated Inputs (camera + LiDAR) →

Edge AI Model detects objects from camera frames →

Map Builder updates environment using LiDAR →

GUI + Voice Assistant interacts with the user and displays the system status.

🚀 Run the System
bash
Copy
Edit
# Run the simulation pipeline
python main.py

# OR run with GUI + voice assistant
python main1.py

📚 Documentation & Report
Detailed documentation is available in the project report Phase 5-TEAM 1.pdf, including system design, testing, and future improvements.
