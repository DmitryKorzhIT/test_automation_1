from code.add_to_watchlist_dir.add_to_watchlist import AddToWatchlist


# Watchlist through burger menu:
def test_1():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.burger_menu_item(nav_item_name='Watchlist')
    app.click_on_watchlist_btn()
    flag = app.is_auth_exist()
    assert flag


def test_2():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.burger_menu_item(nav_item_name='Watchlist')
    app.click_on_product_image()
    app.choose_product_size()
    app.click_on_watchlist_btn_2()
    flag = app.is_auth_exist()
    assert flag


def test_3():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.burger_menu_item(nav_item_name='Watchlist')
    app.click_on_product_image()
    app.choose_product_size()
    app.click_on_watchlist_btn_3()
    flag = app.is_auth_exist()
    assert flag


# Watchlist through header icons:
def test_4():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.header_icons_item(header_icons_item_name='Watchlist')
    app.click_on_watchlist_btn()
    flag = app.is_auth_exist()
    assert flag


def test_5():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.header_icons_item(header_icons_item_name='Watchlist')
    app.click_on_product_image()
    app.choose_product_size()
    app.click_on_watchlist_btn_2()
    flag = app.is_auth_exist()
    assert flag


def test_6():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.header_icons_item(header_icons_item_name='Watchlist')
    app.click_on_product_image()
    app.choose_product_size()
    app.click_on_watchlist_btn_3()
    flag = app.is_auth_exist()
    assert flag


# Watchlist through tabs:
def test_7():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.tabs_item(tabs_item_name='Watch')
    app.click_on_watchlist_btn()
    flag = app.is_auth_exist()
    assert flag


def test_8():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.tabs_item(tabs_item_name='Watch')
    app.click_on_product_image()
    app.choose_product_size()
    app.click_on_watchlist_btn_2()
    flag = app.is_auth_exist()
    assert flag


def test_9():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.tabs_item(tabs_item_name='Watch')
    app.click_on_product_image()
    app.choose_product_size()
    app.click_on_watchlist_btn_3()
    flag = app.is_auth_exist()
    assert flag