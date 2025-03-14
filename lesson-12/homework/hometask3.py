import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")

# Wait for categories to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "itemc"))
)

buttons = driver.find_elements(By.ID, "itemc")
if len(buttons) > 1:
    buttons[1].click()  # Click second category
else:
    print("No second button found!")

time.sleep(3)  # Let products load

# Click "Next" button if it exists
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "next2"))
    )
    next_button.click()
    time.sleep(3)  # Wait for products to load
except:
    print("Next button not found or not clickable.")

# Extract product details
notebooks = []
products = driver.find_elements(By.CLASS_NAME, "card-block")

for product in products:
    name = product.find_element(By.CLASS_NAME, "card-title").text
    price = product.find_element(By.TAG_NAME, "h5").text
    description = product.find_element(By.CLASS_NAME, "card-text").text

    notebooks.append({"name": name, "price": price, "description": description})

# Save data
json_data = json.dumps(notebooks, indent=4)
print(json_data)

with open("products.json", "w") as file:
    json.dump(notebooks, file, indent=4)

driver.quit()
