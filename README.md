# Chess.com-API

## Overview
The Chess.com-API project is a Python-based tool designed to fetch and analyze chess game data from the [Chess.com API](https://www.chess.com/news/view/published-data-api). This project is particularly useful for data scientists and chess enthusiasts interested in analyzing their own games or general chess game trends. The script retrieves various game details such as opponent's rating, game datetime, number of moves, color of your pieces, and game results, and saves them into a CSV file for further analysis.

## Files in the Repository
- `main.py`: The main program that orchestrates the data fetching process.
- `chess_data_script.py`: This script handles the data scraping from the Chess.com API.

## Usage
To use this script, simply run `main.py`. The script will automatically fetch the game data and save it into a CSV file. This CSV file can then be used for various data analysis tasks.

**Note:** No API key is needed to use this script as it accesses publicly available data on Chess.com.

## Current Features
- Fetching opponent's rating.
- Retrieving datetime of the game.
- Number of moves in the game.
- Color of your pieces.
- Results of the games.

## Upcoming Features and Fixes
- **Opening's Name**: Currently working on fetching the name of the opening played in each game.
- **Game Duration**: There is a plan to include the duration of each game in the dataset.

## Contribution
This project is open for contributions, especially in the areas of feature enhancement and bug fixes. If you have ideas or improvements, feel free to fork the repository and submit a pull request.

## About the Author
[Nassri Ayman] - I'm an avid enthusiast of mathematics, problem-solving, and chess, with a deep-rooted passion for uncovering the beauty and complexity of these fields through analytical thinking and strategic planning. My journey in chess not only enhances my tactical skills but also mirrors my approach to problem-solving in mathematics, where each challenge is a new puzzle to be solved.

As an aspiring data scientist, I am constantly exploring ways to merge my interests with the power of data analysis. By integrating principles of mathematics and problem-solving strategies from chess, I aim to bring a unique perspective to the field of data science. I believe that the rigor of mathematics, combined with the strategic depth of chess, can lead to innovative solutions in data-driven decision-making.

Through projects like Chess.com-API, I am taking my first steps into the vast world of data science, eager to learn, grow, and contribute to a community that values data as a tool for understanding and innovation.


## License
This project is open source and available under the [MIT License](LICENSE).
