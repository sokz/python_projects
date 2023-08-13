# Tic-Tac-Toe 
# As part of a Udemy Course by Jose Portilla 
# The program requires a way to manage players, display the board, check for victory 
# conditions 

from os import system # For system("cls")


# Function that prints the board
def display_board(board):

    system("cls")
    print("   |   |")
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print("   |   |")
    print("____________")
    print("   |   |")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("   |   |")
    print("____________")
    print("   |   |")
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print("   |   |")


# Function to take in a player input and assign marker 'X' or 'O'
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()
    
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


# Function that takes the board input and a desired position number and assign to the board

def place_marker(board, marker, position):
    board[position] = marker

test_board = ['#','X','O','X','O','X','O','X','O','X']
place_marker(test_board, '$', 8)
display_board(test_board)

# Main function where the flow of control happens
# The following lines contain the logic of the program is contained

#print("Welcome to Tic-Tac-Toe!")
#p1_name = input("Enter name of Player 1: ") or 'Player 1' # takes user-input or assigns default value in case of empty input
#p2_name = input("Enter name of Player 2: ") or 'Player 2'

