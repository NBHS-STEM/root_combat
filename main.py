import random

def sim_combat(attackers, defenders, n):
	"""
	Returns the expected outcome of a combat in a clearing with 
	atk_units attacking, def_units defending, and simulated n times.

	Remember that in Root, two dice with values from 0-3 are rolled
	simultaneously with the attacker claiming the higher number.
	"""
	score = 0
	for _ in range(n):
		rolls = (random.randint(0, 3), random.randint(0, 3))
		atk_hits, def_hits = min(attackers, max(rolls)), min(defenders, min(rolls))
		score += min(atk_hits, defenders) - min(def_hits, attackers)
	return score / n
