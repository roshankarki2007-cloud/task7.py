 #Solve these questions using for loop
 
# QUESTION 1: Even or Odd from 1 to 5

print("--- Question 1 ---")
for i in range(1, 6):
    if i % 2 == 0:
        print(f"Number {i} is even.")
    else:
        print(f"Number {i} is odd.")
print("\n" + "="*40 + "\n")


# QUESTION 2: Running Total of a List

print("--- Question 2 ---")
my_list = [10, 20, 30, 40]
running_total = 0

for num in my_list:
    running_total += num
    print(f"Added {num}. Running total is {running_total}.")
print("-" * 30)
print(f"Total Sum: {running_total}")
print("\n" + "="*40 + "\n")


# QUESTION 3: Personalized Student Greetings

print("--- Question 3 ---")
student_names = ["Ram", "Hari", "Sita"]
print(" --- Email Greetings Generated ---")
for name in student_names:
    print(f"Hi {name}, your course approval is ready!")
print("\n" + "="*40 + "\n")


# QUESTION 4: Book Chapter Summary

print("--- Question 4 ---")
chapters = [45, 30, 50, 40]
print("--- Book Chapter Summary ---")
for index, pages in enumerate(chapters, start=1):
    print(f"Chapter {index} has {pages} pages.")
print("\n" + "="*40 + "\n")


# QUESTION 5: Product of Elements in a List

print("--- Question 5 ---")
prod_list = [4, 5, 3, 2]
product = 1
for num in prod_list:
    product *= num
print(f"Product of all elements: {product}")
print("\n" + "="*40 + "\n")


# QUESTION 6: Multiplication Table of 11

print("--- Question 6 ---")
table_num = 11
for i in range(1, 11):
    print(f"{table_num} x {i} = {table_num * i}")
print("\n" + "="*40 + "\n")


# QUESTION 7: Reverse a List

print("--- Question 7 ---")
orig_list = [3, 2, 1, 4, 5]
reversed_list = orig_list[::-1]
print(f"Reversed list: {reversed_list}")
print("\n" + "="*40 + "\n")


# QUESTION 8: Common Elements in Two Lists

print("--- Question 8 ---")
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []

for item in list1:
    if item in list2:
        common_elements.append(item)
print(f"Common elements: {common_elements}")
print("\n" + "="*40 + "\n")


# QUESTION 9: Print Specific Elements (1 and 4)

print("--- Question 9 ---")
lst9 = [1, 2, 3, 4]
for x in lst9:
    if x == 1 or x == 4:
        print(x)
print("\n" + "="*40 + "\n")


# QUESTION 10: Remove Vowels from a String

print("--- Question 10 ---")
input_string = "Hello World"
vowels = "aeiouAEIOU"
no_vowels = ""

for char in input_string:
    if char not in vowels:
        no_vowels += char
print(f"String without vowels: {no_vowels}")
print("\n" + "="*40 + "\n")


# QUESTION 11: Count Vowels and Consonants

print("--- Question 11 ---")
sentence = "Loops are Fun"
vowels_str = "aeiou"
vowel_count = 0
consonant_count = 0

for char in sentence.lower():
    if char.isalpha():
        if char in vowels_str:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"vowels: {vowel_count}")
print(f"consonants: {consonant_count}")
print("\n" + "="*40 + "\n")


# QUESTION 12: Separate Elements into Odd and Even Categories

print("--- Question 12 ---")
mixed_numbers = [1, 2, 3, 4, 5]
odds = []
evens = []

for num in mixed_numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print(f"Odd numbers: {odds}")
print(f"Even numbers: {evens}")
print("\n" + "="*40 + "\n")


# QUESTION 13: Check if Number is Prime

print("--- Question 13 ---")
prime_num = int(input("Enter a number to check if it is prime: "))
is_prime = True

if prime_num <= 1:
    is_prime = False
else:
    for i in range(2, int(prime_num ** 0.5) + 1):
        if prime_num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{prime_num} is a prime number.")
else:
    print(f"{prime_num} is not a prime number.")
print("\n" + "="*40 + "\n")


