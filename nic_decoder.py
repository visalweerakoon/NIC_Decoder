from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def decode_nic(nic):
    nic = nic.strip()

    # Detect NIC type
    if len(nic) == 10:  # Old NIC
        if not (nic[:-1].isdigit() and nic[-1].upper() == 'V'):
            return None
        year = int(nic[0:2])
        year += 1900 if year > 20 else 2000
        day_count = int(nic[2:5])

    elif len(nic) == 12:  # New NIC
        if not nic.isdigit():
            return None
        year = int(nic[0:4])
        day_count = int(nic[4:7])

    else:
        return None

    # Gender detection
    if day_count > 500:
        gender = "Female"
        day_count -= 500
    else:
        gender = "Male"

    # Validate day count
    max_days = 366 if is_leap(year) else 365
    if day_count < 1 or day_count > max_days:
        return None

    # Convert to REAL birthday (fixed -1 day issue)
    birthday = datetime(year, 1, 1) + timedelta(days=day_count - 1)
    birthday = birthday - timedelta(days=1)

    # Age calculation
    today = datetime.today()
    age = today.year - birthday.year - (
        (today.month, today.day) < (birthday.month, birthday.day)
    )

    return {
        "Year": year,
        "Gender": gender,
        "Birthday": birthday.strftime("%Y-%m-%d"),
        "Age": age
    }


def process():
    nic = entry.get()
    result = decode_nic(nic)

    if not result:
        messagebox.showerror("Error", "Invalid NIC Number")
        return

    year_label.config(text=f"Year: {result['Year']}")
    gender_label.config(text=f"Gender: {result['Gender']}")
    birthday_label.config(text=f"Birthday: {result['Birthday']}")
    age_label.config(text=f"Age: {result['Age']}")


# GUI Window
root = tk.Tk()
root.title("NIC Decoder LK")
root.geometry("350x300")
root.resizable(False, False)

# Title
title = tk.Label(root, text="NIC Decoder LK", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Input
entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=10)

entry.bind("<Return>", lambda event: process())

# Button
btn = tk.Button(root, text="Decode", command=process, font=("Arial", 12))
btn.pack(pady=5)

# Results
year_label = tk.Label(root, text="", font=("Arial", 11))
year_label.pack()

gender_label = tk.Label(root, text="", font=("Arial", 11))
gender_label.pack()

birthday_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
birthday_label.pack()

age_label = tk.Label(root, text="", font=("Arial", 11))
age_label.pack(pady=5)

# Run app
root.mainloop()