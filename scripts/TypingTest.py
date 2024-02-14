from selenium.webdriver.common.by import By


def typing_test(driver, start_time, target_score):

    text = ""
    position = 0
    raw_text = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div/span')
    for raw_character in raw_text:
        character = raw_character.text
        if character == "":
            character = " "
        text += character
        print("\r" + " " * 50 + "\r", end='', flush=True)
        print(f"Character {position} out of {len(raw_text)} "
              f"({round(position/len(raw_text)*100, 1)}%)", end='', flush=True)

        position += 1

    print("\r" + " " * 50 + "\r", end='', flush=True)
    print("Text Read Successfully (100%)")

    typing_form = driver.find_element(By.CSS_SELECTOR, ".letters.notranslate")

    typing_form.send_keys(text)

    typing_parameters = f"Words written: {round(len(raw_text)/5)}"
    return typing_parameters
