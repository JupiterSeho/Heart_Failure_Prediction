# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your FastAPI application will run on
EXPOSE 5000

# Define environment variable for Prometheus
ENV prometheus_multiproc_dir /tmp

# Run FastAPI when the container launches
CMD ["uvicorn", "api_heart_failure:app", "--host", "127.0.0.1", "--port", "5000", "--log-level", "info", "--workers", "2"]
