import tkinter as tk
from tkinter import ttk
# Create the main application window
root = tk.Tk()
root.geometry("3840x2160")
root.title("Totalmente no es un virus.exe")
root.attributes(fullscreen="True")
def on_button_click():
    cacota = tk.Tk()
    cacota.geometry("1920x1080")
    cacota.title("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.exe")
    cacota.attributes(fullscreen="True")
    caca = tk.Label(cacota, text="¡NO!", font=("Arial", 500, "bold"))
    caca.pack()
    root.after(1, on_button_click)
# Add a label widget
label = tk.Label(root, text="¡Juega al Dandys World!", font=("Arial", 50, "bold"))
label.pack()
# Add a button widget
btn = ttk.Button(
    root,
    text="Cerrar",       # Text on the button
    #state=ttk.NORMAL,       # NORMAL or DISABLED
    #bg="red",        # Background color
    #fg="white",            # Text color
    #font=("Arial", 100, "bold"),  # Font style
    #width=15, #height=2,    # Size in text units
    #relief=ttk.RAISED,      # RAISED, SUNKEN, FLAT, GROOVE, RIDGE
    cursor="hand2",         # Mouse cursor style
    command=on_button_click
)
btn.pack(pady=10)
# Run the application
root.mainloop()