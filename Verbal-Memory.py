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

driver.get("https://humanbenchmark.com/tests/verbal-memory")


timeout = 10

# Accepting Cookies
try:
    accept_cookies = WebDriverWait(driver, timeout).until(
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

for _ in range(desired_points):
    word_element = driver.find_element(By.CLASS_NAME, "word")
    word = word_element.text

    if word in seen_words:
        seen_button = driver.find_elements(By.CSS_SELECTOR, ".css-de05nr.e19owgy710")[0]
        seen_button.click()

    else:
        new_button = driver.find_elements(By.CSS_SELECTOR, ".css-de05nr.e19owgy710")[1]
        new_button.click()
        seen_words.add(word)

end_time = time.time()
delta_time = end_time - start_time

alive = True

while alive:
    try:
        try_to_give_up = driver.find_elements(By.CSS_SELECTOR, ".css-de05nr.e19owgy710")[0]
        try_to_give_up.click()
    except IndexError:
        alive = False

save_score = driver.find_element(By.CSS_SELECTOR, ".css-qm6rs9.e19owgy710")
save_score.click()


# Getting Percentage
try:

    percentage_element = WebDriverWait(driver, timeout).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-bv69nn"))
    )
    percentage = percentage_element.text

except TimeoutException:
    print("Timed out waiting for the percentage to load")
    percentage = "* Percentage timed out *"


report = f"""

You successfully got a score equal or higher than {desired_points}
Percentage:Top {percentage}
Time taken: {round(delta_time,3)}s
Points per second: {round(desired_points/delta_time,3)}

"""

print(report)


input("Press any key to exit")
exit()
