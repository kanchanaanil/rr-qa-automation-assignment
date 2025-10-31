import pytest
import json
from selenium.webdriver.common.by import By

# Load test data
with open("data/filters.json") as f:
    filter_data = json.load(f)

@pytest.mark.parametrize("test_input", filter_data)
def test_filter_movies(driver, test_input):
    driver.get("https://tmdb-discover.surge.sh/")

    # Select category
    driver.find_element(By.XPATH, f"//button[contains(text(),'{test_input['category']}')]").click()

    # Select type
    driver.find_element(By.XPATH, f"//button[contains(text(),'{test_input['type']}')]").click()

    # Apply year filter
    year_input = driver.find_element(By.ID, "year")
    year_input.clear()
    year_input.send_keys(test_input["year"])

    # Apply rating filter
    rating_input = driver.find_element(By.ID, "rating")
    rating_input.clear()
    rating_input.send_keys(test_input["rating"])

    # Apply genre filter
    driver.find_element(By.XPATH, f"//button[contains(text(),'{test_input['genre']}')]").click()

    # Assert results are displayed
    results = driver.find_elements(By.CLASS_NAME, "card")
    assert len(results) > 0, f"No results found for {test_input}"
