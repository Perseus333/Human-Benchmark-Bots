from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def aim_trainer(driver, start_time, target_score):

    driver.get("https://humanbenchmark.com/tests/aim")

    for _ in range(31):  # 30 Targets + 1 Target to start the test
        # Finding the target
        WebDriverWait(driver, 1).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div/div/div[6]'))).click()

    aim_parameters = ""

    return aim_parameters
