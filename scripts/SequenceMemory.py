import time

from selenium.webdriver.common.by import By


def sequence_memory(driver, start_time, target_score):

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
        start_time = time.time()
        while len(sequence) < level:
            # In case any key is missed, time out
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

    sequence_parameters = ""
    return sequence_parameters
