FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies required by TensorFlow and h5py
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libatlas-base-dev \
    libhdf5-dev \
    protobuf-compiler \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -e .

# Train the model
RUN python pipeline/training_pipeline.py

# Expose the port used by Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "application.py"]
