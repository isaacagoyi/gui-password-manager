from tkinter import *
from tkinter import messagebox
import random
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(LETTERS))

    for char in range(nr_symbols):
        password_list += random.choice(SYMBOLS)

    for char in range(nr_numbers):
        password_list += random.choice(NUMBERS)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data=password_entry.get()

    is_ok = messagebox.askokcancel(title="Confirm login details", message=f"These are the credentials entered.\n Website:{website_data}\n Email:{email_data}\n Password:{password_data}\n OK to proceed?")

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Ooops", message="Please enter the required fields in website details and password details.")
    else:
        if is_ok:
            with open('data.txt', "a") as file:
                file.write(f"{website_data}|{email_data}|{password_data}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


# Creating a window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creating a canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=2, row=1)

# Creating Labels
website_column = Label(text="Website:")
website_column.grid(column=1, row=2)

email_column = Label(text="Email/Username:")
email_column.grid(column=1, row=3)

password_column = Label(text="Password:")
password_column.grid(column=1, row=4)

# Creating Entries
website_entry = Entry(width=53)
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()

email_entry = Entry(width=53)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=33)
password_entry.grid(column=2, row=4)

# Creating Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=3, row=4)

add_button=Button(text="Add", width=36, command=save_password)
add_button.grid(column=2, row=5, columnspan=2)


window.mainloop()