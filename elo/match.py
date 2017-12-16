import json
from datetime import datetime
from argparse import ArgumentParser
from os import path, mkdir, getcwd
from constants import *
from League import League

if __name__ == '__main__':
    parser = ArgumentParser(description='New Match Played')

    parser.add_argument('--home', dest='home_player', required=True)
    parser.add_argument('--away', dest='away_player', required=True)
    parser.add_argument('--home-score', dest="home_score", type=int, required=True)
    parser.add_argument('--away-score', dest="away_score", type=int, required=True)
    parser.add_argument('--overtime', dest="overtime", required=False, default = 0)
    parser.add_argument('--league', dest="league", required=False, default = DEFAULT_LEAGUE)

    match_info = vars(parser.parse_args())
    match_info['time'] = datetime.now().strftime("%Y-%m-%d %H:%M")

    league_path = LEAGUE_PATH.format(match_info['league'])

    print(getcwd())
    if not path.exists(league_path):
        mkdir(league_path)

    match_path = path.join(league_path,
                           'matches.json')
    player_scores_path = path.join(league_path,
                                   'player_scores.json')

    with open(match_path, 'a+') as f:
        f.write(json.dumps(match_info) + '\n')

    league = League()
    if path.exists(player_scores_path):
        league.load_json(player_scores_path)
    league.match(match_info)
    league.save(player_scores_path)
