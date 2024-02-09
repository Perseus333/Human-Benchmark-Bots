import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# ===== Headless Mode Config =====
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--remote-debugging-port=9222')

# Add argument "options=chrome_options" for headless mode
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://humanbenchmark.com/tests/reactiontime")

# Accepting Cookies
try:
    accept_cookies = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-47sehv"))
    )
    accept_cookies.click()

except TimeoutException:
    print("Timed out waiting for the cookies notice button to load")
    exit()


# The Main Loop

driver.find_element(By.CLASS_NAME, "view-splash").click()


i = 0
while i < 5:

    try:
        # Finding the target by XPATH
        target = driver.find_element(By.CLASS_NAME, 'view-go')
        target.click()
        target.click()
        i += 1

    except NoSuchElementException:
        pass

time.sleep(0.5)
# Getting the numerical score
score = driver.find_element(By.CLASS_NAME, "css-0").text

# Saving the score
save_score = driver.find_element(By.CSS_SELECTOR, ".css-qm6rs9.e19owgy710")
save_score.click()


# Getting Percentage
try:

    percentage_element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-1l6lsyu"))
    )
    percentage = percentage_element.text

except TimeoutException:
    print("Timed out waiting for the percentage to load")
    percentage = "* Percentage timed out *"


report = f"""

You got an average time of: {score}
Percentage: Top {percentage}

"""

print(report)


input("Press any key to exit")
exit()
