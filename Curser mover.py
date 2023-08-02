import pyautogui

def move_mouse_to(x, y):
    pyautogui.moveTo(x, y)

# Enable the fail-safe feature to stop the script if you move the mouse to the top-left corner of the screen
pyautogui.FAILSAFE = False

# Example usage:
if __name__ == "__main__":
    x_position = 500  # Replace with the desired X coordinate
    y_position = 300  # Replace with the desired Y coordinate
    
    for i in range(1000):
        # Call move_mouse_to outside the loop to reduce function calls
        move_mouse_to(x_position, y_position)
