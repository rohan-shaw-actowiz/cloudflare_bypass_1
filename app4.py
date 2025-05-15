from seleniumbase import Driver

driver = Driver(uc=True, headless=False)

url = "https://www.hisco.com/"

driver.uc_open_with_reconnect(url, reconnect_time=6)

driver.uc_gui_click_captcha()

driver.save_screenshot("cloudflare-challenge.png")

driver.quit()
