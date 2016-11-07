"""
will import bracket data from smash.gg into a form usable to mELO.py:

{'player_nametag': (current_rating, 'character_played', ('main1', 'main2'))}

notes:

a set has some key features:

2 names, each followed by a number, and the last player is followed 
by a unique letter ID

including this letter ID, each game is 6 lines long, plus one more 
if including the white space preceding the first player
"""

def import_bracket(bracket_link):
	"""
	will return string that was copied from a smash.gg bracket, looks like:

	Mew2King
	2

	Wobbles
	1
	A

	S2J
	0

	Silent Wolf
	2
	B

	Leffen
	1

	Gahtzu
	2
	C

	note: every game has a unique id: ex: 'A', 'B', 'C', ... ,'BD'
	"""

	return none



#	
# code tinkering below
#	

# import webbrowser
# webbroswer.open('https://smash.gg/tournament/the-big-house-6/events/melee-singles/brackets/76016')