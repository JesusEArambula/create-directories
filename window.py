import tkinter as tk

# 1. Create the main application window (root widget)
root = tk.Tk()

# 2. Set the window title (optional)
root.title("My First Application")

# Background color
root.configure(bg="lightblue")
# Window Icon
# PNG and GIF are reliably supported across platforms
icon_image = tk.PhotoImage(file='res/folder-icon.png')
root.iconphoto(True, icon_image)


# 3. Set the initial size of the window (optional, format as 'WidthxHeight')
root.geometry('350x200')

# 4. Start the application's main event loop
# This keeps the window open and responsive to user interactions
root.mainloop()
