from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    pw = pw_input.get()
    if email == 'abhi386@gmail.com' and pw == '1234':
        messagebox.showinfo('S','Login Successful')
    else:
        messagebox.showerror('E','Invalid credentials')




root = Tk()

root.title("Test GUI")

root.minsize(200,200)

root.geometry('370x640')

root.configure(background='#0096DC')
img= Image.open('testimg.png')
resized_img = img.resize((200,200))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image = img)
img_label.pack(pady=20)

text_label = Label(root, text="My gui", fg= 'white', bg= '#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

email_label = Label(root, text = 'Enter Email', fg = 'white', bg= '#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root, width = 50)
email_input.pack(ipady = 3, pady=(1,15))

pw_label = Label(root, text = 'Enter Password', fg = 'white', bg= '#0096DC')
pw_label.pack(pady=(20,5))
pw_label.config(font=('verdana',12))

pw_input = Entry(root, width = 50)
pw_input.pack(ipady = 3, pady=(1,15))

login_btn = Button(root, text= 'Login',bg='white',fg='#0096DC',width=20,height=2, command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',14))




root.mainloop()