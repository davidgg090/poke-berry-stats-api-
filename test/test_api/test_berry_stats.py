from unittest.mock import patch

from app.core.exceptions import ServiceError


def test_get_berry_stats_success(client, mock_berry_data):
    """
    Test the successful retrieval of berry statistics from the API endpoint.

    This function mocks the BerryService to return predefined berry statistics and
    asserts that the API response matches the expected output. It verifies that the
    response status code is 200 and checks the presence and correctness of the
    returned data.

    Args:
        client: The test client used to make requests to the API.
        mock_berry_data: Mock data used for testing the berry statistics.

    Returns:
        None
    """
    with patch('app.services.berry_service.BerryService.get_all_berry_stats') as mock_stats:
        mock_stats.return_value = {
            "berries_names": ["cheri", "chesto", "pecha"],
            "min_growth_time": 3.0,
            "median_growth_time": 3.0,
            "max_growth_time": 3.0,
            "variance_growth_time": 0.0,
            "mean_growth_time": 3.0,
            "frequency_growth_time": [{"growth_time": 3, "frequency": 3}]
        }

        response = client.get("/v1/allBerryStats")

        assert response.status_code == 200
        data = response.json()
        assert "berries_names" in data
        assert len(data["berries_names"]) == 3
        assert data["min_growth_time"] == 3.0


def test_get_berry_stats_error(client):
    """
    Test the error handling of the berry statistics API endpoint.

    This function mocks the BerryService to simulate an error when retrieving berry
    statistics. It asserts that the API responds with a status code of 500 and
    returns the appropriate error message.

    Args:
        client: The test client used to make requests to the API.

    Returns:
        None

    Raises:
        ServiceError: Simulated error during the test.
    """
    with patch('app.services.berry_service.BerryService.get_all_berry_stats') as mock_stats:
        mock_stats.side_effect = ServiceError("Error test")

        response = client.get("/v1/allBerryStats")

        assert response.status_code == 500
        assert response.json()["error"] == "Error test"
