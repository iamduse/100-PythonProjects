from tkinter import *

from prompt_toolkit.input import Input

window = Tk()
window.title("LOGIN FORM")
window.minsize(width=500, height=400)

user_label = Label(text="username", font=("Arial",  24 ))
user_label.pack()

def button_manager():
    info = user_input.get()
    user_label.config(text=info)


#Entary

user_input = Entry(width=10)
user_input.pack()


login_button = Button(text="Login in", command= button_manager)
login_button.pack()














window.mainloop()
