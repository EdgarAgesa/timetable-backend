from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from models import db
from settings import SettingResource
from subjects import SubjectResource
from classrooms import ClassroomResource
from activity import ActivityResource
from teacher import TeacherResource
from customfield import CustomFieldResource
from customfield1 import CustomField1Resource
from day import DayResource
from exams import ExamResource
from timeTableParameters import TimetableParametersResource
from period import PeriodResource
from reports import ReportResource
from classes import ClassResource
from student import StudentResource
from timetabletest import TimetableTestingResource, TestResultsResource


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///time-table.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api=Api(app)
CORS(app)

api.add_resource(SettingResource, '/setting', '/setting/<int:id>')
api.add_resource(SubjectResource, '/subject', '/subject/<int:id>')
api.add_resource(ClassroomResource, '/classroom', '/classroom/<int:id>')
api.add_resource(ActivityResource, '/activity', '/activity/<int:id>')
api.add_resource(TeacherResource, '/teacher', '/teacher/<int:id>')
api.add_resource(CustomFieldResource, '/customfield', '/customfield/<int:id>')
api.add_resource(CustomField1Resource, '/customfield1', '/customfield1/<int:id>')
api.add_resource(DayResource, '/day', '/day/<int:id>')
api.add_resource(ExamResource, '/exam', '/exam/<int:id>')
api.add_resource(TimetableParametersResource, '/timetable_parameters')
api.add_resource(PeriodResource, '/period', '/period/<int:id>')
api.add_resource(ReportResource, '/report', '/report/<int:id>')
api.add_resource(ClassResource, '/class', '/class/<int:id>')
api.add_resource(StudentResource, '/student', '/student/<int:id>')
api.add_resource(TimetableTestingResource, '/timetable_test/test-timetable')
api.add_resource(TestResultsResource, '/timetable_test/test-results')


if __name__ == '__main__':
    app.run(port=5000, debug=True)