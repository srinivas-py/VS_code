from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Optional: set Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keeps browser open after script ends

# Path to ChromeDriver (optional if already in PATH)
# Example: r"C:\path\to\chromedriver.exe"
service = Service()

# Create WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Maximize the browser window
driver.maximize_window()

# Open Amazon website
driver.get("https://www.amazon.in")

# Print page title (optional)
print("Opened:", driver.title)
