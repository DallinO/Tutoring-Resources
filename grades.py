def add_grade(grades):
    grade = int(input("Grade: "))
    if 0 <= grade <= 100:
        grades.append(grade)
    else:
        print("Invalid input")
    

def remove_grade(grades):
    index = int(input("Enter the position of the grade: "))
    if 0 <= index <= len(grades):
        grades.pop(index - 1)
    else:
        print("Invalid input")
    

def display_grades(grades):
    try:
        if len(grades) > 0:
            for i in range(len(grades)):
                print(f"{i + 1}. {grades[i]}")
        else:
            print("No grades available.")
    except TypeError as te:
        print("Error: The 'grades' variable should be a list. Details:", te)
    except IndexError as ie:
        print("Error: An index error occurred. Details:", ie)
    except Exception as e:
        print("An unexpected error occurred. Details:", e)

def calculate_average(grades):
    if len(grades) > 0:
        return sum(grades) / len(grades)
    else:
        print("No grades to calculate average.")
        return None

def grade_to_letter(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 70 <= grade < 80:
        return 'C'
    elif 60 <= grade < 70:
        return 'D'
    elif 0 <= grade < 60:
        return 'F'
    else:
        return 'Invalid grade'

def display_grades_in_letter(grades):
    try:
        if len(grades) > 0:
            for i in range(len(grades)):
                print(f"{i + 1}. {grade_to_letter(grades[i])}")
        else:
            print("No grades available.")
    except TypeError as te:
        print("Error: The 'grades' variable should be a list. Details:", te)
    except IndexError as ie:
        print("Error: An index error occurred. Details:", ie)
    except Exception as e:
        print("An unexpected error occurred. Details:", e)

def main():
    grades = []
    choice = 0

    while choice != 6: 
        print("1) Add Grade")
        print("2) Remove Grade")
        print("3) Display Grade")
        print("4) Calculate Average")
        print("5) Convert To Letter")
        print("6) Quit")

        choice = int(input("Option: "))

        if choice == 1:
            add_grade(grades)
        if choice == 2:
            remove_grade(grades)
        if choice == 3:
            display_grades(grades)
        if choice == 4:
            print(calculate_average(grades))
        if choice == 5:
            grade = float(input("Enter the grade: "))
            print(f"Letter Grade: {grade_to_letter(grade)}")

# Example usage
if __name__ == "__main__":
   main()