# QUESTION 14: Separate Elements' Datatypes into Separate Lists

print("--- Question 14 ---")
mixed_list = [1, 2, 3, 4, "a", "b"]
integers = []
strings = []

for item in mixed_list:
    if type(item) is int:
        integers.append(item)
    elif type(item) is str:
        strings.append(item)

print(f"Integers list: {integers}")
print(f"Strings list: {strings}")
print("\n" + "="*40 + "\n")


# QUESTION 15: Count Digits and Letters in a String

print("--- Question 15 ---")
alphanumeric_str = input("Enter a string with digits and letters: ")
digits = 0
letters = 0

for char in alphanumeric_str:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1

print(f"Letters: {letters}")
print(f"Digits: {digits}")
print("\n" + "="*40 + "\n")


# QUESTION 16: Username and Password Validity Check

print("--- Question 16 ---")
username = input("Enter username: ")
password = input("Enter password: ")

if len(username) >= 4 and len(password) >= 6:
    print("Valid credentials.")
else:
    print("Invalid. Username must be >= 4 chars and password >= 6 chars.")
print("\n" + "="*40 + "\n")

# QUESTION 17: Odd or Even Number

print("--- Question 17 ---")
num17 = int(input("Enter a number to check odd/even: "))
if num17 % 2 == 0:
    print(f"{num17} is Even")
else:
    print(f"{num17} is Odd")
print("\n" + "="*40 + "\n")

# QUESTION 18: Factorial of a Number

print("--- Question 18 ---")
num18 = int(input("Enter a number for factorial calculation: "))
factorial = 1

if num18 < 0:
    print("Factorial does not exist for negative numbers.")
elif num18 == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num18 + 1):
        factorial *= i
    print(f"The factorial of {num18} is {factorial}")
print("\n" + "="*40 + "\n")

# QUESTION 19: Multiplication Tables (1 to 8)

print("--- Question 19 ---")
for i in range(1, 9):
    print(f"--- Multiplication Table of {i} ---")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  
print("\n" + "="*40 + "\n")

# QUESTION 20: Print 1 and 2 Only from List

print("--- Question 20 ---")
lst20 = [1, 2, 3, 4]
for x in lst20:
    if x == 1 or x == 2:
        print(x)
print("\n" + "="*40 + "\n")

# QUESTION 21: Sum of All Odd Numbers in a Range

print("--- Question 21 ---")
start21 = int(input("Enter start of range for odd sum: "))
end21 = int(input("Enter end of range for odd sum: "))
odd_sum = 0

for num in range(start21, end21 + 1):
    if num % 2 != 0:
        odd_sum += num

print(f"Sum of odd numbers: {odd_sum}")
print("\n" + "="*40 + "\n")

# QUESTION 22: Sum of All Even Numbers in a Range

print("--- Question 22 ---")
start22 = int(input("Enter start of range for even sum: "))
end22 = int(input("Enter end of range for even sum: "))
even_sum = 0

for num in range(start22, end22 + 1):
    if num % 2 == 0:
        even_sum += num

print(f"Sum of even numbers: {even_sum}")
print("\n" + "="*40 + "\n")

# QUESTION 23: Count Spaces in a String

print("--- Question 23 ---")
text23 = input("Enter a string to count spaces: ")
space_count = text23.count(" ")
print(f"Number of spaces: {space_count}")
print("\n" + "="*40 + "\n")

# QUESTION 24: Cube the List Items

print("--- Question 24 ---")
lst24 = [1, 2, 3, 4]
cubed_lst = [x**3 for x in lst24]
print(cubed_lst)
print("\n" + "="*40 + "\n")

# QUESTION 25: Reverse a String

print("--- Question 25 ---")
a25 = "programming"
reversed_a = a25[::-1]
print(reversed_a)
print("\n" + "="*40 + "\n")

# QUESTION 26: Break Loop at 7

print("--- Question 26 ---")
for i in range(50):
    print(i)
    if i == 7:
        break
print("\n" + "="*40 + "\n")

# QUESTION 27: Iterate and Print Every Letter

