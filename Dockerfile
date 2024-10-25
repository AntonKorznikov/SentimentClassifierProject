FROM ubuntu:24.04


RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    make \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY . /app


RUN python3 -m venv venv


RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt


ENV PATH="/app/venv/bin:$PATH"


RUN make build

# Build the project
RUN make build

# Define entrypoint
ENTRYPOINT ["make", "run_all"]
