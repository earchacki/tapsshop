import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, cart_page, order_page,place_an_order_page
from time import sleep


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_process(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_areas(self.driver)
        total_price = order_page.take_total_price(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(place_an_order_page.check_order_number(self.driver))
        self.assertTrue(place_an_order_page.check_order_item(self.driver))
        self.assertTrue(place_an_order_page.total_price_is_correct(self.driver, total_price))


if __name__ == '__main__':
    unittest.main()
