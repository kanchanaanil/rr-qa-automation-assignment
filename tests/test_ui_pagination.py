from selenium.webdriver.common.by import By

def test_pagination(driver):
    driver.get("https://tmdb-discover.surge.sh/")

    next_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
    next_btn.click()

    results = driver.find_elements(By.CLASS_NAME, "card")
    assert len(results) > 0, "Pagination failed to load results"
