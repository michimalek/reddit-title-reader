from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Add options to disable infobar, start browser maximized and disable extensions for the ChromeDriver
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Option to disable notification request
# Pass the argument 0 to allow and 1 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

# Initiate Chromedriver and send reddit URL
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.reddit.com/r/SuccessionTV/top/?t=all")

# Loop for scrolling down the page
SCROLL_PAUSE_TIME = 0.25
for i in range(850):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
print("Scrolling finished")

# Transform html source code to a BeautifulSoup object and safe all titles of reddit post in the list titles
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
titles = soup.find_all("h3",class_="_eYtD2XCVieq6emjKBH3m")

# Write everything into a formated .csv
with open('results/succession_titles.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["titles"])
    for title in titles:
        writer.writerow(title)
    f.close()
driver.quit()