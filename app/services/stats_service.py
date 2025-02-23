from collections import Counter
from typing import Dict, List

import numpy as np

from app.core.exceptions import ServiceError


class StatsService:
    """
    Service for calculating statistical metrics and frequencies.

    This class provides methods to calculate various statistical metrics from a list of integers,
    as well as to determine the frequency of growth times. It handles errors gracefully by raising
    a ServiceError when exceptions occur during calculations.

    Methods:
        calculate_statistics(data: List[int]) -> Dict:
            Calculates statistical metrics such as min, max, mean, median, variance, and frequency of the provided data.

        calculate_growth_time_frequency(growth_times: List[int]) -> Dict[int, int]:
            Calculates the frequency of growth times from the provided list.
    """

    def calculate_statistics(self, data: List[int]) -> Dict:
        """
        Calculates statistical metrics from a list of integers.

        This method computes the minimum, maximum, mean, median, variance, and frequency of the provided data.
        It raises a ValueError if the data list is empty.

        Args:
            data (List[int]): A list of integers for which to calculate statistics.

        Returns:
            Dict: A dictionary containing the calculated statistics and their values.

        Raises:
            ValueError: If the data list is empty.
            ServiceError: If an error occurs during the calculation.
        """
        try:
            if not data:
                raise ValueError("Data list is empty")

            arr = np.array(data)

            frequency = Counter(data)

            frequency_list = [
                {"growth_time": k, "frequency": v}
                for k, v in sorted(frequency.items())
            ]
            return {
                'min': float(np.min(arr)),
                'max': float(np.max(arr)),
                'mean': float(np.mean(arr)),
                'median': float(np.median(arr)),
                'variance': float(np.var(arr)),
                'frequency': frequency_list
            }

        except Exception as e:
            raise ServiceError(f"Error calculating statistics: {str(e)}")

    def calculate_growth_time_frequency(self, growth_times: List[int]) -> Dict[int, int]:
        """
        Calculates the frequency of growth times.

        This method counts the occurrences of each growth time in the provided list and returns a sorted
        dictionary of growth times and their corresponding frequencies.

        Args:
            growth_times (List[int]): A list of growth times to calculate frequency for.

        Returns:
            Dict[int, int]: A dictionary mapping each growth time to its frequency.

        Raises:
            ServiceError: If an error occurs during the frequency calculation.
        """
        try:
            frequency = Counter(growth_times)
            return dict(sorted(frequency.items()))
        except Exception as e:
            raise ServiceError(f"Error calculating frequency: {str(e)}")
