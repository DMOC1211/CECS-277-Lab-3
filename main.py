'''Names: Jacob Miranda & Daniel Puerto
Date: 2/2/2026
Group: 11 
Description: Create a program that generates a solution board for the game Minesweeper that prompts the user to enter a grid consisting of rows 
and columns between 5-10 and the total number of mines ranging 5-10.  Then randomly places the mines on the grid and counting the adjacent squares of to check for the number of 
mines (including diagonals). Then display the grid. '''


import random
import check_input

'''Creates a new board (2D list) with between 5 and 10 rows and columns.
This amount is specified by the user.'''
def create_board(rows, cols): 
    board = []
    for i in range(rows):
        list = []
        for j in range(cols):
            list.append(0)
        board.append(list)
    return board

def place_mines (board,mines):
    cols = len(board)
    rows = len(board[0])
    placed = 0
    while placed < mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        
        if board[r][c] == 0:
            board [r][c] = 'X'
            placed +=1 
    

def count_mines(board):
    mines_counter = 0 

def display_board(board):
    for row in board: 
        for value in row:
            print(value, end=" ")
        print()
    


def main():

    rows = check_input.get_int_range("Enter number of rows: (5-10)", 5, 10)
    cols = check_input.get_int_range("Enter number of columns: (5-10)", 5, 10)
    mines = check_input.get_int_range("Enter number of mines: (5-10)", 5, 10)
    new_board = create_board(rows, cols)
    place_mines(new_board, mines)
    display_board(new_board)



main()
