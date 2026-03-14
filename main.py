from train_gui import root, update_from_count
from camcounter import get_count, cleanup

UPDATE_INTERVAL = 100
#change time as req for freq of taking frames

def loop():
    count = get_count()
    update_from_count(count)

    root.after(UPDATE_INTERVAL, loop)

def close_app():
    cleanup()
    root.destroy()

root.bind("q", lambda e: close_app())
root.protocol("WM_DELETE_WINDOW", close_app)

loop()
root.mainloop()