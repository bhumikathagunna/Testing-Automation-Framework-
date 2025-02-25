import pytest
import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pages.login_page import LoginPage  
from test_suits.base_test import BaseTest  

class TestLogin(BaseTest):
    """Test case class for login functionality"""

    def test_valid_login(self):
        login_page = LoginPage(self.driver, self.logger) 
        assert login_page.login("practice", "SuperSecretPassword!") 

    
