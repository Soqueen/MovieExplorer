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
else:
    driver_name = 'chromedriver_mac'

DRIVER_DIR = os.path.join(BASE_DIR, "webdrivers", driver_name)

# If you used different port than 8000, you can change it here.
# But, make sure DO NOT push your change into Git
LOCAL_URL = 'http://127.0.0.1:8000/'
URL = 'http://movieexplorer.ddns.net/'
WAIT_TIME = 3  # wait time for browser to stay open for 3 seconds

# TAG ID
# TODO the tag may change
FILTER_BOX_TAG = 'genreOption'
FILTER_OPTION_TAG = 'option'
SORT_BOX_TAG = 'sortOption'
SORT_OPTION_TAG = 'option'


class ChromeTest(unittest.TestCase):
    # Anything declared in setUp will be executed for all test cases
    def setUp(self):
        # clear database
        self.driver = webdriver.Chrome(DRIVER_DIR)
        # 1. Change to 'LOCAL_URL' instead of 'URL' if you test your local running server.
        # 2. Make sure to run local server before running the TestCases.
        # 3. Finally, Make sure DO NOT push your change here into Git
        self.base_url = URL

    # An individual test case. Must start with 'test_' (as per unittest module)
    def test_home_page(self):
        self.driver.get(self.base_url)
        # A test to ensure the page has keyword 'The Movie Explorer' in the page title
        self.assertEqual('The Movie Explorer', self.driver.title)

        # Pauses the screen so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results. Make sure to put your image test name.
        self.take_screen_shot('test_homepage')

    # test_ST4_1_is_movie_List_Empty
    def test_st1(self):
        """
        Test for registration. Note, It is the left over from the first sprint, so we do not implement all the test cases
        :return:
        """
        self.driver.get(os.path.join(self.base_url, 'register'))
        # Pauses the screen so we have time to confirm it arrived at the right page
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
        self.take_screen_shot('test_st1')

    def test_st2(self):
        """
        Test for login. Note, It is the left over from the first sprint, so we do not implement  all the test cases
        :return:
        """
        self.driver.get(os.path.join(self.base_url, 'login'))
        # Pauses the screen so we have time to confirm it arrived at the right page
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
        self.take_screen_shot('test_st2')

    def test_st5_1(self):
        """
        Test to Sort the movies by release date acceding order.
        :return: None
        """
        self.driver.get(self.base_url)
        # Pauses the screen so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        # Sort select option
        try:
            # TODO the find may change
            sort_select = self.driver.find_element_by_name(SORT_BOX_TAG)
            for option in sort_select.find_elements_by_tag_name(SORT_OPTION_TAG):
                if option.text == 'Release Date Ascending':
                    option.click()
                    break
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_st5_1')

    def test_st5_2(self):
        """
        Test to Sort the movies by release date descending order.
        :return: None
        """
        self.driver.get(self.base_url)
        # Pauses the screen so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        # Sort select option
        try:
            # TODO the find may change
            sort_select = self.driver.find_element_by_name(SORT_BOX_TAG)
            for option in sort_select.find_elements_by_tag_name(SORT_OPTION_TAG):
                if option.text == 'Release Date Descending':
                    option.click()
                    break
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_st5_2')

    def test_st5_3(self):
        """
        Test to Sort the movies by Popularity order.
        :return: None
        """
        self.driver.get(self.base_url)
        # Pauses the screen so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        # Sort select option
        try:
            # TODO the find may change
            sort_select = self.driver.find_element_by_name(SORT_BOX_TAG)
            for option in sort_select.find_elements_by_tag_name(SORT_OPTION_TAG):
                if option.text == 'Popularity':
                    option.click()
                    break
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_st5_3')

    def test_st5_4(self):
        """
        Test to Sort the movies by release date ascending order after filtering by genre.
        :return: None
        """
        self.driver.get(self.base_url)
        # Pauses the screen so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        # Filter select option
        try:
            # TODO the find may change
            filter_select = self.driver.find_element_by_name(FILTER_BOX_TAG)
            for option in filter_select.find_elements_by_tag_name(FILTER_OPTION_TAG):
                if option.text == 'Comedy':
                    option.click()
                    break
        except NoSuchElementException:
            raise Exception('Cannot find Element name')
        # Sort select option
        try:
            # TODO the find may change
            sort_select = self.driver.find_element_by_name(SORT_BOX_TAG)
            for option in sort_select.find_elements_by_tag_name(SORT_OPTION_TAG):
                if option.text == 'Release Date Ascending':
                    option.click()
                    break
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_st5_4')

    def test_st5_5(self):
        """
        Test to Sort the movies by release date descending order after filtering by genre.
        :return: None
        """
        self.driver.get(self.base_url)
        # Pauses the screen so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        # Filter select option
        try:
            # TODO the find may change
            filter_select = self.driver.find_element_by_name(FILTER_BOX_TAG)
            for option in filter_select.find_elements_by_tag_name(FILTER_OPTION_TAG):
                if option.text == 'Comedy':
                    option.click()
                    break
        except NoSuchElementException:
            raise Exception('Cannot find Element name')
        # Sort select option
        try:
            # TODO the find may change
            sort_select = self.driver.find_element_by_name(SORT_BOX_TAG)
            for option in sort_select.find_elements_by_tag_name(SORT_OPTION_TAG):
                if option.text == 'Release Date Descending':
                    option.click()
                    break
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_st5_5')

    def test_st5_6(self):
        """
        Test to Sort the movies by Popularity order after filtering by genre.
        :return: None
        """
        self.driver.get(self.base_url)
        # Pauses the screen so we have time to confirm that we arrived at the right page
        time.sleep(WAIT_TIME)

        # Filter select option
        try:
            # TODO the find may change
            filter_select = self.driver.find_element_by_name(FILTER_BOX_TAG)
            for option in filter_select.find_elements_by_tag_name(FILTER_OPTION_TAG):
                if option.text == 'Comedy':
                    option.click()
                    break
        except NoSuchElementException:
            raise Exception('Cannot find Element name')
        # Sort select option
        try:
            # TODO the find may change
            sort_select = self.driver.find_element_by_name(SORT_BOX_TAG)
            for option in sort_select.find_elements_by_tag_name(SORT_OPTION_TAG):
                if option.text == 'Popularity':
                    option.click()
                    break
        except NoSuchElementException:
            raise Exception('Cannot find Element name')

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_st5_6')

    def test_st4_1(self):
        """
        Display movies for search "Batman Begins"
        There should only be one movie displayed
        :return: None
        """
        self.driver.get(self.base_url)
        # Pauses the screen so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        try:
            search_area = self.driver.find_element_by_name('search')
            search_area.clear()
            search_area.sendKeys("Batman Begins")
        except NoSuchElementException:
            raise Exception('Cannot find Element search')

        try:
            search_button = self.driver.find_element_by_css_selector("input[type=\"submit\"]")
            search_button.click()
        except NoSuchElementException:
            raise Exception('Cannot find Element search button')

        #Pauses the screen so we have time to confirm we have the right page
        time.sleep(WAIT_TIME)

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_st4_1')

    def test_st4_2(self):
        """
        Display movies for search "Batman"
        There should be multiple movies displayed
        :return: None
        """
        self.driver.get(self.base_url)
        # Pauses the screen so we have time to confirm it arrived at the right page
        time.sleep(WAIT_TIME)

        try:
            search_area = self.driver.find_element_by_name('search')
            search_area.clear()
            search_area.sendKeys("Batman")
        except NoSuchElementException:
            raise Exception('Cannot find Element search')

        try:
            search_button = self.driver.find_element_by_css_selector("input[type=\"submit\"]")
            search_button.click()
        except NoSuchElementException:
            raise Exception('Cannot find Element search button')

        #Pauses the screen so we have time to confirm we have the right page
        time.sleep(WAIT_TIME)

        # Make sure the results page returned something
        assert "No results found." not in self.driver.page_source

        # Another pause so we can see what's going on
        time.sleep(WAIT_TIME)

        # Take a screen shot of the results
        self.take_screen_shot('test_st4_2')


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
