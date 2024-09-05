from random import randint
from art import logo

EASY_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 3

def check_answer(user_guess, actual_answer, turns):  
  """checks answer against guess. Returns the number of turns remaining."""
  if user_guess > actual_answer:
    print("Too high.")
    return turns - 1
  elif user_guess < actual_answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {actual_answer}.")


def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(a=1, b=100)
  # print(answer)

  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns) # Corrected line
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return 
    elif guess != answer:    
      print("Guess again.")  


game()
 

  

  