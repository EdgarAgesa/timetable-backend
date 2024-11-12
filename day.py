from flask import jsonify, request
from flask_restful import Resource
from models import db, Day

class DayResource(Resource):
    def get(self, id=None):
        if id:
            day = Day.query.get(id)
            if not day:
                return {"message": "Day not found"}, 404
            return day.to_dict(), 200
        
        days = Day.query.all()
        return jsonify([day.to_dict() for day in days])
    
    def post(self):
        data = request.get_json()
        new_day = Day(
           name=data.get('name'),
           short=data.get('short'),
           description=data.get('description'),
           combinedWith=data.get('combinedWith')
        )
        db.session.add(new_day)
        db.session.commit()
        return new_day.to_dict(), 201
    
    def put(self, id=None):
        if id:
            day = Day.query.get(id)
            if not day:
                return {"message": "No such day"}, 404
            
        else:
            day = Day.query.first()
            if not day:
                return {"message": "No such day"}, 404
            
        data = request.get_json()
        day.name = data.get("name", day.name)
        day.short = data.get("short", day.short)
        day.description = data.get("description", day.description)
        day.combinedWith = data.get("combinedWith", day.combinedWith)

        db.session.commit()
        return day.to_dict(), 200
    
    def delete(self, id=None):
        day = Day.query.get(id)
        if not day:
            return {"message":"No such day"}, 404
        
        db.session.delete(day)
        db.session.commit()
        return {"message":"Day deleted successfully"}