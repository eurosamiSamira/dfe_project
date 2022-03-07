# from unittest import TestCase
from application.models import WorkoutSet
from flask_testing import TestCase
from application import app, db
from flask import url_for

from application.models import Exercises, Relationship

# UTIL


def create_exercise():
    ex = Exercises(exercise='Legs', reps='30', completed=False)
    db.session.add(ex)
    db.session.commit()


def create_mandatory():
    ws = WorkoutSet(name='Short 10 min')
    db.session.add(ws)
    db.session.commit()

    ws = WorkoutSet(name='Medium 20 min')
    db.session.add(ws)
    db.session.commit()

    ws = WorkoutSet(name='Long 30 min')
    db.session.add(ws)
    db.session.commit()

    ws = WorkoutSet(name='Master Blaster 40 min')
    db.session.add(ws)
    db.session.commit()


def create_relationship():
    store = Relationship(fk_exercise=1, fk_workout=1)
    db.session.add(store)
    db.session.commit()


class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///data.db',
            SECRET_KEY='hreuifh7ueyhf',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()  # create table schema
        create_mandatory()

    def tearDown(self):
        # Will be called after every test
        db.drop_all()


class TestViews(TestBase):

    def test_show_home(self):
        response = self.client.get(url_for('show_home'))
        print(response)
        self.assert200(response)

    def test_create_exercise(self):
        response = self.client.get(url_for('create_exercise'))
        self.assert200(response)

    def test_update_exercise(self):
        create_exercise()
        response = self.client.get(url_for('update_exercise', id=1))
        self.assert200(response)

    def test_delete(self):
        create_exercise()
        create_relationship()
        response = self.client.get(url_for('delete', id=1))
        self.assertStatus(response, 302)

    def test_complete(self):
        create_exercise()
        response = self.client.get(url_for('complete', workout_id=1, id=1))
        self.assertStatus(response, 302)

    def test_incomplete(self):
        create_exercise()
        response = self.client.get(url_for('incomplete', workout_id=1, id=1))
        self.assertStatus(response, 302)

    def test_view_set(self):
        create_exercise()
        create_relationship()
        response = self.client.get(url_for('view_set', workout_id=1))
        self.assert200(response)

    def test_edit_set(self):
        response = self.client.get(url_for('edit_set', workout_id=1))
        self.assert200(response)


class TestRead(TestBase):

    def test_read_workouts(self):
        response = self.client.get(url_for('show_home'))
        self.assertIn('Master Blaster 40 min', str(response.data))

    def test_read_exercises(self):
        create_exercise()
        response = self.client.get(url_for('show_home'))
        self.assertIn('Legs', str(response.data))


class TestCreate(TestBase):

    def test_create_exercise(self):
        response = self.client.post(
            url_for('create_exercise'),
            json={
                'exercise': 'Legs',
                'reps': '20',
            },
            follow_redirects=True
        )
        exercise = Exercises.query.get(1)
        self.assertEqual('Legs', exercise.exercise)
        self.assertIn('Legs', str(response.data))
        self.assertIn('20', str(response.data))

    def test_update_exercise(self):
        create_exercise()  # added 'Legs' to DB

        response = self.client.post(
            url_for('update_exercise', id=1),
            data={
                'exercise': 'Arms',
                'reps': '50',
            },
            follow_redirects=True
        )
        exercise = Exercises.query.get(1)
        self.assertEqual('Arms', exercise.exercise)
        self.assertIn('Arms', str(response.data))
        self.assertIn('50', str(response.data))

    def test_edit_workout(self):
        create_exercise()  # added 'Legs' to DB
        # add 'Arms'
        ex = Exercises(exercise='Arms', reps='30', completed=False)
        db.session.add(ex)
        db.session.commit()

        create_relationship()

        response = self.client.post(
            url_for('edit_set', workout_id=1),
            data={
                'workout_id': 1,
                '2': '1',
            },
            follow_redirects=True
        )
        self.assertIn('Arms', str(response.data))
        self.assertIn('30', str(response.data))

    def test_randomise(self):
        create_exercise()  # added 'Legs' to DB
        create_relationship()

        response = self.client.get(
            url_for('randomise', workout_id=1),
            follow_redirects=True,
        )
        self.assertIn('Short 10', str(response.data))

        response = self.client.get(
            url_for('randomise', workout_id=2),
            follow_redirects=True,
        )
        self.assertIn('Medium 20', str(response.data))
        return
