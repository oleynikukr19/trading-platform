# Dockerfile.tests
FROM python:3.9-slim

# Set work directory in container
WORKDIR /app

# Install dependencies
COPY ../requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Change working directory to tests
WORKDIR /app/tests

# Run tests
CMD ["pytest", "--html=report.html"]