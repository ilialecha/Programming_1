from easyinput import read

turns = read(int)

actual_turn = 0 

loser = False

previous = ""

while  not loser or actual_turn < turns*2:
	
	player_num = read(str)
	
	if not actual_turn == 0:
		if player_num.length % 2 == 0:
			
			if not player_num[player_num.length // 2] == previous:
				loser = True
				previous = player_num[player_num.length // 2]
			
			elif not player_num[(player_num.length // 2) +1] == previous:
				loser = True
				previous = layer_num[(player_num.length // 2) +1]

	actual_turn +=1 	




'''
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

'''

