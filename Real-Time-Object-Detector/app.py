# 5)))
import cv2
import torch
import streamlit as st
from ultralytics import YOLO
import numpy as np
import time

# Check if GPU is available, otherwise use CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Streamlit UI - Page Setup
st.set_page_config(page_title="YOLOv8m Object Detection", layout="wide")
st.title("Real-Time Object Detection")
st.markdown("Detect objects with your webcam in real-time!")

# Sidebar Settings
st.sidebar.header("⚙️ Settings")
confidence_threshold = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.6, 0.05)

# Load YOLOv8m Model
model = YOLO("yolov8m.pt").to(device)

# Webcam Initialization
cap = cv2.VideoCapture(0)  # 0 for default webcam

# Buttons with Loading Effect
start_button = st.sidebar.button("🚀 Start Detection")
stop_button = st.sidebar.button("🛑 Stop Detection")

# Placeholder for video feed
frame_placeholder = st.empty()

if start_button:
    with st.spinner("🔄 Loading... Initializing Webcam and  Model..."):
        time.sleep(3)  # Simulated loading time

    st.success("✅ Detection Started Successfully!")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("❌ Failed to grab frame.")
            break

        # Perform Object Detection
        results = model(frame, conf=confidence_threshold)
        frame = results[0].plot()

        # Convert BGR to RGB for Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display in Streamlit
        frame_placeholder.image(frame, channels="RGB", use_container_width=True)

        # Stop Condition with Loader
        if stop_button:
            with st.spinner("🛑 Stopping Detection..."):
                time.sleep(2)  # Simulated stop time
            st.warning("🛑 Detection Stopped.")
            break

# Release Resources
cap.release()
cv2.destroyAllWindows()