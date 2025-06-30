from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

with open("down.txt", 'r') as file:
    links = file.readlines()

# Configure Firefox options for private browsing
firefox_options = Options()
firefox_options.add_argument("-private")
profile_path= r'C:\Users\Deviant-343\AppData\Roaming\Mozilla\Firefox\Profiles\ekaupd7q.default-release'
firefox_profile = FirefoxProfile(profile_path)
firefox_options.profile = firefox_profile
driver = webdriver.Firefox( options=firefox_options)

# Iterate over each link
for link in links:
    link = link.strip()
    driver.get(link[2:])
        
    # Allow the page to load
    time.sleep(2)
    button = driver.find_element(By.XPATH, '//button[@class="link-button text-5xl"]')
    button.click()
    time.sleep(1)  # Wait to observe the effect
    # Try to find and click the button again
    button.click()
    time.sleep(1)  # Wait to observe the effect
    # close tab
    tabs = driver.window_handles #get list of open windows
    driver.switch_to.window(tabs[1])
    driver.close() #close the current window
    driver.switch_to.window(tabs[0]) #return to first window

driver.quit()
print("All links processed.")
