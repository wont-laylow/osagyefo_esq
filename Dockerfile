# -------- Stage 1: Builder --------
FROM python:3.10-slim AS builder

WORKDIR /app

# Install git and build tools for packages that need compiling
RUN apt-get update && \
    apt-get install -y --no-install-recommends git build-essential && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies into a temporary folder
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# -------- Stage 2: Final minimal image --------
FROM python:3.10-slim

WORKDIR /app

# Copy installed Python packages from builder stage
COPY --from=builder /install /usr/local

# Copy only necessary project files
COPY --from=builder /app .

# Expose the Gradio port
EXPOSE 7860

# Start the app
CMD ["python", "app.py"]
