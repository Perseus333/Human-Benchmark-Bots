import copy
import math
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# Wait for load function
def wait_for_load(xpath):
    try:
        return WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        print('driver timeout')
        exit()


# Waiting for a grid update
def wait_grid_update():
    prev_grid_html = copy.copy(grid.get_attribute('outerHTML'))
    while (grid_html_ := copy.copy(grid.get_attribute('outerHTML'))) == prev_grid_html:
        time.sleep(0.05)
    return grid_html_


def complete_level(give_up=False):

    grid_html = wait_grid_update()

    # make active squares list
    selected_squares = []

    # extract active squares from html
    square_class_list = grid_html.split('class')[2:]
    grid_size = int(math.sqrt(len(square_class_list)))

    # add the active squares to the list in row, column format
    for i, square_class in enumerate(square_class_list):
        if (not give_up and square_class[2] == 'a') or (give_up and square_class[2] != 'a'):
            # Adjust the index calculation based on your grid size and requirements
            row = i // grid_size + 1
            col = i % grid_size + 1
            selected_squares.append((row, col))

            if give_up and selected_squares == 3:
                break

    wait_grid_update()

    # click on the squares
    for pos in selected_squares:
        square = driver.find_element(
            By.XPATH, f'//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[{pos[0]}]/div[{pos[1]}]')
        square.click()

    time.sleep(1)


# ===== Headless Mode Config =====
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--remote-debugging-port=9222')


# Add argument "options=chrome_options" for headless mode
# Run driver preemptively
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Assigning Target Score
try:
    target_score = max(1, int(input('Target score: ')))
except ValueError:
    target_score = 10


driver.get("https://humanbenchmark.com/tests/memory")


# Accepting Cookies
try:
    accept_cookies = wait_for_load("//button[@mode='primary' and @size='large' and span[text()='AGREE']]")
    accept_cookies.click()
except TimeoutException:
    print("Timed out waiting for the cookies notice button to load")
    exit()

# click start button
wait_for_load('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button').click()

# create a grid object
grid = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div')

# Getting the score
for score in range(target_score):
    print(f'\rLevel: {score + 1} of {target_score}', end='', flush=True)
    complete_level()


# Giving up
print('\nEnding the game...')

for _ in range(3):
    complete_level(give_up=True)
print('\nGame ended successfully.')

# Getting the score
score = driver.find_element(By.CLASS_NAME, "css-0").text

submit_button = driver.find_element(By.CSS_SELECTOR, ".css-qm6rs9.e19owgy710")
submit_button.click()

# Getting Percentage
try:
    percentage_element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-bv69nn"))
    )
    percentage = percentage_element.text

except TimeoutException:
    print("Timed out waiting for the percentage to load")
    percentage = "* Percentage timed out *"


report = f"""

{score}
Percentage: Top {percentage}

"""

print(report)

input()
exit()
