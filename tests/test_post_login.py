from tests import client

def test_login_post(client):
	url = "/login_post"

	mock_request_data = {
		"email": "test@gm.com",
		"password": "password"
	}

	response = client.post(url, data=mock_request_data)
	assert response.status_code == 200