from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import chromedriver_autoinstaller

# Step 1: Set Up ChromeDriver
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

try:
    # Step 2: Load the webpage
    url = "https://www.inmotionhosting.com/"
    driver.get(url)
    print("Page loaded successfully!")

    # Step 3: Accept Cookies
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        ).click()
        print("Accepted all cookies successfully!")
    except Exception:
        print("No cookie popup found or already dismissed.")

    # Step 4: Wait for Hosting Plans Section
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "imh-rostrum-card"))
    )
    print("Hosting plans loaded!")

    # Step 5: Parse Hosting Plan Containers
    hosting_plans = []
    cards = driver.find_elements(By.CLASS_NAME, "imh-rostrum-card")

    for i, card in enumerate(cards):
        try:
            # Scroll to the current card
            driver.execute_script("arguments[0].scrollIntoView();", card)
            time.sleep(1)

            # Extract Plan Name
            plan_name = card.find_element(By.CLASS_NAME, "imh-rostrum-card-title").text.strip()

            # Extract Plan Description
            description = card.find_element(By.CLASS_NAME, "imh-rostrum-sub-title").text.strip()

            # Extract Active Price (from the connected-switcher)
            active_price = card.find_element(By.CSS_SELECTOR, "div.active.imh-switcher .rostrum-price").text.strip()

            # Extract Additional Features
            feature_list = card.find_elements(By.CSS_SELECTOR, "ul.imh-rostrum-details-list li")
            features = [feature.text.strip() for feature in feature_list]

            # Store the extracted data
            hosting_plans.append({
                "Plan Name": plan_name,
                "Description": description,
                "Price": active_price,
                "Features": "; ".join(features)
            })
            print(f"Extracted data for plan {i+1}: {plan_name}")

        except Exception as e:
            print(f"Error extracting data for card {i+1}: {e}")

    # Step 6: Save Data to CSV
    if hosting_plans:
        df = pd.DataFrame(hosting_plans)
        print("\nExtracted Hosting Plan Data:")
        print(df)
        df.to_csv("detailed_inmotion_hosting_plans.csv", index=False)
        print("Data successfully saved to 'detailed_inmotion_hosting_plans.csv'")
    else:
        print("No hosting plans found!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Step 7: Close the browser
    driver.quit()
    print("WebDriver closed.")


print(df.head())
