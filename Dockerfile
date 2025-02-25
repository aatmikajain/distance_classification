# Use official Python image with version 3.11
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the local project directory to the container
COPY . .

# Install required dependencies
RUN pip install numpy pandas scikit-learn wandb

# Set the command to run your Python script when the container starts
CMD ["python", "distance_classification.py"]
