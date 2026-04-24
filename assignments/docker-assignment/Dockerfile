# Use official Ubuntu base image
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update apt repository cache and install required packages
RUN apt-get update && apt-get install -y \
    git \
    lynx \
    python3 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create and set working directory
WORKDIR /workspace

# Clone public repository into the container
RUN git clone https://github.com/mit-pdos/xv6-public.git

# Copy local Hello World program into container
COPY hello.py /workspace/hello.py

# Automatically run the Python program when container starts
CMD ["python3", "/workspace/hello.py"]