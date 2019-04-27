from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class AntyCaptchaExcercise1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://antycaptcha.amberteam.pl:5443/exercises/exercise1?seed=b21db0ad-1353-4316-8af4-700d235922d9")
	WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/pre/code')))


    def test_button1(self):
        self.driver.refresh()
	self.czekaj_na_przycisk("btnButton1")
        przycisk = self.driver.find_element_by_id("btnButton1")
        przycisk.click()
        self.sprawdz_wynik_przycisku("b1")

    def test_button2(self):
        self.driver.refresh()
	self.czekaj_na_przycisk("btnButton2")
        przycisk = self.driver.find_element_by_id("btnButton2")
        przycisk.click()
        self.sprawdz_wynik_przycisku("b2")

    def test_buttons(self):
        self.driver.refresh()
        self.czekaj_na_przycisk("btnButton1")
        self.czekaj_na_przycisk("btnButton2")
        przycisk = self.driver.find_element_by_id("btnButton1")
        przycisk.click()
        przycisk = self.driver.find_element_by_id("btnButton2")
        przycisk.click()
        przycisk = self.driver.find_element_by_id("btnButton1")
        przycisk.click()
        self.sprawdz_wynik_przycisku("b1b2b1")

    def tearDown(self):
        self.driver.quit()

    def sprawdz_wynik_przycisku(self, odczytZPrzycisku):
        tekstZOkna = self.driver.find_element_by_xpath('/html/body/div/div[3]/pre/code')
        tekstDoSpr = tekstZOkna.text
        self.assertEqual(tekstDoSpr, odczytZPrzycisku)

    def czekaj_na_przycisk(self, przycisk):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, przycisk)))

if __name__ == "__main__":
    unittest.main(verbosity=2)
