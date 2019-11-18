"""
Name: Alexander Faucheux
CWID: 101-47-247
Date: 11/12/2019
Assignment #: 3
Description: An AI that uses the minimax algorithm to play othello against a real human
"""


from Othello import *


window = Tk() # Initialize window
window.wm_geometry("400x400")  # Size of the board.
window.resizable(width=False, height=False) # Disable resizability
p = Board(window)
p.draw_board()  # Calls the refresh function inside the class Board
p.initialize()  # Initialize board
window.mainloop()  # Display window
