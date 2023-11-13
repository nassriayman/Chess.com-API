import pandas as pd
import requests
from datetime import datetime
import json
from chess_data_script import fetch_chess_data

# You can replace 'username' with your actual Chess.com username to analyze your games
username = 'username'
games_data = fetch_chess_data(username)

if games_data:
    df = pd.DataFrame(games_data)
    # Save to CSV
    df.to_csv('chess_games.csv', index=False) # A csv file will be saved in the same folder as your main function
    print("Data saved to chess_games.csv")
else:
    print("No data retrieved.")

#pd.read_csv('chess_games.csv') # Delete the '#' if you want to read the datasetyou need to import pandas library for it
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
main.py[+] [unix] (00:59 01/01/1970)                                     3,6 All
-- INSERT --

