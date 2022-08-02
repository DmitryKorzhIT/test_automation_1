from code.add_to_watchlist_dir.add_to_watchlist import AddToWatchlist


def test_1():
    app = AddToWatchlist()
    app.land_first_page()
    app.password_auth()
    app.burger_menu_item()
    app.click_on_watchlist_btn()
    flag = app.is_auth_exist()
    assert flag