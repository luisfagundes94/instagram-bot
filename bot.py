from selenium import webdriver
from time import sleep


class InstagramBot:
    def __init__(self, username, password):
        self.username = username,
        self.password = password
        self.driver = webdriver.Firefox(executable_path='E:\Downloads\geckodriver\geckodriver.exe')
        self.driver.get("https://instagram.com")
        self.driver.maximize_window()
        sleep(2)

    def login(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(text(), 'Conecte-se')]").click()
        sleep(2)
        driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(3)

    def close_turn_on_notification_box(self):
        driver = self.driver
        driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()

    def like_photo(self, person):
        driver = self.driver
        driver.get("https://www.instagram.com/" + person + "/")
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]')\
            .click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')\
            .click()
