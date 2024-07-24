from datetime import datetime
import csv

PRODUCTS_FILE = "products.csv"
REQUEST_FILE = "request.csv"
I_KEY = 0
I_NAME = 1
I_PRICE = 2
I_QUANTITY = 1

def main():
    products_dict = read_dictionary(PRODUCTS_FILE, I_KEY)
    print(products_dict)

    print("Requested Items")
    with open(REQUEST_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            product_id = row[I_KEY]
            name = products_dict[product_id][I_NAME]
            quantity = row[I_QUANTITY]
            price = float(products_dict[product_id][I_PRICE])

            print(f"{name}: {quantity} @ ${price}")
            




def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    file_dict = {}

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            file_dict[key] = row

    return file_dict
            

if __name__ == "__main__":
    main()







'''
                    0                              1        ....
            0         1         2       0       1         2
reader = [[D150,1 gallon milk,[2.85, 0]], [D083,1 cup yogurt,0.75], []]

     list
reader[0][2][0]



'''