from .base import Base
from . import constant as const
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


BASE_URL = const.BASE_URL
PASSWORD = const.PASSWORD


class Register(Base):
    pass