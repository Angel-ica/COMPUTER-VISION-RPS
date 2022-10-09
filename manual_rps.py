#Import necessary libraries
import random

#create a list of valid options/moves
moves=['rock','paper','scissors']

#create game class
class RPS:
    def __init__(self,moves):
        self.player_name = input('\n>>player name: ').lower()
        self.player_choice = input('>>your  move: ').lower()
        self.opponent_choice=random.choice(moves)
        self.opponent_choice=random.choice(moves)
        self.player_score=0
        self.opponent_score=0

    def validate_choice(self):
        self.player_choice
        self.player_name
        if self.player_choice in moves:
            print(f"\n{self.player_name} chooses {self.player_choice} and opponent chooses {self.opponent_choice}")
        else:
            print(f"invalid input '{self.player_choice}'")

    def award_points (self):
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
    print("\nlet's play\n")
    game=RPS(moves)
    game.game_mode() 
    
play_game()

