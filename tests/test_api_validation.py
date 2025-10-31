import requests

def test_api_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {"api_key": "demo_key", "language": "en-US", "page": 1}
    response = requests.get(url, params=params)

    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)
