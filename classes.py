from models import Class, db
from flask import jsonify, request
from flask_restful import Resource

class ClassResource(Resource):
    def get(self, id=None):
        if id:
            class_instance = Class.query.get(id)
            if not class_instance:
                return {"message": "Class not found"}, 404
            return class_instance.to_dict(), 200
        
        classes = Class.query.all()
        return jsonify([class_instance.to_dict() for class_instance in classes])

    def post(self):
        data = request.get_json()
        new_class = Class(
            name=data.get('name'),
            short=data.get('short'),
            teacher=data.get('teacher'),
            grade=data.get('grade'),
            timeOff=data.get('timeOff'),
            allowSecondLesson=data.get('allowSecondLesson'),
            preparation=data.get('preparation'),
            lunch=data.get('lunch'),
            maxQuestionMarked=data.get('maxQuestionMarked'),
            specificTimeEveryDay=data.get('specificTimeEveryDay'),
            lessonsStartPeriod=data.get('lessonsStartPeriod'),
            lessonsEndPeriod=data.get('lessonsEndPeriod'),
            lessonsPerDayInterval=data.get('lessonsPerDayInterval'),
            daysWithLessons=data.get('daysWithLessons'),
            schedule=data.get('schedule')
        )
        
        db.session.add(new_class)
        db.session.commit()
        return new_class.to_dict(), 201

    def put(self, id):
        class_instance = Class.query.get(id)
        if not class_instance:
            return {"message": "Class not found"}, 404

        data = request.get_json()
        class_instance.name = data.get('name', class_instance.name)
        class_instance.short = data.get('short', class_instance.short)
        class_instance.teacher = data.get('teacher', class_instance.teacher)
        class_instance.grade = data.get('grade', class_instance.grade)
        class_instance.timeOff = data.get('timeOff', class_instance.timeOff)
        class_instance.allowSecondLesson = data.get('allowSecondLesson', class_instance.allowSecondLesson)
        class_instance.preparation = data.get('preparation', class_instance.preparation)
        class_instance.lunch = data.get('lunch', class_instance.lunch)
        class_instance.maxQuestionMarked = data.get('maxQuestionMarked', class_instance.maxQuestionMarked)
        class_instance.specificTimeEveryDay = data.get('specificTimeEveryDay', class_instance.specificTimeEveryDay)
        class_instance.lessonsStartPeriod = data.get('lessonsStartPeriod', class_instance.lessonsStartPeriod)
        class_instance.lessonsEndPeriod = data.get('lessonsEndPeriod', class_instance.lessonsEndPeriod)
        class_instance.lessonsPerDayInterval = data.get('lessonsPerDayInterval', class_instance.lessonsPerDayInterval)
        class_instance.daysWithLessons = data.get('daysWithLessons', class_instance.daysWithLessons)
        class_instance.schedule = data.get('schedule', class_instance.schedule)

        db.session.commit()
        return class_instance.to_dict(), 200

    def delete(self, id):
        class_instance = Class.query.get(id)
        if not class_instance:
            return {"message": "Class not found"}, 404

        db.session.delete(class_instance)
        db.session.commit()
        return {"message": "Class was deleted"}, 200
