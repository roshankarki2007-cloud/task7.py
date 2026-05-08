#4
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard")
elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions")
else:
    print("Invalid Credentials. Please try again.")


#5 
light = input("Enter the traffic light color (red, yellow, green): ").lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get Ready")
elif light == "green":
    print("Go")
else:
    print("Error: Invalid traffic light color")

 #6
    season_number=int(input('enter a season number:'))
    if season_number==1:
        print('spring')
    elif season_number==2:
        print('summer')
    elif season_number==3: 
        print('autum')
    elif season_number==4:
        print('winter')
    else:
        print('unknown')

#7  
age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
approved = True

if age < 21 or age > 60:
    print("Condition Failed: Age must be between 21 and 60.")
    approved = False

if income < 30000:
    print("Condition Failed: Monthly income must be at least 30,000.")
    approved = False

if credit_score < 700:
    print("Condition Failed: Credit score must be at least 700.")
    approved = False
if approved:
    print("Loan Approved")
else:
    print("Loan Not Approved")  


#8    

age = int(input("Enter your age: "))
membership = input("Do you have a membership card? (yes/no): ")

if age < 12:
    print("Ticket is free")
else:
    if age <= 60:
        if membership.lower() == "yes":
            print("Ticket price is Rs. 150")
        else:
            print("Ticket price is Rs. 200")
    else:
        print("Ticket price is Rs. 100")

#9
salary = float(input("Enter your salary: "))
years = int(input("Enter your years of service: "))
if years > 5:
    bonus = salary * 0.05
    print("Bonus amount is:", bonus)
else:
    print("No bonus applicable")

 
 #10 
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
print("Area of the circle is:", area)

# 11
 
age = int(input("Enter your age: "))
gender = input("Enter your gender, M or F: ").capitalize()

if 30 > age >= 18:
    if gender == 'M':
        print("Your wage per day is 700")
    
    elif gender == 'F':
        print("Your wage per day is 750")

    else:
        print("Invalid Gender!")

elif 40 >= age >= 30:
    if gender == 'M':
        print("Your wage per day is 800")
    
    elif gender == 'F':
        print("Your wage per day is 850")

    else:
        print("Invalid Age!")

    #12

    num = int(input("Enter a number: "))

if num % 3 == 0:
    if num % 5 == 0:
        print("Fizz Buzz")
    else:
        print("Fizz")

else:
    if num % 5 == 0:
        print("Buzz")
    
    else:
        print(num)
    
    # 13

    usage = float(input("Enter your electricity usage in units: "))

if usage < 100:
    print(f"Cost: Rs. {usage * 5}")

elif usage <= 300:
    print(f"Cost: Rs. {(100 * 5) + ((usage - 100) * 8)}")

elif usage > 300:
    print(f"Cost: Rs. {(100 * 5) + (200 * 8) + ((usage - 300) * 10)}")

    # 14

    player1 = input("Enter your move, Rock, Paper or Scissors: ").lower()
player2 = input("Enter your move, Rock, Paper or Scissors: ").lower()

moves = ['rock', 'paper', 'scissors']

if player1 not in moves or player2 not in moves:
    print("Invalid Move")

else:
    if player1 == player2:
        print("It is a draw")
    
    elif player1 == 'rock' and player2 == 'scissors':
        print("Player 1 wins")
    
    elif player1 == 'paper' and player2 == 'rock':
        print("Player 1 wins")

    elif player1 == 'scissors' and player2 == 'paper':
        print("Player 1 wins")

    else:
        print("Player 2 wins")

     #15

        num = int(input("Enter a number: "))

if num >= 0:
    if num % 2 == 0:
        print(f"{num} is positive and even")
    
    else:
        print(f"{num} is positive and odd")

else:
    print(f"{num} is negative")

# 16

totalAmount = float(input("Enter the total amount: "))
isMember = input("Are you a member? Yes or No: ").lower()

if totalAmount > 1000:
    if isMember == 'yes':
        print(f"Final Amount: {totalAmount - (totalAmount * 0.2)}")

    else:
        print(f"Final Amount: {totalAmount - (totalAmount * 0.1)}")

else:
    print(f"Final Amount: {totalAmount}")


#17

userWeight = float(input("Enter your Earth Weight: "))
planetNum = int(input("Enter a planet number, 1 to 7: "))

relativeGravity = {1 : 0.38, 2 : 0.91, 3 : 0.38, 4 : 2.53, 5 : 1.07, 6 : 0.89, 7 : 1.14}

if planetNum not in relativeGravity:
    print("invalid Planet Number")

else:
    print(f"Your weight on planet {planetNum} is {userWeight * relativeGravity[planetNum]} kg")


# 18

mark1 = int(input("Enter the marks of the first subject: "))
mark2 = int(input("Enter the marks of the second subject: "))
mark3 = int(input("Enter the marks of the third subject: "))
mark4 = int(input("Enter the marks of the fourth subject: "))

totalMarks = mark1 + mark2 + mark3 + mark4
percentage = (totalMarks/400) * 100

print(f"Total Marks: {totalMarks}")
print(f"Percentage: {percentage}")

if percentage <= 40:
    print("Grade: Fail")

elif percentage > 70:
    print("Grade: Distinction")

elif percentage > 60:
    print("Grade: First Division")

elif percentage > 40:
    print("Grade: Pass")


# 19

accountBalance = 5000

pin = input("Enter your pin: ")

if pin == '123':
    option = input("Select the appropriate option: 1. Withdraw  2. Check Balance  3. Exit: ")

    if option == 1:
        amount = int(input("Enter the amount to withdraw: "))
        
        if amount > accountBalance:
            print("Insufficient Funds!")

        else:
            accountBalance -= amount
            print(f"Successfully withdrawn Rs. {amount}! New balance is Rs. {accountBalance}")
    
    elif option == 2:
        print(f"Current balance: {accountBalance}")

    elif option == 3:
        print("Thank you for Visitng!")

    else:
        print("Invalid option!")

else:
    print("Invalid pin! Access Denied!")


# 20

print("Welcome to the Magic Forest!")

direction = input("Where do you want to go? North or South?: ").lower()

if direction == 'north':
    choice = input("Cross the River or follow the path? Cross or follow?: ").lower()

    if choice == 'cross':
        print("Game Over!")
    
    elif choice == 'follow':
        choice = input("Choose from Fairy, Ogre or Elf: ").lower()
        if choice == 'fairy' or choice == 'ogre':
            print("Game Over!")
        
        elif choice == 'elf':
            print("You Win!")

        else:
            print("Invalid Option!")

    else:
        print("Invalid Option!")

elif direction == 'south':
    print("Game Over!")

else:
    print("Invalid Option! Please choose the right direction")


# 21

floorNum = int(input("Enter the floor number: "))

isDoorClosed = True
isRunning = False

if floorNum <= 10 and floorNum >= 0:
    weight = float(input("Enter the total weight: "))
    if weight <= 500:
        
        if isDoorClosed:
            isRunning = True
        else:
            print("Close the door!")
    
    else:
        print("Overweight! Lift Cannot Move!")

else:
    print("Invalid Floor Number!")




