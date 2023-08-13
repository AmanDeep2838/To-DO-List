import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")

        self.tasks = []
        self.history = []

        self.task_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=20)

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), selectbackground="#3498db")
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        self.update_button = ttk.Button(root, text="Update", command=self.update_task)
        self.update_button.pack()

        self.delete_button = ttk.Button(root, text="Delete", command=self.delete_task)
        self.delete_button.pack()

        self.history_button = ttk.Button(root, text="View History", command=self.view_history)
        self.history_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.history.append(f"Added task: {task}")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            updated_task = self.task_entry.get()
            if updated_task:
                selected_task = self.task_listbox.get(selected_index)
                self.tasks[selected_index[0]] = updated_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, updated_task)
                self.task_entry.delete(0, tk.END)
                self.history.append(f"Updated task '{selected_task}' to '{updated_task}'")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index[0])
            self.history.append(f"Deleted task: {selected_task}")

    def view_history(self):
        history_text = "\n".join(self.history)
        if history_text:
            messagebox.showinfo("History", history_text)
        else:
            messagebox.showinfo("History", "No history available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
