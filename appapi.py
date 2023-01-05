import math
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
# constructing app() using library Api and storing
# the house into a variable called api
api = Api(app)  # using Api library which is a constructor


# Setting posted_data to null
posted_data = {

}


def checkData(posted_data, functionName):
    # getting JSON data
    posted_data = request.get_json()
    global a, b, c, x, y
    a = posted_data["a"]
    b = posted_data["b"]
    c = posted_data["c"]
    x = posted_data["x"]
    y = posted_data["y"]
    # conv data to int
    a = int(a)
    b = int(b)
    c = int(c)
    x = int(x)
    y = int(y)
    d = b**2 - (4 * a * c)  # Error prevention function
    if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in posted_data or "y" not in posted_data:
            return 301  # Missing parameter
        else:
            return 200
    elif (functionName == "division"):
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif int(posted_data["y"]) == 0:
            return 302
        else:
            return 200
    elif (functionName == "quadratic"):
        if "a" not in posted_data or "b" not in posted_data or "c" not in posted_data:
            return 301  # Missing Param
        elif d < 0:
            return 606
        else:
            return 200


class Add(Resource):
    def post(self):
        # If I am here, it means Resource Add was requested using the method POST
        # Step 2: Verifying data validity
        # Supplying FunctionName param as Identification method
        status_code = checkData(posted_data, "add")
        if status_code != 200:
            error_json = {
                "Message": "Error don happen",
                "Status code": status_code
            }
            return error_json
    # If I am here, status code is 200
        answer = x + y
        answer_Map = {
            "Message": answer,
            "Status code": 200
        }
        return answer_Map


class Subtract(Resource):
    def post(self):
        # If I am here, it means Resource Subtract was requested using the method POST
        # getting posted data

        status_code = checkData(posted_data, "subtract")
        if status_code != 200:
            error_json = {
                "Message": "Error don happen",
                "Status code": status_code
            }
            return error_json

        answer = x - y
        answer_Map = {
            "Message": answer,
            "Status code": 200
        }
        return answer_Map


class Divide(Resource):
    def post(self):
        # If I am here, it means Resource Divide was requested using the method POST
        # getting posted data

        status_code = checkData(posted_data, "divide")
        if status_code != 200:
            error_json = {
                "Message": "Error don happen",
                "Status code": status_code
            }
            return error_json

        answer = x / y
        answer_Map = {
            "Message": answer,
            "Status code": 200
        }
        return answer_Map


class Multiply(Resource):
    def post(self):  # post() here is a method, not a function
        # If I am here, it means Resource Multiply was requested using the method POST
        # getting posted data

        status_code = checkData(posted_data, "multiply")
        if status_code != 200:
            error_json = {
                "Message": "Error don happen",
                "Status code": status_code
            }
            return error_json

        answer = x * y
        answer_Map = {
            "Message": answer,
            "Status code": 200
        }
        return answer_Map


class Quadratic(Resource):
    def post(self):
        # a = request.form.get('inputName')
        # If I am here, it means Resource Quadratic was requested using the method POST
        # TODO check for errors
        status_code = checkData(posted_data, "quadratic")
        if status_code != 200:
            error_json = {
                "Message": "Error don happen",
                "Status code": status_code
            }
            return error_json
        root1 = (-b + math.sqrt(b**2 - (4 * a * c)))/(2*a)
        root2 = (-b - math.sqrt(b**2 - (4 * a * c)))/(2*a)
        result_json = {
            "Root One": root1,
            "Root Two": root2
        }
        return result_json


@app.route('/')
def index():
    return "Hello"


# mapping classes to api
# Add is mapped and its accessible via route "/add"
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Divide, "/divide")
api.add_resource(Multiply, "/multiply")
api.add_resource(Quadratic, "/quadratic")

if __name__ == "__main__":
    app.run(debug=True)
