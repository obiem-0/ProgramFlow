# Exercise 2 start
x = 8
y = 7

if x > y:
    print('x is greater than y')
elif x < y:
    print('x is smaller than y')
else:
    print('x equals y')
# Exercise 2 ends

# Challenge exercise -
print()
name = input("Whats your name? ")
age = int(input("Whats your age? "))

if 18 <= age <= 30:
    print("You're within the age range. Welcome!")
else:
    print("Unfortunately have to refuse you entry")

print("Your name is {0} and you are {1} years old.".format(name, age))
# Challenge done

# Challenge exercise - Print out capital letters in a string
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for check in quote:
    if check.isupper():
        print(check)
# Challenge done

# Challenge Exercise - Range challenge
for i in range(0, 10):
    print(i)
# Challenge done

# Challenge Exercise - For loop with step to check numbers divisible by 7
for i in range(0, 101):
    if i % 7 == 0:
        print(i)
# Challenge done
