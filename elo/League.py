import pandas as pd
import json
import datetime
from constants import *

class League():

    def __init__(self, players=None, scores=None, base_score=1500):
        '''
        players should be a dict with player names and
        elo scores (initialise at 1500)
        '''
        if players is None:
            self.players = []
            self.player_scores = dict()
        else:
            if scores is None:
                scores = [1500] * len(players)
            self.players = [i.lower() for i in players]
            self.player_scores = dict(zip(self.players, scores))

    def expected_score(self, player1, player2):
        return 1 / (1 + 10 ** ((self.player_scores[player2] - self.player_scores[player1]) / 400))

    def add_player(self, player, base_score=1500):
        self.players.append(player)
        self.player_scores[player] = base_score
        return self

    def update(self, player, exp, score):
        self.player_scores[player] = self.player_scores[player] + SCORE_WEIGHT * (score - exp)
        return self

    def match(self, match_info):

        home_player = match_info['home_player']
        away_player = match_info['away_player']
        home_score = match_info['home_score']
        away_score = match_info['away_score']
        overtime = match_info['overtime']

        if home_player not in self.players:
            self.add_player(home_player)
        if away_player not in self.players:
            self.add_player(away_player)

        exp = self.expected_score(home_player, away_player)

        if home_score == away_score:
            self = self.update(home_player, exp, 0.5)
            self = self.update(away_player, 1-exp, 0.5)

        if home_score > away_score:
            self = self.update(home_player, exp, 1 + (1-exp) * (home_score - away_score) * GD_FACTOR)
            self = self.update(away_player, 1-exp, 0 + exp * (away_score - home_score + overtime / 2) * GD_FACTOR)

        if away_score > home_score:
            self = self.update(home_player, exp, 0 + (1-exp)*(home_score - away_score + overtime / 2) * GD_FACTOR)
            self = self.update(away_player, 1-exp, 1 + exp*(away_score - home_score) * GD_FACTOR)

        return self

    def load_json(self, path):
        with open(path, 'r') as f:
            self.player_scores = json.loads(f.read())
            self.players = list(self.player_scores.keys())

    def save(self, path):
        with open(path, 'w') as f:
            json.dump(self.player_scores, f)
