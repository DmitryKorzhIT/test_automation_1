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


    def click_on_watchlist_btn(self, product_number=2):
        ''' Click on one of the products watchlist buttons. '''

        watchlist_btns = self.find_elements(By.CLASS_NAME, 'watch--alternative')
        watchlist_btns[product_number].click()


    def is_auth_exist(self):
        ''' Check is authentication message is shown. '''

        auth_window = self.find_element(By.CLASS_NAME, 'auth')
        return auth_window


    def click_on_product_image(self, product_number=3):
        ''' Click on a product image to load the product card. '''

        product_images = self.find_elements(By.CSS_SELECTOR, 'a[class="product"]')
        product_images[product_number].click()


    def choose_product_size(self, size_number=0):
        ''' Click on one of sizes buttons to choose size of a product. '''

        product_sizes = self.find_elements(By.CLASS_NAME, 'product-sizes__size')
        product_sizes[size_number].click()


    def click_on_watchlist_btn_2(self):
        ''' Click on watchlist button which is inside the product card. '''

        watchlist_btn = self.find_element(By.CSS_SELECTOR, 'img[alt="Add to favorite"]')
        watchlist_btn.click()
