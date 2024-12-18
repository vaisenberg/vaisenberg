import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import chromedriver_autoinstaller

# Install and set up ChromeDriver
chromedriver_autoinstaller.install()

# Start Chrome WebDriver in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode for faster scraping
driver = webdriver.Chrome(options=options)

try:
    # Load the webpage
    url = "https://www.inmotionhosting.com/shared-hosting"
    driver.get(url)
    print("Page loaded successfully!")

    # Accept Cookies if available
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        ).click()
        print("Accepted all cookies successfully!")
    except Exception:
        print("No cookie popup found or already dismissed.")

    # Wait for page content to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "container"))
    )
    print("Page content loaded successfully.")

    # Re-parse the page to get updated table
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Extract the table container
    table = soup.select_one(".imh-spec-table-container table")

    if not table:
        print("No table data found.")
        driver.quit()
        exit()

    # Extracting the header prices for each plan (excluding the 'Select' buttons)
    plan_headers = []
    prices = []
    for th in table.select("thead.desktop-view th"):
        plan_name = th.find("span", class_="column-title")
        price_container = th.select_one("div.imh-switcher.active .rostrum-price")

        if plan_name and price_container:
            plan_name_text = plan_name.get_text(strip=True)
            price_text = price_container.get_text(strip=True).replace('$', '')
            plan_headers.append(f"{plan_name_text} (${price_text}/mo)")
            prices.append(price_text)
        else:
            plan_headers.append("N/A")
            prices.append("N/A")

    # Extract features from the body (excluding any links related to "Select")
    features = []
    feature_rows = table.select("tbody.desktop-view tr")
    for row in feature_rows:
        feature_name = row.find("td", class_="tooltips-table")
        feature_values = row.find_all("td")[1:]  # Get all plan values for this feature
        if feature_name:
            feature_name_text = feature_name.get_text(strip=True)
            feature_values_text = [val.get_text(strip=True) for val in feature_values]
            features.append([feature_name_text] + feature_values_text)

    if not plan_headers or not features:
        print("No data found.")
        driver.quit()
        exit()
    # Create DataFrame for the features and prices
    data = []
    for feature, price in zip(features, prices):
        data.append(feature + [price])
    columns = ["Feature"] + plan_headers  # Adding plan names as headers
    df = pd.DataFrame(data, columns=columns)

    # Save to CSV
    df.to_csv("hosting_plans_data.csv", index=False)
    print("Data saved to 'hosting_plans_data.csv'.")
    print(df.head())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("WebDriver closed.")
