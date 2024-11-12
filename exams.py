from models import db, Exam
from flask_restful import Resource
from flask import jsonify, request

class ExamResource(Resource):
    def get(self, id=None):
        if id:
            exam = Exam.query.get(id)
            if not exam:
                return {"message": "No exam found"}, 404
            return exam.to_dict(), 200
        exams = Exam.query.all()
        return jsonify([exam.to_dict() for exam in exams])
    
    def post(self):
        data = request.get_json()
        new_exam = Exam(
            subject = data.get('subject'),
            date = data.get('date'),
            startTime = data.get('startTime'),
            endTime = data.get('endTime'),
            classroom = data.get('classroom')
        )

        db.session.add(new_exam)
        db.session.commit()
        return new_exam.to_dict(), 201
    
    def put(self, id=None):
        if id:
            exam = Exam.query.get(id)
            if not exam:
                return {"message": "No exam found"}, 404
        else:
            exam = Exam.query.first()
            if not exam:
                return {"message": "No exam found"}, 404
            
        data = request.get_json()
        exam.subject = data.get('subject', exam.subject)
        exam.date = data.get('date', exam.date)
        exam.startTime = data.get('startTime', exam.startTime)
        exam.endTime = data.get('endTime', exam.endTime)
        exam.classroom = data.get('classroom', exam.classroom)

        db.session.commit()
        return exam.to_dict(), 200
    
    def delete(self, id=None):
        exam = Exam.query.get(id)
        if not exam:
            return {"message": "No exam found"}, 404
        
        db.session.delete(exam)
        db.session.commit()
        return {"message": "Exam was deleted"}
