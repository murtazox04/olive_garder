# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY ./requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Ensure entrypoint script is executable
RUN ["chmod", "+x", "./docker/admin/entrypoint.sh"]

# Set the entrypoint
ENTRYPOINT ["./docker/admin/entrypoint.sh"]
