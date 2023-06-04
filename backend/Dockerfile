# Use a base Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Python requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask program file
COPY flast_converter.py .

# Set the environment variables
ENV INFURA_PROJECT_ID your_infura_project_id

# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]

