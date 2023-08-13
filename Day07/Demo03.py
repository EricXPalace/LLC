from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

option = Options()
# This line was abandon as Selenium is now pre-installed webdriver on it.
# option.chrome_executable_path = "C:\Users\USER\coding\Day05\chromedriver.exe"

with webdriver.Chrome(options=option) as driver:
    driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")

    for count in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(10)
    jobs = driver.find_elements(By.CLASS_NAME, "base-search-card__title")

    counter = 0
    for job in jobs:
        counter += 1
        print(f"{counter}.\t{job.text}")

        if counter % 5 == 0:
            print("==========================================")

    




