# Use the official Python image as a base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . /app

# Set environment variables
ENV API_TOKEN=${API_TOKEN}
ENV MONGO_URI=${MONGO_URI}

# Command to run your application
CMD ["python", "src/app.py"]
