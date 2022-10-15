#Import necessary libraries
import random

#create a list of valid options/moves
moves=['rock','paper','scissors']
print(f"\nlet's play\n")
name=input('>>please enter your name: ')
print('nice name!')
#create game class
class RPS:
    def __init__(self,moves):
        self.player_choice = input(f"\n>>your  move @{name}: ").lower()
        self.opponent_choice=random.choice(moves)
        self.opponent_choice=random.choice(moves)
        self.player_score=0
        self.opponent_score=0

    def validate_choice(self):
        self.player_choice
        if self.player_choice in moves:
            print(f"{name} chooses {self.player_choice} and opponent chooses {self.opponent_choice}")
        else:
            print(f"invalid input '{self.player_choice}'")

    def award_points(self):
        if self.opponent_choice!=self.player_choice:
            if(self.opponent_choice == 'scissors' and self.player_choice == 'rock') or (self.opponent_choice =='rock' and self.player_choice == 'paper') or (self.opponent_choice == 'paper' and self.player_choice == 'scissors'):
                self.player_score+=1
                print(f"you scored: {self.player_score}\nopponent scored: {self.opponent_score}")
            elif (self.player_choice == 'rock' and self.opponent_choice == 'paper') or (self.player_choice == 'paper' and self.opponent_choice == 'scissors') or (self.player_choice == 'scissors' and self.opponent_choice == 'rock'):
                self.opponent_score+=1
                print(f"you scored: {self.player_score}\nopponent scored: {self.opponent_score}")
        else:
            print(f"both players chose {self.player_choice}, it's a tie!")

    def game_mode(self):
        self.validate_choice()
        self.award_points()


def play_game():
    game=RPS(moves)
    game.game_mode() 
    
play_game()

