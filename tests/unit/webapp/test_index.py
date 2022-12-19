from tests.unit.webapp import client

def test_landing(client):
	landing = client.get("/")
	html = landing.data.decode()

	# assert "M-Finder" in html

	assert landing.status_code == 200