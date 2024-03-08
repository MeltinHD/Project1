#The base image is python 3.11 slim
FROM python:3.11-slim

#Create the working directory
WORKDIR /app

#Copy all the code to the Docker image 
COPY . /app

# Install MySQL connector
RUN pip install mysql-connector-python
RUN pip install bcrypt

#Expose the application port
EXPOSE 8000

# Run the python Server, which will return 
#Toronto current time as JSON for GET requests
CMD [ "python", "server.py" ]