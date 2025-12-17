import tkinter as tk
from tkinter import ttk
# Create the main application window
root = tk.Tk()
root.geometry("1920x1080")
root.title("Totalmente no es un virus.exe")
cacota = tk.Tk()
cacota.geometry("1280x720")
cacota.title("Totalmente no es un virus.exe")
# Add a label widget
label = tk.Label(root, text="¡Juega al Dandys World!", font=("Arial", 50, "bold"))
label.pack()
caca = tk.Label(cacota, text="¡NO!", font=("Arial", 100, "bold"))
caca.pack()
# Add a button widget
btn = tk.Button(
    root,
    text="Cerrar",       # Text on the button
    state=tk.NORMAL,       # NORMAL or DISABLED
    bg="red",        # Background color
    fg="white",            # Text color
    font=("Arial", 100, "bold"),  # Font style
    width=15, height=2,    # Size in text units
    relief=tk.RAISED,      # RAISED, SUNKEN, FLAT, GROOVE, RIDGE
    cursor="hand2"         # Mouse cursor style
)
btn.pack(pady=10)
# Run the application
root.mainloop()