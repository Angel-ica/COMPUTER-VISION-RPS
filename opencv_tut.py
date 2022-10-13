from os import nice
from webbrowser import get
import time 
import cv2 as cv
import numpy as np
import random
from labels3 import moves_values
from keras.models import load_model
loaded_model=load_model('keras_model.h5', compile =True)
moves =['rock','paper','scissors']
# player_score =0
# opponent_score =0

def get_player_name():
    player_name= input('please enter your name: ')
    return player_name
name = get_player_name()

def get_player_choice():
    cap = cv.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    if not cap.isOpened():
        print('cannot open camera')
        exit()
    ret, frame = cap.read()
    if not ret:
        print("can't receive frame(ending stream)")
        exit()
        #
    gray=cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    cv.imshow('ROCK,PAPER,SCISSORS??', gray)
    prediction=loaded_model.predict(data)
    max_index=np.argmax(prediction[0])
    print(f"{name} chooses {max_index}")
    if cv.waitKey(3) & 0xFF == ord('q'):
        exit()

    cap.release()
    cv.destroyAllWindows

player_choice = get_player_choice


def get_opponent_choice(moves_values):
        opponent_choice= random.choice(moves)
        for index,value in enumerate(moves_values):
            if (opponent_choice == value) or (moves.index(opponent_choice)==index):
                print(f"opponent chooses {opponent_choice} ")

opponent_choice = get_opponent_choice

def game():
    time_limit = 3
    start_time=time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        timer =(time_limit)-(elapsed_time)
        print(timer)
        if timer ==0:
            get_player_choice()
            get_opponent_choice(moves_values)
            break


def award_points():
    player_score=0
    opponent_score=0
    if player_choice != opponent_choice:
        if(opponent_choice == 'scissors' and player_choice == 'rock') or (opponent_choice =='rock' and player_choice == 'paper') or (opponent_choice == 'paper' and player_choice == 'scissors'):
            player_score+=1
            print(f"you scored: {player_score}\nopponent scored: {opponent_score}")
        elif (player_choice == 'rock' and opponent_choice == 'paper') or (player_choice == 'paper' and opponent_choice == 'scissors') or (player_choice == 'scissors' and opponent_choice == 'rock'):
            opponent_score+=1
            print(f"you scored: {player_score}\nopponent scored: {opponent_score}")
    else:
            print(f"both players chose {player_choice}, it's a tie!")

def play():
    player_score=0
    opponent_score=0
    if player_choice != opponent_choice:
        if(opponent_choice == 'scissors' and player_choice ==0) or (opponent_choice =='rock' and player_choice == 1) or (opponent_choice == 'paper' and player_choice == 2):
            player_score+=1
            print(f"you scored: {player_score}\nopponent scored: {opponent_score}")
        elif (player_choice == 0 and opponent_choice == 'paper') or (player_choice == 1 and opponent_choice == 'scissors') or (player_choice == 2 and opponent_choice == 'rock'):
            opponent_score+=1
            print(f"you scored: {player_score}\nopponent scored: {opponent_score}")
    else:
            print(f"both players chose {player_choice}, it's a tie!")
            

        

game()
play()
#award_points()

