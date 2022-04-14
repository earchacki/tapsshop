from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


# funkcja najeżdzą na element, aż się rozwinie zawartość na skutek najechania
def hover_over_element(driver_instance, selector_type, selector):
    elem = driver_instance.find_element(selector_type, selector)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def wait_for_visibility_of_element(driver_instance, selector_type, selector, time_to_wait=5):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((selector_type, selector)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element(inv_driver_instance, selector_type, selector, time_to_wait=8):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((selector_type, selector)))
    return inv_elem
