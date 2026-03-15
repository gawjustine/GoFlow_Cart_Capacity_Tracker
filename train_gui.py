from PIL import Image, ImageTk
import tkinter as tk

window_width = 1280
window_height = 675

root = tk.Tk()
root.title("Train Opacity Demo")
root.geometry(f"{window_width}x{window_height}")

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

#Function to convert # heads to a %
def count_to_percent(count):
    max_capacity = 3 #modify later with research
    if max_capacity <= 0:
        return 0
    percent = (count / max_capacity) * 100
    return max(0, min(100, percent))

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

def update_from_count(count):
    percent = count_to_percent(count)
    update_train_fill(percent)
