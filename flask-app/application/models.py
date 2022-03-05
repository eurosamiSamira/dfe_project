from application import db

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(40), nullable=False)
    reps = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False)

