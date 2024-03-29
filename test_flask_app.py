import pytest
from flask import session
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert b'You are not logged in' in response.data

def test_login(client):
    response = client.post('/login', data={'username': 'user1', 'password': 'password1'}, follow_redirects=True)
    assert session['username'] == 'user1'
    assert b'You are not logged in' not in response.data  # Check that the login was successful and redirected away from the login page

def test_invalid_login(client):
    response = client.post('/login', data={'username': 'invalid', 'password': 'invalid'})
    assert b'Invalid username/password combination' in response.data

def test_logout(client):
    client.post('/login', data={'username': 'user1', 'password': 'password1'})
    response = client.get('/logout', follow_redirects=True)
    assert b'You are not logged in' in response.data

def test_signup(client):
    response = client.post('/signup', data={'name': 'testuser', 'dob': '01-01-2000', 'email': 'testuser@example.com', 'password': 'testpassword'}, follow_redirects=True)
    assert b'You are not logged in' not in response.data  # Check that the signup was successful and redirected away from the signup page

def test_empty_signup_form(client):
    response = client.post('/signup', data={})
    assert b'Please fill in all details' in response.data
