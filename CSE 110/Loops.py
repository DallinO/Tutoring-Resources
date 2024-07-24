number = -1

while number != 0:
    number = int(input("Enter the number to factor: "))
    for x in range(1, number + 1):
        if (number % x) == 0:
            print(x)


# WHILE (CONDITION) -- the condition is evalutated to be true or false