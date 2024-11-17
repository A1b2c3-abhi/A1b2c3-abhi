import tkinter as tk

def on_button_click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(screen.get())
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif button_text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")


# Change the window background color
root.configure(bg="lightblue")

screen = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, bg="white", fg="black")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10)

buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "=", "+"
]

button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack()

for i, text in enumerate(buttons):
    button = tk.Button(button_frame, text=text, font="Arial 18", relief=tk.RAISED, width=4, height=2, bg="lightgray", fg="black")
    button.grid(row=i//4, column=i%4, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)

root.mainloop()
