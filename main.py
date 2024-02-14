import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from scripts.AimTrainer import aim_trainer
from scripts.ChimpTest import chimp_test
from scripts.NumberMemory import number_memory
from scripts.TypingTest import typing_test
from scripts.VisualMemory import visual_memory
from scripts.VerbalMemory import verbal_memory
from scripts.ReactionTime import reaction_time
from scripts.SequenceMemory import sequence_memory

# ===== Headless Mode Config =====
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--remote-debugging-port=9222')

# Add argument "options=chrome_options" for headless mode
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

tests = {'typing': typing_test,
         'sequence': sequence_memory,
         'aim': aim_trainer,
         'reaction': reaction_time,
         'number': number_memory,
         'chimp': chimp_test,
         'visual': visual_memory,
         'verbal': verbal_memory}

url = {'typing': "typing",
       'sequence': "sequence",
       'aim': "aim",
       'reaction': "reactiontime",
       'number': "number-memory",
       'chimp': "chimp",
       'visual': "memory",
       'verbal': "verbal-memory"}

command = input("Which test would you like to ace? (See docs for commands)\n> ")


def load_website(command):
    driver.get(f"https://humanbenchmark.com/tests/{url[command]}")

    # Accepting Cookies
    try:
        accept_cookies = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "css-47sehv"))
        )
        accept_cookies.click()

    except TimeoutException:
        print("Timed out waiting for the cookies notice button to load")
        pass

    # Some test do not have start button
    try:
        start_test = WebDriverWait(driver, 2).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".css-de05nr.e19owgy710"))
        )
        start_test.click()

    except TimeoutException:
        pass


target_score = 50


try:
    target_score = max(1, int(input('Target score: ')))
except ValueError:
    target_score = 50
    print("Invalid response. Target score set to 50")

load_website(command)

# The Main Loop
start_time = time.time()

# ========================
report_parameters = tests[command](driver, start_time, target_score)

# ========================

end_time = time.time()
delta_time = end_time - start_time

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
Score: {score}
Test completed in: {round(delta_time,3)}s
Percentage: Top {percentage}

{report_parameters}
"""

print(report)


input("Press any key to exit")
exit()
