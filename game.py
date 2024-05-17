import random
import words.txt
def game_instruction():
  print("""Welcome to my wordle. 
Every correct letter in the correct position will be "✔". 
Every incorrect letter will be "❌".
Every correct letter but in the wrong place will be "➕".  """)

def check_word():
    hidden_word = words[random.randint(0,7000]
    attempt = 6
    while attempt > 0:
        guess = str(input("Guess the word: "))
        if guess == hidden_word:
            print("You guessed the word! No way!")
            break
        else:
            attempt -= 1
            print(f"You have {attempt} attempts left \n")
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    print(word + "✔")
                elif word in hidden_word:
                    print(word + "➕")
                else:
                    print(word + "❌")
            if attempt == 0:
                print(" Game over !!!!!")


game_instruction()
check_word()
