from flask_restful import Resource
from models import Subject, db
from flask import jsonify, request

class SubjectResource(Resource):
    def get(self, id=None):
        if id:
            subject = Subject.query.get(id)
            if not subject:
                return {"message": "Subject not found"}, 404
            return subject.to_dict(), 200
        
        subjects = Subject.query.all()
        return jsonify([subject.to_dict() for subject in subjects])
    
    def post(self):
        data = request.get_json()
        new_subject = Subject(
            title=data.get('title'),
            short=data.get('short'),
            count=data.get('count'),
            timeOff=data.get('timeOff'),
            distribution=data.get('distribution'),
            homeworkPreparationRequired=data.get('homeworkPreparationRequired'),
            maxOnTheQuestionMarked=data.get('maxOnTheQuestionMarked'),
            doubleLessons=data.get('doubleLessons'),
            classrooms=data.get('classrooms')
        )

        db.session.add(new_subject)
        db.session.commit()
        return new_subject.to_dict(), 201
    
    def put(self, id):
        # Fetch the subject by id
        subject = Subject.query.get(id)
        if not subject:
            return {"message": "Subject not found"}, 404
        
        # Get JSON data from request
        data = request.get_json()

        # Update attributes if new values are provided
        subject.title = data.get('title', subject.title)
        subject.short = data.get('short', subject.short)
        subject.count = data.get('count', subject.count)
        subject.timeOff = data.get('timeOff', subject.timeOff)
        subject.distribution = data.get('distribution', subject.distribution)
        subject.homeworkPreparationRequired = data.get('homeworkPreparationRequired', subject.homeworkPreparationRequired)
        subject.maxOnTheQuestionMarked = data.get('maxOnTheQuestionMarked', subject.maxOnTheQuestionMarked)
        subject.doubleLessons = data.get('doubleLessons', subject.doubleLessons)
        subject.classrooms = data.get('classrooms', subject.classrooms)

        # Commit changes to the database
        db.session.commit()
        return subject.to_dict(), 200
        
    def delete(self, id):
        subject = Subject.query.get(id)
        if not subject:
            return {"message": "Subject not found"}, 404
        
        db.session.delete(subject)
        db.session.commit()
        return {"message": "Subject deleted successfully"}, 204