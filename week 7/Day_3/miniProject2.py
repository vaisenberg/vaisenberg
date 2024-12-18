#there are no pop ups
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import chromedriver_autoinstaller

# Installing and setting up ChromeDriver
chromedriver_autoinstaller.install()

# Starting Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Loading the webpage
    url = "https://www.scrapethissite.com/pages/frames/"
    driver.get(url)
    print("Page loaded successfully!")
# Waiting for page content to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "container"))
    )
    print("Page content loaded successfully.")
 # Switching to the iframe with the turtle families list
    iframe = driver.find_element(By.ID, "iframe")
    driver.switch_to.frame(iframe)
    print("Switched to iframe.")
# Parse the content inside the iframe using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
# Extracting the turtle families
    turtle_families = []
    links = []
    images = []
    
 # Locating  all family cards
    family_cards = soup.find_all("div", class_="col-md-4 turtle-family-card")
    for card in family_cards:
        family_name = card.find("h3", class_="family-name").get_text(strip=True)
        link = card.find("a")["href"]
        image = card.find("img")["src"]
 # Adding the family name, link, and image to the lists
        turtle_families.append(family_name)
        links.append(link)
        images.append(image)
    
#Saving all the data
    turtles_data = pd.DataFrame({
        "Turtle Family": turtle_families,
        "Link": links,
        "Image URL": images
    })
    
    turtles_data.to_csv("turtle_families_with_links_images.csv", index=False)
    print("Data saved to 'turtle_families_with_links_images.csv'.")
    print(turtles_data.head())

    # Switch back to the main page
    driver.switch_to.default_content()
    print("Switched back to the main page.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
    print("WebDriver closed.")
