from functions_dir.add_to_watchlist import AddToWatchlist


add_to_watchlist = AddToWatchlist()

add_to_watchlist = AddToWatchlist()
add_to_watchlist.land_first_page()
add_to_watchlist.password_auth()
add_to_watchlist.burger_menu_item(nav_item_name='Watchlist')
add_to_watchlist.click_on_watchlist_btn()
flag = add_to_watchlist.is_auth_exist()
print(flag)


