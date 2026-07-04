import os
from tkinter import *
from PIL import Image
import ast

def inches_to_pixels(size):
    x, y = size
    return (int(x * 96), int(y * 96))

def formatImage(directory, size, filename, inches):
    if inches:
        size = inches_to_pixels(size)

    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}

    for f in os.listdir(directory):
        full_path = os.path.join(directory, f)

        # skip subfolders
        if not os.path.isfile(full_path):
            continue

        file_name, ext = os.path.splitext(f)

        # skip non-image files
        if ext.lower() not in valid_extensions:
            continue

        if file_name == filename:
            new_name = f"{file_name}_in_{size[0]}x{size[1]}{ext}"
            new_path = os.path.join(directory, new_name)

            try:
                img = Image.open(full_path)
                img = img.resize(size)
                img.save(new_path)
                return True, f"✅ Saved resized image to {new_path}"
            except Exception as e:
                return False, f"❌ Error processing file: {e}"

    return False, "❌ File not found in that directory."


root = Tk()
root.title("Image Sizer")
root.geometry("560x500")
root.configure(bg="#E3F6FC")

# Card frame
card = Frame(root, bg="white", bd=2, relief=GROOVE)
card.place(relx=0.5, rely=0.5, anchor=CENTER, width=520, height=460)

title = Label(
    card,
    text="Image Sizer Tool",
    font=("Helvetica", 18, "bold"),
    bg="white",
    fg="#173D7A"
)
title.pack(pady=(14, 8))

Label(card, text="Directory:", font=("Helvetica", 12), bg="white").pack(pady=(4, 1))
directory = Entry(card, width=40, font=("Consolas", 11), bd=2, relief=SOLID)
directory.pack()

Label(card, text="Required size (x, y):", font=("Helvetica", 12), bg="white").pack(pady=(6, 1))
size = Entry(card, width=24, font=("Consolas", 11), bd=2, relief=SOLID)
size.pack()

Label(card, text="Unit (pixels=False, inches=True):", font=("Helvetica", 12), bg="white").pack(pady=(6, 1))
s_b = Entry(card, width=14, font=("Consolas", 11), bd=2, relief=SOLID)
s_b.pack()

Label(card, text="Filename w/o extension:", font=("Helvetica", 12), bg="white").pack(pady=(6, 1))
fn = Entry(card, width=30, font=("Consolas", 11), bd=2, relief=SOLID)
fn.pack()

# Status label
result = Label(
    card,
    text="",
    font=("Helvetica", 12, "bold"),
    bg="white",
    fg="black",
    wraplength=460,
    justify=CENTER
)
result.pack(pady=(18, 8))

def clicked():
    dir_path = directory.get().strip()

    if not os.path.isdir(dir_path):
        result.config(text="Directory must be a valid folder path", fg="red")
        return

    sz = size.get().strip()
    try:
        sz = ast.literal_eval(sz)
        if not (isinstance(sz, tuple) and len(sz) == 2 and all(isinstance(x, int) for x in sz)):
            raise ValueError
    except:
        result.config(text="Size must be a tuple like (120, 120)", fg="red")
        return
    boolean = s_b.get().strip().lower()
    if boolean == "true":
        boolean = True
    elif boolean == "false":
        boolean = False
    else:
        result.config(text="Unit must be True or False", fg="red")
        return
    file = fn.get().strip()
    if not file:
        result.config(text="Please enter a filename without extension", fg="red")
        return
    success, message = formatImage(dir_path, sz, file, boolean)
    if success:
        result.config(text=message, fg="green")
    else:
        result.config(text=message, fg="red")

btn = Button(
    card,
    text="Resize Image",
    bg="#1E96FC",
    fg="white",
    font=("Helvetica", 12, "bold"),
    relief=RAISED,
    bd=2,
    command=clicked,
    activebackground="#173D7A"
)
btn.pack(pady=(6, 10))

root.mainloop()