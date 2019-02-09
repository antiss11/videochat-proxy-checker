from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import threading
import time
import sys


READ_FILE = "proxy.txt"
WRITE_FILE = "checked.txt"
CHECK_WEBSITE = "https://ome.tv/"
PROXY_LENGHT = len(open(READ_FILE).readlines())
THREADS_SUM = 10


def read_file(file):
    with open(file) as file:
        proxy_list = file.readlines()
        for proxy in proxy_list:
            yield proxy.rstrip('\n')


class FileWriter:

    def __init__(self, file):
        self.file = open(file, 'w+')

    def __len__(self):
        return len(self.file.readlines())

    def write(self, string):
        self.file.write(string + '\n')


class Browser:

    def __init__(self, proxy):
        self.browser_option = webdriver.ChromeOptions()
        self.browser_option.add_argument('--proxy-server=%s' % proxy)
        # self.browser_option.add_argument('--headless')
        self.browser = webdriver.Chrome(options=self.browser_option)

    def open_page(self, url):
        self.browser.get(url)

    def check_ban(self):
        try:
            element = self.browser.find_element_by_class_name("ban-popup__body")
            if element.is_displayed():
                return True
        except NoSuchElementException:
            return False

    def check_access_dummy(self):
        try:
            element = self.browser.find_element_by_class_name("access-dummy")
            if element.is_displayed():
                return True
        except NoSuchElementException:
            return False

    def check_connection(self):
        try:
            self.browser.find_element_by_class_name("neterror")
            return False
        except NoSuchElementException:
            return True

    def close(self):
        self.browser.close()


class Main:

    def __init__(self):
        self.proxies = read_file(READ_FILE)
        self.checked_proxy = FileWriter(WRITE_FILE)

    def start_check(self):
        try:
            proxy = next(self.proxies)
            browser = Browser(proxy)
            browser.open_page(CHECK_WEBSITE)
            connection = browser.check_connection()
            dammy = browser.check_access_dummy()
            ban = browser.check_ban()
            if (ban is False) and (dammy is False) and (connection is False):
                self.checked_proxy.write(proxy)
            browser.close()
            self.threads_count -= 1
        except StopIteration:
            pass
        except ValueError:
            pass

    def thread(self):
        self.threads_count = 0
        while True:
            if self.threads_count < 10:
                threading.Thread(target=self.start_check).start()
                self.threads_count += 1
            else:
                time.sleep(1)


def checker():
    while True:
        print(threading.active_count())
        if threading.active_count() == 2:
            sys.exit()
        else:
            time.sleep(1)


class ReadyException(Exception):
    def __init__(self):
        print("Ready")


if __name__ == "__main__":
    start = Main()
    start.thread()
    checker()

