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
        #//a[contains(text(),'Top rated')]
        logger.debug(f"Selecting category: {test_input['category']}")
        driver.find_element(By.XPATH, f"//a[contains(text(),'{test_input['category']}')]").click()

        # Type
        #//input[@id='react-select-2-input']
        logger.debug(f"Selecting type: {test_input['type']}")
        year_input_from = driver.find_element(By.XPATH,//input[@id='react-select-2-input'])      
        year_input_from.clear()
        year_input.send_keys(test_input["type"])

        # Year
        logger.debug(f"Entering year: {test_input['year']}")
       # year_input = driver.find_element(By.ID, "year")
        year_input_from = driver.find_element(By.XPATH,//input[@id='react-select-4-input'])      
        year_input_from.clear()
        year_input.send_keys(test_input["year"])
        
        year_input_to = driver.find_element(By.XPATH,//input[@id='react-select-5-input'])
        year_input_to.clear()
        year_input.send_keys(test_input["year"])

        # Rating
        logger.debug(f"Entering rating: {test_input['rating']}")
        rating_input = driver.find_element(By.XPATH, "//div[@role='radio' and @aria-checked='true' and @aria-posinset='5']")
        rating_input.click()

        # Genre
        logger.debug(f"Selecting genre: {test_input['genre']}")
        genre = driver.find_element(By.XPATH, //input[@id="react-select-3-input"])      
        genre.clear()
        genre.send_keys(test_input["genre"])

        results = driver.find_elements(By.CLASS_NAME, "card")
        logger.info(f"Found {len(results)} results for {test_input}")
        if( driver.find_element(By.XPATH, //div[text()="No results found."]) .is_displayed()){
            log
        }else{
            while
            {
                if (driver.find_element(By.XPATH, /a[@role="button" and @aria-disabled='true']) .is_displayed()){
                    break;
                }else{
            driver.find_element(By.XPATH, /a[@role="button" and @aria-disabled='false']).click()
                }
            }
        }
        assert len(results) > 0, f"No results found for {test_input}"

    except Exception as e:
        logger.error(f"Test failed for input {test_input}: {e}")
        raise
