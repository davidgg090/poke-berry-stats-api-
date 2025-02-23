# Poke Berry Stats API
[![Poke Berry Stats API CI/CD](https://github.com/davidgg090/poke-berry-stats-api-/actions/workflows/main.yml/badge.svg)](https://github.com/davidgg090/poke-berry-stats-api-/actions/workflows/main.yml)

[![codecov](https://codecov.io/gh/davidgg090/poke-berry-stats-api-/branch/main/graph/badge.svg?token=PX0UX2K36A)](https://codecov.io/gh/davidgg090/poke-berry-stats-api-)

REST API that provides statistics about Pokemon berries growth time, built with FastAPI and Python. You can visit the site running at https://poke-berry-stats-api.fly.dev/.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Docker](#docker)
- [Contributing](#contributing)

## Overview
This API connects to the [PokeAPI](https://pokeapi.co/) to retrieve information about berries and calculate various statistics about their growth times. The statistics include minimum, maximum, median, variance, mean and frequency distribution of growth times.

## Features
- Retrieves berry data from PokeAPI
- Calculates growth time statistics
- RESTful API endpoint
- Docker support
- Unit tests
- Input validation
- Error handling
- API documentation

## Requirements
- Python 3.12+
- FastAPI
- Uvicorn
- Requests
- NumPy
- Docker (optional)

## Project Structure

    poke-berry-stats-api/
    ├── app/
    │   ├── api/             # API layer with routes and responses
    │   ├── core/            # Core configurations
    │   ├── clients/         # External API clients
    │   ├── services/        # Business logic layer
    │   └── utils/           # Utility functions
    ├── tests/               # Unit tests
    ├── Dockerfile
    ├── requirements.txt
    └── README.md

## Installation

### Local Setup
1. Clone the repository
```bash
git clone https://github.com/yourusername/poke-berry-stats-api.git
cd poke-berry-stats-api
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Environment variables can be set in a `.env` file in the root directory of the project.

5. Running the Application
```bash
uvicorn app.main:app --reload
```


## API Endpoints
GET /allBerryStats
Returns statistics about Pokemon berries growth time.

```json
{
    "berries_names": ["cheri", "chesto"],
    "min_growth_time": 2,
    "median_growth_time": 15,
    "max_growth_time": 24,
    "variance_growth_time": 61.49,
    "mean_growth_time": 12.85,
    "frequency_growth_time": [
        {"growth_time": 2, "frequency": 5},
        {"growth_time": 3, "frequency": 5}
    ]
}
```

## Testing
Unit tests are implemented using the `pytest` framework.

To run the tests, execute the following command:
```bash
pytest
```

## Docker
Docker support is included in the project.

To build the Docker image, run the following command:
```bash
docker build -t poke-berry-stats-api .
```

To run the Docker container, use the following command:
```bash
docker run -p 8000:8000 poke-berry-stats-api
```

## API Documentation
Once running, visit:
```
Swagger UI: http://localhost:8000/docs || https://poke-berry-stats-api.fly.dev/docs
ReDoc: http://localhost:8000/redoc || https://poke-berry-stats-api.fly.dev/redoc
```

## Contributing
Contributions are welcome!

## License
This project is licensed under the MIT License