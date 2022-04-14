from tests.helpers.support_functions import *


page_header = '//*[@id="post-8"]/header/h1'
order_number = '//*[@id="post-8"]/div/div/div/ul/li[1]/strong'
order_item = '//*[@id="post-8"]/div/div/div/section[2]/table/tbody/tr/td[1]/a'
total_price_in_summary = '//*[@id="post-8"]/div/div/div/section[2]/table/tfoot/tr[5]/td/span'

header_content = 'Zamówienie otrzymane'
item_describe = 'Hoodie with Zipper'


def check_order_number(driver_instance):
    try:
        wait_for_visibility_of_element(driver_instance, By.XPATH, order_number)
        return True
    except NoSuchElementException:
        return False


def check_order_item(driver_instance):
    elem = driver_instance.find_element(By.XPATH, order_item)
    if elem.text == item_describe:
        return True
    else:
        return False


def total_price_is_correct(driver_instance, total_price):
    elem = driver_instance.find_element(By.XPATH, total_price_in_summary)
    if elem.text == total_price:
        return True
    else:
        return False
