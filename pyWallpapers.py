from tkinter import *
from PIL import ImageTk, Image
import os

def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter +=1

counter = 1
root = Tk()
root.title('Mesa Viewer')
root.state('zoomed')

root.geometry('1920x1080')
root.configure(background='black')

files = os.listdir('mesa')

img_array= []
for file in files:
    img = Image.open(os.path.join('mesa', file))
    resized_img = img.resize((1280,720))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image = img_array[0])
img_label.pack()

next_btn = Button(root, text = 'Next', bg = 'white', fg = 'black', width= 25, height= 2, command = rotate_img)
next_btn.place(x=680,y=740)


root.mainloop()