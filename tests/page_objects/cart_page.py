from tests.helpers.support_functions import *

item_in_card = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]'
remove_item_from_cart_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]/td[1]/a'
submit_cart = '//*[@id="post-7"]/div/div/div[2]/div/div/a'


def check_item_in_cart(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, item_in_card)
    return elem.is_displayed()


def remove_item_from_cart(drive_instance):
    elem = drive_instance.find_element(By.XPATH, remove_item_from_cart_button)
    elem.click()


def check_item_not_in_cart(driver_instance):
    try:
        wait_for_invisibility_of_element(driver_instance, By.XPATH, item_in_card)
        return True
    except NoSuchElementException:
        return False


def approve_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, submit_cart)
    elem.click()