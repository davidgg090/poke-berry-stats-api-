from unittest.mock import patch

import pytest

from app.core.exceptions import ServiceError
from app.services.berry_service import BerryService


@pytest.fixture
def berry_service():
    return BerryService()


@pytest.mark.asyncio
async def test_get_all_berry_stats_success(berry_service, mock_berry_data):
    """
    Test the successful retrieval of all berry statistics from the BerryService.

    This asynchronous function verifies that the BerryService correctly returns
    the expected berry statistics when called. It ensures that the service behaves
    as intended and provides the correct data structure.

    Args:
        berry_service: The instance of the BerryService being tested.
        mock_berry_data: Mock data used for testing the berry statistics.

    Returns:
        None
    """
    with patch('app.clients.poke_api.PokeAPIClient.get_all_berries') as mock_get_berries:
        with patch('app.clients.poke_api.PokeAPIClient.get_berry_details') as mock_get_details:
            mock_get_berries.return_value = mock_berry_data['berries']
            mock_get_details.side_effect = lambda name: mock_berry_data['berry_details'][name]

            result = await berry_service.get_all_berry_stats()

            assert isinstance(result, dict)
            assert "berries_names" in result
            assert len(result["berries_names"]) == 3
            assert result["min_growth_time"] == 3.0


@pytest.mark.asyncio
async def test_get_all_berry_stats_api_error(berry_service):
    """
    Test the error handling of the BerryService when retrieving all berry statistics.

    This function verifies that the BerryService correctly handles errors during
    the retrieval of berry statistics. It ensures that appropriate error responses
    are returned when an issue occurs.

    Args:
        berry_service: The instance of the BerryService being tested.

    Returns:
        None

    Raises:
        ServiceError: Simulated error during the test.
    """
    with patch('app.clients.poke_api.PokeAPIClient.get_all_berries') as mock_get_berries:
        mock_get_berries.side_effect = Exception("API Error")

        with pytest.raises(ServiceError):
            await berry_service.get_all_berry_stats()


@pytest.mark.parametrize("growth_times,expected", [
    (
            [3, 3, 3],
            {
                "min": 3.0,
                "max": 3.0,
                "mean": 3.0,
                "variance": 0.0
            }
    ),
    (
            [2, 3, 4],
            {
                "min": 2.0,
                "max": 4.0,
                "mean": 3.0,
                "variance": 0.6666666666666666
            }
    )
])
def test_calculate_statistics(berry_service, growth_times, expected):
    """
    Test the calculation of statistics for berry growth times.

    This function uses parameterized tests to verify that the BerryService's
    statistical calculations for growth times return the expected results. It
    ensures that the calculations for minimum, maximum, mean, and variance are
    accurate based on the provided growth times.

    Args:
        berry_service: The instance of the BerryService being tested.
        growth_times: A list of growth times to calculate statistics for.
        expected: A dictionary containing the expected statistical results.

    Returns:
        None
    """
    result = berry_service.stats_service.calculate_statistics(growth_times)

    for key, value in expected.items():
        assert pytest.approx(result[key]) == value
