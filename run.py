from add_to_watchlist_dir.add_to_watchlist import AddToWatchlist


app = AddToWatchlist()

app.land_first_page()
app.password_auth()
app.tabs_item(tabs_item_name='Register')


