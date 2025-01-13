import json
from tkinter import *
from tkinter import  messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters = [random.choice(letters) for _ in range(nr_letters)]
    symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters+symbol+number
    random.shuffle(password_list)

    password = "".join(password_list)
    Password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_data():
    if len(Website_input.get())<1 or len(Password.get())<1 :
        messagebox.showerror(title="Error", message="Fill all the details")
    else:
        is_ok = messagebox.askokcancel(title="check details", message=f"These are the details you've entered \n website: {Website_input.get()}"
                                                              f"\nEmail: {Email.get()}"
                                                              f"\nPassword: {Password.get()}\n Do you want to add them?")
        new_data = {
            Website_input.get().title():{
                "Email": Email.get(),
                "Password": Password.get()
            }
        }
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)


                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                Website_input.delete(0, END)
                Password.delete(0, END)

            messagebox.showinfo(message="Data Successfully added")
        else:
            Website_input.delete(0, END)
            Password.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_website():
    Website = Website_input.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except:
        messagebox.showerror(title="Error!", message="Website not found")
    else:
        if Website.title() or Website in data:
            messagebox.showinfo(title="Website_info", message=f"Email: {data[Website]["Email"]}\nPassword: {data[Website]["Password"]}")
        else:
            messagebox.showerror(title="Error!",message="Data doesn't exist.")
    finally:
        Website_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password manage")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= lock_img)
canvas.grid(column=1, row=0)

Website_input = Entry(width=35)
Website_input.grid(column=1, row=1, columnspan=2)
Website_input.focus()

website = Label(text="website:", font=("Arial", 10, "bold"))
website.grid(column=0, row=1)

Email = Entry(width=35)
Email.grid(column=1, row=2, columnspan=2)
Email.insert(0, "Sudeep7303@gmail.com")

Email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
Email_label.grid(column=0, row=2)

Password = Entry(width=35)
Password.grid(column=1, row=3, columnspan = 2)

Password_text = Label(text="Password:", font=("Arial", 10, "bold"))
Password_text.grid(column=0, row=3)

Generate_password = Button(text="Generate Password",command=generate_password)
Generate_password.grid(column=2,row=3)

search_button = Button(text="search", width=25, command=search_website)
search_button.grid(column=3, row=1)

Add_button = Button(text="Add", width=36, command=write_data)
Add_button.grid(column=1, row=4, columnspan = 2)
print(Website_input.get())



window.mainloop()