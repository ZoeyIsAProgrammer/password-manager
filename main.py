import json
import random
from tkinter import *
from tkinter import messagebox
import pyperclip

pdx = 3
pdy = 3


# ---------------------------- Search ------------------------------- #
def tied_with_search():
    answer = website_entry.get().title()
    try:
        with open('my_passwords.json', 'r') as json_file:
            web_dict = json.load(json_file)
            username = web_dict[answer]['username']
            password = web_dict[answer]['password']
    except FileNotFoundError:
        messagebox.showinfo(message="There's no information stored yet!")
    except KeyError:
        messagebox.showinfo(message="Please enter the correct website name.")
    else:
        messagebox.showinfo(title=answer, message=f'Username: {username}\nPassword: {password}')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def tied_to_generate():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def tied_to_add():
    web_str = website_entry.get().title()
    em_str = email_entry.get()
    pw_str = password_entry.get()
    new_data = {
        web_str: {
            "username": em_str,
            "password": pw_str
        }
    }
    if len(web_str) == 0 or len(em_str) == 0 or len(pw_str) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t let any of the fields empty.')
    else:
        is_on = messagebox.askokcancel(title=web_str, message=f"These are the details entered\nWebsite: {web_str}\n"
                                                              f"Password: {pw_str}\nIs it okay to save?")
        if is_on:
            try:
                with open('my_passwords.json', 'r') as json_file:
                    data = json.load(json_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open('my_passwords.json', 'w') as json_file:
                    json.dump(new_data, json_file, indent=4)
            else:
                with open('my_passwords.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
            website_entry.delete(0, 'end')
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #


wd = Tk()
wd.config(padx=20, pady=20, bg='skyblue')
wd.title('Password Manager')
canvas = Canvas(width=200, height=200, bg='skyblue', highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', background='skyblue')
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg='skyblue')
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg='skyblue')
password_label.grid(column=0, row=3)

website_entry = Entry(width=26)
website_entry.focus()
website_entry.grid(column=1, row=1, padx=pdx, pady=pdy)
email_entry = Entry(width=44)
email_entry.insert(0, 'change_this_to_your_default_email@email.com')
email_entry.grid(column=1, row=2, columnspan=2, padx=pdx, pady=pdy)
password_entry = Entry(width=26)
password_entry.grid(column=1, row=3, pady=pdy, padx=10)

search_button = Button(text='Search', width=16, bg='white', command=tied_with_search)
search_button.grid(column=2, row=1, pady=pdy)
generate_pw_button = Button(text='Generate Password', bg='white', command=tied_to_generate)
generate_pw_button.grid(column=2, row=3, pady=pdy)
add_button = Button(text='Add', width=42, bg='white', command=tied_to_add)
add_button.grid(column=1, row=4, columnspan=2, padx=pdx, pady=pdy)

wd.mainloop()
