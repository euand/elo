import pandas as pd
import json
from argparse import ArgumentParser
from constants import *
from os import path

if __name__ == '__main__':
    parser = ArgumentParser(description='Print League Table')

    parser.add_argument('--league', dest="league", required=False, default = DEFAULT_LEAGUE)

    league = parser.parse_args().league
    league_path = LEAGUE_PATH.format(league)

    player_scores_path = path.join(league_path,
                                   'player_scores.json')

    with open(player_scores_path, 'r') as f:
        player_scores = json.loads(f.read())

    players = list(player_scores.keys())
    table = pd.DataFrame({'Player': players, 'Score': [player_scores[i] for i in players]})
    table.sort_values(by = 'Score', ascending = False, inplace = True)
    table.reset_index(inplace=True)
    table.drop('index', 1, inplace = True)

    print(table)
