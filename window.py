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
# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# print(f"Screen resolution: {screen_width}x{screen_height}")
# Set window size to a fraction of the screen size (e.g., 70% of width and height)
window_width = int(screen_width * 0.7)
window_height = int(screen_height * 0.7)
# Format the geometry string as "widthxheight"
root.geometry(f"{window_width}x{window_height}")
# Optional: set minimum size to prevent layout issues on smaller screens
root.minsize(int(screen_width * 0.5), int(screen_height * 0.5))
# Calculate the positions of the screen 
# to center the screen on opening
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# 4. Start the application's main event loop
# This keeps the window open and responsive to user interactions
root.mainloop()
