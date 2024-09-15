import tkinter as tk

# Function to update the expression in the input field
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = str(eval(screen.get()))
            screen_var.set(expression)
        except Exception as e:
            screen_var.set("Error")
            screen.update()
    elif text == "C":
        screen_var.set("")
        screen.update()
    else:
        screen_var.set(screen_var.get() + text)
        screen.update()

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Create the input field
screen_var = tk.StringVar()
screen_var.set("")
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10)

# Button layout and their functionalities
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create the buttons
for button_row in buttons:
    frame = tk.Frame(root)
    for button in button_row:
        btn = tk.Button(frame, text=button, font="lucida 15 bold", padx=20, pady=20)
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.bind("<Button-1>", click)
    frame.pack(expand=True, fill=tk.BOTH)

# Start the Tkinter event loop
root.mainloop()
