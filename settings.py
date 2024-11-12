from models import db, Setting
from flask_restful import Resource
from flask import jsonify, request

class SettingResource(Resource):
    def get(self, id=None):
        if id:
            setting = Setting.query.get(id)
            if not setting:
                return {"message": "Setting not found"}, 404
            return setting.to_dict(), 200 
        settings = Setting.query.all()
        return jsonify([setting.to_dict() for setting in settings])

    def post(self):
        data = request.get_json()
        new_setting = Setting(
            schoolName=data.get("schoolName"),
            academicYear=data.get("academicYear"),
            registrationName=data.get("registrationName"),
            periodsPerDay=data.get("periodsPerDay"),
            zeroPeriods=data.get("zeroPeriods", False),
            allowZeroPeriodLessons=data.get("allowZeroPeriodLessons", False),
            numberOfDays=data.get("numberOfDays"),
            weekend=data.get("weekend"),
            multiTerm=data.get("multiTerm", False)
        )
        db.session.add(new_setting)
        db.session.commit()
        return new_setting.to_dict(), 201


    def put(self, id=None):
        # If an ID is provided, attempt to find the specific setting
        if id:
            setting = Setting.query.get(id)
            if not setting:
                return {"message": "Setting not found"}, 404
        else:
            # If no ID is provided, fall back to the first setting
            setting = Setting.query.first()
            if not setting:
                return {"message": "Setting not found"}, 404
        
        data = request.get_json()
        # Update attributes with data provided in the request, or keep the current values if not provided
        setting.schoolName = data.get("schoolName", setting.schoolName)
        setting.academicYear = data.get("academicYear", setting.academicYear)
        setting.registrationName = data.get("registrationName", setting.registrationName)
        setting.periodsPerDay = data.get("periodsPerDay", setting.periodsPerDay)
        setting.zeroPeriods = data.get("zeroPeriods", setting.zeroPeriods)
        setting.allowZeroPeriodLessons = data.get("allowZeroPeriodLessons", setting.allowZeroPeriodLessons)
        setting.numberOfDays = data.get("numberOfDays", setting.numberOfDays)
        setting.weekend = data.get("weekend", setting.weekend)
        setting.multiTerm = data.get("multiTerm", setting.multiTerm)

        db.session.commit()
        return setting.to_dict(), 200


    def delete(self, id):
        setting = Setting.query.get(id)
        if not setting:
            return {"message": "Setting not found"}, 404
        
        db.session.delete(setting)
        db.session.commit()
        return {"message": "Setting deleted"}
