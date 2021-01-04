# Use Debian Buster with Python 3.9.1
FROM python:3.9.1-buster

# Set the working directory where the code of our project will be stored
WORKDIR /project

# Copy requirements first to leverage Docker caching
COPY requirements.txt ./

# Install pip packages
RUN pip install -r requirements.txt

# Expose port 80                                    <-- This is optional, but it's a good practice
EXPOSE 80

# Copy the rest of the code inside the container    <-- Here usually caching stops
COPY . .

# Start gunicorn server with 3 workers, uvicorn worker type and use the 0.0.0.0 host with port 80
ENTRYPOINT ["gunicorn", "-w", "3",  "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:80", "main:app"]
