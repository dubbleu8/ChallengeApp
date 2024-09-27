import pytest
from app import app  # Importa l'applicazione Flask

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test della homepage"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Hello, World!" in rv.data
