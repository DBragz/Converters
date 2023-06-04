# Use the official PostgreSQL image as the base image
FROM postgres

# Set the environment variables
ENV POSTGRES_USER your_username
ENV POSTGRES_PASSWORD your_password
ENV POSTGRES_DB your_database_name

# Copy the SQL script to the Docker container
COPY baseline.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432

# Use a base Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Python requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python program file
COPY your_python_program.py .

# Set the environment variables for PostgreSQL and Infura
ENV POSTGRES_HOST your_postgres_host
ENV POSTGRES_PORT your_postgres_port
ENV POSTGRES_DATABASE your_postgres_database
ENV POSTGRES_USER your_postgres_user
ENV POSTGRES_PASSWORD your_postgres_password
ENV INFURA_PROJECT_ID your_infura_project_id

# Run the Python program
CMD ["python", "your_python_program.py"]

