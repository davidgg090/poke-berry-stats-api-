from typing import Dict, List, Union

import requests

from app.core.config import settings
from app.core.exceptions import PokeAPIException


class PokeAPIClient:
    """
    Client for interacting with the PokeAPI.

    This class provides methods to fetch data from the PokeAPI, including retrieving a list of all berries
    and obtaining details for a specific berry. It manages the session and handles pagination for berry requests.

    Attributes:
        base_url (str): The base URL for the PokeAPI.
        timeout (int): The timeout duration for API requests.
        session (requests.Session): The session used for making requests to the API.
    """

    def __init__(self):
        """
        Initializes the PokeAPIClient with base URL and timeout settings.
        """
        self.base_url = settings.POKEAPI_BASE_URL
        self.timeout = settings.POKEAPI_TIMEOUT
        self.session = requests.Session()

    def __del__(self):
        """
        Closes the session when the client is deleted.
        """
        self.session.close()

    def _make_request(self, endpoint: str) -> Dict:
        """
        Makes a request to the specified endpoint of the PokeAPI.

        This method handles the request and response, raising an exception if the request fails.

        Args:
            endpoint (str): The API endpoint to request data from.

        Returns:
            Dict: The JSON response from the API.

        Raises:
            PokeAPIException: If there is an error during the request.
        """
        try:
            response = self.session.get(
                f"{self.base_url}/{endpoint}",
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise PokeAPIException(f"Error calling PokeAPI: {str(e)}")

    def get_all_berries(self) -> List[Dict[str, str]]:
        """
        Retrieves a complete list of berries from the PokeAPI.

        This method handles pagination automatically to gather all berry data.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing berry information.

        Raises:
            PokeAPIException: If there is an error fetching the berries list.
        """
        berries = []
        endpoint = "berry"

        try:
            while endpoint:
                data = self._make_request(endpoint)
                berries.extend(data['results'])
                if data.get('next'):
                    endpoint = data['next'].replace(f"{self.base_url}/", "")
                else:
                    endpoint = None

            return berries
        except Exception as e:
            raise PokeAPIException(f"Error fetching berries list: {str(e)}")

    def get_berry_details(self, berry_name: str) -> Dict[str, Union[str, int, dict]]:
        """
        Fetches details for a specific berry.

        This method retrieves detailed information about a berry given its name.

        Args:
            berry_name (str): The name of the berry.

        Returns:
            Dict[str, Union[str, int, dict]]: A dictionary containing details of the berry.

        Raises:
            ValueError: If the berry name is empty.
            PokeAPIException: If there is an error during the API request.
        """
        if not berry_name:
            raise ValueError("Berry name cannot be empty")

        try:
            return self._make_request(f"berry/{berry_name.lower().strip()}")
        except Exception as e:
            raise PokeAPIException(f"Error fetching berry {berry_name}: {str(e)}")


poke_api_client = PokeAPIClient()
