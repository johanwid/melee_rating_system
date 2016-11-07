# melee_rating_system
python files for "mELO", a melee rating system that reads a bracket from smash.gg

melee rating system - "mELO"

player information format(dictionary):

{'player_nametag': (current_rating, 'character_played', ('main1', 'main2'))}

ex: 

{'mew2king': (2600, 'pichu', ('marth', 'shiek', 'fox'))}

for future: 
'mew2king' can be recognized in database as:
'm2k', 'mvg mew2king', 'mvg echofox mew2king', etc. and 
is not case sensitive`

determining factors of rating outcome:

definite:
player's rating, character used in each game, matchup difficulty, 
player's main, amount of games each player won in a set

maybe: 
winning a set should not hurt winner's rating, tournament importance*,
stock count at end, any self destructs, bo5 more important than bo3

* tournament importance: more people practice for evo than another tournament,
base value for tournament is 1, evo could be 1.25
