import pytest
from app import app as flask_app

def test_index_route():
    client = flask_app.test_client()
    
    # Test GET request to index route
    response = client.get('/')
    assert response.status_code == 200
    
    # Test POST request to index route
    data = {'name': 'Test User'}
    response = client.post('/', data=data)
    assert response.status_code == 302  # Check for redirect after POST
    assert 'User_id' in flask_app.session  # Check if User_id is stored in session

