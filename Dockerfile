# TEMP ballab/streamlit-app:0.0.2
# Use an official Python runtime as a parent image
FROM python:3.8-slim


RUN apt-get -y update
RUN apt install -y  gcc curl
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV STREAMLIT_SERVER_PORT=8501

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]

