FROM python:3.12-slim

# Install Tkinter and clean cache
RUN apt-get update && \
    apt-get install -y python3-tk && \
    rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy all project files
COPY . .

# Install optional Python dependencies
# (Only tkinter here, usually pre-installed)
RUN pip install --no-cache-dir tk

# Run the main app (GUI will not show inside Docker)
CMD ["python", "main.py"]
