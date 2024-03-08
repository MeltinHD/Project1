#The base image is python 3.11 slim
FROM python:3.11-slim

#Create the working directory
WORKDIR /app

#Copy all the code to the Docker image 
COPY . /app

# Install MySQL connector
RUN pip install mysql-connector-python
RUN pip install bcrypt
RUN pip install -r requirements.txt

#Expose the application port
EXPOSE 8080

# Run the python Server, which will return 
CMD [ "python", "-u", "server.py" ]