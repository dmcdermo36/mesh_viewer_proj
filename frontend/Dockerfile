# Use Python base image
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libgl1-mesa-glx \
        xvfb \
        procps \
    || apt-get update && apt-get install -y \
        libgl1-mesa-glx \
        xvfb \
        procps \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code (app.py) to the container
COPY . /app

# Set up virtual framebuffer for headless rendering
ENV DISPLAY=:99

# Run Xvfb in the background and then run the Streamlit app
CMD Xvfb :99 -screen 0 1024x768x24 & streamlit run app.py --server.headless true
