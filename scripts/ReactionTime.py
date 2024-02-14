import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def reaction_time(driver, start_time, target_score):
    driver.find_element(By.CLASS_NAME, "view-splash").click()

    # The Main Loop
    i = 0
    while i < 5:
        try:
            # Finding the target by XPATH
            target = driver.find_element(By.CLASS_NAME, 'view-go')
            target.click()
            target.click()

            # The element takes at least 2.5 to load
            time.sleep(2.5)
            i += 1

        except NoSuchElementException:
            pass

    reaction_parameters = ""
    return reaction_parameters
