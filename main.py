'''Names: Jacob Miranda & Daniel Puerto
Date: 2/2/2026
Group: 11 
Description: '''


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
    

def count_mines(board):
    mines = 0 
    if 


def main():

    x = check_input.get_int_range("Enter number of rows: (5-10)", 5, 10)
    y = check_input.get_int_range("Enter number of columns: (5-10)", 5, 10)
    mines_placed = check_input.get_int_range("Enter number of mines: (5-10)", 5, 10)
    new_board = create_board(x, y)
    print(new_board)



main()
