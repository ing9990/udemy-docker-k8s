import random

min = int(input("Enter the min value: "))
max = int(input("Enter the max value: "))

print("")

if min >= max:
    print("Invalid value")
else:
    print(random.randint(min, max))
