# module 

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import urllib.request
from urllib.request import urlopen

# splash screen
splash = Tk()
splash.title ('GuessGame')
splash.geometry ('400x400')
splash.resizable (0,0)
splash.configure (background = 'red')
spl_lab = Label (splash, text = 'GodARD Devos \n GuessGame', bg = 'yellow', fg = 'blue', font = ('vendana', 20, 'bold'))
spl_lab.pack (pady = 150)

# details and giving shape

def main_game_window():
    global attempts
    global pcnum
    global LabH
    global LabL
    global LabO
    global LabW
    splash.destroy()
    guessgame = tk.Tk()
    guessgame.geometry ('1200x770')
    guessgame.title ("GuessIT Game")
    guessgame.configure (background = '#BF3EFF')
    guessgame.resizable (0,0)
    guessgame.minsize (width = 950, height = 600)


    # app logic

    LabW = Label(guessgame)  
    LabO = Label(guessgame)
    LabH = Label(guessgame) 
    LabL = Label(guessgame)

    attempts = 3
    pcnum = random.randint (1,10)

    def clear():
            usernum.delete (0, END)

    def gamelogic():
            global pcnum
            global attempts
            global LabW
            global LabL
            global LabH
            global LabO
            attempts = attempts - 1
            userguess = int (usernum.get())
            restarts ['state'] = DISABLED

            if ( attempts >= 0 ) :

                    if (userguess == pcnum):
                            LabW = Label (frameB1, bg = '#EE1289', fg = '#7FFF00', text = "  Congratulations ! You Won !  ", font = ('vendana',25, 'bold'))
                            LabW.pack( anchor = 'sw', pady = 20, padx = 358)
                            restarts ['state'] = NORMAL
                            submit ['state'] = DISABLED

                    elif ( attempts == 0 ) :
                            LabO = Label (frameB3, bg = '#2E2E2E', fg = '#FF4040', text = f'No Attempts Left ! You Lose ! PC Guess Was {pcnum} . Restart .', font = ('vendana', 25, 'bold'))
                            LabO.pack( anchor = 'sw', pady = 5, padx = 155)
                            restarts ['state'] = NORMAL
                            usernum ['state'] = DISABLED
                            submit ['state'] = DISABLED
                    

                    elif ( userguess > pcnum ):
                            LabL = Label (frameB2, bg = '#FF1493', fg = '#00FF00', text = f'Try Something Lower & You Have {attempts} Attempts Left !', font = ('vendana', 20, 'bold'))
                            LabL.pack( anchor = 'sw', pady = 5, padx = 263)

                    elif ( userguess < pcnum ):
                            LabH = Label (frameB2, bg = '#FF1493', fg = '#00FF00', text = f'Try Something Higher & You Have {attempts} Attempts Left !', font = ('vendana', 20, 'bold'))
                            LabH.pack( anchor = 'sw', pady = 5, padx = 260)

    def quitout ():
        messagebox.showinfo ( 'GuessGame', 'You Want To Exit The Game ? \n Click "OK" If You Want To !! ')
        return guessgame.destroy()

    def restart ():
            gamelogic()
            frameB1.pack_forget()
            frameB2.pack_forget()
            LabW.pack_forget()
            LabO.pack_forget()
            LabL.pack_forget()
            usernum ['state'] = NORMAL
            submit ['state'] = NORMAL
            usernum.delete (0, END)
            usernum.insert(0, 'Enter Guess Here') 
            

    # frames

    frameH = Frame (guessgame, width = 30, height = 100, bg = 'cyan')
    frameH.pack(fill = 'both', side = 'top')

    frameBH = Frame (guessgame,width = 30, height = 4, bg = 'orange')
    frameBH.pack(fill = 'both', side = 'top')

    frameB1 = Frame (guessgame, width = 2000, height = 30, bg = 'orange')
    frameB1.pack()

    frameB2 = Frame (guessgame, width = 2000, height = 30, bg = 'orange')
    frameB2.pack()

    frameB3 = Frame (guessgame, width = 2000, height = 30, bg = 'orange')
    frameB3.pack()

    frameBT = Frame (guessgame, bg = 'orange', width = 2000, height = 175)
    frameBT.pack()

    frameT = Frame (guessgame, width = 950, height = 30, bg = 'blue')
    frameT.pack( fill = 'both', side = 'bottom' )

    # open photos

    # resize image

    # labels

    head = Label (frameH, text = '[ ! Guess IT ! ]', bg = 'magenta', fg = 'yellow', font = ('vendana', 40, 'bold'))
    head.pack(side = 'top')

    rule = Label (frameBH, text = '''>>><<<

    1. Computer Picked A Number. (1 - 10)
                    2. Guess The Picked Number In Three Guesses.
            3. Computer Will Guide You By Command.
    4. Commands Are Higher And Lower.
    5. Press 'Clear' First Then Start To Play.

    >>><<<''', bg = 'red', fg = 'blue', font = ('vendana',11, 'bold', 'italic'))
    rule.pack(fill = 'both', side = 'top', pady = 10, padx = 5)

    tail = Label (frameT, text = '! Thank You For Playing ! Restart To Play Again !', bg = '#00FF00', fg = 'magenta', font = ('vendana',40, 'bold'))
    tail.pack(padx = 3, pady = 5)

    # user

    usernum = Entry (frameBH, width = 25, bg = 'pink', fg = 'green', borderwidth = 4,
    font = ('vendana', 30, 'bold', 'italic', 'underline'))
    usernum.insert (0,"Enter Guess Here")
    usernum.pack()

    # button

    clear = Button (frameBH, bg = 'hotpink', fg = 'blue', text = 'CLEAR', font = ('vendana', 15, 'bold'), command = clear)
    clear.pack( side = 'left', padx = 300 , pady = 2)

    submit = Button (frameBH, bg = 'blue', fg = 'hotpink', text = 'SUBMIT', font  = ('vendana', 15, 'bold'), command = gamelogic)
    submit.pack( side = 'left', padx = 1 , pady = 2)

    restarts = Button (frameBH, bg = 'hotpink', fg = 'blue', text = 'RESTART', font = ('vendana', 15, 'bold'), command = restart )
    restarts.pack( side = 'left', padx = 2 , pady = 2)

    quitout = Button (frameBH, bg = 'blue', fg = 'hotpink', text = 'QUIT', font = ('vendana', 15, 'bold'), command = quitout)
    quitout.pack(anchor = 'sw')

# spalsh screen timer

splash.after ( 2500, main_game_window)

# run app

mainloop()