## Parent Image
FROM python:3.10-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container
WORKDIR /app

## Installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Upgrade pip and clean cache before installing
RUN pip install --upgrade pip setuptools wheel && pip cache purge

## Copying all contents from local to container
COPY . .

## install Python dependencies
RUN pip install --no-cache-dir -e .

## Expose flask port
EXPOSE 5000

# Run Flask App
CMD ["python", "app/application.py"]
