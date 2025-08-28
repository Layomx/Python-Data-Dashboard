import tkinter as tk

# Create the main application window
root  = tk.Tk()
root.title("Data Dashboard with Python and Tkinter")
root.geometry("300x150") # Set window size

# This function is called when the button is clicked
def on_button_click():
    print("Button clicked!")
    label.config(text="Button was clicked!")
    
# Create the widget elements for the application
label = tk.Label(root, text = "Welcome to the Dashboard. Click the button below.")
button = tk.Button(root, text = "Click Me", command = on_button_click)

# Place the widgets in the window
label.pack(pady=10)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()