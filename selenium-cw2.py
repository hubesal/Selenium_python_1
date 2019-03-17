from selenium import webdriver
import unittest

class AntyCaptchaExcercise2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_type_text_and_button(self):
        self.driver.get('https://antycaptcha.amberteam.pl:5443/exercises/exercise2?seed=bb2cfa67-207d-46c9-b349-c5924448366a')
        textField = self.driver.find_element_by_css_selector('#t14')
        textField.clear()
        textField.send_keys('Friend issue.')
        przyciskB1 = self.driver.find_element_by_css_selector('#btnButton1')
        przyciskB1.click()
        przyciskCheck = self.driver.find_element_by_css_selector('#solution')
        przyciskCheck.click()
        textOutputField = self.driver.find_element_by_css_selector('.wrap')
        self.assertEqual(textOutputField.text, "OK. Good answer")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=4)
