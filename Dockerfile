# Use the official Python 3.11.3 image as the base
FROM python:3.11.3-slim

# Set the working directory inside the container
WORKDIR /app

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the content of the current directory inside the container
COPY . .

# Expose the port the app runs on 
EXPOSE 5000

# Specify the command to run the application
CMD ["python", "flask_app/app.py"]
