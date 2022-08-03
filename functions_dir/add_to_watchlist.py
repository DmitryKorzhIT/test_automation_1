from .base import Base
from . import constant as const
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


BASE_URL = const.BASE_URL
PASSWORD = const.PASSWORD


class AddToWatchlist(Base):
    def click_on_watchlist_btn(self, product_number=2):
        ''' Click on one of the product's watchlist buttons. '''

        watchlist_btns = self.find_elements(By.CLASS_NAME, 'watch--alternative')
        watchlist_btns[product_number].click()


    def click_on_watchlist_btn_2(self):
        ''' Click on the watchlist button which is inside the product card.
        This button is located top right. '''

        watchlist_btn = self.find_element(By.CSS_SELECTOR, 'img[alt="Add to favorite"]')
        watchlist_btn.click()


    def click_on_watchlist_btn_3(self):
        ''' Click on the watchlist button which is inside the product card.
        This button is located under product sizes. '''

        watchlist_btn = self.find_element(By.CLASS_NAME, 'product-actions__btn')
        watchlist_btn.click()
