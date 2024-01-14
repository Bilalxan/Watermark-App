from tkinter import *
from PIL import Image

# 1. Main Window:
# A clearly labeled window with a title like "Image Watermarking Tool" or "Watermark Wizard".
# A prominent button labeled "Upload Image" or "Choose Image" for selecting the image to be watermarked.
# A preview area displaying the chosen image, allowing users to visualize the watermark placement.
window = Tk()
window.title("Image Watermarking Tool")
window.minsize(width=800, height=800)
window.config(bg="skyblue")

# Watermark Editor
def image1_watermark():
    def add_watermark():
        canvas1.create_text(100, 160, text=entry.get(), fill=color.get(), font=("Lemon", 20, "normal"))
    entry = Entry(bg="skyblue")
    entry.insert(0, "Watermark goes here")
    color = Entry(bg="skyblue")
    color.insert(0, "Choose your color. E.g. blue")
    button = Button(text="Add this watermark", command=add_watermark, bg="skyblue", highlightbackground="skyblue")
    entry.grid(row=5, column=1)
    color.grid(row=6, column=1, pady=8)
    button.grid(row=7, column=1)
def image2_watermark():
    def add_watermark():
        canvas2.create_text(100, 140, text=entry.get(), fill=color.get(), font=("Lemon", 20, "normal"))
    entry = Entry(bg="skyblue")
    entry.insert(0, "Watermark goes here")
    color = Entry(bg="skyblue")
    color.insert(0, "Choose your color. E.g. blue")
    button = Button(text="Add this watermark", command=add_watermark, bg="skyblue", highlightbackground="skyblue")
    entry.grid(row=5, column=2)
    color.grid(row=6, column=2, pady=8)
    button.grid(row=7, column=2)

def image3_watermark():
    def add_watermark():
        canvas3.create_text(100, 160, text=entry.get(), fill=color.get(), font=("Lemon", 20, "normal"))
    entry = Entry(bg="skyblue")
    entry.insert(0, "Watermark goes here")
    color = Entry(bg="skyblue")
    color.insert(0, "Choose your color. E.g. blue")
    button = Button(text="Add this watermark", command=add_watermark, bg="skyblue", highlightbackground="skyblue")
    entry.grid(row=5, column=3)
    color.grid(row=6, column=3, pady=8)
    button.grid(row=7, column=3)

label = Label(text="Create your unique watermark image", font=(("Times", 40, "bold italic")), bg="skyblue", highlightbackground="skyblue")
label.grid(row=1, column=2, pady=50)

# Images
image_1 = PhotoImage(file="6-2-nature-high-quality-png-thumb.png")
image_2 = PhotoImage(file="58018-car-2002-2000-2001-z8-bmw-thumb.png")
image_3 = PhotoImage(file="5-audi-png-car-image-thumb.png")

# Canvas Images
canvas1 = Canvas(width=200, height=200, bg="skyblue", highlightbackground="skyblue")
canvas1.create_image(100, 100, image=image_1)
canvas1.grid(row=3, column=1)
canvas2 = Canvas(width=200, height=200, bg="skyblue", highlightbackground="skyblue")
canvas2.create_image(100, 100, image=image_2)
canvas2.grid(row=3, column=2)
canvas3 = Canvas(width=200, height=200, bg="skyblue", highlightbackground="skyblue")
canvas3.create_image(100, 100, image=image_3)
canvas3.grid(row=3, column=3)

# Buttons
button1 = Button(text="Edit Image", command=image1_watermark, bg="skyblue", highlightbackground="skyblue")
button1.grid(row=4, column=1, padx=20)
button2 = Button(text="Edit Image", command=image2_watermark, bg="skyblue", highlightbackground="skyblue")
button2.grid(row=4, column=2, padx=20)
button3 = Button(text="Edit Image", command=image3_watermark, bg="skyblue", highlightbackground="skyblue")
button3.grid(row=4, column=3, padx=20)




window.mainloop()
