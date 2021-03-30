from app import app as application
import pytest
from flask import url_for


@pytest.fixture
def app():
    return application

