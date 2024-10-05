# FOR LOOPS
# Primary used for iterating through a collection

# 1) For-In Loop 
# Iterate through a collection from START to FINISH and visit each element seqentially

# for [item place holder variable] in [collection]

#             0        1       2     ....   N
groceries = ["apple", "milk", "eggs", "bread"]

for item in groceries:
    print(item)

# 2) Range Loop 
# Iterate through a range of numbers. Primarily used to for accessessing collections by index value.

# for [variable to store the current number] in range([start], [stop], [step])
#              start  stop

#             0        1       2     ....   N
groceries =  ["apple", "milk", "eggs", "bread"]
price =      [ 1.50,    4.30,   2.25,   3.50]

for x in range(  0,   len(groceries)):
    print(f"Item: {groceries[x]}")
    print(f"Price: {price[x]}")


# 3) Enumerator Loop 
# Iterate through a range of numbers. Primarily used to for accessessing collections by index value.

#             0        1       2     ....   N
groceries = ["apple", "milk", "eggs", "bread"]

for index, item in enumerate(groceries):
    print(f"{item} is at position {index}")






# WHILE LOOP


# WHILE (CONDITION) -- the condition is evalutated to be true or false

cont = True

while cont == True:
    print("do something...")
    # Add logic to break the loop

    

if cont == True:
    print("do something...")

    

print("END")