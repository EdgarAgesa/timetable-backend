from models import db, Period
from flask_restful import Resource
from flask import jsonify, request

class PeriodResource(Resource):
    def get(self, id=None):
        if id:
            period = Period.query.get(id)
            if not period:
                return {"message": "No period found"}, 404
            return period.to_dict(), 200
        periods = Period.query.all()
        return jsonify([period.to_dict() for period in periods])
    
    def post(self):
        data = request.get_json()
        new_period = Period(
            name = data.get('name'),
            short = data.get('short'),
            start = data.get('start'),
            end = data.get('end'),
            length = data.get('length'),
            print = data.get('print'),
            bell = data.get('bell')
        )

        db.session.add(new_period)
        db.session.commit()
        return new_period.to_dict(), 201
    
    def put(self, id):
        period = Period.query.get(id)
        if not period:
            return {"message": "No period found"}, 404

        data = request.get_json()
        period.name = data.get('name', period.name)
        period.short = data.get('short', period.short)
        period.start = data.get('start', period.start)
        period.end = data.get('end', period.end)
        period.length = data.get('length', period.length)
        period.print = data.get('print', period.print)
        period.bell = data.get('bell', period.bell)

        db.session.commit()
        return period.to_dict(), 200
    
    def delete(self, id):
        period = Period.query.get(id)
        if not period:
            return {"message": "No period found"}, 404
        
        db.session.delete(period)
        db.session.commit()
        return {"message": "Period was deleted"}
