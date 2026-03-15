from PIL import Image, ImageTk
import tkinter as tk

window_width = 1280
window_height = 675

root = tk.Tk()
root.title("Train Opacity Demo")
root.geometry(f"{window_width}x{window_height}")


# Sizing ======================

# Load image
# train_img = Image.open("train.png").convert("RGBA")
# img_width, img_height = train_img.size

# # Compute ratio to fit image inside window while keeping aspect ratio
# ratio = min(window_width / img_width, window_height / img_height)
# new_width = int(img_width * ratio)
# new_height = int(img_height * ratio)

# # Resize image
# train_img = train_img.resize((new_width, new_height), Image.Resampling.LANCZOS)

# # Display image centered
# tk_train_img = ImageTk.PhotoImage(train_img)
# train_item = canvas.create_image(window_width//2, window_height//2, image=tk_train_img)

# Create canvas matching window size (or image size)
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Load background
bg_img = Image.open("bg.png").resize((1280,675), Image.Resampling.LANCZOS)
tk_bg = ImageTk.PhotoImage(bg_img)
bg_item = canvas.create_image(0,0, image=tk_bg, anchor="nw")

# Load train
train_img = Image.open("gotrain.png").convert("RGBA")
tk_train_img = ImageTk.PhotoImage(train_img)

alpha = train_img.split()[3]  # alpha channel
bbox = alpha.getbbox()  # returns (left, upper, right, lower)
train_cropped = train_img.crop(bbox)
train_width, train_height = train_cropped.size

train_item = canvas.create_image(640, 337, image=None)
# width, height = train_img.size

#Function to convert # heads to a %
def count_to_percent(count):
    max_capacity = 3 #modify later with research
    if max_capacity <= 0:
        return 0
    percent = (count / max_capacity) * 100
    return max(0, min(100, percent))

# # Opacity ======================
# # Function to update opacity
# def update_opacity(percent):
#     global tk_train_img
#     percent = max(0, min(100, percent))
#     alpha_factor = percent / 100

#     # Copy the image
#     new_img = train_img.copy()

#     # Extract existing alpha channel
#     r, g, b, alpha = new_img.split()
    
#     # Multiply existing alpha by factor
#     alpha = alpha.point(lambda a: int(a * alpha_factor))
    
#     # Put modified alpha back
#     new_img.putalpha(alpha)

#     tk_train_img = ImageTk.PhotoImage(new_img)
#     canvas.itemconfig(train_item, image=tk_train_img)

#===========================================
# Fill ======================
# Function to fill the train
# def update_train_fill(percent):
#     """
#     Show the train filling up with itself from bottom to top.
#     Transparent background remains transparent.
#     """
#     percent = max(0, min(100, percent))

#     # Height to show
#     visible_height = int(height * percent / 100)
    
#     # Crop only the visible bottom portion of the train
#     visible_train = train_img.crop((0, height - visible_height, width, height))
    
#     # Create a new fully transparent image of the same size
#     new_img = Image.new("RGBA", (width, height), (0,0,0,0))
    
#     # Paste the visible portion at the bottom
#     new_img.paste(visible_train, (0, height - visible_height), visible_train)
    
#     # Update Tkinter image
#     global tk_train_img
#     tk_train_img = ImageTk.PhotoImage(new_img)
#     canvas.itemconfig(train_item, image=tk_train_img)

def update_train_fill(percent):
    visible_height = int(train_height * percent / 100)
    visible_train = train_cropped.crop((0, train_height - visible_height, train_width, train_height))
    
    new_img = Image.new("RGBA", train_cropped.size, (0,0,0,0))
    new_img.paste(visible_train, (0, train_height - visible_height), visible_train)

    global tk_train_img
    tk_train_img = ImageTk.PhotoImage(new_img)

    # Center the train on the background
    x = bg_img.width // 2 - 15
    # y = bg_img.height // 2 + (train_height // 2 - visible_height // 2)
    y = bg_img.height // 2 + 44
    canvas.itemconfig(train_item, image=tk_train_img)
    canvas.coords(train_item, x, y)

# Demo: simulate filling
# current_percent = 0
# def simulate_fill():
#     global current_percent
#     current_percent += 5
#     if current_percent > 100:
#         current_percent = 0
#     update_train_fill(current_percent)
#     root.after(200, simulate_fill)

def update_from_count(count):
    percent = count_to_percent(count)
    # update_opacity(percent)
    update_train_fill(percent)
    # root.after(5000, update_from_count)  # call again in 5s
    # don't need

# --- Start loop ---
# update_from_count(2)
# simulate_fill()
# root.mainloop()