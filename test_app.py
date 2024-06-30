import pytest
from app import app as flask_app, mysql
import MySQLdb

@pytest.fixture(scope='module')
def client():
    # Setup: Configure Flask app for testing
    flask_app.config['TESTING'] = True
    flask_app.config['MYSQL_DB'] = 'test_Sports_db'

    # Ensure test database exists
    connection = MySQLdb.connect(
        host=flask_app.config['MYSQL_HOST'],
        user=flask_app.config['MYSQL_USER'],
        password=flask_app.config['MYSQL_PASSWORD']
    )
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS test_Sports_db')
    cursor.close()
    connection.close()

    # Use the test client
    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client

    # Teardown: Drop test database after tests
    connection = MySQLdb.connect(
        host=flask_app.config['MYSQL_HOST'],
        user=flask_app.config['MYSQL_USER'],
        password=flask_app.config['MYSQL_PASSWORD']
    )
    cursor = connection.cursor()
    cursor.execute('DROP DATABASE test_Sports_db')
    cursor.close()
    connection.close()

@pytest.fixture(scope='function', autouse=True)
def setup_database():
    # Setup: Populate test database with schema and initial data
    connection = MySQLdb.connect(
        host=flask_app.config['MYSQL_HOST'],
        user=flask_app.config['MYSQL_USER'],
        password=flask_app.config['MYSQL_PASSWORD'],
        database='test_Sports_db'
    )
    cursor = connection.cursor()
    with open('path/to/Sports_db.sql', 'r') as f:
        cursor.execute(f.read(), multi=True)
    connection.commit()
    cursor.close()
    connection.close()

def test_index_route(client):
    # Test GET request to index route
    response = client.get('/')
    assert response.status_code == 200
    assert b'<form' in response.data  # Example check for the presence of a form

    # Test POST request to index route
    data = {'name': 'Test User'}
    response = client.post('/', data=data)
    assert response.status_code == 302  # Check for redirect after POST

    # Check if User_id is stored in session
    with client.session_transaction() as sess:
        assert 'User_id' in sess

def test_football_route(client):
    # Test GET request to Football route
    response = client.get('/Football')
    assert response.status_code == 200
    assert b'<form' in response.data  # Example check for the presence of a form

    # Test POST request to Football route
    with client.session_transaction() as sess:
        sess['User_id'] = 1
    data = {'team': 1}
    response = client.post('/Football', data=data)
    assert response.status_code == 302  # Check for redirect after POST

    with client.session_transaction() as sess:
        assert 'Football_team_id' in sess

def test_basketball_route(client):
    # Test GET request to Basketball route
    response = client.get('/Basketball')
    assert response.status_code == 200
    assert b'<form' in response.data  # Example check for the presence of a form

    # Test POST request to Basketball route
    with client.session_transaction() as sess:
        sess['User_id'] = 1
        sess['Football_team_id'] = 1
    data = {'team': 2}
    response = client.post('/Basketball', data=data)
    assert response.status_code == 302  # Check for redirect after POST

def test_results_route(client):
    # Insert mock data for testing results
    with client.session_transaction() as sess:
        sess['User_id'] = 1
        sess['Football_team_id'] = 1
        sess['Basketball_team_id'] = 2

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO Choices (User_id, Football_team_id, Basketball_team_id) VALUES (%s, %s, %s)', (1, 1, 2))
    mysql.connection.commit()

    # Test GET request to Results route
    response = client.get('/Results')
    assert response.status_code == 200
    assert b'% chosen' in response.data  # Example check for percentage text


