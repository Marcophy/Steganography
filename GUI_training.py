from tkinter import *

# ******** Root
root = Tk()  # Initialize the object

root.title("Steganography")

root.resizable(True, True)

root.iconbitmap("Stegano.ico")

# root.geometry("800x600")  # If we have a frame, we don't need to define the size here

root.config(bg="blue")  # Background color of the root

# ******* Create a frame
my_frame = Frame()

# -- Fit the frame to the root
my_frame.pack()

# -- Frame size
my_frame.config(width=600, height=800)

# -- How resize the frame together the root
# my_frame.pack(side="left", anchor="n")
# my_frame.pack(fill="both", expand=True)

# -- Frame background color
my_frame.config(bg="red")

# -- Mouse response over the frame
# my_frame.config(cursor="hand2")
# my_frame.config(cursor="pirate")

# -- Edges
my_frame.config(bd=10)
# my_frame.config(relief="groove")
my_frame.config(relief="sunken")

# ********* Labels
# my_label = Label(my_frame, text="Hi, this is a test.")
# my_label.place(x=100, y=200)

# If we don't need to assign a variable to the label, we can use the following syntax
Label(my_frame, text="Hi, this is a test.", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

# --- Add one image
# my_image = PhotoImage(file="new_picture.png")
# Label(my_frame, image=my_image).place(x=10, y=10)

# ********* Entry
text_box = Entry(my_frame).grid(row=0, column=2)
# text_box.place(x=50, y=50)
# text_box.grid(row=0, column=1)  # This option is for using
Label(my_frame, text="Name:").grid(row=0, column=0, sticky="w", padx=10, pady=10)

# ---- GUI loop
root.mainloop()  # Start the main loop
