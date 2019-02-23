from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from requests.exceptions import ProxyError
import threading
import requests
import gui
from PyQt5 import QtWidgets
from PyQt5.Qt import QWidget, QEvent
import sys

"""
Change THREADS_SUM less if you have got a not powerful CPU
or increase it if you have got a powerful CPU. Enjoy it :)

"""

READ_FILE = "proxy.txt"
WRITE_FILE = "checked.txt"
CHECK_WEBSITE = "https://ome.tv/"
THREADS_SUM = 5
PROTOCOL = "https"
THREADS_RUN = 0


def read_file(file):
    with open(file) as file:
        proxy_list = file.readlines()
        formatted_proxies = filter(lambda proxy: proxy != '\n', proxy_list)
        for proxy in formatted_proxies:
            yield proxy.rstrip()


class FileWriter:
    def __init__(self, file):
        self.file = open(file, 'w+')
        self.mutex = threading.Lock()

    def write(self, string):
        with self.mutex:
            self.file.write(str(string) + '\n')


class Browser:

    def __init__(self, proxy):
        self.browser_option = webdriver.ChromeOptions()
        self.browser_option.add_argument('--proxy-server=%s' % proxy)
        self.browser_option.add_argument('--headless')
        self.browser = webdriver.Chrome(options=self.browser_option)

    def open_page(self, url):
        self.browser.get(url)

    def check_ban(self):
        try:
            element = self.browser.find_element_by_class_name("ban-popup__body")
            if element.is_displayed():
                return True
            elif not element.is_displayed():
                return False
        except NoSuchElementException:
            return False

    def check_access_dummy(self):
        try:
            element = self.browser.find_element_by_class_name("access-dummy")
            if element.is_displayed():
                return True
            elif not element.is_displayed():
                return False
        except NoSuchElementException:
            return False

    def check_connection_error(self):
        try:
            self.browser.find_element_by_class_name("neterror")
            return True
        except NoSuchElementException:
            return False

    def close(self):
        self.browser.close()


class Checker:

    def __init__(self, obj, mutex):
        self.checked_proxy = FileWriter(WRITE_FILE)
        self.mutex = mutex
        self.obj = obj

    def start_check(self, proxy):
        global THREADS_RUN
        proxy_works = check_proxy_works(CHECK_WEBSITE, "https", proxy)
        if proxy_works is True:
            browser = Browser(proxy)
            browser.open_page(CHECK_WEBSITE)
            connection_error = browser.check_connection_error()
            dummy_access = browser.check_access_dummy()
            ban = browser.check_ban()
            if (connection_error is False) and (dummy_access is False) and (ban is False):
                with self.mutex:
                    self.checked_proxy.write(proxy)
                    Gui.write_prx(self.obj, proxy)
            browser.close()
        THREADS_RUN -= 1


class Gui(QtWidgets.QMainWindow, gui.Ui_MainWindow, QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton_start.installEventFilter(self)
        self.lock = threading.Lock()

    def eventFilter(self, obj, event):
        if obj == self.pushButton_start and event.type() == QEvent.MouseButtonPress:
            self.main_thread()

        return QWidget.eventFilter(self, obj, event)

    def main(self):
        file = read_file(READ_FILE)
        obj = Checker(self.textBrowser_wrkPrx, self.lock)
        threads = []
        global THREADS_RUN
        while True:
            try:
                if THREADS_RUN == THREADS_SUM:
                    pass
                elif THREADS_RUN != THREADS_SUM:
                    proxy = next(file)
                    with self.lock:
                        self.write_prx(self.textBrowser_chckPrx, proxy)
                    thread = threading.Thread(target=obj.start_check, args=(proxy,))
                    thread.start()
                    THREADS_RUN += 1
                    threads.append(thread)
            except StopIteration:
                break
        for thread in threads:
            thread.join()

    def main_thread(self):
        thread = threading.Thread(target=self.main)
        thread.start()

    @staticmethod
    def write_prx(obj, prx):
        obj.append(str(prx))


def create_gui():
        app = QtWidgets.QApplication(sys.argv)
        gui = Gui()
        gui.show()
        app.exec_()


def check_proxy_works(url, protocol, proxy):
    _proxy = dict()
    _proxy[protocol] = proxy
    try:
        requests.get(url, proxies=_proxy)
        return True
    except ProxyError:
        return False


if __name__ == "__main__":
    create_gui()


