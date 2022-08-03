from . import constant as const
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


BASE_URL = const.BASE_URL
PASSWORD = const.PASSWORD


class Base(webdriver.Chrome):
    def __init__(self, teardown=False):  # the teardown is a condition for the __exit__ method
        self.teardown = teardown
        super(Base, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
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
        ''' Pick any element from the left side burger menu. '''

        burger_element = self.find_element(By.CLASS_NAME, 'left-side__burger')
        burger_element.click()

        burger_menu_items = self.find_element(By.CLASS_NAME, 'menus-block-nav')
        burger_menu_items = burger_menu_items.find_elements(By.CLASS_NAME, 'nav-item')
        for item in burger_menu_items:
            if str(item.get_attribute('innerHTML')).strip() == nav_item_name:
                item.click()


    def is_auth_exist(self):
        ''' Check if authentication message is shown. '''

        auth_window = self.find_element(By.CLASS_NAME, 'auth')
        return auth_window


    def click_on_product_image(self, product_number=3):
        ''' Click on a product image to load the product card. '''

        product_images = self.find_elements(By.CSS_SELECTOR, 'a[class="product"]')
        product_images[product_number].click()


    def choose_product_size(self, size_number=0):
        ''' Click on one of the sizes buttons to choose the size of a product. '''

        product_sizes = self.find_elements(By.CLASS_NAME, 'product-sizes__size')
        product_sizes[size_number].click()


    def header_icons_item(self, header_icons_item_name: str = 'Watchlist'):
        ''' Pick any element from the header icons which are on the top right. '''

        header_icons_items = self.find_element(By.CLASS_NAME, 'header-icons')
        header_icons_items = header_icons_items.find_elements(By.CLASS_NAME, 'header-icons-item__text')
        for item in header_icons_items:
            if str(item.get_attribute('innerHTML')).strip() == header_icons_item_name:
                item.click()


    def tabs_item(self, tabs_item_name: str = 'Watch'):
        ''' Pick any element from the tabs which are on the bottom of the page. '''

        action = ActionChains(self)
        tabs_items = self.find_element(By.CLASS_NAME, 'tabs')
        tabs_items = tabs_items.find_elements(By.CLASS_NAME, 'button__link.ng-star-inserted')
        for item in tabs_items:
            if str(item.get_attribute('innerHTML')).strip() == tabs_item_name:
                self.execute_script("arguments[0].click();", item)  # the only way I could click the link
