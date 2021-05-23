from selenium import webdriver
from pages.trial_page import TrialPage
import unittest


#------------------VERSION 1--------------------------------

class Page(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()

    def test_stone_input(self):
        driver = self.driver
        trial_page = TrialPage(driver=driver)
        trial_page.go()
        trial_page.stone_input.input_text("rock")
        trial_page.stone_button.click()
        self.assertEqual(trial_page.stone_button.text, 'Answer')

    def test_secrets_input(self):
        driver = self.driver
        trial_page = TrialPage(driver=driver)
        trial_page.go()
        trial_page.secrets_input.input_text("monday")
        trial_page.secrets_button.click()
        self.assertEqual(trial_page.secrets_button.text, 'Answer')
        self.assertEqual(trial_page.is_url, True)
        self.assertEqual(trial_page.secrets_button.is_displayed, True)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()



"""
#------------------VERSION 2--------------------------------

browser = webdriver.Chrome()
trial_page = TrialPage(driver=browser)
trial_page.go()

trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()
assert trial_page.stone_button.text == 'Answer'

trial_page.secrets_input.input_text("monday")
trial_page.secrets_button.click()
assert trial_page.secrets_button.text == 'Answer'
assert trial_page.is_url
assert trial_page.secrets_button.is_displayed

browser.quit()
"""
