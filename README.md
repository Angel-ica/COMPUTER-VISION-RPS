# Computer-Vision
This project is an immersive game of Rock-Paper-Scissors between the computer (the opponent) and the player that uses python's Open-Cv library to classify the player's move. 
Teachable Machines is used to train and test our models(player's accepted and expected moves) which are then used together with the OPen-Cv library for the running of our application.

'manual_rps.py' is used to play a normal game of RPS, no form of image classification is employed here. 

The main task of image classification/ recognition is performed in 'webcam_rps.py'. 

--------------------------------

#Import necessary libraries

import time 
--- Best out of 3 wins, time is used to countdown to next round.

--------------------------------
import cv2 as cv 
--- cv2 is used for image processing, to capture and display the player's moves. 

--------------------------------
import numpy as np
--- numpy is used to store the image for prediction.

--------------------------------
import random 
--- randomly select the opponent's (the computer's) move.

--------------------------------
from keras.models import load_model 
--- keras.models is a module in the keras library for providing an interface for training nn models.

--------------------------------
loaded_model=load_model('keras_model.h5', compile =True) 
--- uses the 'load_model' function to load the pretrained model in 'keras_model.h5' file. Compile =True means that after loading, the model will be recompiled using the same parameters during training. 

--------------------------------
moves =['rock','paper','scissors','nothing'] 
--- a list of valid moves. 

--------------------------------
A timer specifies the start of a new round and points are awarded to the winner of each round. After 3 rounds, the winner is announced and then the game terminates. (An option to play again is available.)
