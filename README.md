# Payments API
Goal: Improve my skills on API development and Python.
Framework: Flask
ORM: SQL Alchemy
DB: MySQL
Docker: running locally db

Steps to run the app:
Initialize DB in docker.
Install dependencies using make install


#Comments - only for learning/dev purpose
#Must have docker installed
#This file will generate an image based on database.sql
#Creating Image:
#sudo docker build -f mysql-dockerfile . -t payments
#Running Image:
#docker run -d --name paymentsdb -p 3306:3306 payments
#In case terminal is needed:
#To access terminal sudo docker exec -it containerId bash
#mysql -u root -p 
#types in password as defined in this file: 1234
#List all containers 
#docker ps -a

Testing API
curl http://127.0.0.1:5000/v1/credit-card/1
curl http://127.0.0.1:5000/v1/credit-card







