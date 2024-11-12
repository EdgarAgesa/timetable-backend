from models import db, TimetableParameters
from flask_restful import Resource
from flask import jsonify, request

class TimetableParametersResource(Resource):
    def get(self, id=None):
        if id:
            parameter = TimetableParameters.query.get(id)
            if not parameter:
                return {"message": "No timetable parameter found"}, 404
            return parameter.to_dict(), 200
        parameters = TimetableParameters.query.all()
        return jsonify([parameter.to_dict() for parameter in parameters])
    
    def post(self):
        data = request.get_json()
        new_parameter = TimetableParameters(
            generateDifferentTimetables = data.get('generateDifferentTimetables'),
            checkExhaustion = data.get('checkExhaustion'),
            maxExhaustion = data.get('maxExhaustion'),
            checkWindowsOfTeachers = data.get('checkWindowsOfTeachers'),
            maxWindows = data.get('maxWindows'),
            allowZeroPeriod = data.get('allowZeroPeriod')
        )

        db.session.add(new_parameter)
        db.session.commit()
        return new_parameter.to_dict(), 201
    
    def put(self):
        data = request.get_json()

        # Iterate over each parameter and update fields as needed
        parameters = TimetableParameters.query.all()
        for parameter in parameters:
            parameter.generateDifferentTimetables = data.get('generateDifferentTimetables', parameter.generateDifferentTimetables)
            parameter.checkExhaustion = data.get('checkExhaustion', parameter.checkExhaustion)
            parameter.maxExhaustion = data.get('maxExhaustion', parameter.maxExhaustion)
            parameter.checkWindowsOfTeachers = data.get('checkWindowsOfTeachers', parameter.checkWindowsOfTeachers)
            parameter.maxWindows = data.get('maxWindows', parameter.maxWindows)
            parameter.allowZeroPeriod = data.get('allowZeroPeriod', parameter.allowZeroPeriod)

        db.session.commit()
        return {"message": "All timetable parameters updated successfully"}, 200

    
    def delete(self, id=None):
        parameter = TimetableParameters.query.get(id)
        if not parameter:
            return {"message": "No timetable parameter found"}, 404
        
        db.session.delete(parameter)
        db.session.commit()
        return {"message": "Timetable parameter was deleted"}
