# Tic-Tac-Toe 
# As part of a Udemy Course by Jose Portilla 
# The program requires a way to manage players, display the board, check for victory 
# conditions 

from os import system # For system("cls")


# Function that prints the board
def display_board(board):

    system("cls")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("   |   |")
    print("____________")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("   |   |")
    print("____________")
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("   |   |")


# Function to take in a player input and assign marker 'X' or 'O'
def player_input():
    





test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

# Main function where the flow of control happens
# The following lines contain the logic of the program is contained

#print("Welcome to Tic-Tac-Toe!")
#p1_name = input("Enter name of Player 1: ") or 'Player 1' # takes user-input or assigns default value in case of empty input
#p2_name = input("Enter name of Player 2: ") or 'Player 2'

