import os
from tkinter import *
from PIL import Image
import ast
def formatImage(directory,size,filename,inches):
        for f in os.listdir(directory):
            file_name = f.split(".")[0]
            ext = f.split(".")[1]
            ext = "."+ext
            if file_name == filename:
                if inches:
                    size = inches_to_pixels(size)
                f_path = directory+"/"+f
                print(f_path)
                f_name = file_name+f"in_{size}"+ext
                try:
                    # Open the image
                    img = Image.open(f_path)
                    
                    # Resize the image
                    img = img.resize(size)
                    
                    # Save the image
                    path = os.path.join(directory,f_name)
                    img.save(path)
                    print(f"Saved resized image to {path}")
                    return True
                    
                except Exception as e:
                    print(f"Error processing file {f}: {e}")
                    return False
def inches_to_pixels(size):
    x = size[0]
    y = size[1]
    x_pix = x*96
    y_pix = y*96
    return (x_pix,y_pix)
root = Tk()

# root window title and dimension
root.title("Welcome to Image Sizer")
# Set geometry (widthxheight)
root.geometry('2000x2000')
bg = PhotoImage(file = "C:/Users/subha/AppData/Local/Programs/Python/Python311/IMAZER.png")
bg_label = Label(root,image = bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
lbl = Label(root, text = "Enter the directory",font=("Helvetica"),fg = "Black")
lbl.pack(padx= 10,pady=10) 
# adding Entry Field
directory = Entry(root, width=10)
directory.pack(padx= 10,pady=10) 
lbl_1 = Label(root, text = "Enter the required size in the format (x,y)",font=("Helvetica"),fg = "Black")
lbl_1.pack(padx= 10,pady=10) 
size = Entry(root, width=10)
size.pack(padx= 10,pady=10) 
lbl_3 = Label(root, text = "Enter the unit of size(if pixels say False, if inches say True)",font=("Helvetica"),fg = "Black")
lbl_3.pack(padx= 10,pady=10) 
s_b = Entry(root, width=10)
s_b.pack(padx= 10,pady=10) 
lbl_2 = Label(root, text = "Enter the filename w/o extension",font=("Helvetica"),fg = "Black")
lbl_2.pack(padx= 10,pady=10) 
fn = Entry(root, width=10)
fn.pack(padx= 10,pady=10) 

# function to display user text when 
# button is clicked
def clicked():
    dir = directory.get()
    sz = size.get()   
    sz = ast.literal_eval(sz)
    file = fn.get() 
    boolean = s_b.get()
    boolean = eval(boolean)
    b = formatImage(dir,sz,file,boolean)
    if b:
        op = Label(root, text = "Process Complete !!! ",font=("Helvetica"),fg = "Black")
        op.pack(padx= 10,pady=10) 
 
# button widget with red color text inside
btn = Button(root, text = "Click once you enter all the details",font=("Helvetica"),fg = "Blue", command=clicked)
# Set Button Grid
btn.pack(padx= 10,pady=10) 

root.mainloop()
