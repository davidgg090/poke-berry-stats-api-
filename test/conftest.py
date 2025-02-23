import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def event_loop():
    """
    Fixture that provides a new event loop for testing.

    This fixture creates a new asyncio event loop that can be used for running asynchronous tests.
    It ensures that the loop is properly closed after the tests are completed.

    Yields:
        asyncio.AbstractEventLoop: A new event loop instance for the test session.
    """
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def client():
    """Client for testing the API"""
    return TestClient(app)


@pytest_asyncio.fixture
async def mock_berry_data():
    """Mock data for berries"""
    return {
        'berries': [
            {'name': 'cheri', 'url': 'https://pokeapi.co/api/v2/berry/1/'},
            {'name': 'chesto', 'url': 'https://pokeapi.co/api/v2/berry/2/'},
            {'name': 'pecha', 'url': 'https://pokeapi.co/api/v2/berry/3/'}
        ],
        'berry_details': {
            'cheri': {'growth_time': 3, 'name': 'cheri'},
            'chesto': {'growth_time': 3, 'name': 'chesto'},
            'pecha': {'growth_time': 3, 'name': 'pecha'}
        }
    }
