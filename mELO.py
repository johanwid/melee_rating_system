"""
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
"""

def tier_multiplier(player1, player2):
	"""
	returns mulitplier values in (int1, int2), where a higher number
	corresponds to a better character, ex:
	fox is 1.00 and mario is 0.65
	"""

	tier01 = ('fox', 'falco', 'marth', 'shiek', 'jigglypuff', 'peach')
	tier02 = ('ice climbers', 'captain falcon')
	tier03 = ('pikachu', 'samus')
	tier04 = ('doctor mario', 'yoshi', 'luigi', 'ganondorf', 'mario')
	# tier05 = ...

	for key in player1:
		character_played1 = player1[key][1]	
	for key in player2:
		character_played2 = player2[key][1]

	if character_played1 in tier01:
		mult1 = 1.00
	elif character_played1 in tier02:
		mult1 = 0.90
	elif character_played1 in tier03:
		mult1 = 0.75
	elif character_played1 in tier04:
		mult1 = 0.65	
	else:
		mult1 = 0.5

	if character_played2 in tier01:
		mult2 = 1.00
	elif character_played2 in tier02:
		mult2 = 0.85
	elif character_played2 in tier03:
		mult2 = 0.75
	elif character_played2 in tier04:
		mult2 = 0.65	
	else:
		mult2 = 0.5		

	return (mult1, mult2)

def main_multiplier(player1, player2):
	"""
	returns mulitplier values in (int1, int2), where a 1.00 means
	the player is using his main, and a lower number means he
	is using a nother character, ex:
	armada using peach = 1.00
	mew2king using peach < 1.00	
	"""

	tier_multiplier(player1, player2)
	tier_multiplier_result = tier_multiplier(player1, player2)
	player1_tier_mult = tier_multiplier_result[0]
	#player1's tier multiplier extracted
	player2_tier_mult = tier_multiplier_result[1]
	# player2's tier multiplier extracted

	for key in player1:
		character_played = player1[key][1]
    	if character_played in player1[key][2]:
        	mult1 = 1.00
    	else:
        	mult1 = player1_tier_mult - .10
	
	for key in player2:
		character_played = player2[key][1]
    	if character_played in player2[key][2]:
        	mult2 = 1.00
    	else:
        	mult2 = player2_tier_mult - .10

	return (mult1, mult2)

def matchup_multiplier(player1, player2):
	"""
	"""

def results_multiplier(player1, player2, results):
	"""
	returns a multiplier based on results of set, where the results argument will
	look like:
	(player1's games won, player2's games won), ex:
	(3, 0), which signifies player1 won a bo5 with a score of 3-0
	(1, 2), which signifies player2 won a bo3 with a score of 2-1

	games won/lost will affect how much a rating rises/falls, i.e.a 3-2 loss will 
	not lower loser's rating as much as a 3-0 loss
	"""

	if results[0] > results[1]:
		# player1 won
		return None

	else: # if results[1] > results[1]:
		# player2 won
		return None

def sample_rating_system(player1, player2):
	"""
	returns a sample rating based on two already-rated players
	player1/2 should be a string of just the player's gamertag
	results should be a list
	in the future:

	the gamertag will then be referenced to a database
	where it will import all of the information in dictionary form

	the victor, along with theamount of games won out of the set for 
	each player will also be imported

	for testing purposes, assume each player used the same character for
	all games played in the set
	"""	
	
	tier_multiplier(player1, player2)
	tier_multiplier_result = tier_multiplier(player1, player2)
	
	player1_tier_mult = tier_multiplier_result[0]
	# player1's tier multiplier extracted
	player2_tier_mult = tier_multiplier_result[1]
	# player2's tier multiplier extracted

	main_multiplier(player1, player2)
	main_multiplier_result = main_multiplier(player1, player2)
	player1_main_mult = main_multiplier_result[0]
	player2_main_mult = main_multiplier_result[1]

	player1_character_multiplier = player1_tier_mult * player1_main_mult
	player2_character_multiplier = player2_tier_mult * player2_main_mult
	# ex: mango playing mario will equal: 
	# .65 (mario's rating) * .55 (mario's rating - .1, since mango
	# does not main mario) = .3575
	# so a player playing/losing with  a character that is a) not their main 


	return (player1_character_multiplier, player2_character_multiplier)





#	
# code tinkering below
#	

mango = {'mang0': (2600, 'mario', ('fox', 'falco', 'marth'))}

# for key in mango:
#     print mango[key][1] <- this will print 'mario'

mike_haze = {'mike haze': (1800, 'fox', ('fox'))}

print sample_rating_system(mango, mike_haze)
,


results = (1, 2)
    
multiplier_bo3 = {(2, 0): 1.5, (2, 1): 1.2, (1, 2): -1.2, (0, 2): -1.5}

if results in multiplier_bo3:
    
    results_mult = multiplier_bo3[results]
    print results_mult

# import webbrowser
# webbroswer.open('https://smash.gg/tournament/the-big-house-6/events/melee-singles/brackets/76016')
