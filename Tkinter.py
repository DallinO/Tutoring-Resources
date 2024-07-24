import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def create_widgets():
    create_date_field()
    create_hour_dropdown()
    create_minute_dropdown()
    create_description_field()
    create_submit_button()

def create_date_field():
    tk.Label(root, text="Select Date:").grid(row=0, column=0, padx=10, pady=5)
    global cal
    cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
    cal.grid(row=0, column=1, padx=10, pady=5)

def create_hour_dropdown():
    tk.Label(root, text="Select Hour:").grid(row=1, column=0, padx=10, pady=5)
    global hour_var
    hour_var = tk.StringVar()
    hour_dropdown = ttk.Combobox(root, textvariable=hour_var)
    hour_dropdown['values'] = [str(i) for i in range(1, 25)]
    hour_dropdown.grid(row=1, column=1, padx=10, pady=5)
    hour_dropdown.current(0)  # Set default value

def create_minute_dropdown():
    tk.Label(root, text="Select Minute:").grid(row=2, column=0, padx=10, pady=5)
    global minute_var
    minute_var = tk.StringVar()
    minute_dropdown = ttk.Combobox(root, textvariable=minute_var)
    minute_dropdown['values'] = [str(i) for i in range(0, 60)]
    minute_dropdown.grid(row=2, column=1, padx=10, pady=5)
    minute_dropdown.current(0)  # Set default value

def create_description_field():
    tk.Label(root, text="Description:").grid(row=3, column=0, padx=10, pady=5)
    global desc_entry
    desc_entry = tk.Entry(root, width=30)
    desc_entry.grid(row=3, column=1, padx=10, pady=5)

def create_submit_button():
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

def submit():
    selected_date = cal.get_date()
    selected_hour = hour_var.get()
    selected_minute = minute_var.get()
    description = desc_entry.get()
    
    submission = {
        "Date": selected_date,
        "Hour": selected_hour,
        "Minute": selected_minute,
        "Description": description
    }
    
    submissions.append(submission)
    
    print("Submission saved:", submission)

# Create the main window
root = tk.Tk()
root.title("Input Form")

# Create a list to store submissions
submissions = []

# Create and arrange the widgets
create_widgets()

# Run the application
root.mainloop()
