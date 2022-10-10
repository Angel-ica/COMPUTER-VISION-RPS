#importing necessary libraries
import random
import cv2 as cv
import numpy as np
from keras.models import load_model
#pass the loaded model/images into a variable
loaded_model = load_model('keras_model.h5')
#creating a list of valid computer moves
opponent_moves =['rock','paper','scissors']

#create game class
class RPS:
    def __init__(self,opponent_moves,loaded_model):
        self.player_name=input('your name: ')
        self.computer_choice= random.choice(opponent_moves)
        #self.player_choice=loaded_model.predict

    def get_player_choice(self):
            #open the dafault camera (our webcam)
            cap = cv.VideoCapture(0)
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            #initiate an infinite loop(to be broken later by 'break' statement)
            while True: 
                #ret is a boolean regarding whether or not theres a return or not and the frame is each frame that is returned
                ret, frame = cap.read()
                resized_frame = cv.resize(frame, (224, 224), interpolation = cv.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
                data[0] = normalized_image
                prediction = loaded_model.predict(data)
                cv.imshow('frame', frame)
                #print(prediction)
                print('rps')
                max_index=np.argmax(prediction[0])
                for index,value in enumerate(opponent_moves):
                    print(index,value)
                    print(f"{self.player_name} chose {max_index}")
                print(f"opponent chose {self.computer_choice}")
                # Press q to close the window
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break

def run_game():
    game=RPS(opponent_moves,loaded_model)
    game.get_player_choice()

run_game()
