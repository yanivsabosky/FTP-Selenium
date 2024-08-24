from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Finds and returns the text of the first 'num_headings' heading elements (h1-h6) on a webpage
def find_headings(driver, num_headings=2):
    # Use a single XPath to find all heading elements (h1 to h6)
    xpath = "//h1 | //h2 | //h3 | //h4 | //h5 | //h6"
    headings = driver.find_elements(By.XPATH, xpath)

    # Filter out headings with no text or only whitespace
    filtered_headings = [heading.text.strip() for heading in headings if heading.text.strip()]


    # Return the text of the headings, limited to the requested number
    # This list comprehension extracts the text from each heading element
    # The slice [:num_headings] ensures we don't return more than requested
    return [heading.text for heading in headings[:num_headings]]

# Finds and returns the text of the first 'num_paragraphs' paragraph elements on a webpage
def find_paragraphs(driver, num_paragraphs=2):
    # Use XPath to find all paragraph elements
    xpath = "//p"
    paragraphs = driver.find_elements(By.XPATH, xpath)

    # Filter out paragraphs with no meaningful content
    filtered_paragraphs = [p.text.strip() for p in paragraphs if p.text.strip()]

    # Return the text of the paragraphs, limited to the requested number
    return filtered_paragraphs[:num_paragraphs]


