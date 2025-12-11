from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    #List comprehensive concept
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_number + password_symbol + password_letter
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    # validate the inputs before saving
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Website and Password can not be empty")
    else:
        is_sure = messagebox.askyesno(website, "Are You sure to save this data ", )
        if is_sure:
            with open("data.txt", "a") as data_file:
                data_file.write(f"\nwebsite: {website} | email: {email} | password: {password}")
                website_input.delete(0, END)
                # email_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200 , height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image =logo_image)
canvas.grid(row=0, column=1)

# label
website_label = Label(text="Website: ")
website_label.grid(row=1 , column=0)
email_label =Label(text="Username/Email: ")
email_label.grid(row=2 ,column=0)
password_label = Label(text="password: ")
password_label.grid(row=3, column=0)

#inputs
website_input = Entry(width=38)
website_input.grid(row=1 , column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=38)
email_input.grid(row=2 , column=1, columnspan=2 )
email_input.insert(0 , "example@gmail.com")
password_input = Entry(width=21, )
password_input.grid(row=3 , column=1,)

#buttons
gen_button = Button(text="Generate Password", command=generate_pass)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
