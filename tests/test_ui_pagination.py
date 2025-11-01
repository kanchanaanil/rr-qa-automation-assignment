from selenium.webdriver.common.by import By
from logger import get_logger

logger = get_logger("UI-Pagination")

def test_pagination(driver):
    logger.info("Starting pagination test")
    driver.get("https://tmdb-discover.surge.sh/")

    try:
        next_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
        logger.debug("Clicking Next button")
        next_btn.click()

        results = driver.find_elements(By.CLASS_NAME, "card")
        logger.info(f"Number of results on next page: {len(results)}")
        assert len(results) > 0, "Pagination failed to load results"

    except Exception as e:
        logger.error(f"Pagination test failed: {e}")
        raise
