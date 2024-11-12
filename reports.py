from models import db, Report
from flask import jsonify, request
from flask_restful import Resource

class ReportResource(Resource):
    def get(self, id=None):
        if id:
            report = Report.query.get(id)
            if not report:
                return {"message": "No report found"}, 404
            return report.to_dict(), 200
        reports = Report.query.all()
        return jsonify([report.to_dict() for report in reports])
    
    def post(self):
        data = request.get_json()
        new_report = Report(
            title=data.get('title'),
            description=data.get('description'),
            type=data.get('type')
        )

        db.session.add(new_report)
        db.session.commit()
        return new_report.to_dict(), 201
    
    def put(self, id):
        report = Report.query.get(id)
        if not report:
            return {"message": "No report found"}, 404

        data = request.get_json()
        report.title = data.get('title', report.title)
        report.description = data.get('description', report.description)
        report.type = data.get('type', report.type)

        db.session.commit()
        return report.to_dict(), 200
    
    def delete(self, id):
        report = Report.query.get(id)
        if not report:
            return {"message": "No report found"}, 404
        
        db.session.delete(report)
        db.session.commit()
        return {"message": "Report was deleted"}
