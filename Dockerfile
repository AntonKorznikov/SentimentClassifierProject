# Use the latest Ubuntu image as the base
FROM ubuntu:24.04

# Set non-interactive mode for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install Python and pip
RUN apt-get update && \
    apt-get install -y bash && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Project into the container
COPY . /app

# Setting variables
ENV API_TOKEN=${API_TOKEN}
ENV MONGO_URI=${MONGO_URI}

# Command to run the project
CMD ["python", "src/app.py"]
