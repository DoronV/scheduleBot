from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

class Connector():

    def connect_to_sportja(self):
        chromium_options = Options()
        chromium_options.add_argument("--headless")
        sportjaDriver = webdriver.Chrome(chrome_options=chromium_options)
        sportjaDriver.get("https://sportja.virtuagym.com/")

        return sportjaDriver

    def login_to_sportja(self, sportjaDriver):
        user = sportjaDriver.find_element_by_name("username")
        user.clear()
        user.send_keys("doronvoerman@gmail.com")
        password = sportjaDriver.find_element_by_name("password")
        password.clear()
        password.send_keys("JdT!c*QtXAb9yAEb32")
        password.send_keys(Keys.RETURN)
        sleep(1)

        return sportjaDriver