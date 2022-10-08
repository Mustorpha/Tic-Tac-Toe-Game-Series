from tkinter import *
import tkinter.messagebox
from functools import partial
import random
from copy import deepcopy
from intelligence.minimax import Intelligence

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
player = Intelligence('X', 'O')

global board # a global 3x3 dimension list to hold every state of the game
board = [[" " for x in range(3)] for y in range(3)] # the button widget retrieves text value from their corresponding index

# Decide the next move of computer

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
        i, j = player.findBestMove(board)
        board[i][j] = 'X'
        button[i][j].config(text=board[i][j])
        playerb = player2_name.get() + " Wins!"
        pa = player1_name.get() + " Wins!"
        if winner(board, "X"):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', pa)
            reset(board)
            return
        elif(flag == 8):
            tkinter.messagebox.showinfo('Tic-Tac-Toe', "it is a tie")
            reset(board)
            return
        bclick = True
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
