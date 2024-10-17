def save_result(game_result):
    with open('game_results.txt', 'a') as file:
        file.write(game_result)
