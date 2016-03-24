import sys

global N, M 			# N - Total number of balls, M - Max no of balls to remove

N = 13
M = 3

print "Dr.NIM : Welcome to the game of NIM!\nDr.NIM : We will be playing this game with", N, "balls, allowing a maximum of",M,"balls to be removed per turn.\n"

user_selection = int(input("\nDr.NIM : To play the game, just enter the number of balls that you want to remove : "))
comp_selection = 0

key = [[3, 2, 1]]*N
turn = 0

while N > 0 :
	if turn % 2 == 0 :
		if user_selection > M or user_selection < 1 :
			print "Invalid input"
			sys.exit(0)
		N -= user_selection
	else :
		N -= comp_selection

	print "\nThere are now", N , "balls left!"

	if turn % 2 != 0 :
		user_selection = int(input("Dr.NIM : How many do u take now?"))
	else :
		comp_selection = key[turn][user_selection-1]
		print "Dr.NIM : I'm choosing", comp_selection, "balls."
	turn += 1

print "Game Over!"

if turn % 2 != 0 :
	print "Dr.NIM WON!"
else :
	print "YOU WON!!! CONGRATULATION!"