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

driver.get("https://humanbenchmark.com/tests/typing")

# Accepting Cookies
try:
    accept_cookies = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-47sehv"))
    )
    accept_cookies.click()

except TimeoutException:
    print("Timed out waiting for the cookies notice button to load")
    exit()


# Storing all the letters
text = ""
position = 0
raw_text = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div/span')
for raw_character in raw_text:
    character = raw_character.text
    if character == "":
        character = " "
    text += character
    print("\r" + " " * 50 + "\r", end='', flush=True)
    print(f"Character {position} out of {len(raw_text)} ({round(position/len(raw_text)*100, 1)}%)", end='', flush=True)

    position += 1


print("\r" + " " * 50 + "\r", end='', flush=True)
print("Text Read Successfully (100%)")

typing_form = driver.find_element(By.CSS_SELECTOR, ".letters.notranslate")

time_start = time.time()

typing_form.send_keys(text)

time_end = time.time()
delta_time = time_end - time_start


score = driver.find_element(By.CLASS_NAME, "css-0").text

submit_button = driver.find_element(By.CSS_SELECTOR, ".css-qm6rs9.e19owgy710")
submit_button.click()

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

WPM: {score}
Percentage: Top {percentage}

Test completed in: {round(delta_time,3)}s
Words written: {round(len(raw_text)/5)}

"""

print(report)


input("Press any key to exit")
exit()
