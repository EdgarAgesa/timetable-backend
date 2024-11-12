from flask import jsonify, request
from flask_restful import Resource
from models import Teacher, db

class TeacherResource(Resource):

    def get(self, id=None):
        if id:
            teacher = Teacher.query.get(id)
            if not teacher:
                return {"message": "Teacher not found"}, 404
            return teacher.to_dict(), 200
        teachers = Teacher.query.all()
        return jsonify([teacher.to_dict() for teacher in teachers])
    
    def post(self):
        data = request.get_json()
        new_teacher = Teacher(
            name=data.get('name'),
            short=data.get('short'),
            email=data.get('email'),
            phone=data.get('phone'),
            count=data.get('count'),
            timeOff=data.get('timeOff'),
            classTeacher=data.get('classTeacher'),
            Qualification=data.get('Qualification'),
            maxWindows=data.get('maxWindows'),
            daysTaught=data.get('daysTaught'),
            lessonIntervals=data.get('lessonIntervals'),
            maxQuestionsMarked=data.get('maxQuestionsMarked'),
            maxWindowsPerDay=data.get('maxWindowsPerDay'),
            avoidThreeConsecutiveFreePeriods=data.get('avoidThreeConsecutiveFreePeriods'),
            avoidTwoConsecutiveFreePeriods=data.get('avoidTwoConsecutiveFreePeriods'),
            contract=data.get('contract')
        )
        
        db.session.add(new_teacher)
        db.session.commit()
        return new_teacher.to_dict(), 201

    def put(self, id):
        teacher = Teacher.query.get(id)
        if not teacher:
            return {"message": "Teacher not found"}, 404

        data = request.get_json()
        teacher.name = data.get('name', teacher.name)
        teacher.short = data.get('short', teacher.short)
        teacher.email = data.get('email', teacher.email)
        teacher.phone = data.get('phone', teacher.phone)
        teacher.count = data.get('count', teacher.count)
        teacher.timeOff = data.get('timeOff', teacher.timeOff)
        teacher.classTeacher = data.get('classTeacher', teacher.classTeacher)
        teacher.Qualification = data.get('Qualification', teacher.Qualification)
        teacher.maxWindows = data.get('maxWindows', teacher.maxWindows)
        teacher.daysTaught = data.get('daysTaught', teacher.daysTaught)
        teacher.lessonIntervals = data.get('lessonIntervals', teacher.lessonIntervals)
        teacher.maxQuestionsMarked = data.get('maxQuestionsMarked', teacher.maxQuestionsMarked)
        teacher.avoidThreeConsecutiveFreePeriods = data.get('avoidThreeConsecutiveFreePeriods', teacher.avoidThreeConsecutiveFreePeriods)
        teacher.avoidTwoConsecutiveFreePeriods = data.get('avoidTwoConsecutiveFreePeriods', teacher.avoidTwoConsecutiveFreePeriods)
        teacher.contract = data.get('contract', teacher.contract)

        
        db.session.commit()
        return teacher.to_dict(), 200

    def delete(self, id):
        teacher = Teacher.query.get(id)
        if not teacher:
            return {"message": "Teacher not found"}, 404

        db.session.delete(teacher)
        db.session.commit()
        return {"message": "Teacher deleted successfully"}, 204
