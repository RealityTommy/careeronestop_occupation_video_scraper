# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy local files to the container
COPY . .

# Install required Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-transport-https ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir requests beautifulsoup4 pandas tqdm

# Create input and output directories
RUN mkdir -p input output

# Run the application
CMD ["python", "main.py"]
