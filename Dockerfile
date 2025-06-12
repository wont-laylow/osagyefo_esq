FROM python:3.10-slim

WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Upgrade pip and install dependencies with a longer timeout and optional faster mirror
RUN pip install --upgrade pip && \
    pip install --default-timeout=100 --no-cache-dir -r requirements.txt -i https://pypi.org/simple

EXPOSE 7860

CMD ["python", "app.py"]
