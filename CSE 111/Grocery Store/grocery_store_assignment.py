from datetime import datetime
import csv

PRODUCTS_FILE = "products.csv"
REQUEST_FILE = "request.csv"
I_KEY = 0
I_NAME = 1
I_PRICE = 2
I_QUANTITY = 1
SALES_TAX = 0.06

def main():
    products_dict = read_product_dictionary(PRODUCTS_FILE, I_KEY)
    request_dict = read_request_dictionary(REQUEST_FILE, I_KEY)

    print("Inkom Emporium")

    number_of_items = 0
    subtotal = 0
    for key in request_dict:
        name = products_dict[key][I_NAME]
        quantity = request_dict[key]
        price = float(products_dict[key][I_PRICE])

        number_of_items += quantity
        subtotal += price * quantity

        print(f"{name}: {quantity} @ ${price}")

    subtotal = round(subtotal, 2)
    tax = round(subtotal * SALES_TAX, 2)
    total = subtotal + tax
    time = datetime.now().strftime("%a %b %d %Y -- %H:%M:%S")

    print(f"Number of Items: {number_of_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${tax:.2f}")
    print(f"Total: {total:.2f}")
    print("Thank you for shopping at the Inkom Emporium.")
    print(time)


def read_product_dictionary(filename, key_column_index):
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


def read_request_dictionary(filename, key_column_index):
    file_dict = {}

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            if key in file_dict:
                file_dict[key] += int(row[I_QUANTITY])
            else:
                file_dict[key] = int(row[I_QUANTITY])

    return file_dict
            

if __name__ == "__main__":
    main()