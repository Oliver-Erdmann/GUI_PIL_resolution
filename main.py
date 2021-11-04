from tkinter import *
import random
from PIL import Image
from tkinter import ttk
from tkinter import filedialog as fd

root=Tk()
root.geometry("300x300")

def select_files():
    global my_image
    global filename
    filetypes = (('image files', '*.jpg .png'),('All files', '.*'))
    filename = fd.askopenfilename(title='Open files', initialdir='/', filetypes=filetypes)
    my_image = Image.open(filename)
    #loop_img(my_image)

def loop_img():
    my_image = Image.open(filename)
    #size = 1920, 1080
    #im = Image.open(select_files)
    im_resized = my_image.resize(size, Image.ANTIALIAS)
    #im_resized.save(select_files, "PNG")
    im_resized.show()

res = ttk.Button(root,text='Change resolution',command=loop_img)
res.grid(row=7, column=0)

open_button = ttk.Button(root,text='Open Files',command=select_files)
open_button.grid(row=0, column=0)

def radio_1():
    global size
    size = 256, 144
def radio_2():
    global size
    size = 320, 240
def radio_3():
    global size
    size = 480, 360
def radio_4():
    global size
    size = 852, 480
def radio_5():
    global size
    size = 1280, 720
def radio_6():
    global size
    size = 1920, 1080

R1 = Radiobutton(root, text="144p", value=0, command=radio_1)
R1.grid(row=1, column=0)
R2 = Radiobutton(root, text="240p", value=1, command=radio_2)
R2.grid(row=2, column=0)
R3 = Radiobutton(root, text="360p", value=2, command=radio_3)
R3.grid(row=3, column=0)
R4 = Radiobutton(root, text="480p", value=3, command=radio_4)
R4.grid(row=4, column=0)
R5 = Radiobutton(root, text="720p", value=4, command=radio_5)
R5.grid(row=5, column=0)
R6 = Radiobutton(root, text="1080p", value=5, command=radio_6)
R6.grid(row=6, column=0)


root.mainloop()