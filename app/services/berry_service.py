from typing import Dict

from app.clients.poke_api import poke_api_client
from app.core.exceptions import ServiceError
from app.services.stats_service import StatsService


class BerryService:
    """
    Service for retrieving and calculating statistics related to berries.

    This class interacts with the PokeAPI to fetch details about berries and their growth times. 
    It utilizes the StatsService to compute statistical metrics based on the growth times of the berries.

    Methods:
        get_all_berry_stats() -> Dict:
            Asynchronously retrieves all berry statistics, including names and growth time metrics.
    """
    def __init__(self):
        """Initializes the BerryService and its dependency on StatsService."""
        self.stats_service = StatsService()

    async def get_all_berry_stats(self) -> Dict:
        """
        Retrieves statistics for all berries.

        This method fetches all berries from the PokeAPI, collects their growth times, and calculates 
        statistical metrics such as minimum, median, maximum, variance, and mean growth times. 
        It raises a ServiceError if an error occurs during the data retrieval or calculation process.

        Returns:
            Dict: A dictionary containing berry names and their corresponding growth time statistics.

        Raises:
            ServiceError: If an error occurs while retrieving berry stats or calculating statistics.
        """
        try:
            berries = poke_api_client.get_all_berries()

            growth_times = []
            berries_names = []

            for berry in berries:
                berry_detail = poke_api_client.get_berry_details(berry['name'])
                growth_times.append(berry_detail['growth_time'])
                berries_names.append(berry_detail['name'])

            stats = self.stats_service.calculate_statistics(growth_times)

            return {
                "berries_names": berries_names,
                "min_growth_time": stats['min'],
                "median_growth_time": stats['median'],
                "max_growth_time": stats['max'],
                "variance_growth_time": stats['variance'],
                "mean_growth_time": stats['mean'],
                "frequency_growth_time": stats['frequency']
            }

        except Exception as e:
            raise ServiceError(f"Error getting berry stats: {str(e)}") from e


berry_service = BerryService()
