import os
import datetime
import time
import requests
import unittest
from selenium import webdriver
from sys import platform
from xml.etree import ElementTree
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
URL = 'http://104.131.51.38:8000/'
LOCAL_URL = 'http://127.0.0.1:8000/'

#   Check the os platform of running computer
if platform == 'linux':
    driver_name = 'chromedriver_linux'
elif platform == 'win32':
    driver_name = 'chromedriver'
else:
    driver_name = 'chromedriver_mac'

DRIVER_DIR = os.path.join(BASE_DIR, "webdrivers", driver_name)


class ChromeTest(unittest.TestCase):
    # Anything declared in setUp will be executed for all test cases
    def setUp(self):
        self.driver = webdriver.Chrome(DRIVER_DIR)
        self.base_url = URL  # Change to 'LOCAL_URL' if you test your local running server
        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

    # An individual test case. Must start with 'test_' (as per unittest module)
    def test_home_page(self):
        driver = self.driver
        # Go to google.com
        driver.get(self.base_url)
        # A test to ensure the page has keyword 'The Movie Explorer' in the page title
        self.assertEqual('The Movie Explorer', driver.title)

        # Pauses the screen for 5 seconds so we have time to confirm it arrived at the right page
        time.sleep(3)

        # Take a screen shot of the results
        self.take_screen('test_home_page')

    def test_register(self):
        # Go to google.com
        self.driver.get(os.path.join(self.base_url, 'register'))
        # Pauses the screen for 5 seconds so we have time to confirm it arrived at the right page
        time.sleep(3)

        # Input username
        # Find and select the search box element on the page
        search_box = self.driver.find_element_by_name('username')
        # Enter text into the search box
        search_box.send_keys('heng')

        # Input Email
        search_box = self.driver.find_element_by_name('email')
        search_box.send_keys('sok@lim.ca')

        # Input Password
        search_box = self.driver.find_element_by_name('password')
        search_box.send_keys('heng')

        # Input Confirm Password
        search_box = self.driver.find_element_by_name('confirm_pwd')
        search_box.send_keys('heng')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Submit the search box form
        search_box.submit()

        # Can also use Keys function to submit
        # search_box.send_keys(Keys.RETURN)

        # Another pause so we can see what's going on
        time.sleep(3)

        # Take a screen shot of the results
        self.take_screen('test_register')

    def test_login(self):
        # Go to google.com
        self.driver.get(os.path.join(self.base_url, 'login'))
        # Pauses the screen for 5 seconds so we have time to confirm it arrived at the right page
        time.sleep(3)

        # Input username
        search_box = self.driver.find_element_by_name('username')
        search_box.send_keys('sokheng')

        # Input Password
        search_box = self.driver.find_element_by_name('password')
        search_box.send_keys('sokheng')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Submit the search box form
        search_box.submit()

        # Can also use Keys function to submit
        # search_box.send_keys(Keys.RETURN)

        # Another pause so we can see what's going on
        time.sleep(5)

        # Take a screen shot of the results
        self.take_screen('test_login')

    def take_screen(self, test_name):
        """
        Taking screen shot of the test result. The purpose is need when the test fail
        :param test_name: Name of screen shot
        :return:
        """
        now = datetime.datetime.now()
        directory = os.path.join(BASE_DIR, 'test_result', now.strftime("%Y-%m-%d"))
        if not os.path.exists(directory):
            os.makedirs(directory)
        image_name = '.'.join([test_name + now.strftime("_%H:%M:S"), 'png'])
        return self.driver.save_screenshot(os.path.join(directory, image_name))

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
