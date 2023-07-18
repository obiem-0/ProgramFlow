parrot = "Norwegian Blue"

for character in parrot:
    print(character)


for i in range(25):
    print("i is now {}".format(i))

for i in range(10, -3, -2):  # backwards
    print("i is now {}".format(i))

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i*j))
    print("-------------------------")
