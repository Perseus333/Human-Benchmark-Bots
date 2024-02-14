import time

from selenium.webdriver.common.by import By


def chimp_test(driver, start_time, target_score):

    target_score = 37

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

    end_time = time.time()
    squares_clicked = sum((4 + n) for n in range(target_score))
    delta_time = end_time - start_time

    chimp_parameters = f"""
Squares_clicked: {squares_clicked}
Squares per second: {round(squares_clicked/delta_time, 2)}
    
    """
    return chimp_parameters
