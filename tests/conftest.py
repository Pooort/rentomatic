import pytest

from app import create_app
from flask_settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)
