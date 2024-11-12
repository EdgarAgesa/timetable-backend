from flask import jsonify, request
from flask_restful import Resource
from models import db, CustomField

class CustomFieldResource(Resource):
    def get(self, id=None):
        if id:
            field = CustomField.query.get(id)
            if not field:
                return {"message": "Field not found"}, 404
            return field.to_dict(), 200
        fields = CustomField.query.all()
        return jsonify([field.to_dict() for field in fields])
    
    def post(self):
        data = request.get_json()
        new_field = CustomField(
            name=data.get('name'),
            value=data.get('value')
        )

        db.session.add(new_field)
        db.session.commit()
        return new_field.to_dict(), 201
    
    def put(self, id=None):
        if id:
            field = CustomField.query.get(id)
            if not field:
                return {"message": "No such field"}
            else:
                field=CustomField.query.first()
                if not field:
                    return {"message": "No such field"}
            
            data = request.get_json()
            field.name = data.get('name', field.name)
            field.value = data.get('value', field.value)

            db.session.commit()
            return field.to_dict(), 200
        
    def delete(self, id=None):
        if id:
            field = CustomField.query.get(id)
            if not field:
                return {"message": "No such field"}, 404
            
            db.session.delete(field)
            db.session.commit()
            return {"message": "Field deleted successfully"}