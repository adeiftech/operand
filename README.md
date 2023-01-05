# operand
a python api that takes data in via JSON using postman and run the data through a specified class then return the result

# TO USE LOCALLY
Since this is a flask app, you will need to start flask on your cmd
by running 'FLASK_APP=appapi.py' and 'flask run' after you have specified the file folder

Download Postman via https://www.postman.com/downloads/

Open the postman app and select POST as the method

Type localhost:5000/ to the Postman browser

You can specify for each class by running localhost:5000/subtract for Subtract class

localhost:5000/add for Add class and so on

There is also a class to perform quadratic process localhost:5000/quadratic