print("--- Question 27 ---")
text27 = "Python"
for letter in text27:
    print(letter)
print("\n" + "="*40 + "\n")

# QUESTION 28: Greet Names in List

print("--- Question 28 ---")
a28 = ["ram", "shyam", 1, 2]
for name in a28:
    if isinstance(name, str):
        print(f"Hello!, {name}")
print("\n" + "="*40 + "\n")

# QUESTION 29: Append "Dr." Prefix

print("--- Question 29 ---")
a29 = ["ram", "shyam", 1, 2]
dr_list = []
for item in a29:
    dr_list.append(f"Dr.{item}")
print(dr_list)
print("\n" + "="*40 + "\n")

# QUESTION 30: Append Squares to New List

print("--- Question 30 ---")
numbers30 = [1, 2, 3, 4]
squares = []
for num in numbers30:
    squares.append(num**2)
print(squares)
print("\n" + "="*40 + "\n")


# QUESTION 31: Append Positive Numbers to a New List

print("--- Question 31 ---")
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
positive_lst = []

for num in lst1:
    if num > 0:
        positive_lst.append(num)

print(f"Positive numbers: {positive_lst}")
print("\n" + "="*40 + "\n")


# QUESTION 32: Print Numbers Except 3 and 6

print("--- Question 32 ---")
given_list = [0, 1, 2, 3, 4, 5, 6]

for num in given_list:
    if num == 3 or num == 6:
        continue
    print(num)
print("\n" + "="*40 + "\n")


# QUESTION 33: Append Type of Each Element to a New List

print("--- Question 33 ---")
first_list = [10, "Hello", 3.14, True, [1, 2]]
type_list = []

for element in first_list:
    type_list.append(type(element))

print(f"Types list: {type_list}")
print("\n" + "="*40 + "\n")


# QUESTION 34: Use Else Block After For Loop

print("--- Question 34 ---")
for i in range(5):
    print(i)
else:
    print("Done")
print("\n" + "="*40 + "\n")


# QUESTION 35: Print Number Series (105 down to 7, step -7)

print("--- Question 35 ---")
for num in range(105, 6, -7):
    print(num, end=" ")
print()  # For newline
print("\n" + "="*40 + "\n")


# QUESTION 36: Remove Bad Characters and Spaces from String

print("--- Question 36 ---")
bad_chars = [';', ':', '!', "*", " "]
string = "py;th* o:n ! ;py * t*h:o !n"
clean_string = ""

for char in string:
    if char not in bad_chars:
        clean_string += char

print(f"Cleaned string: {clean_string}")
print("\n" + "="*40 + "\n")


# QUESTION 37: Count Even and Odd Numbers from a Series

print("--- Question 37 ---")
numbers_series = [12, 35, 9, 56, 24, 73, 80, 95]
even_count = 0
odd_count = 0

for num in numbers_series:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
print("\n" + "="*40 + "\n")


# QUESTION 38: Sum of Multiples of 3 or 5 Below 100

print("--- Question 38 ---")
multiples_sum = 0

for num in range(3, 100):
    if num % 3 == 0 or num % 5 == 0:
        multiples_sum += num

print(f"Sum of multiples of 3 or 5: {multiples_sum}")
print("\n" + "="*40 + "\n")


# QUESTION 39: Sum of Even and Odd Numbers Separately (1 to 100)

print("--- Question 39 ---")
total_even_sum = 0
total_odd_sum = 0

for num in range(1, 101):
    if num % 2 == 0:
        total_even_sum += num
    else:
        total_odd_sum += num

print(f"Sum of even numbers (1-100): {total_even_sum}")
print(f"Sum of odd numbers (1-100): {total_odd_sum}")
print("\n" + "="*40 + "\n")


# QUESTION 40: Count Occurrences of a Specific Number

print("--- Question 40 ---")
search_list = [1, 3, 7, 8, 7, 5, 4, 7, 2]
target_num = 7
occurrence_count = 0

for num in search_list:
    if num == target_num:
        occurrence_count += 1

print(f"The number {target_num} appears {occurrence_count} times.")
print("\n" + "="*40 + "\n")

 