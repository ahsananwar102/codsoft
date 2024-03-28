import tkinter as tk

# FUNCTION DEFINITIONS

def add_task(): # Function to add a task to the to-do list.
    task = textbox.get("1.0", tk.END).strip()
    if task:
        tasksListbox.insert(tk.END, task)
        tasksListbox.itemconfig(tk.END, fg="black")  # Set default color to black
        textbox.delete("1.0", tk.END)

def delete_task(): # Function to delete a selected task from the to-do list.
    selectedTask = tasksListbox.curselection()
    if selectedTask:
        tasksListbox.delete(selectedTask)
        update_button_state()

def update_button_state(event=None): # Function to update the state of the buttons based on whether a task is selected.
    if tasksListbox.curselection():
        selectedIndex = tasksListbox.curselection()[0]
        color = tasksListbox.itemcget(selectedIndex, "fg")
        delete_button.config(state=tk.NORMAL)
        if color == "black":
            mark_button.config(state=tk.NORMAL)
            unmark_button.config(state=tk.DISABLED)
        elif color == "#BAC5C9":
            mark_button.config(state=tk.DISABLED)
            unmark_button.config(state=tk.NORMAL)
    else:
        delete_button.config(state=tk.DISABLED)
        mark_button.config(state=tk.DISABLED)
        unmark_button.config(state=tk.DISABLED)

def mark_off(): # Function to mark off the tasks as completed
    selectedTask = tasksListbox.curselection()
    if selectedTask:
        tasksListbox.itemconfig(selectedTask, fg="#BAC5C9")
        update_button_state()

        tasksListbox.selection_clear(0, tk.END)

def unmark(): # Function to unmark the tasks
    selectedTask = tasksListbox.curselection()
    if selectedTask:
        tasksListbox.itemconfig(selectedTask, fg="black")
        update_button_state()

        tasksListbox.selection_clear(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

label = tk.Label(root, text="To-Do List", font=("Cambria", "22", "bold"))
label.pack(padx=10, pady=10)

textboxLabel = tk.Label(root, text="Enter a task:", font=("Arial", "12", "bold"), anchor="w")
textboxLabel.pack(fill=tk.X, padx=10)

# Adding a textbox for the user to enter the task
textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=10, pady=10)

# Button for adding the task to the list
add_button = tk.Button(root, text="Add Task", command=add_task, anchor="w", font=("Arial", "12"))
add_button.pack(pady=10)

# Rendering a frame for the list box
taskDisplayFrame = tk.LabelFrame(root, text="Tasks", font=("Arial", "12", "bold"))
taskDisplayFrame.pack(padx=10, fill="x")

# Adding a listbox
tasksListbox = tk.Listbox(taskDisplayFrame, height=6, font=("Arial", "14"), selectbackground="#5D767F", activestyle="none")
tasksListbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)
tasksListbox.bind('<<ListboxSelect>>', update_button_state) #This function only enables the delete button once a task is selected from the list

# Adding a scrollbar for the list box
scrollbar = tk.Scrollbar(taskDisplayFrame, orient="vertical", command=tasksListbox.yview)
scrollbar.pack(side="right", fill="y")
tasksListbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10, expand=True)

# Delete button
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Arial", "12"),  state="disabled")
delete_button.grid(padx=10, row=0, column=0)

# Mark-off button
mark_button = tk.Button(button_frame, text="Mark off as completed", command=mark_off, font=("Arial", "12"), state="disabled")
mark_button.grid(padx=10, row=0, column=1)

# Unmark button
unmark_button = tk.Button(button_frame, text="Unmark task", command=unmark, font=("Arial", "12"), state="disabled")
unmark_button.grid(padx=10, row=0, column=2)

root.geometry("800x500") # Setting the dimensions of the window
root.mainloop()