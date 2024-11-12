from flask import jsonify, request
from models import Activity, db
from flask_restful import Resource


class ActivityResource(Resource):

    def get(self, id=None):
        if id:
            activity=Activity.query.get(id)
            if not activity:
                return {"message": "No activity found"}, 404
            return activity.to_dict(), 200
        
        activities=Activity.query.all()
        return jsonify([activity.to_dict() for activity in activities])

    def post(self, id=None):
        data=request.get_json()
        new_activity=Activity(
            name=data.get('name'),
            date=data.get('date'),
            description=data.get('description')
        )

        db.session.add(new_activity)
        db.session.commit()
        return new_activity.to_dict(), 201
    
    def put(self, id=None):
        if id:
            activity=Activity.query.get(id)
            if not activity:
                return {"message": "No activity found"}, 404
        else:
            activity=Activity.query.first()
            if not activity:
                return {"message": "No activity found"}, 404
            
        data = request.get_json()
        activity.name=data.get('name', activity.name)
        activity.date=data.get('date', activity.date)
        activity.description=data.get('description', activity.description)

        db.session.commit()
        return activity.to_dict(), 200
    
    def delete(self, id=None):
        activity = Activity.query.get(id)
        if not activity:
            return {"message": "No activity found"}, 404
        
        db.session.delete(activity)
        db.session.commit()
        return {"message": "Activity deleted"}
        