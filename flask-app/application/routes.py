from random import sample
from application import app, db
from application.models import Exercises
from application.forms import ExerciseForm
from flask import render_template, redirect, url_for, request


# EXERCISES
@app.route('/', methods=['GET'])
def show_home():
    exercises = Exercises.query.all()
    if not exercises:
        exercises = []

    return render_template('home.html', exercises=exercises)


@app.route('/create/exercise', methods=['GET', 'POST'])
def create_exercise():
    form = ExerciseForm()

    if request.method == 'POST':
        exer = form.exercise.data
        rep = form.reps.data

        entry = Exercises(exercise=exer, reps=rep)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('show_home'))

    return render_template('add_exercise.html', form=form)