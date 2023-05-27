# Use Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY ../requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY server ./server

# Expose the port on which the server will run
EXPOSE 8000

# Set the entry point for the container
CMD ["uvicorn", "server.app.server:app", "--host", "0.0.0.0", "--port", "8000"]
