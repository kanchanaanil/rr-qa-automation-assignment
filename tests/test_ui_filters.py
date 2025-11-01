import pytest
import json
from selenium.webdriver.common.by import By
from logger import get_logger

logger = get_logger("UI-Filters")

with open("data/filters.json") as f:
    filter_data = json.load(f)

@pytest.mark.parametrize("test_input", filter_data)
def test_filter_movies(driver, test_input):
    logger.info(f"Starting filter test with data: {test_input}")
    driver.get("https://tmdb-discover.surge.sh/")

    try:
        # Category
        logger.debug(f"Selecting category: {test_input['category']}")
        driver.find_element(By.XPATH, f"//button[contains(text(),'{test_input['category']}')]").click()

        # Type
        logger.debug(f"Selecting type: {test_input['type']}")
        driver.find_element(By.XPATH, f"//button[contains(text(),'{test_input['type']}')]").click()

        # Year
        logger.debug(f"Entering year: {test_input['year']}")
        year_input = driver.find_element(By.ID, "year")
        year_input.clear()
        year_input.send_keys(test_input["year"])

        # Rating
        logger.debug(f"Entering rating: {test_input['rating']}")
        rating_input = driver.find_element(By.ID, "rating")
        rating_input.clear()
        rating_input.send_keys(test_input["rating"])

        # Genre
        logger.debug(f"Selecting genre: {test_input['genre']}")
        driver.find_element(By.XPATH, f"//button[contains(text(),'{test_input['genre']}')]").click()

        results = driver.find_elements(By.CLASS_NAME, "card")
        logger.info(f"Found {len(results)} results for {test_input}")
        assert len(results) > 0, f"No results found for {test_input}"

    except Exception as e:
        logger.error(f"Test failed for input {test_input}: {e}")
        raise
