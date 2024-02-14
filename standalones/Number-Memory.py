import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


desired_points = int(input("Write the amount of points you want: "))

# ===== Headless Mode Config =====

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--remote-debugging-port=9222')


# Add argument "options=chrome_options" for headless mode
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://humanbenchmark.com/tests/number-memory")

general_timeout = 10

# Accepting Cookies
try:
    accept_cookies = WebDriverWait(driver, general_timeout).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-47sehv"))
    )
    accept_cookies.click()

except TimeoutException:
    print("Timed out waiting for the cookies notice button to load")
    exit()


action = ActionChains(driver)


start_button = driver.find_element(By.CLASS_NAME, "css-de05nr")
start_button.click()

start_time = time.time()

seen_words = set()


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


for _ in range(desired_points):
    main_loop()

main_loop(give_up=True)


# Getting Percentage
try:

    percentage_element = WebDriverWait(driver, general_timeout).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-bv69nn"))
    )
    percentage = percentage_element.text

except TimeoutException:
    print("Timed out waiting for the percentage to load")
    percentage = "* Percentage timed out *"


report = f"""

You successfully got a score equal or higher than {desired_points}
Percentage:Top {percentage}

"""

print(report)


input("Press any key to exit")
exit()



