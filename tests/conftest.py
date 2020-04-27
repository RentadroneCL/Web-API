import pytest
from flask import Flask
from app import create_app


@pytest.fixture
def app() -> Flask:
    """
    Provides an instance of our Flask app
    Returns
    -------
    Flask
    """
    return create_app()
