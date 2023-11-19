from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

window = tk.Tk()
window.title("BlueNotes")
window.geometry("600x280")
style = Style(theme='superhero')
style = ttk.Style()

note_entry = ttk.Notebook(window, style="TNotebook")

note_entry = tk.Text(window)
note_entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

window.mainloop()
