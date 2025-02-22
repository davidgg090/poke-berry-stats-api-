from typing import List, Dict

from pydantic import BaseModel, Field


class BerryStatsResponse(BaseModel):
    """
    Model representing the response structure for berry statistics.

    This class defines the schema for the response containing statistical metrics related to berry growth times.
    It includes fields for berry names, minimum, median, maximum, variance, mean growth times, and their frequencies.

    Attributes:
        berries_names (List[str]): A list of names of the berries.
        min_growth_time (float): The minimum growth time among the berries.
        median_growth_time (float): The median growth time among the berries.
        max_growth_time (float): The maximum growth time among the berries.
        variance_growth_time (float): The variance of the growth times.
        mean_growth_time (float): The average growth time.
        frequency_growth_time (Dict[str, int]): A dictionary mapping growth times to their frequencies.
    """
    berries_names: List[str] = Field(..., description="List of berry names")
    min_growth_time: float = Field(..., description="Minimum growth time")
    median_growth_time: float = Field(..., description="Median growth time")
    max_growth_time: float = Field(..., description="Maximum growth time")
    variance_growth_time: float = Field(..., description="Variance of growth times")
    mean_growth_time: float = Field(..., description="Average growth time")
    frequency_growth_time: Dict[str, int] = Field(..., description="Frequency of growth times")

    class Config:
        """Configuration for the BerryStatsResponse model."""
        schema_extra = {
            "example": {
                "berries_names": ["cheri", "chesto", "pecha"],
                "min_growth_time": 2,
                "median_growth_time": 3,
                "max_growth_time": 5,
                "variance_growth_time": 1.2,
                "mean_growth_time": 3.5,
                "frequency_growth_time": {
                    "2": 1,
                    "3": 2,
                    "5": 1
                }
            }
        }
