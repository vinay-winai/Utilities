from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

with open('down.txt', 'r') as file:
    links = file.readlines()[2:]

# Configure Firefox options for private browsing
firefox_options = Options()
firefox_options.add_argument("-private")

# Iterate over each link
for link in links:
    link = link.strip()
    try:
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(link)
        
        # Allow the page to load
        time.sleep(5)
        
        # Try to find and click the first button 'x'
        try:
            button = driver.find_element(By.XPATH, "//button[text()='x']")
            button.click()
            time.sleep(2)  # Wait to observe the effect
            
            # Try to find and click the button again
            button.click()
            time.sleep(2)  # Wait to observe the effect
            
        except NoSuchElementException:
            print(f"Button 'x' not found on page: {link}")
        
        # Close the tab
        driver.quit()
    
    except WebDriverException as e:
        print(f"Failed to load the page or other browser error for link: {link}\nError: {e}")

print("All links processed.")
