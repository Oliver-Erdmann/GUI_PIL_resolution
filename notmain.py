from tkinter import filedialog as fd
from PIL.ImageFilter import (EDGE_ENHANCE_MORE, BLUR)

def select_files():
    global filename
    filetypes = (('image files', '*.jpg .png'), ('All files', '.*'))
    filename = fd.askopenfilename(title='Open files', initialdir='/', filetypes=filetypes)
    print(filename)
    return filename

def blur_img(image_res):
    im_blur = image_res.filter(BLUR)
    im_blur.show()

def sharpen_img(image_res):
    im_sharp = image_res.filter(EDGE_ENHANCE_MORE)
    im_sharp.show()