# WITH OPEN( FILENAME, MODE) AS *VARIABLE*
# COMMON MODES:
#   "a" - Append
#   "r" - Read
#   "w" - Write
with open("Volume Data.txt", "r") as file:
    for line in file:
        data = line.split(',')
        print(f"Width: {data[0]}")
        print(f"Ratio: {data[1]}")

for x in range(3):
    with open("Volume Data.txt", "a") as file:
        width = int(input("Width: "))
        ratio = int(input("Ratio: "))
        diameter = int(input("Diameter: "))
        volume = width * ratio / diameter
        # Add a '\n' at the end of the write so that the next data
        # to be writen to the file starts on a new line.
        file.write(f"{width},{ratio},{diameter},{volume}\n")





# with open( FILENAME, MODE) as VARIABLE
with open("Volume Data.txt", "a") as f:
    f.write("9")

with open("Volume Data.txt", "r") as f:
    for line in f:
        print(line)