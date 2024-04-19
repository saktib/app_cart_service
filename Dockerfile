# Use the custom base image
FROM lalitbits2023/scalable:base

# Install Python and pip
RUN apt-get update && apt-get install -y python3-pip

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY package/requirements.txt .

# Install any dependencies
RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py

# Command to run on container start
CMD ["python3", "code/app.py"]