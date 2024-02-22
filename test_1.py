import time
from testpage import OperationsHelpers
import logging
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser, get_title_font_size):
    logging.info("Test_1: Get title font-size starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("leonid")
    testpage.enter_pass("142153c067")
    testpage.click_login_button()
    time.sleep(3)
    testpage.click_about_button()
    time.sleep(3)
    assert testpage.get_title_about() == get_title_font_size

