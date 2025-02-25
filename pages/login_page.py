from automation.lib.helpers import Helper

class ElementMap:
    """Stores XPaths for elements on the Login page"""
    USERNAME_XPATH = "//input[@name='username']"
    PASSWORD_XPATH = "//input[@name='password']"
    LOGIN_BUTTON_XPATH = "//button[text()='Login']"
    ERROR_MESSAGE_XPATH = "//div[@class='error']"  
  

class LoginPage(Helper):
    """Page Object Model for Login Page"""
    
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.element_map = ElementMap()
        self.logger.info("Navigating to login page.")
        self.driver.get('https://practice.expandtesting.com/login')
    
    def enter_username(self, username):
        """Enters the username in the username field"""
        if self.send_keys_to_element(self.driver, ElementMap.USERNAME_XPATH, username):
            self.logger.info('Successfully entered username.')
            return True
        else:
            self.logger.error('Unable to enter username.')
            return False
        
    def enter_password(self, password):
        """Enters the password in the password field"""
        if self.send_keys_to_element(self.driver, ElementMap.PASSWORD_XPATH, password):
            self.logger.info('Successfully entered password.')
            return True
        else:
            self.logger.error('Unable to enter password.')
            return False
            
    def click_login_button(self):
        """Clicks the login button"""
        if self.click_element(self.driver, ElementMap.LOGIN_BUTTON_XPATH):
            self.logger.info('Successfully clicked login button.')
            return True
        else:
            self.logger.error('Unable to click on login button.')
            return False
    
    def get_error_message(self):
        """Gets the error message, if any"""
        error_message = self.driver.find_element_by_xpath(self.element_map.ERROR_MESSAGE_XPATH).text
        self.logger.info(f'Error message found: {error_message}')
        return error_message

    def login(self, username, password):
        """Performs the entire login action"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return True
