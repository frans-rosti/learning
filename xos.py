# This set is used to determine the locations for the Xs and Os.
# 0 being top left and 8 being bottom right.
board_locations = ["#"," "," "," "," "," "," "," "," "," "]

# Stores the players' signs (X or O)
p1_choice = ""
p2_choice = ""

# Counts the current turn (1 for Player One and 2 for Player Two)
turn_counter = 1
# Counts which turn it currently is. (maximum amount of turns is 9)
total_turns = 0


# Determines which sign each player will have based on player one choice.
def player_one_choice():
	
	global p1_choice
	global p2_choice

	print("Player One, choose X or O!")
	p1_choice = input().upper()

	if p1_choice.upper() == "X":
		p2_choice = "O"
	elif p1_choice.upper() == "O":
		p2_choice = "X"
	else:
		print("Nope. Try again.")
		player_one_choice()

	player_input()


# Starts the game.
def game_start():

	print("Welcome to Tic Tac Toe!")
	display_board()

	player_one_choice()


# Prints out the current board state.
def display_board():

	print("   |   |   ")
	print(" {one} | {two} | {three} ".format(one=board_locations[1],two=board_locations[2],three=board_locations[3]))
	print("___|___|___")
	print("   |   |   ")
	print(" {four} | {five} | {six} ".format(four=board_locations[4],five=board_locations[5],six=board_locations[6]))
	print("___|___|___")
	print("   |   |   ")
	print(" {seven} | {eight} | {nine} ".format(seven=board_locations[7],eight=board_locations[8],nine=board_locations[9]))
	print("   |   |   ")

valid_choices = [1,2,3,4,5,6,7,8,9]
valids_stringed = ["1","2","3","4","5","6","7","8","9"]

# This one is long and ugly, takes player's input (depending on whose turn it is) and places it on the board.
# Big Problem: if a user inputs anything other than a number from 1-9, the game breaks.
def player_input():

	global board_locations
	global turn_counter
	global total_turns
	global p1_choice
	global p2_choice
	global valid_choices

	print(" ")
	print(" ")
	print(" ")
	print("----------------------------------------")
	print(" ")
	print(" ")
	print(" ")

	display_board()

	print(" ")
	print(" ")
	print(" ")

	turn_going = False

	print(f"Player {turn_counter}, make your choice:")
	pchoice = input()

	if pchoice in valids_stringed:
		if turn_counter == 1:

			pchoice = int(pchoice)

			turn_going = True

			while turn_going == True and turn_counter == 1:
				if board_locations[pchoice] == "X":
					print("\n\nOops! Choose a different section.")
					player_input()
				elif board_locations[pchoice] =="O":
					print("\n\nOops! Choose a different section.")
					player_input()
				else:
					board_locations[pchoice] = p1_choice
					turn_counter = 2
					total_turns += 1
					turn_going == False
					win_check()

		# This is used if it is player two's turn.
		elif turn_counter == 2:

			pchoice = int(pchoice)

			turn_going = True

			while turn_going == True and turn_counter == 2:
				if board_locations[pchoice] == "X":
					print("\n\nOops! Choose a different section.")
					player_input()
				elif board_locations[pchoice] =="O":
					print("\n\nOops! Choose a different section.")
					player_input()
				else:
					board_locations[pchoice] = p2_choice
					turn_counter = 1
					total_turns += 1
					turn_going == False
					win_check()
	else:
		print("\n\nINVALID INPUT! Please enter a number from 1-9!")
		player_input()

winner = ""

# This is used to check the board if the game is won or not. this is also really ugly.
def win_check():

	global board_locations
	global winner

	# lists for the three rows
	row1 = [board_locations[1],board_locations[2],board_locations[3]]
	row2 = [board_locations[4],board_locations[5],board_locations[6]]
	row3 = [board_locations[7],board_locations[8],board_locations[9]]

	# lists for the three columns
	column1 = [board_locations[1],board_locations[4],board_locations[7]]
	column2 = [board_locations[2],board_locations[5],board_locations[8]]
	column3 = [board_locations[3],board_locations[6],board_locations[9]]

	# lists for the two crosses
	across1 = [board_locations[1],board_locations[5],board_locations[9]]
	across2 = [board_locations[3],board_locations[5],board_locations[7]]

	x_win = ["X","X","X"]
	o_win = ["O","O","O"]

	# compares x_win (three Xs in a row) to the current board (if the x_win list is currently the same as the row/column/across list)
	if row1 == x_win or row2 == x_win or row3 == x_win or column1 == x_win or column2 == x_win or column3 == x_win or across1 == x_win or across2 == x_win:
		if p1_choice == "X":
			winner = "Player One"
		elif p2_choice == "X":
			winner = "Player Two"
		victory()
	# compares o_win (three Os in a row) to the current board (if the o_win list is currently the same as the row/column/across list)
	elif row1 == o_win or row2 == o_win or row3 == o_win or column1 == o_win or column2 == o_win or column3 == o_win or across1 == o_win or across2 == o_win:
		if p1_choice == "O":
			winner = "Player One"
		elif p2_choice == "O":
			winner = "Player Two"
		victory()
	# if the game lapses 9 turns and there is no winner, the game ends.
	elif total_turns == 9:
		print("Game Over! No winner.")

		end()
	else:
		player_input()


# displays the winner that was defined in the win_check function
def victory():
	print("---------------------------")
	print(" ")
	print(f"Congratulations {winner}!")
	display_board()
	print(" ")
	print("---------------------------")
	end()

# asks the player if they want to replay or quit. if replay, then it resets all the stats and clears the board. if quit, the code stops.
def end():
	global board_locations
	global total_turns
	global turn_counter

	print("Play again? Y/N")
	replay = input()

	if replay.upper() == "Y":
		print("---------------------------")
		print(" ")
		print("Restarting.")
		print(" ")
		print("---------------------------")
		print(" ")
		print(" ")
		board_locations = ["#"," "," "," "," "," "," "," "," "," "]
		total_turns = 0
		turn_counter = 1
		game_start()
	elif replay.upper() == "N":
		print("------------------------")
		print(" ")
		print("Quitting. Thanks for playing!")
		quit()

# starts the game with the game_start function
game_start()
