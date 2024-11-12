# Flask Application for File Upload and Data Analysis

This project is a Flask web application that allows users to upload CSV files, display the data, and generate descriptive statistics. Additionally, users can download an example CSV file.

## Description

This Flask application includes the following features:
- Upload CSV files and save them to a server directory.
- Display the contents of the uploaded CSV file.
- Generate and display descriptive statistics for the uploaded CSV file.
- Download an example CSV file.

## Installation Instructions

To set up and run this application, follow the steps below:

### 1. Clone the Repository

```bash
git clone git@github.com:delnouty/ProjectDocker.git
cd your-repo-name
```

### 2. Create a Virtual Environment

Create and activate a virtual environment to manage dependencies:

- **On Windows:**

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
  
### 3. Install Dependencies
Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```
### 4. Create Uploads Directory

Create an `uploads` directory in the project root to store uploaded files:

```bash
mkdir uploads

```
## Run Instructions

### 1. Running the Flask Application Locally

To run the Flask application locally, use the following command:

```bash
python flask_app/app.py

```

### 2. Running the Flask Application in Docker
If you prefer to use Docker, follow these steps:

#### Build the Docker Image, Run the Docker Container, Access the Application

Build the Docker image from the Dockerfile:
```bash
docker build -t flask_app:latest .
docker run -p 5000:5000 flask_app
http://localhost:5000
```
