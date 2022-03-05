from random import sample
from application import app, db
from application.models import Exercises, WorkoutSet, Relationship
from application.forms import ExerciseForm
from flask import render_template, redirect, url_for, request


# EXERCISES
@app.route('/', methods=['GET'])
def show_home():
    workouts = WorkoutSet.query.all()
    exercises = Exercises.query.all()
    if not exercises:
        exercises = []

    return render_template('home.html', workouts=workouts, exercises=exercises)


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


@app.route('/delete/<id>')
def delete(id):
    relationships = Relationship.query.filter_by(fk_exercise=id).all()
    for entry in relationships:
        db.session.delete(entry)
        db.session.commit()

    entry = Exercises.query.get(id)
    db.session.delete(entry)
    db.session.commit()

    return redirect(url_for('show_home'))


@app.route('/update/<id>', methods=['GET', 'POST'])
def update_exercise(id):
    if request.method == 'POST':
        form = ExerciseForm()
        entry = Exercises.query.get(id)

        entry.exercise = form.exercise.data
        entry.reps = form.reps.data
        db.session.commit()

        return redirect(url_for('show_home'))

    else:
        entry = Exercises.query.get(id)
        form = ExerciseForm()
        form.exercise.data = entry.exercise
        form.reps.data = entry.reps

        return render_template('update_exercise.html', form=form)


@app.route('/complete/<workout_id>/<id>', methods=['GET'])
def complete(workout_id, id):
    entry = Exercises.query.get(id)
    entry.completed = True
    db.session.commit()
    return redirect(url_for('view_set', workout_id=workout_id))


@app.route('/incomplete/<workout_id>/<id>', methods=['GET'])
def incomplete(workout_id, id):
    entry = Exercises.query.get(id)
    entry.completed = False
    db.session.commit()
    return redirect(url_for('view_set', workout_id=workout_id))


# WORKOUTS
@app.route('/viewset/<workout_id>')
def view_set(workout_id):
    workout = WorkoutSet.query.get(workout_id)
    exercises = []
    relationships = Relationship.query.filter_by(fk_workout=workout_id).all()
    for relationship in relationships:
        exercise = Exercises.query.get(relationship.fk_exercise)
        exercises.append(exercise)

    return render_template('view_workout.html', current_exercises=exercises, workout=workout)


@app.route('/editset/<workout_id>', methods=['GET', 'POST'])
def edit_set(workout_id):
    id = workout_id
    if request.method == 'POST':
        id = request.form.get('workout_id')  # get posted workout id

        # clean up existing registered entries in relationship table
        relationships = Relationship.query.filter_by(fk_workout=id).all()
        if relationships is not None:
            for entry in relationships:
                if int(entry.fk_workout) == int(id):
                    db.session.delete(entry)
                    db.session.commit()

        # insert posted keys
        for key in request.form.keys():
            try:
                if float(key) >= 0:
                    store = Relationship(
                        fk_exercise=int(key), fk_workout=int(id))
                    db.session.add(store)
                    db.session.commit()

            except ValueError:
                pass

        return redirect(url_for('view_set', workout_id=id))

    workout = WorkoutSet.query.get(workout_id)
    all = Exercises.query.all()

    return render_template('update_workout.html', available_exercises=all, workout=workout)
