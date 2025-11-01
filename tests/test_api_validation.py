import requests
from logger import get_logger

logger = get_logger("API-Validation")

def test_api_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {"api_key": "demo_key", "language": "en-US", "page": 1}

    logger.info(f"Sending GET request to {url} with params {params}")
    response = requests.get(url, params=params)

    logger.debug(f"Response status: {response.status_code}")
    assert response.status_code == 200, "API did not return 200 OK"

    data = response.json()
    logger.debug(f"Response keys: {list(data.keys())}")
    assert "results" in data, "Missing 'results' in response"
    assert isinstance(data["results"], list), "'results' is not a list"

    logger.info(f"API returned {len(data['results'])} results")
