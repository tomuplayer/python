from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

koodi = ""
i = 0

koodi = input("Syötä kahoot pelikoodi: ")


botit = input("Kuinka monta botti pelaajaa haluat lisätä peliin: ")


selain = webdriver.Chrome()
selain.get("https://kahoot.it/")


kirjoitus = selain.find_element_by_id("game.input")
kirjoitus.sendkeys(koodi)
kirjoitus.send_keys(Keys.RETURN)