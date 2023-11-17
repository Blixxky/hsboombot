import time
import random
import pyautogui
import cv2

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"Leaving battle in {remaining} seconds...")
        time.sleep(1)

def find_and_click(image_path, confidence=0.7, sleep_time=0):
    if sleep_time > 0:
        print(f"Waiting for {image_path}...")
        if image_path == image_sequence[3]:
            countdown_timer(int(sleep_time))
        else:
            time.sleep(sleep_time)
    else:
        print(f"Looking for {image_path}...")

    location = None
    while location is None:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        screenshot = cv2.imread("screenshot.png")
        template = cv2.imread(image_path)

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= confidence:
            location = (max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2)
        else:
            print(f"Unable to locate {image_path}. Retrying...")
            with open("BOOM.LOG", "a") as log_file:
                log_file.write(f"Unable to locate {image_path}. Retrying...\n")

    # Add natural mouse movement before clicking
    pyautogui.moveTo(location, duration=random.uniform(0.1, 0.5))

    pyautogui.click()
    print(f"Clicked on {image_path}")

# Main loop
rounds = 0
image_sequence = ["portrait.png", "play.png", "confirm.png", "settings.png", "leave.png", "defeat.png"]

while True:
    find_and_click(image_sequence[0], confidence=0.7, sleep_time=3)
    find_and_click(image_sequence[1], confidence=0.7, sleep_time=6)
    find_and_click(image_sequence[2], confidence=0.7, sleep_time=15)
    find_and_click(image_sequence[3], confidence=0.7, sleep_time=random.uniform(1111, 1222))
    find_and_click(image_sequence[4], confidence=0.7, sleep_time=3)
    find_and_click(image_sequence[5], confidence=0.7, sleep_time=4)

    rounds += 1
    print(f"Completed round {rounds}")

    # Log the completion of each round
    with open("BOOM.LOG", "a") as log_file:
        log_file.write(f"Completed round {rounds}\n")
