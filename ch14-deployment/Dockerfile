# Use Debian Buster with Python 3.9.1
FROM python:3.9.1-buster

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Install pip packages
RUN pip install -r requirements.txt

# Create and use a new user, so we don't use "root" user
RUN useradd --create-home --shell /bin/bash app
WORKDIR /home/app
USER app

# IMPORTANT: At the beginning of this chapter, I use port 80 and then switch to 8000
#            Make sure you use the right port below!
# Expose port 80  <-- This is optional, but it's a good practice
EXPOSE 80

# Copy the rest of the code inside the container
COPY . .

# Start gunicorn server with 3 workers, uvicorn worker type and use the 0.0.0.0 host with port 80
ENTRYPOINT ["gunicorn", "-w", "3",  "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:80", "main:app"]
