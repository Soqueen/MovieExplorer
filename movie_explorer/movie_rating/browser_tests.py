import datetime
import os
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from sys import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#   Check the os platform of running computer
if platform == 'linux':
    driver_name = 'chromedriver_linux'
elif platform == 'win32':
    driver_name = 'chromedriver'
else:
    driver_name = 'chromedriver_mac'

DRIVER_DIR = os.path.join(BASE_DIR, "webdrivers", driver_name)

# If you used different port than 8000, you can change it here.
# But, make sure DO NOT push your change into Git
LOCAL_URL = 'http://127.0.0.1:8000/'
URL = 'http://movieexplorer.ddns.net/'
WAIT_TIME = 3  # wait time for browser to stay open for 3 seconds


class ChromeTest(unittest.TestCase):
    # Anything declared in setUp will be executed for all test cases
    def setUp(self):
        # clear database
        self.driver = webdriver.Chrome(DRIVER_DIR)
        # 1. Change to 'LOCAL_URL' instead of 'URL' if you test your local running server.
        # 2. Make sure to run local server before running the TestCases.
        # 3. Finally, Make sure DO NOT push your change here into Git
        self.base_url = LOCAL_URL

    # An individual test case. Must start with 'test_' (as per unittest module)
    def test_home_page(self):
        driver = self.driver
        # Go to google.com
        driver.get(self.base_url)
        # A test to ensure the page has keyword 'The Movie Explorer' in the page title
        self.assertEqual('The Movie Explorer', driver.title)

        # Pauses the screen for 5 seconds so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results. Make sure to put your image test name.
        self.take_screen_shot('test_home_page')

    def test_register(self):
        # Go to google.com
        self.driver.get(os.path.join(self.base_url, 'register'))
        # Pauses the screen for 5 seconds so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        # Input username
        # Find and select the search box element on the page
        try:
            search_box = self.driver.find_element_by_name('username')
            search_box.send_keys('heng')
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Input Email
        try:
            search_box = self.driver.find_element_by_name('email')
            search_box.send_keys('sok@lim.ca')
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Input Password
        try:
            search_box = self.driver.find_element_by_name('password')
            search_box.send_keys('heng')
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Input Confirm Password
        try:
            search_box = self.driver.find_element_by_name('confirm_pwd')
            search_box.send_keys('heng')
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Submit the search box form
        search_box.submit()

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_register')

    def test_login(self):
        # Go to google.com
        self.driver.get(os.path.join(self.base_url, 'login'))
        # Pauses the screen for 5 seconds so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        # Input username
        try:
            search_box = self.driver.find_element_by_name('username')
            search_box.send_keys('sokheng')
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Input Password
        try:
            search_box = self.driver.find_element_by_name('password')
            search_box.send_keys('sokheng')
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Submit the search box form
        search_box.submit()

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_login')

    def take_screen_shot(self, test_name):
        """
        Taking screen shot of the test result. The purpose is need when the test fail
        :param test_name: Name of screen shot
        :return:
        """
        now = datetime.datetime.now()
        directory = os.path.join(BASE_DIR, 'test_results_img', now.strftime("%Y-%m-%d"))
        if not os.path.exists(directory):
            os.makedirs(directory)
        image_name = '.'.join([test_name + now.strftime("_%H:%M:%S"), 'png'])
        return self.driver.save_screenshot(os.path.join(directory, image_name))

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
