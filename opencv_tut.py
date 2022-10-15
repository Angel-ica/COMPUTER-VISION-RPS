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

player_total_scores=[]
opponent_total_scores=[]


def get_player_name():
    player_name= input('\n>>please enter your name: ')
    return player_name

name = get_player_name()

def get_player_choice():
    print('please get ready, game will begin in 3 secs\n')
    time_limit = 3
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        timer =(time_limit)-(elapsed_time)
        #print(timer)
        if timer == 0:
            #get the image through the webcam
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
                #transform the image color to gray
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
            print(f"you choose {value}")
            return value

#randomly select a the ocmputer/opponent's choice from the list of options 
def get_opponent_choice():
    opponent_choice= random.choice(moves)
    print(f"opponent chooses {opponent_choice} ")
    return opponent_choice

#awards points to the winner of each round 
def award_points():        
    player_score=0
    opponent_score=0
    user_choice =get_player_choice()
    comp_choice = get_opponent_choice()
    if user_choice != comp_choice:
        if user_choice =='nothing':
            opponent_score+=1
            opponent_total_scores.append(opponent_score)
            print(f"you scored: {player_score} \nopponent scored: {opponent_score} ")
        elif comp_choice == 'nothing':
            player_score+=1
            player_total_scores.append(player_score)
            print(f"player scored: {player_score} \nopponent scored: {opponent_score}")
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
def play_game():
    round = 1
    while True:
        print(f"\nROUND{round} @{name}\n")
        award_points()
        round+=1
        #finds the player with the highest score after 3 rounds and ends the game
        if round ==4:
            if sum(player_total_scores) > sum(opponent_total_scores):
                print(f"\n@{name}, your total score is {sum(player_total_scores)}")
                print(f"opponent's total score is {sum(opponent_total_scores)}")
                print(f"\ncongratulations {name}, you win!")
                break
            elif sum(opponent_total_scores) > sum(player_total_scores):
                print(f"\n@{name}, your total score is {sum(player_total_scores)}")
                print(f"opponent's total score is {sum(opponent_total_scores)}")
                print(f"\nbetter luck next time {name}, you lose...")
                break
            else:
                print(f"\nit's a tie! how about another game to settle...")
                break
play_game()

