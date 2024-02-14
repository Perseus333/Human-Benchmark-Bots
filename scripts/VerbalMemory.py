import time

from selenium.webdriver.common.by import By


def verbal_memory(driver, start_time, target_score):

    seen_words = set()

    for _ in range(target_score):
        word_element = driver.find_element(By.CLASS_NAME, "word")
        word = word_element.text

        if word in seen_words:
            seen_button = driver.find_elements(By.CSS_SELECTOR, ".css-de05nr.e19owgy710")[0]
            seen_button.click()

        else:
            new_button = driver.find_elements(By.CSS_SELECTOR, ".css-de05nr.e19owgy710")[1]
            new_button.click()
            seen_words.add(word)

    alive = True

    while alive:
        try:
            try_to_give_up = driver.find_elements(By.CSS_SELECTOR, ".css-de05nr.e19owgy710")[0]
            try_to_give_up.click()
        except IndexError:
            alive = False
    delta_time = time.time() - start_time

    report = f"Points per second: {round(target_score / delta_time, 3)}"

    return report
