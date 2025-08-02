import os
from tkinter import *
from PIL import Image
import ast

def formatImage(directory, size, filename, inches):
    for f in os.listdir(directory):
        file_name = f.split(".")[0]
        ext = f.split(".")[1]
        ext = "." + ext
        if file_name == filename:
            if inches:
                size = inches_to_pixels(size)
            f_path = os.path.join(directory, f)
            f_name = file_name + f"_in_{size}" + ext
            try:
                img = Image.open(f_path)
                img = img.resize(size)
                path = os.path.join(directory, f_name)
                img.save(path)
                print(f"Saved resized image to {path}")
                return True
            except Exception as e:
                print(f"Error processing file {f}: {e}")
                return False

def inches_to_pixels(size):
    x, y = size
    return (int(x * 96), int(y * 96))

root = Tk()
root.title("Image Sizer")
root.geometry('540x400')
root.configure(bg='#E3F6FC')  # light blue background

# Card frame for form elements
card = Frame(root, bg='white', bd=2, relief=GROOVE)
card.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=350)

title = Label(card, text="Image Sizer Tool", font=("Helvetica", 18, "bold"), bg='white', fg='#173D7A')
title.pack(pady=(20,10))

Label(card, text="Directory:", font=("Helvetica", 12), bg='white').pack(pady=(8,2))
directory = Entry(card, width=35, font=("Consolas", 11), bd=2, relief=SOLID)
directory.pack()

Label(card, text="Required size (x, y):", font=("Helvetica", 12), bg='white').pack(pady=(8,2))
size = Entry(card, width=20, font=("Consolas", 11), bd=2, relief=SOLID)
size.pack()

Label(card, text="Unit (pixels=False, inches=True):", font=("Helvetica", 12), bg='white').pack(pady=(8,2))
s_b = Entry(card, width=12, font=("Consolas", 11), bd=2, relief=SOLID)
s_b.pack()

Label(card, text="Filename w/o extension:", font=("Helvetica", 12), bg='white').pack(pady=(8,2))
fn = Entry(card, width=25, font=("Consolas", 11), bd=2, relief=SOLID)
fn.pack()

def clicked():
    dir = directory.get().strip()
    sz = size.get().strip()
    try:
        sz = ast.literal_eval(sz)
        if not (isinstance(sz, tuple) and len(sz) == 2 and all(isinstance(x, int) for x in sz)):
            raise ValueError
    except:
        result['text'] = "Size must be a tuple like (120, 120)"
        result.config(fg="red")
        return

    file = fn.get().strip()
    boolean = s_b.get().strip()
    try:
        boolean = eval(boolean)
    except:
        result['text'] = "Unit must be True or False"
        result.config(fg="red")
        return

    b = formatImage(dir, sz, file, boolean)
    if b:
        result['text'] = "✅ Process Complete!"
        result.config(fg="green")
    else:
        result['text'] = "❌ Error processing image."
        result.config(fg="red")

btn = Button(card, text="Resize Image", bg='#1E96FC', fg="white", font=("Helvetica", 12, "bold"),
             relief=RAISED, bd=2, command=clicked, activebackground='#173D7A')
btn.pack(pady=14)

result = Label(card, text="", font=("Helvetica", 12), bg='white')
result.pack(pady=(5,10))

root.mainloop()