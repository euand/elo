## ELO

This is an implementation of the [Elo ranking](https://en.wikipedia.org/wiki/Elo_rating_system) for use by BGSE Data Science students in determining who is the best FIFA player.

## Default League

This repo comes with the option to name a default league. To change the default league run

```bash
$ make default DEFAULT=new_default
```

## Adding matches
Say that in league `our_league` player `X` beat player `Y` 1-0 and the game did not go into overtime. To add this score run

```bash
python3 elo/match.py --home X --away Y --home-score 1 --away-score 0 --overtime 0 --league our_league
```

## Print league table

To print the league table for league `our_league` run

```bash
make table LEAGUE=our_league
```
