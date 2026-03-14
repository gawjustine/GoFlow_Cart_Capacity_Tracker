from PIL import Image, ImageTk
import tkinter as tk

window_width = 400
window_height = 700

root = tk.Tk()
root.title("Train Opacity Demo")
root.geometry(f"{window_width}x{window_height}")


# Sizing ======================
# Load image
train_img = Image.open("train.png").convert("RGBA")
img_width, img_height = train_img.size

# Compute ratio to fit image inside window while keeping aspect ratio
ratio = min(window_width / img_width, window_height / img_height)
new_width = int(img_width * ratio)
new_height = int(img_height * ratio)

# Resize image
train_img = train_img.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Create canvas matching window size (or image size)
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Display image centered
tk_train_img = ImageTk.PhotoImage(train_img)
train_item = canvas.create_image(window_width//2, window_height//2, image=tk_train_img)

#Function to convert # heads to a %
def count_to_percent(count):
    max_capacity = 3 #modify later with research
    if max_capacity <= 0:
        return 0
    percent = (count / max_capacity) * 100
    return max(0, min(100, percent))

# Opacity ======================
# Function to update opacity

# NON-TRANSPARENT VER 1.
# def update_opacity(percent):
#     percent = max(0, min(100, percent))
#     alpha = int(255 * (percent / 100))
#     new_img = train_img.copy()
#     new_img.putalpha(alpha)
#     global tk_train_img
#     tk_train_img = ImageTk.PhotoImage(new_img)
#     canvas.itemconfig(train_item, image=tk_train_img)

# PNG VER 2.
def update_opacity(percent):
    global tk_train_img
    percent = max(0, min(100, percent))
    alpha_factor = percent / 100

    # Copy the image
    new_img = train_img.copy()

    # Extract existing alpha channel
    r, g, b, alpha = new_img.split()
    
    # Multiply existing alpha by factor
    alpha = alpha.point(lambda a: int(a * alpha_factor))
    
    # Put modified alpha back
    new_img.putalpha(alpha)

    tk_train_img = ImageTk.PhotoImage(new_img)
    canvas.itemconfig(train_item, image=tk_train_img)

# Testing:
# root.after(2000, lambda: update_opacity(50))  # sets 50% opacity
# update_opacity(42)  # sets opacity to 42%
# update_opacity(count_to_percent(8))

def update_from_count(count):
    percent = count_to_percent(count)
    update_opacity(percent)
    # root.after(5000, update_from_count)  # call again in 5s
    # don't need

# --- Start loop ---
# update_from_count()
# root.mainloop()