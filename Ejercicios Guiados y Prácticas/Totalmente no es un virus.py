import tkinter as tk
# Create the main application window
root = tk.Tk()
root.geometry("3840x2160")
root.title("Totalmente no es un virus.exe")
def on_button_click():
    cacota = tk.Tk()
    cacota.geometry("3840x2160")
    cacota.title("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.exe")
    caca = tk.Label(cacota, text="¡NO!", font=("Arial", 100, "bold"))
    caca.pack()
    root.after(100, on_button_click)
# Add a label widget
label = tk.Label(root, text="¡Juega al Dandys World!", font=("Arial", 50, "bold"))
label.pack()
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
    cursor="hand2",         # Mouse cursor style
    command=on_button_click
)
btn.pack(pady=10)
# Run the application
root.mainloop()