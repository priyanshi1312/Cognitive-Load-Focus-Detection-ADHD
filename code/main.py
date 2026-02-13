
import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Cognitive Load & Focus Detection System")
root.geometry("500x300")

# Title Label
title_label = tk.Label(root, text="Cognitive Load & Focus Detection", font=("Arial", 16))
title_label.pack(pady=20)

# Description
desc_label = tk.Label(root, text="Task-Based Focus Assessment for ADHD Support", font=("Arial", 12))
desc_label.pack(pady=10)

# Start Button Function
def start_test():
    messagebox.showinfo("Start", "Assessment will begin soon!")

# Start Button
start_button = tk.Button(root, text="Start Assessment", font=("Arial", 12), command=start_test)
start_button.pack(pady=20)

# Run App
root.mainloop()
