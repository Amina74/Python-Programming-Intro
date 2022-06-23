import random
rand = random.randint(1, 100)
count = 0


while count < 10:
  
    count += 1
    print("Guess", count, ":", end='')
    guess = int(input())
    if guess < rand:
        print("You may want to consider guessing higher values")
    elif guess > rand:
        print("You are way high")    
    else:
        print("\nCorrect answer after only", count, "guesses - Excellent!")    
        break
       