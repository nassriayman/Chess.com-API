def fetch_chess_data(username):
    # Headers to mimic a browser visit
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # URL for game data archives
    archive_url = f"https://api.chess.com/pub/player/{username}/games/archives"
    
    # Making a request to the API
    response = requests.get(archive_url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve data")
        return None

    # Extract the archive URLs from the response
    archives = response.json().get('archives', [])
    all_games_data = []

    for archive_url in archives:
        archive_response = requests.get(archive_url, headers=headers)
        if archive_response.status_code != 200:
            continue

        monthly_games = archive_response.json().get('games', [])
        for game in monthly_games:
            # Filter out non-rapid games
            if game['time_class'] != 'rapid':
                continue

            # Calculate game duration if start and end time are available
            game_duration = None
            if 'end_time' in game and 'start_time' in game:
                game_duration = game['end_time'] - game['start_time']

            # Extract the opening name from the ECOUrl
            opening_url = game.get('ECOUrl', '')
            opening_name = 'Unknown'
            if opening_url:
                url_parts = opening_url.split('/')
                if url_parts:
                    last_part = url_parts[-1]
                    if last_part:
                        opening_name = ' '.join(last_part.split('-')[1:]).title()
            
            print(f"ECOUrl: {opening_url}, Extracted Opening: {opening_name}")  # Debug print

            # Count the number of moves
            number_of_moves = len(game['pgn'].split()) // 2

            # Extracting game data
            game_data = {
                'username': username,
                'date': datetime.fromtimestamp(game.get('end_time')).strftime('%Y-%m-%d %H:%M:%S') if 'end_time' in game else None,
                'opponent_rating': game['white']['rating'] if game['black']['username'].lower() == username else game['black']['rating'],
                'user_color': 'white' if game['white']['username'].lower() == username else 'black',
                'result': game['white']['result'] if game['white']['username'].lower() == username else game['black']['result'],
                'game_duration': game_duration,
                'opening': opening_name,
                'number_of_moves': number_of_moves
            }
            all_games_data.append(game_data)

    return all_games_data
