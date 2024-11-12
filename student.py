from flask import jsonify, request
from models import db, Student
from flask_restful import Resource

class StudentResource(Resource):
    def get(self, id=None):
        if id:
            student = Student.query.get(id)
            if not student:
                return {"message": "Student not found"}, 404
            return student.to_dict(), 200

        students = Student.query.all()
        return jsonify([student.to_dict() for student in students])

    def post(self):
        data = request.get_json()
        
        if not data.get('name') or not data.get('className') or not data.get('rollNumber'):
            return {"message": "Name, className, and rollNumber are required"}, 400

        if Student.query.filter_by(rollNumber=data.get('rollNumber')).first():
            return {"message": "Roll number already exists"}, 400

        new_student = Student(
            name=data['name'],
            className=data['className'],
            rollNumber=data['rollNumber']
        )

        db.session.add(new_student)
        db.session.commit()
        return new_student.to_dict(), 201

    def put(self, id):
        student = Student.query.get(id)
        if not student:
            return {"message": "Student not found"}, 404

        data = request.get_json()
        
        student.name = data.get('name', student.name)
        student.className = data.get('className', student.className)
        
        new_roll_number = data.get('rollNumber')
        if new_roll_number and new_roll_number != student.rollNumber:
            if Student.query.filter_by(rollNumber=new_roll_number).first():
                return {"message": "Roll number already exists"}, 400
            student.rollNumber = new_roll_number

        db.session.commit()
        return student.to_dict(), 200

    def delete(self, id):
        student = Student.query.get(id)
        if not student:
            return {"message": "Student not found"}, 404

        db.session.delete(student)
        db.session.commit()
        return {"message": "Student was deleted"}, 200

