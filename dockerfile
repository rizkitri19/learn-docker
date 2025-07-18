# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY hello.py .

# Run the script when the container starts
CMD ["python", "hello.py"]
