from . import constant as const
from selenium import webdriver
from selenium.webdriver.common.by import By


BASE_URL = const.BASE_URL
PASSWORD = const.PASSWORD


class AddToWatchlist(webdriver.Chrome):
    def __init__(self, teardown=False):  # teardown is a condition for __exit__ method
        self.teardown = teardown
        super(AddToWatchlist, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            # time.sleep(10)
            self.quit()


    def land_first_page(self):
        self.get(BASE_URL)


    def password_auth(self):
        ''' Password authentication is the first step to
        get access to the website.'''

        password_element = self.find_element(By.ID, 'password')
        password_element.clear()
        password_element.send_keys(PASSWORD)

        send_password_element = self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]')
        send_password_element.click()


    def burger_menu_item(self, nav_item_name: str = 'Watchlist'):
        ''' Pick any element from left side burger menu. '''

        burger_element = self.find_element(By.CLASS_NAME, 'left-side__burger')
        burger_element.click()

        burger_menu_items = self.find_element(By.CLASS_NAME, 'menus-block-nav')
        burger_menu_items = burger_menu_items.find_elements(By.CLASS_NAME, 'nav-item')
        for item in burger_menu_items:
            if str(item.get_attribute('innerHTML')).strip() == f'{nav_item_name}':
                item.click()


    def click_on_watchlist_btn(self):
        ''' Click on one of the products watchlist buttons. '''

        watchlist_btns = self.find_elements(By.CLASS_NAME, 'watch--alternative')
        watchlist_btns[2].click()


    def is_auth_exist(self):
        ''' Check is authentication message is shown. '''

        auth_window = self.find_element(By.CLASS_NAME, 'auth')
        return auth_window






