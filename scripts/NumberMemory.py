from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def number_memory(driver, start_time, target_score):

    def main_loop(give_up=False):

        number_timeout = 2

        try:
            number_element = WebDriverWait(driver, number_timeout).until(
                ec.presence_of_element_located((By.CLASS_NAME, "big-number")))
            number = number_element.text
            timeout = len(number) + 2

        except TimeoutException:
            print("Timed out waiting for the number to appear")
            exit()
        try:
            number_form = WebDriverWait(driver, timeout).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, 'input[pattern="[0-9]*"][type="text"]'))
            )
            if give_up:
                number_form.send_keys("Never gonna give you up")
            number_form.send_keys(number)

            # It asks you to say next twice (Submit and Next)
            for _ in range(2):
                submit_button = driver.find_element(By.CLASS_NAME, "e19owgy710")
                submit_button.click()

        except TimeoutException:
            print("Timed out waiting for the number form to appear")
            exit()

    for _ in range(target_score):
        main_loop()

    main_loop(give_up=True)

    number_parameters = ""

    return number_parameters
