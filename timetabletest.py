from flask import jsonify, request
from models import db, Timetable, Class, Teacher, Subject
from flask_restful import Resource


class TimetableTestingResource(Resource):
    def post(self):
        data = request.get_json()
        subjects = data.get("subjects", [])
        
        results = [{"subject": subject, "result": f"Scheduled test for {subject}", "status": "Success"} for subject in subjects]
        return jsonify({"tests": results})

class TestResultsResource(Resource):
    def get(self):
        test_results = [
            {"subject": "Math", "result": "Scheduled test for Math", "status": "Success"},
            {"subject": "Physics", "result": "Scheduled test for Physics", "status": "Success"},
            {"subject": "Chemistry", "result": "Scheduled test for Chemistry", "status": "Success"}
        ]
        return jsonify({"tests": test_results})