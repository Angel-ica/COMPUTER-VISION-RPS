#Import necessary libraries
from os import nice
from webbrowser import get
import time 
import cv2 as cv
import numpy as np
import random
#from labels3 import moves_values
from keras.models import load_model
#load our trained models
loaded_model=load_model('keras_model.h5', compile =True)
#a list of valid moves
moves =['rock','paper','scissors','nothing']


def get_player_name():
    player_name= input('\n>>please enter your name: ')
    return player_name

name = get_player_name()
print('\ngame will begin in 5 secs')

def get_player_choice():
    #get the image through the webccam
    cap = cv.VideoCapture(0)
    #pass the image into a np array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    #return the print statement if the camera isn't opened and exit
    if not cap.isOpened():
        print('cannot open camera')
        exit()
    ret, frame = cap.read()
    if not ret:
        print("can't receive frame(ending stream)")
        exit()
        #transform the image color
    gray=cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    cv.imshow('ROCK,PAPER,SCISSORS??', gray)
    prediction=loaded_model.predict(data)
    #get the max index of the predictions which are returned in a list
    max_index=np.argmax(prediction[0])
    value=moves[max_index]
    if cv.waitKey(3) & 0xFF == ord('q'):
        exit()
    #release all the used memory 
    cap.release()
    cv.destroyAllWindows
    print(f"{name} chooses {value}")
    return value

#randomly select a move from the list of options 
def get_opponent_choice():
    opponent_choice= random.choice(moves)
    print(f"opponent chooses {opponent_choice} ")
    return opponent_choice
    
def award_points():        
    player_score=0
    opponent_score=0
    user_choice =get_player_choice()
    comp_choice = get_opponent_choice()
    player_total_scores=[]
    opponent_total_scores=[]
    if user_choice != comp_choice:
        if user_choice =='nothing':
            opponent_score+=1
            print(f" you scored {player_score} and opponent scored {opponent_score} ")
        elif comp_choice == 'nothing':
            player_score+=1
            print(f"player scored {player_score} and opponent scored {opponent_score}")
        else:
            if(comp_choice == 'scissors' and user_choice == 'rock') or (comp_choice =='rock' and user_choice == 'paper') or (comp_choice == 'paper' and user_choice == 'scissors'):
                player_score+=1
                player_total_scores.append(player_score)
                print(f"you scored: {player_score}\nopponent scored: {opponent_score}")
            elif (user_choice == 'rock' and comp_choice == 'paper') or (user_choice == 'paper' and comp_choice == 'scissors') or (user_choice == 'scissors' and comp_choice == 'rock'):
                opponent_score+=1
                opponent_total_scores.append(opponent_score)
                print(f"you scored: {player_score}\nopponent scored: {opponent_score}")
    else:
        print(f"both players chose {user_choice}, it's a tie!")
    #return player_score, opponent_score

#main game loop
def game():
    time_limit = 3
    start_time=time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        timer =(time_limit)-(elapsed_time)
        print(timer)
        if timer == 0:
            award_points()
            break  
#game()
#award_points()

def third_time():
    round = 0
    while True:
        award_points()
        round+=1
        get_player_name()
        if round ==3:
            break
third_time()

