print("Welcome! To Guess The Number Game🎮")
import random
score=0
while True:
    secret_number = random.randint(1, 20)
    attempts = 0  
    print("\n🎲 I'm Thinking Of A Number Between 1 and 20. Can You Guess It?")


    while True:
        guess=int(input("Enter Your Guess:"))
        attempts +=1
    
        if guess<secret_number:
            print("Too Low📉")
        elif guess>secret_number:
         print("Too High📈")
        else:
            print(f"🎉CORRECT! You Guessed It In {attempts} Tries.")
            score += 1
            break

    print(f"🏆 Your Current Score: {score}")

    play_again = input("🔁 Do you want to play again? (yes/no): ").lower()

    if play_again !="yes":
     print("Thanks For Playing 🎉 Final Score:",score)
     break