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

# ===== Headless Mode Config =====
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--remote-debugging-port=9222')

# Add argument "options=chrome_options" for headless mode
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://humanbenchmark.com/tests/aim")

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

# The Main Loop
start_time = time.time()

for _ in range(31):  # 30 Targets + 1 Target to start the test
    t0 = time.time()

    # Finding the target
    target = driver.find_element(By.CSS_SELECTOR, ".css-17nnhwz.e6yfngs4")
    action.move_to_element(target).click().perform()

end_time = time.time()
delta_time = end_time - start_time

# Getting the numerical score
score = driver.find_element(By.CLASS_NAME, "css-0").text

# Saving the score
save_score = driver.find_element(By.CSS_SELECTOR, ".css-qm6rs9.e19owgy710")
save_score.click()


# Getting Percentage
try:

    percentage_element = WebDriverWait(driver, timeout).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-1l6lsyu"))
    )
    percentage = percentage_element.text

except TimeoutException:
    print("Timed out waiting for the percentage to load")
    percentage = "* Percentage timed out *"


report = f"""

Test completed in: {round(delta_time,3)}s
You got an average time of: {score}
Percentage: Top {percentage}

"""

print(report)


input("Press any key to exit")
exit()
