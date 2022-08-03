from code.functions_dir.add_to_watchlist import AddToWatchlist


# Watchlist through burger menu:
def test_1():
    add_to_watchlist = AddToWatchlist()
    add_to_watchlist.land_first_page()
    add_to_watchlist.password_auth()
    add_to_watchlist.burger_menu_item(nav_item_name='Watchlist')
    add_to_watchlist.click_on_watchlist_btn()
    flag = add_to_watchlist.is_auth_exist()
    assert flag


def test_2():
    add_to_watchlist = AddToWatchlist()
    add_to_watchlist.land_first_page()
    add_to_watchlist.password_auth()
    add_to_watchlist.burger_menu_item(nav_item_name='Watchlist')
    add_to_watchlist.click_on_product_image()
    add_to_watchlist.choose_product_size()
    add_to_watchlist.click_on_watchlist_btn_2()
    flag = add_to_watchlist.is_auth_exist()
    assert flag


def test_3():
    add_to_watchlist = AddToWatchlist()
    add_to_watchlist.land_first_page()
    add_to_watchlist.password_auth()
    add_to_watchlist.burger_menu_item(nav_item_name='Watchlist')
    add_to_watchlist.click_on_product_image()
    add_to_watchlist.choose_product_size()
    add_to_watchlist.click_on_watchlist_btn_3()
    flag = add_to_watchlist.is_auth_exist()
    assert flag


# Watchlist through header icons:
def test_4():
    add_to_watchlist = AddToWatchlist()
    add_to_watchlist.land_first_page()
    add_to_watchlist.password_auth()
    add_to_watchlist.header_icons_item(header_icons_item_name='Watchlist')
    add_to_watchlist.click_on_watchlist_btn()
    flag = add_to_watchlist.is_auth_exist()
    assert flag


def test_5():
    add_to_watchlist = AddToWatchlist()
    add_to_watchlist.land_first_page()
    add_to_watchlist.password_auth()
    add_to_watchlist.header_icons_item(header_icons_item_name='Watchlist')
    add_to_watchlist.click_on_product_image()
    add_to_watchlist.choose_product_size()
    add_to_watchlist.click_on_watchlist_btn_2()
    flag = add_to_watchlist.is_auth_exist()
    assert flag


def test_6():
    add_to_watchlist = AddToWatchlist()
    add_to_watchlist.land_first_page()
    add_to_watchlist.password_auth()
    add_to_watchlist.header_icons_item(header_icons_item_name='Watchlist')
    add_to_watchlist.click_on_product_image()
    add_to_watchlist.choose_product_size()
    add_to_watchlist.click_on_watchlist_btn_3()
    flag = add_to_watchlist.is_auth_exist()
    assert flag


# Watchlist through tabs:
def test_7():
    add_to_watchlist = AddToWatchlist()
    add_to_watchlist.land_first_page()
    add_to_watchlist.password_auth()
    add_to_watchlist.tabs_item(tabs_item_name='Watch')
    add_to_watchlist.click_on_watchlist_btn()
    flag = add_to_watchlist.is_auth_exist()
    assert flag


def test_8():
    add_to_watchlist = AddToWatchlist()
    add_to_watchlist.land_first_page()
    add_to_watchlist.password_auth()
    add_to_watchlist.tabs_item(tabs_item_name='Watch')
    add_to_watchlist.click_on_product_image()
    add_to_watchlist.choose_product_size()
    add_to_watchlist.click_on_watchlist_btn_2()
    flag = add_to_watchlist.is_auth_exist()
    assert flag


def test_9():
    add_to_watchlist = AddToWatchlist()
    add_to_watchlist.land_first_page()
    add_to_watchlist.password_auth()
    add_to_watchlist.tabs_item(tabs_item_name='Watch')
    add_to_watchlist.click_on_product_image()
    add_to_watchlist.choose_product_size()
    add_to_watchlist.click_on_watchlist_btn_3()
    flag = add_to_watchlist.is_auth_exist()
    assert flag