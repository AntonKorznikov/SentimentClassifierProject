# Dockerfile

FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    make \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Build the project
RUN make build

# Define entrypoint
ENTRYPOINT ["make", "run_all"]
