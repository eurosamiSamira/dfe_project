from application import db

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(40), nullable=False)
    reps = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    relationship = db.relationship('Relationship', backref='exercises')


class WorkoutSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    relationship = db.relationship('Relationship', backref='workoutsets')


class Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_exercise = db.Column('fk_exercise', db.Integer, db.ForeignKey('exercises.id'))
    fk_workout = db.Column('fk_workout', db.Integer, db.ForeignKey('workout_set.id'))
