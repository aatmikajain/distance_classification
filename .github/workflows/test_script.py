import os
import pandas as pd
from PIL import Image

# Verify that dataset files exist
dataset_path = "C:\\Users\\Aatmika\\Downloads\\Lab 5-Spring 2025 (1).ipynb"  # Updated with actual dataset path
if os.path.exists(dataset_path):
    print("✅ Dataset file found:", dataset_path)
else:
    print("❌ Dataset file NOT found!")

# Verify that images load properly
image_path = "C:\\Users\\Aatmika\\Downloads\\Dr_Shashi_Tharoor (1).jpg"  # Updated with actual image path
try:
    img = Image.open(image_path)
    print("✅ Image loaded successfully:", image_path)
except Exception as e:
    print("❌ Failed to load image:", e)

# Verify Jupyter Notebook exists
notebook_path = "C:\\Users\\Aatmika\\Downloads\\Lab 5-Spring 2025 (1).ipynb"  # Updated with actual notebook path
if os.path.exists(notebook_path):
    print("✅ Jupyter Notebook found:", notebook_path)
else:
    print("❌ Jupyter Notebook NOT found!")

