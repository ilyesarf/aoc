from get_input import get_input
import os

if os.getenv('DEBUG')=="1":
    input = [l.strip() for l in open('ex', 'r').readlines()]
else:
    input = [l.strip() for l in get_input(2, 2023)]


def isValidGame(game):
    for set in game.split(';'):
        for draw in set.split(','):
            val, color = draw.split()
            if int(val) > {'red':12,'green':13,'blue':14}[color]:
                return False
    
    return True

def getPowers(game):
    colors = {'red': 0, 'green': 0, 'blue': 0}

    for set in game.split(';'):
        for draw in set.split(','):
            val, color = draw.split()
            colors[color] = max(int(val), colors[color])
    
    powers = 1
    for x in colors.values():
        powers *= x
    
    return powers

if __name__ == "__main__":
    sum_games = 0
    sum_powers = 0
    for game in input:
        ind, game = game.split(':')
        if isValidGame(game):
            sum_games += int(ind.split()[-1])
        
        sum_powers += getPowers(game)
        
    print(f"part 1: {sum_games}")
    print(f"part 2: {sum_powers}")
        

