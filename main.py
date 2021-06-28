import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

#ENTER YOUR USERNAME AND PASSWORD ACCORDINGLY
FACEBOOK_USERNAME = "xyz@gmail.com"
FACEBOOK_PASSWORD = "PASSWORD"
chrome_driver_path = "D://Applications/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")
driver.maximize_window()
time.sleep(2)

login_button = driver.find_element_by_xpath("//*[@id='u2005023502']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login_button.click()
time.sleep(4)

#Switch to Facebook login window

try:
    facebook_login = driver.find_element_by_xpath("//*[@id='u276642426']/div/div/div[1]/div/div[3]/span/div[2]/button")
    facebook_login.click()
except NoSuchElementException:
    time.sleep(4)
    more_options= driver.find_element_by_xpath("//*[@id='u276642426']/div/div/div[1]/div/div[3]/span/button")
    more_options.click()
    time.sleep(4)
    facebook_login = driver.find_element_by_xpath("//*[@id='u276642426']/div/div/div[1]/div/div[3]/span/div[2]/button")
    facebook_login.click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to_window(fb_window)
print(driver.title)

#Login and hit enter
username = driver.find_element_by_xpath("//*[@id='email']")
username.send_keys(FACEBOOK_USERNAME)

password = driver.find_element_by_id("pass")
password.send_keys(FACEBOOK_PASSWORD)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to_window(base_window)
print(driver.title)
time.sleep(5)
#allow location
try:
    allow = driver.find_element_by_xpath("//*[@id='u276642426']/div/div/div/div/div[3]/button[1]")
    allow.click()
except NoSuchElementException:
    time.sleep(5)
time.sleep(2)
#disallow notification
notifications_off = driver.find_element_by_xpath("//*[@id='u276642426']/div/div/div/div/div[3]/button[2]")
notifications_off.click()
time.sleep(5)

for n in range(100):
    time.sleep(6)
    try:
        swipe_right = driver.find_element_by_xpath(
            "//*[@id='u2005023502']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span")
        swipe_right.click()
    except NoSuchElementException:
        swipe_right = driver.find_element_by_xpath(
            "//*[@id='u2005023502']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span")
        swipe_right.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
