from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Helper:
    @staticmethod
    def click_element(driver, xpath, timeout=20):
        """Clicks on an element by XPath with a dynamic wait."""
        try:
            # Wait until the element is clickable
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            return True
        except Exception as e:
            print(f"Error occurred while clicking element: {e}")
            raise
            return False

    @staticmethod
    def send_keys_to_element(driver, xpath, keys, timeout=20):
        """Sends keys to an element by XPath with a dynamic wait."""
        try:
            # Wait until the element is visible
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            element.clear()  # Optional: Clears any existing text before sending keys
            element.send_keys(keys)
            return True
        except Exception as e:
            print(f"Error occurred while sending keys: {e}")
            raise
            return False
