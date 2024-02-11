import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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

try:
    target_score = min(37, max(1, int(input('Target score [1-37]: '))))
except ValueError:
    target_score = 37
    print("Invalid response. Target score set to 37")

driver.get("https://humanbenchmark.com/tests/chimp")

# Accepting Cookies
try:
    accept_cookies = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-47sehv"))
    )
    accept_cookies.click()

except TimeoutException:
    print("Timed out waiting for the cookies notice button to load")
    exit()

start_test = driver.find_element(By.CSS_SELECTOR, ".css-de05nr.e19owgy710")
start_test.click()

start_time = time.time()

# The Main Loop
for level in range(1, target_score+1):

    print(f"\rRunning Level {level} of {target_score}...", end="")
    # Finds all the targets
    for target in range(1, level+4):
        driver.find_element(By.XPATH, f'//div[@data-cellnumber="{target}"]').click()

    # Game ends at level 37 (41 squares)
    if level == 37:
        break

    continue_button = driver.find_element(By.CSS_SELECTOR, ".css-de05nr.e19owgy710")
    continue_button.click()

# Getting the numerical score
score = driver.find_element(By.CLASS_NAME, "css-0").text

end_time = time.time()
delta_time = end_time - start_time

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

squares_clicked = sum((4 + n) for n in range(38))

report = f"""

Test completed in: {round(delta_time,3)}s
Squares_clicked: {squares_clicked}
Squares per second: {round(squares_clicked/delta_time, 2)}
You got a score of: {score}
Percentage: Top {percentage}

"""

print(report)


input("Press any key to exit")
exit()
