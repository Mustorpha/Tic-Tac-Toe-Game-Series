from tkinter import *
import tkinter.messagebox
from functools import partial
import random
from math import inf as infinity

menu = Tk()
menu.geometry("370x500")
menu.title("Tic Tac Toe")

pa =  StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()
buttons = StringVar()
INTELLIGENCE_NAME = "A.Intelligence"
bclick = True
flag = 0
player, opponent = ('X', 'O')

global board # a global 3x3 dimension list to hold every state of the game
board = [[" " for x in range(3)] for y in range(3)] # the button widget retrieves text value from their corresponding index

# Decide the next move of computer
def isMovesLeft(board) :
        
        '''
        Return False if the game board is full and
        True otherwise
        '''

        for i in range(3) :
            for j in range(3) :
                if (board[i][j] == ' ') :
                    return True
        return False

def evaluate(b) :

    '''
    Check if a player won the game for a particular
    state of the board and return a value which is 
    known as the value of the game at that state
    '''

    # Checking for Rows for X or O victory.
    for row in range(3) :	
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :	
            if (b[row][0] == player) :
                return 10
            elif (b[row][0] == opponent) :
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3) :
    
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
        
            if (b[0][col] == player) :
                return 10
            elif (b[0][col] == opponent) :
                return -10

    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
    
        if (b[0][0] == player) :
            return 10
        elif (b[0][0] == opponent) :
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
    
        if (b[0][2] == player) :
            return 10
        elif (b[0][2] == opponent) :
            return -10

    # Else if none of them have won then return 0
    return 0

def minimax(board, depth, isMax, alpha = -infinity, beta = infinity) :

    '''
    This is the minimax function. It considers all
    the possible ways the game can go and returns
    the value of the game for each route
    '''
    score = evaluate(board)

    # If Maximizer has won the game return it's evaluated score
    if (score == 10) :
        return score - depth    # go for the fastest winning route

    # If Minimizer has won the game return it's evaluated score
    if (score == -10) :
        return score + depth    # go for the slowest losing route

    # If there are no more moves and no winner then it is a tie
    if (isMovesLeft(board) == False) :
        return 0

    # If this is maximizer's move
    if (isMax) :	
        best = -infinity #-INFINITY

        # Traverse all cells
        for i in range(3) :		
            for j in range(3) :
            
                # Check if cell is empty
                if (board[i][j]==' ') :
                
                    # Make the move
                    board[i][j] = player

                    # Call minimax recursively and choose the maximum value
                    best = max( best, minimax(board,
                                            depth + 1,
                                            False, alpha, beta) )
                    alpha = max(alpha, best)
                    # Undo the move
                    board[i][j] = ' '
                    if beta <= alpha:
                        break
                    
        return best

    # If this minimizer's move
    else :
        best = infinity #+INFINITY

        # Traverse all cells
        for i in range(3) :		
            for j in range(3) :
            
                # Check if cell is empty
                if (board[i][j] == ' ') :
                
                    # Make the move
                    board[i][j] = opponent

                    # Call minimax recursively and choose the minimum value
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    beta=min(beta,best)
                    # Undo the move
                    board[i][j] = ' '
                    if beta <= alpha:
                        break
        return best

# Decide the next move of computer
def findBestMove(board) : 
    bestVal = -infinity
    bestMove = (-1, -1)

    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3) :	
        for j in range(3) :
        
            # Check if cell is empty
            if (board[i][j] == ' ') :
            
                # Make the move
                board[i][j] = player

                # compute evaluation function for this
                # move.
                moveVal = minimax(board, 0, False)

                # Undo the move
                board[i][j] = ' '

                # If the value of the current move is
                # more than the best value, then update
                # best value
                if (moveVal > bestVal) :			
                    bestMove = (i, j)
                    bestVal = moveVal

    print("The value of the best Move is :", bestVal)
    print(bestMove)
    return bestMove

