import pytest, unittest
from application import app, db
from application.models import CarConfig
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
            )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_conconfig_view(self):
        response = self.client.post(
            url_for('carconfig'),
            data=dict(
                car = "Tesla Roadster",
                Weapon = "Invisibility Cloak"
            ),
        )
        self.assertIn(b"Tesla Roadster", response.data)
    
    def test_carconfig_mock(requests_mock):
        requests_mock.get('http://service4test.com', text='data')
        assert 'data' == requests.get('http://service4test.com').text