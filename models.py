from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Activity Model
class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.String)
    description = db.Column(db.String)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))

    # Relationships
    activity_class = db.relationship("Class", back_populates="activities")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "description": self.description
        }

# Class Model
class Class(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    short = db.Column(db.String(100))
    teacher = db.Column(db.String)
    grade = db.Column(db.String)
    timeOff = db.Column(db.String)
    allowSecondLesson = db.Column(db.Boolean, default=False)
    preparation = db.Column(db.String)
    lunch = db.Column(db.String)
    maxQuestionMarked = db.Column(db.String)
    specificTimeEveryDay = db.Column(db.String)
    lessonsStartPeriod = db.Column(db.String)
    lessonsEndPeriod = db.Column(db.String)
    lessonsPerDayInterval = db.Column(db.String)
    daysWithLessons = db.Column(db.String)
    schedule = db.Column(db.String)

    # Relationships
    students = db.relationship("Student", back_populates="student_class", lazy="select")
    activities = db.relationship("Activity", back_populates="activity_class")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "short": self.short,
            "teacher": self.teacher,
            "grade": self.grade,
            "timeOff": self.timeOff,
            "allowSecondLesson": self.allowSecondLesson,
            "preparation": self.preparation,
            "lunch": self.lunch,
            "maxQuestionMarked": self.maxQuestionMarked,
            "specificTimeEveryDay": self.specificTimeEveryDay,
            "lessonsStartPeriod": self.lessonsStartPeriod,
            "lessonsEndPeriod": self.lessonsEndPeriod,
            "lessonsPerDayInterval": self.lessonsPerDayInterval,
            "daysWithLessons": self.daysWithLessons,
            "schedule": self.schedule
        }


# Classroom Model
class Classroom(db.Model):
    __tablename__ = 'classrooms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    short = db.Column(db.String(100))
    count = db.Column(db.Integer)
    timeOff = db.Column(db.String(50))
    type = db.Column(db.String(50))

    # Relationships
    exams = db.relationship("Exam", back_populates="exam_classroom")
    timetables = db.relationship("Timetable", back_populates="timetable_classroom")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "short": self.short,
            "count": self.count,
            "timeOff": self.timeOff,
            "type": self.type,
        }


# Custom Fields Models
class CustomField(db.Model):
    __tablename__ = 'custom_fields'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    value = db.Column(db.String(500))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value
        }
    
class CustomField1(db.Model):
    __tablename__ = 'custom_fields1'
    
    name = db.Column(db.String(200), primary_key=True)
    value = db.Column(db.String(500))

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value
        }

# Day Model
class Day(db.Model):
    __tablename__ = 'days'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    short = db.Column(db.String(100))
    description = db.Column(db.String)
    combinedWith = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "short": self.short,
            "description": self.description,
            "combinedWith": self.combinedWith
        }


# Exam Model
class Exam(db.Model):
    __tablename__ = 'exams'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200))
    date = db.Column(db.String)
    startTime = db.Column(db.String)
    endTime = db.Column(db.String)
    classroom = db.Column(db.Integer, db.ForeignKey('classrooms.id'))

    # Relationships
    exam_classroom = db.relationship("Classroom", back_populates="exams")

    def to_dict(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "date": self.date,
            "startTime": self.startTime,
            "endTime": self.endTime,
            "classroom": self.classroom
        }


# Item Model
class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    success = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "success": self.success
        }


# Period Model
class Period(db.Model):
    __tablename__ = 'periods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    short = db.Column(db.String, nullable=False)
    start = db.Column(db.String, nullable=False)
    end = db.Column(db.String, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    print = db.Column(db.Boolean, default=False)
    bell = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "short": self.short,
            "start": self.start,
            "end": self.end,
            "length": self.length,
            "print": self.print,
            "bell": self.bell
        }


# Relations Model
class Relations(db.Model):
    __tablename__ = 'relations'

    id = db.Column(db.Integer, primary_key=True)
    subjects = db.Column(db.String)
    classes = db.Column(db.String)
    condition = db.Column(db.String)
    condition_order = db.Column(db.String)
    importance = db.Column(db.String, default='Normal')
    note = db.Column(db.String)


# Report Model
class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String)
    type = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "type": self.type
        }


