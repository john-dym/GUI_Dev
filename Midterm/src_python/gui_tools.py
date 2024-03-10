# GUI Tools
# Author: John Morales
# Access to commonly used functions

from PIL import Image, ImageTk
from re import fullmatch
from tkinter import messagebox
def calculate_window_pos(display_width, display_height, window_width, window_height):
    #Calculates the center position of the app window on startup
    screen_center_x = display_width // 2
    screen_center_y = display_height // 2
    window_x_offset = screen_center_x - (window_width // 2)
    window_y_offset = screen_center_y - (window_height // 2)
    return window_x_offset, window_y_offset

def parse_window_size(window_size):
    window_size = window_size.split("x")
    return int(window_size[0]), int(window_size[1])

def windows_geometry(rootTK, window_size):
    #https://stackoverflow.com/questions/25636804/centering-window-python-tkinter

    display_w = rootTK.winfo_screenwidth()
    display_h = rootTK.winfo_screenheight()
    win_size_int = parse_window_size(window_size)
    window_offset = calculate_window_pos(display_w, display_h, win_size_int[0], win_size_int[1])
    return window_size + "+" + str(window_offset[0]) + "+" + str(window_offset[1])

def open_photo(image_path, size):
    #size is a 2 int tuple
    with Image.open(image_path) as img:
        resized_image = img.resize(size)
        return ImageTk.PhotoImage(img)

def image_to_label(image_path, label_widget, label_size):
    # Disabled: winfo function doesnt work unless the window is updated first
    # lbl_size = (label_widget.winfo_width(), label_widget.winfo_height())
    photo = open_photo(image_path, label_size)

    label_widget.configure(image=photo)
    label_widget.image = photo

def validate_int_input(input_str):
    re_string = "-?[0-9]+"
    return re_match(re_string, input_str)

def validate_float_input(input_str):
    re_string = "-?[0-9]*\\.?[0-9]*"
    return re_match(re_string, input_str)

def validate_positive_float_input(input_str):
    re_string = "[0-9]*\\.?[0-9]*"
    return re_match(re_string, input_str)

def re_match(re_string, input_str):
    if input_str.isspace() or len(input_str) == 0: return False

    match = fullmatch(re_string, input_str)

    if match:
        return True
    else:
        return False

def error_message(title, error_message):
    messagebox.showerror(title=title, message=error_message)

if __name__ == "__main__":
    pass