from flask import request,jsonify,make_response,Blueprint
from ..models.students import Student
from ..extensions.database import db


#function to create a student

def create_student(name,age):
    return Student(name=name,age=age)

api_bp=Blueprint('api',__name__)

@api_bp.route('/hello')
def hello():
    return jsonify({"message":"Hello"})

@api_bp.route('/',methods=['POST'])
def create_record():
    data=request.get_json()

    name=data.get('name')

    age=data.get('age')

    create_student(name=name,age=age).save()

    return jsonify({"message":"Created",
                    "student":{
                        "name":name,
                        "age":age
                    }
                })