# Setting Model
class Setting(db.Model):
    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True)
    schoolName = db.Column(db.String(200))
    academicYear = db.Column(db.String)
    registrationName = db.Column(db.String)
    periodsPerDay = db.Column(db.Integer)
    zeroPeriods = db.Column(db.Boolean, default=False)
    allowZeroPeriodLessons = db.Column(db.Boolean, default=False)
    numberOfDays = db.Column(db.Integer)
    weekend = db.Column(db.String)
    multiTerm = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "schoolName": self.schoolName,
            "academicYear": self.academicYear,
            "registrationName": self.registrationName,
            "periodsPerDay": self.periodsPerDay,
            "zeroPeriods": self.zeroPeriods,
            "allowZeroPeriodLessons": self.allowZeroPeriodLessons,
            "numberOfDays": self.numberOfDays,
            "weekend": self.weekend,
            "multiTerm": self.multiTerm
        }


# Student Model
class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    className = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    rollNumber = db.Column(db.String(50), unique=True)

    # Relationships
    student_class = db.relationship("Class", back_populates="students", lazy="joined")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "className": self.className,
            "rollNumber": self.rollNumber
        }



# Subject Model
class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    short = db.Column(db.String(100))
    count = db.Column(db.Integer)
    timeOff = db.Column(db.String(50))
    distribution = db.Column(db.String)
    homeworkPreparationRequired = db.Column(db.String)  # Changed to string to match frontend
    maxOnTheQuestionMarked = db.Column(db.String)  # Changed to string to match frontend
    maxOfOnePerDay = db.Column(db.Boolean, default=False)
    doubleLessons = db.Column(db.String)  # Added to match frontend
    classrooms = db.Column(db.String)  # Added to match frontend

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "short": self.short,
            "count": self.count,
            "timeOff": self.timeOff,
            "distribution": self.distribution,
            "homeworkPreparationRequired": self.homeworkPreparationRequired,
            "maxOnTheQuestionMarked": self.maxOnTheQuestionMarked,
            "maxOfOnePerDay": self.maxOfOnePerDay,
            "doubleLessons": self.doubleLessons,
            "classrooms": self.classrooms
        }



# Teacher Model
class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    short = db.Column(db.String(100))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    count = db.Column(db.Integer)
    timeOff = db.Column(db.String)
    classTeacher = db.Column(db.Boolean, default=False)
    Qualification = db.Column(db.String(100))
    maxWindows = db.Column(db.Integer)
    daysTaught = db.Column(db.Integer)
    lessonIntervals = db.Column(db.String)
    maxQuestionsMarked = db.Column(db.Integer)
    maxWindowsPerDay = db.Column(db.Integer)
    avoidThreeConsecutiveFreePeriods = db.Column(db.Boolean, default=False)
    avoidTwoConsecutiveFreePeriods = db.Column(db.Boolean, default=False)
    contract = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "short": self.short,
            "email": self.email,
            "phone": self.phone,
            "count": self.count,
            "timeOff": self.timeOff,
            "classTeacher": self.classTeacher,
            "Qualification": self.Qualification,
            "maxWindows": self.maxWindows,
            "daysTaught": self.daysTaught,
            "lessonIntervals": self.lessonIntervals,
            "maxQuestionsMarked": self.maxQuestionsMarked,
            "maxWindowsPerDay": self.maxWindowsPerDay,
            "avoidThreeConsecutiveFreePeriods": self.avoidThreeConsecutiveFreePeriods,
            "avoidTwoConsecutiveFreePeriods": self.avoidTwoConsecutiveFreePeriods,
            "contract": self.contract
        }



# Timetable Model
class Timetable(db.Model):
    __tablename__ = 'timetables'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(200))
    day = db.Column(db.String(200))
    classroom_id = db.Column(db.Integer, db.ForeignKey('classrooms.id'))

    # Relationships
    timetable_classroom = db.relationship("Classroom", back_populates="timetables")

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "day": self.day,
            "classroom_id": self.classroom_id
        }

# TimetableParameters Model
class TimetableParameters(db.Model):
    __tablename__ = 'timetable_parameters'

    id = db.Column(db.Integer, primary_key=True)
    generateDifferentTimetables = db.Column(db.Boolean, nullable=False, default=False)
    checkExhaustion = db.Column(db.Boolean, nullable=False, default=False)
    maxExhaustion = db.Column(db.Integer, nullable=True)
    checkWindowsOfTeachers = db.Column(db.Boolean, nullable=False, default=False)
    maxWindows = db.Column(db.Integer, nullable=True)
    allowZeroPeriod = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "generateDifferentTimetables": self.generateDifferentTimetables,
            "checkExhaustion": self.checkExhaustion,
            "maxExhaustion": self.maxExhaustion,
            "checkWindowsOfTeachers": self.checkWindowsOfTeachers,
            "maxWindows": self.maxWindows,
            "allowZeroPeriod": self.allowZeroPeriod,
        }
