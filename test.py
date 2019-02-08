from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import threading

##################
class FileReader:

    def __init__(self, file):
        self.file = open(file)

    def __next__(self):
        proxy = self.file.readline()
        print(proxy)


class Browser:

    def __init__(self, proxy=None):
        self.browser_option = webdriver.ChromeOptions()
        if proxy is not None:
            self.browser_option.add_argument('--proxy-server=http://%s' % proxy)
        self.browser = webdriver.Chrome(options=self.browser_option)

    def open_page(self, url):
        self.browser.get(url)

    def check_ban(self):
        element = self.browser.find_element_by_class_name("ban-popup__body")
        if element.is_displayed():
            return True
        else:
            return False

    def check_access_dummy(self):
        element = self.browser.find_element_by_class_name("access-dummy")
        if element.is_displayed():
            return True
        else:
            return False


proxy = FileReader("proxy.txt")
i = 0
for j in range(3):
    browser = Browser()
    browser.open_page("https://videochatru.com/")
    print(browser.check_ban(), browser.check_access_dummy(), ">>>", "browser")

