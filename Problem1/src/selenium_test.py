from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class FrontendBackendTest(unittest.TestCase):
    def setUp(self):
        # Use webdriver-manager to automatically manage ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def test_greeting_message(self):
        driver = self.driver

        # Ensure frontend URL is correct
        node_port = "50983"  # Replace with your actual NodePort
        driver.get(f"http://127.0.0.1:{node_port}/")
        
        # Allow some time for the page to load
        time.sleep(5)

        # Fetch the greeting message displayed on the frontend
        greeting_message = driver.find_element(By.TAG_NAME, "h1").text

        # Check if the greeting message is as expected
        self.assertEqual(greeting_message, "Hello from the Backend!")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

