import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task from the list
def remove_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create a frame to hold the input and buttons
frame = tk.Frame(root)
frame.pack(pady=10)

# Create an entry widget to input tasks
entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=0, padx=5)

# Create a button to add tasks
add_button = tk.Button(frame, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=5)

# Create a button to remove tasks
remove_button = tk.Button(frame, text="Remove Task", width=10, command=remove_task)
remove_button.grid(row=0, column=2, padx=5)

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Start the main event loop
root.mainloop()
