# Use official Python image as base
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder content
COPY . .

# Expose port 5000 to the outside of the container
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
