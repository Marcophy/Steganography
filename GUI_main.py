# Create Tabbed widget in Python GUI Application
import tkinter as tk
from tkinter import ttk

win_root = tk.Tk()
win_root.title("Steganography")
win_root.iconbitmap("Stegano.ico")

# Create Tab Control
tabControl = ttk.Notebook(win_root)
# Tab1
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Hide message')
# Tab2
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Discover message')
tabControl.pack(expand=1, fill="both")
# Tab Name Labels
ttk.Label(tab1, text="This is Tab 1").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab2, text="This is Tab 2").grid(column=0, row=0, padx=10, pady=10)
# Calling Main()
win_root.mainloop()
