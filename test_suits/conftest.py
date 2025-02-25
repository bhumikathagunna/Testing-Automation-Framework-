import pytest
import sys
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="class")
def init_logger(request):
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    request.cls.logger = logger

    yield
    logger.info("Tearing down the logger.")
    logger.removeHandler(handler)

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    logger = request.cls.logger
    logger.info("Initializing WebDriver...")

    chrome_options = Options()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    logger.info("WebDriver initialized successfully.")

    driver.maximize_window()
    driver.implicitly_wait(10)
    logger.info("Browser window maximized and implicit wait set.")

    request.cls.driver = driver

    yield driver

    logger.info("Quitting WebDriver.")
    driver.quit()
    logger.info("WebDriver closed successfully.")
