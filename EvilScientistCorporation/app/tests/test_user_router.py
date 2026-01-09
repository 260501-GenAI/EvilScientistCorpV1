from fastapi.testclient import TestClient

from app.main import app

# Create a TestClient so we can test our routes with HTTP requests
# Notice we're wrapping app from main.py with this
client = TestClient(app)

# This test suite tests create_user. We'll see a green test, red test, and a mocked test
# Green test - test that the function behaves as expect with valid user input
# Red test - test that the function raises the appropriate exception etc. with INVALID user input
# Mocked test - We'll use a "mock" for the user database so we don't manipulate real data


# Green test
def test_create_user_success():

    # Send a real POST request to create a user, and save the response
    response = client.post(
        "/users/", # the endpoint create_user() lives at
        json={
            "username":"testuser",
            "password":"testpassword",
            "email":"testemail@email.com"
        }
    )

    # Assert that the response is what we expect (status code, message, returned data)
    assert response.status_code == 201

    # Parse the JSON response body so we can test the returned data
    data = response.json()

    assert "message" in data # assert the message key exists in the first place
    assert data.get("message") == "testuser created successfully!" # assert message value

    # We won't assert on ALL the returned data - just the username so we see it
    inserted_user = data.get("inserted_user", {}) # default to empty dict if dict isn't found
    assert inserted_user.get("username") == "testuser"

    # We're saving the data in a variable so we can test all the fields more easily
    # We then use .get() on the returned data since it's a JSON object (not a UserModel)


# Here's one of many possible red tests (duplicate username)
def test_create_user_with_duplicate_username():

    # Send two post requests, which share a value for username (which should raise an Exception)
    client.post(
        "/users/",
        json={
            "username":"duplicate",
            "password":"password",
            "email":"email@email.com"
        }
    )

    # NOTE: we only want to save this response, since we're testing the error response
    response = client.post(
        "/users/",
        json={
            "username":"duplicate",
            "password":"password",
            "email":"email@email.com"
        }
    )

    # Assert the 400 status code and the error message
    assert response.status_code == 400
    assert response.json().get("message") == "Username taken! Choose another."


# NOTE on mocking: In a real app, we definitely don't always want to hit a real database
# Sometimes, we just want to test the logic AROUND the actual DB, without manipulating real data
    # You'll hear the term "in isolation" -
    # sometimes we want to test things IN ISOLATION without worrying about their dependencies!
# Libraries like unittest.mock or pytest-mock can help with this.

def test_create_user_success_with_mock(mocker):

    # Mock the user_database to be an empty dict
    mock_db = {}
    mocker.patch("app.routers.users.user_database", mock_db)

    # Send the POST and do some asserts as usual
    response = client.post(
        "/users/", # the endpoint create_user() lives at
        json={
            "username":"testuser",
            "password":"testpassword",
            "email":"testemail@email.com"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert "message" in data
    assert data.get("message") == "testuser created successfully!"

    # a different assertion - just make sure the length of the map increased
    assert len(mock_db) == 1


