# GUI Tools
# Author: John Morales
# Access to commonly used functions

import ctypes

def screen_size():
    #https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def windows_geometry_pos(window_size):
    #Calculates the center position of the app window on startup
    #geometry example: "800x600+632+324"
    screen_sz = screen_size()
    screen_center = (screen_sz[0] // 2, screen_sz[1] // 2)
    window_size_int = parse_window_size(window_size)
    window_offset = (screen_center[0] - (window_size_int[0] // 2), screen_center[1] - (window_size_int[1] // 2))

    return window_size + "+" + str(window_offset[0]) + "+" + str(window_offset[1])

def parse_window_size(window_size):
    window_size = window_size.split("x")
    return int(window_size[0]), int(window_size[1])