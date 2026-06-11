# question 1 : you are a adult 



while True:
  age = int(input('please enter your age'))
  if age < 18:
    print('you are a minor')
  elif age >= 18 and age < 60:
      print('you are an adult')
  elif age  >=60:
    print('you are an senior citizen')
    user_input = input('do you wnat to continue:')
    if user_input =='no':
        break


# Question 2: Bus Waiting Simulator    

while(user_input:=input('vehicle name :')) !='bus':
    if user_input =='bus':

     print('wait is over')
else:
    print('waiting')



# Question 3: Frequency Table Generator
ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
content_ratings = {}
for i in ratings:
   if i in content_ratings:
      content_ratings[i]+=1
   else:
      content_ratings[i]=1
      print( content_ratings)

for i in ratings:
   content_ratings[i]= content_ratings.get(i,0)+1
   print(content_ratings)

for i in range(len(ratings)):
   content_ratings[ratings[i]]= content_ratings.get(ratings[i],0)+1
   i+=1
   print(content_ratings)

i=0
while i< len(ratings):
   content_ratings[ratings[i]]= content_ratings.get(ratings[i],0)+1
   i+=1
   print(content_ratings)


# Question 4: Guessing Game
import random

secret_number = random.randint(1, 10)
attempts = 0


print("I have chosen a random number between 1 and 10. Try to guess it!")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Guess higher!")
    elif guess > secret_number:
        print("Guess lower!")
    else:
        print(f"Correct! It took you {attempts} attempts to guess the correct number.")
        break
print("\n" + "="*40 + "\n")



# question 5 Login System with Limited Attempts
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "1234":
        print("Login successful")
        break
    else:
        print("Invalid credentials, try again.")
        attempts += 1

if attempts == 3:
    print("too many failed attempts")
print("\n" + "="*40 + "\n")

# Question 6: Multiplication Quiz System
import random

while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    correct_answer = num1 * num2
    
    user_input = input(f"What is {num1} * {num2}? (or type 'exit' to quit): ").strip().lower()
    
    if user_input == 'exit':
        print("Quiz ended.")
        break
        
    if int(user_input) == correct_answer:
        print("correct")
    else:
        print("Incorrect, try again.")
print("\n" + "="*40 + "\n")


# Question 7  Count Good Luck Phrases

count = 0

while count < 3:
    name = input("Enter a name: ").strip().lower()
    
    if name == "good luck":
        count += 1
        if count < 3:
            print(f"you typed the same word {count} times.")
        else:
            print("you typed good luck three times.")
print("\n" + "="*40 + "\n")


import random

# Question 8: 7-Attempt Guessing Game
target_num = random.randint(1, 50)
remaining_attempts = 7
print("I have chosen a random number between 1 and 50. You have 7 attempts to guess it!")

while remaining_attempts > 0:
    print(f"Remaining attempts: {remaining_attempts}")
    guess_input = input("Enter your guess: ")
    
    if not guess_input.isdigit():
        print("Please enter a valid number.")
        continue
        
    guess = int(guess_input)
    remaining_attempts -= 1
    
    if guess == target_num:
        print("Correct! You win!")
        break
    elif guess < target_num:
        print("Guess higher!")
    else:
        print("Guess lower!")

if remaining_attempts == 0 and guess != target_num:
    print(f"Game over! The correct number was {target_num}.")
print("\n" + "="*40 + "\n")

# Question 9: Elevator System Simulator
current_floor = 1
print(f"Elevator is currently at floor {current_floor}.")

while True:
    floor_input = input("Enter destination floor (or 0 to exit): ").strip()
    
    try:
        target_floor = int(floor_input)
    except ValueError:
        print("Invalid input. Please enter a valid floor number.")
        continue
        
    if target_floor == 0:
        print("Thank you for riding. Goodbye!")
        break
        
    if target_floor > current_floor:
        print("Going up...")
        current_floor = target_floor
        print(f"Arrived at floor {current_floor}.")
    elif target_floor < current_floor:
        print("Going down...")
        current_floor = target_floor
        print(f"Arrived at floor {current_floor}.")
    else:
        print(f"You are already on floor {current_floor}.")
print("\n" + "="*40 + "\n")



# Question 10: Rock, Paper, Scissors Game
player1_score = 0
player2_score = 0

while True:
    p1_choice = input("Player 1, enter rock, paper, or scissor: ").strip().lower()
    p2_choice = input("Player 2, enter rock, paper, or scissor: ").strip().lower()
    
    if p1_choice == p2_choice:
        print("it's a tie")
    elif (p1_choice == "rock" and p2_choice == "scissor") or \
         (p1_choice == "paper" and p2_choice == "rock") or \
         (p1_choice == "scissor" and p2_choice == "paper"):
        player1_score += 1
    else:
        player2_score += 1
        
    print(f"Current Score -> Player 1: {player1_score} | Player 2: {player2_score}")
    
    if player1_score == 5:
        print("player1 won the game")
        break
    elif player2_score == 5:
        print("player2 won the game")
        break
print("\n" + "="*40 + "\n")

# Question 11: Decoupled Counter Output
left = 1
right = 49

while left <= 49:
    print(f"{left} – {right}")
    left += 1
    right -= 1
print("\n" + "="*40 + "\n")

# Question 12: Sum Up To Given Number
limit = int(input("Enter a number: "))
total_sum = 0
current = 1

while current <= limit:
    total_sum += current
    current += 1

print(f"The sum of all numbers from 1 up to {limit} is: {total_sum}")
print("\n" + "="*40 + "\n")

# Question 13: Alphabet Series A to Z
ascii_val = 65
alphabet_string = ""

while ascii_val <= 90:
    alphabet_string += chr(ascii_val) + " "
    ascii_val += 1

print(alphabet_string.strip())
print("\n" + "="*40 + "\n")

# Question 14: Find Numbers Below 20
number = [2, 40, 21, 31, 10, 7, 5]
index = 0

print("Numbers below 20:")
while index < len(number):
    if number[index] < 20:
        print(number[index])
    index += 1
print("\n" + "="*40 + "\n")