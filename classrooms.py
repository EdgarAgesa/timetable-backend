from models import Classroom, db
from flask_restful import Resource
from flask import jsonify, request

class ClassroomResource(Resource):
    def get(self, id=None):
        if id:
            classroom = Classroom.query.get(id)
            if not classroom:
                return {"message": "Classroom not found"}, 404
            return classroom.to_dict(), 200
        
        classrooms = Classroom.query.all()
        return jsonify([classroom.to_dict() for classroom in classrooms])
    

    def post(self):
        data= request.get_json()
        new_classroom = Classroom(
            name=data.get('name'),
            short=data.get('short'),
            count=data.get('count'),
            timeOff=data.get('timeOff'),
            type=data.get('type')
        )

        db.session.add(new_classroom)
        db.session.commit()
        return new_classroom.to_dict(), 201
    
    def put(self, id=None):
        # If an ID is provided, attempt to find the specific classroom
        if id:
            classroom = Classroom.query.get(id)
            if not classroom:
                return {"message": "Classroom not found"}, 404
        else:
            return {"message": "Classroom ID required for PUT request"}, 400
        
        # Get JSON data from request
        data = request.get_json()
        classroom.name = data.get('name', classroom.name)
        classroom.short = data.get('short', classroom.short)
        classroom.count = data.get('count', classroom.count)
        classroom.timeOff = data.get('timeOff', classroom.timeOff)
        classroom.type = data.get('type', classroom.type)

        # Commit changes to the database
        db.session.commit()
        return classroom.to_dict(), 200
    
    def delete(self, id):
        classroom = Classroom.query.get(id)
        if not classroom:
            return {"message": "Classroom not found"}, 404
        
        db.session.delete(classroom)
        db.session.commit()
        return {"message": "Classroom deleted successfully"}, 204