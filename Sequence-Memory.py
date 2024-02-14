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
    target_score = max(1, int(input('Target score: ')))
except ValueError:
    target_score = 50
    print("Invalid response. Target score set to 50")

driver.get("https://humanbenchmark.com/tests/sequence")

# Accepting Cookies
try:
    accept_cookies = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "css-47sehv"))
    )
    accept_cookies.click()

except TimeoutException:
    print("Timed out waiting for the cookies notice button to load")
    pass

start_test = driver.find_element(By.CSS_SELECTOR, ".css-de05nr.e19owgy710")
start_test.click()

start_test_time = time.time()

# The Main Loop
grid = []

# Getting the XPATH of the squares in the main grid
for row in [1, 2, 3]:
    for col in [1, 2, 3]:
        square_element = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[4]/div[1]'
                                                       f'/div/div/div/div[2]/div/div[{row}]/div[{col}]')
        print(f"[{row}][{col}]: Found")
        grid.append(square_element)


for level in range(1, target_score+1):
    sequence = []
    # Getting to the desired score
    # The sequence length at one level is the same as the level number
    while len(sequence) < level:
        # In case any key is missed, time out
        start_time = time.time()
        if (time.time() - start_time) > (level * 2 + 2):
            print("Timed out")
            print("Press any key to exit")
            input()
            exit()
        # Checks all the squares for 'active' ones
        for square in grid:
            if square.get_attribute('class') == 'square active':
                # To not add the same square twice (it can't happen)
                if len(sequence) == 0 or square != sequence[-1]:
                    sequence.append(square)
                    print(f"[{grid.index(square)}]: Added to Sequence")
                    break

    # Just to make sure that the sequence has finished and the elements are clickable
    time.sleep(0.5)

    if level < target_score:
        for step in sequence:
            step.click()
            print(f"Step {grid.index(step)} clicked")

    # Ends the game by missing the first click
    else:
        for square in grid:
            if square != sequence[0]:
                square.click()
                break
        # To ensure the score element loads
        time.sleep(0.5)
        break
# Getting the numerical score
score = driver.find_element(By.CLASS_NAME, "css-0").text

end_time = time.time()
delta_time = end_time - start_test_time

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
