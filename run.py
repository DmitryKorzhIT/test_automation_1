from add_to_watchlist_dir.add_to_watchlist import AddToWatchlist


app = AddToWatchlist()

# try:
app.land_first_page()
app.password_auth()
app.burger_menu_item()
app.click_on_watchlist_btn()
app.is_auth_exist()


# except:
#     print("Something doesn't work.")