def play(g, single):

    '''
    Prepares the game board for the players
    '''

    g.destroy()
    tk = Tk()
    tk.title("TIC TAC TOE")

    global button
    button = []

    global player1_name
    global player2_name

    label = Label(tk, text="Player X:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=1, column=0)

    label = Label(tk, text="Player O:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=2, column=0)

    player1_name = Entry(tk, textvariable=p1, bd=5)
    player1_name.grid(row=1,column=1, columnspan=8)
    player2_name = Entry(tk, textvariable=p2, bd=5)
    player2_name.grid(row=2, column=1, columnspan=8)

    if single:
        player1_name.insert(END, INTELLIGENCE_NAME)
        player1_name.configure(state=DISABLED)

    for i in range(3): # create a 3x3 dimension list with each element binded to a button widget
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            if single:
                set_text = partial(btnClickSingle, board, i, j)
            else:
                set_text = partial(btnClick, board, i, j)
            button[i][j] = Button(tk, font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=set_text)
            button[i][j].grid(row=m, column=n)

def reset (b):

    '''reset the game after the end of a session'''
    
    global flag
    flag = 0
    for i in range(3):
        for j in range(3):
            b[i][j] = ' '
            button[i][j].config(text=' ')

def winner(b, l):
    '''
    check if a player wins by matching three values
    in the same row, column or diagonal if they
    are equal
    '''
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))

def btnClick(board, i, j):

    '''
    Handles the click turns by each player in a
    multi player game and check for winner after each
    turn
    '''

    global bclick, flag, playerb, pa
	
    if board[i][j] == ' ' and bclick == True:
        board[i][j] = 'O'
        button[i][j].config(text=board[i][j])
        playerb = player2_name.get() + " Wins!"
        pa = player1_name.get() + " Wins!"
        if winner(board, "O"):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', pa)
            reset(board)
            return
        elif(flag == 8):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', "it is a tie")
            reset(board)
            return
        bclick = False
        flag += 1

    elif  board[i][j] == ' ' and bclick == False:
        board[i][j] = 'X'
        button[i][j].config(text=board[i][j])
        playerb = player2_name.get() + "Wins!"
        pa = player1_name.get() + "Wins!"
        if winner(board, "X"):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', playerb)
            reset(board)
            return
        elif(flag == 8):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', "it is a tie")
            reset(board)
            return
        bclick = True
        flag += 1
    
    else:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Button already clicked')

def btnClickSingle(board, i, j):
    '''
    Handles the click a by each player in a single
    player game and query the A.I function for it's move
    at it's turn
    '''

    global bclick, flag, playerb, pa
    if board[i][j] == ' ' and bclick == True:
        board[i][j] = 'O'
        button[i][j].config(text=board[i][j])
        playerb = player2_name.get() + " Wins!"
        pa = player1_name.get() + " Wins!"
        if winner(board, "O"):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', playerb)
            reset(board)
            return
        elif(flag == 8):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', "it is a tie")
            reset(board)
            return
        bclick = False
        flag += 1
    else:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Button already clicked')
        return

    if  flag % 2 != 2 and bclick == False:
        i, j = findBestMove(board)
        board[i][j] = 'X'
        button[i][j].config(text=board[i][j])
        playerb = player2_name.get() + " Wins!"
        pa = player1_name.get() + " Wins!"
        bclick = True
        if winner(board, "X"):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', pa)
            reset(board)
            return
        elif(flag == 8):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', "it is a tie")
            reset(board)
            return
        flag += 1

game_single = partial(play, menu, True)
game_multiple = partial(play, menu, False)

head = Label(menu, text = "---Welcome to tic-tac-toe---",
            fg = "black", width = 100, font = 'summer 15 bold', bd = 5)

B1 = Button(menu, text = "Single Player", command = game_single,
            activeforeground = 'red',
            activebackground = "yellow", bg = "red",
            fg = "yellow", width = 100, font = 'summer 15', bd = 5)

B2 = Button(menu, text = "Multi Player", command = game_multiple, activeforeground = 'red',
            activebackground = "yellow", bg = "red", fg = "yellow",
            width = 100, font = 'summer 15', bd = 5)

B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red',
            activebackground = "yellow", bg = "red", fg = "yellow",
            width = 100, font = 'summer 15', bd = 5)
head.pack(side = 'top')
B1.pack(side = 'top')
B2.pack(side = 'top')
B3.pack(side = 'top')
while True:
    menu.mainloop()
