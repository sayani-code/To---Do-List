import customtkinter as ctk
from tkinter import messagebox

# -----------------------------
# App Settings
# -----------------------------
ctk.set_appearance_mode("dark")      # "light" or "dark"
ctk.set_default_color_theme("blue")

tasks = []

# -----------------------------
# Functions
# -----------------------------
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    tasks.append({
        "name": task,
        "completed": False
    })

    task_entry.delete(0, "end")
    update_tasks()


def update_tasks():
    task_list.delete("0.0", "end")

    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        task_list.insert(
            "end",
            f"{index}. {task['name']}   {status}\n"
        )


def complete_task():
    selected = number_entry.get()

    if not selected.isdigit():
        messagebox.showerror("Error", "Enter a valid task number.")
        return

    index = int(selected) - 1

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        update_tasks()
        number_entry.delete(0, "end")
    else:
        messagebox.showerror("Error", "Task not found.")


def delete_task():
    selected = number_entry.get()

    if not selected.isdigit():
        messagebox.showerror("Error", "Enter a valid task number.")
        return

    index = int(selected) - 1

    if 0 <= index < len(tasks):
        tasks.pop(index)
        update_tasks()
        number_entry.delete(0, "end")
    else:
        messagebox.showerror("Error", "Task not found.")


# -----------------------------
# Main Window
# -----------------------------
app = ctk.CTk()
app.title("To-Do List")
app.geometry("500x600")
app.resizable(False, False)

title = ctk.CTkLabel(
    app,
    text="📝 To-Do List",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

task_entry = ctk.CTkEntry(
    app,
    width=350,
    placeholder_text="Enter a new task..."
)
task_entry.pack(pady=10)

add_btn = ctk.CTkButton(
    app,
    text="Add Task",
    command=add_task,
    width=200
)
add_btn.pack(pady=10)

task_list = ctk.CTkTextbox(
    app,
    width=420,
    height=250,
    font=("Arial", 15)
)
task_list.pack(pady=20)

number_entry = ctk.CTkEntry(
    app,
    width=200,
    placeholder_text="Task Number"
)
number_entry.pack(pady=10)

complete_btn = ctk.CTkButton(
    app,
    text="Complete Task",
    command=complete_task,
    width=200
)
complete_btn.pack(pady=10)

delete_btn = ctk.CTkButton(
    app,
    text="Delete Task",
    command=delete_task,
    fg_color="red",
    hover_color="#8B0000",
    width=200
)
delete_btn.pack(pady=10)

app.mainloop()