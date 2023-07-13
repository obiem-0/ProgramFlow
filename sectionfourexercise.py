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

# Challenge exercise
print()
name = input("Whats your name? ")
age = int(input("Whats your age? "))

if 18 <= age <= 30:
    print("You're within the age range. Welcome!")
else:
    print("Unfortunately have to refuse you entry")

print("Your name is {0} and you are {1} years old.".format(name, age))
