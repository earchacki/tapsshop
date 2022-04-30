import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, cart_page
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Tests(unittest.TestCase):
    def setUp(self):
        self.selenium_grid_url = 'http://192.168.50.12:4444/wd/hub'
        # self.capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        self.driver = webdriver.Remote(options=webdriver.ChromeOptions(), command_executor=self.selenium_grid_url)
        # self.driver = webdriver.Remote(desired_capabilities=self.capabilities, command_executor=self.selenium_grid_url)
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_add_item_to_cart(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))

    def test2_remove_item_from_cart(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.remove_item_from_cart(self.driver)
        self.assertTrue(cart_page.check_item_not_in_cart(self.driver))
