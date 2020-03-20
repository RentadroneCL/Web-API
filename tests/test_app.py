from flask import request
from app import __version__
from config.application import config


def test_version():
    assert __version__ == '0.1.0'


def test_request_headers(client):
    headers = {
        'Content-Type': 'application/json'
    }

    client.post(config['url'], headers=headers)

    assert request.headers['Content-Type'] == 'application/json'
