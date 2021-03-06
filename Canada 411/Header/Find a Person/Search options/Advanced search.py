import sys
import myModule as My
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable PATH stores the directory of the chrome driver
PATH = "C:\\Users\\mbroui01\\Downloads\\chromedriver_win32 (v76)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


class Canada411Home:
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    is_success = False

    def advanced_search_link(self, link):
        """
        >> This function verifies that the Advanced search toggle is clickable and functional.
        """
        # Locating the Find a Person container
        find_a_person_container = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]')
        if find_a_person_container:
            pass
        else:
            return

        # Locating the More search options toggle
        more_search_options_toggle = My.search_clickable_webelement(
            find_a_person_container, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/a')
        if more_search_options_toggle:
            more_search_options_toggle.click()
            pass
        else:
            return

        # Locating the Advanced search link
        advanced_search = My.search_presence_webelement(
            driver, By.XPATH, '//*[@id="c411ContentArea"]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[1]/a')
        if advanced_search:
            advanced_search.click()
            pass
        else:
            return

        # Validating the URL of the current web page
        print(str(driver.current_url))
        if driver.current_url == link + 'search/advanced.html':
            Canada411Home.is_success = True
            return
        else:
            return

    def testing_advanced_search_link(self, link):
        My.search_merchant_page(driver, link)
        test.advanced_search_link(link)
        if Canada411Home.is_success:
            print("-->> Test case is successful!")
        else:
            print("-->> Test case is unsuccessful!")
        driver.quit()
        sys.exit()


test = Canada411Home(driver)
test.testing_advanced_search_link(My.c411_qa_web_link)
