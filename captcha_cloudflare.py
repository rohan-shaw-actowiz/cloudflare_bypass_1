from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from seleniumbase import Driver
import time 
import pyautogui

def setup():
    driver = Driver(uc=True, headless=False, undetected=True)


    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    
    driver.maximize_window()

    return driver

def locate_and_click_captcha(driver):
    location = pyautogui.locateCenterOnScreen('captchaimg.png', confidence=0.8)
    if location:
        import random
        driver.uc_gui_click_captcha()
        pyautogui.moveTo(random.randint(0, 700), random.randint(0, 700))
    else:
        print("CAPTCHA checkbox not found. Make sure the image is visible and correct.")

driver = setup()

wait = WebDriverWait(driver, 20)

# url = "https://2captcha.com/demo/cloudflare-turnstile-challenge"
url = "https://www.inmuebles24.com/"

driver.uc_open_with_reconnect(url, reconnect_time=7)

locate_and_click_captcha(driver)

driver.save_screenshot("cloudflare-challenge2.png")

time.sleep(10)

driver.quit()