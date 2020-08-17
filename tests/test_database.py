""" pytests for SQLAlchemy models """

import os
import pytest
from app import app
from app.database import db
from app.models import Link

TESTDB_PATH = "test.db"
TEST_DATABASE_URI = 'sqlite:///' + TESTDB_PATH


@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    app.config['CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DATABASE_URI
    db.init_app(app)

    yield client
    with app.app_context():
        print("Tearing down test.db...")
        Link.query.filter_by(Text="new").delete()
        db.session.commit()

    return app.test_client()


def test_link_model_creates(client):
    with app.app_context():
        new_link = Link(LinkId=None, Text="new", URL="https://newurl.com")
        db.session.add(new_link)
        db.session.commit()
        link = Link.query.filter_by(Text="new").first()
        assert link.Text == "new"


def test_link_model_returns(client):
    with app.app_context():
        links = Link.query.all()
        assert len(links) > 0
