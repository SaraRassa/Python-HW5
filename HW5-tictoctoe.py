import random
from termcolor import colored
import time
start=time.time()
def Game_board():
    for i in range(3):
        for j in range(3):
            print(Game[i][j], end=" ")
        print()
Game=[["_","_","_"],
      ["_","_","_"],
      ["_","_","_"]]
Game_board()

def Check():
    if counter==9:
        end=time.time()
        print(colored("Draw!","red","on_green"))
        print("Time=", end-start)
        exit()
    else:
        for i in range(3):
            for j in range(3):
                if Game[i][0]==Game[i][1]==Game[i][2]==colored("X","green")\
                    or Game[0][j]==Game[1][j]==Game[2][j]==colored("X","green") \
                    or Game[0][0]==Game[1][1]==Game[2][2]==colored("X","green")\
                    or Game[0][2]==Game[1][1]==Game[2][0]==colored("X","green"):
                    end=time.time()
                    print(colored("Player 1 wins!!!","red","on_green"))
                    print("Time=", end-start)
                    exit()
                elif Game[i][0]==Game[i][1]==Game[i][2]==colored("O","yellow")\
                    or Game[0][j]==Game[1][j]==Game[2][j]==colored("O","yellow") \
                    or Game[0][0]==Game[1][1]==Game[2][2]==colored("O","yellow")\
                    or Game[0][2]==Game[1][1]==Game[2][0]==colored("O","yellow"):
                    end=time.time()
                    print(colored("Player 2 wins!!!","red","on_green"))
                    print("Time=", end-start)
                    exit()
def Player(n,s):
    print("Player ",n, "(",s,")")
    while True:
        row=int(input("Which row do you choose? "))
        col=int(input("Which column do you choose? "))
        if 0<= row <= 2 and 0<= col <= 2:
            if Game[row][col]=="_":
                Game[row][col]=s
                break
            else:
                print(colored("Cell is not empty.Try again","red"))
        else:
            print(colored("Out of index.Try again","red"))
    print(colored("Counter= ","red"),counter)
    Game_board()
    Check()

Setting=input("For One Player Enter 1" "\nFor Tow Player Enter 2: " )
if Setting=="2":
    counter=1
    while True:
        Player(1,colored("X","green"))
        counter=counter+1
        Player(2,colored("O","yellow"))
        counter=counter+1
        
if Setting=="1":
    counter=0
    while True:
        Player(1,colored("X","green"))
        counter=counter+1
        print(colored("Computer (O)","yellow"))
        while True:
            row=random.randint(0,2)
            col=random.randint(0,2)
            if Game[row][col]=="_":
                Game[row][col]=colored("O","yellow")
                counter=counter+1
                break
            else:
                print(colored("Cell is not empty.Try again","red"))
            
        print(colored("Counter= ","red"),counter)
        Game_board()
        Check()