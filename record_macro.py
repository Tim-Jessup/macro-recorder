from pynput import mouse, keyboard
import time

actions = []
pressed_keys = set()
recording_time = 10  # seconds

def on_click(x, y, button, pressed):
    if pressed:
        actions.append(f"pyautogui.click({x}, {y})")

def on_press(key):
    pressed_keys.add(key)

    # Hotkey detection
    if keyboard.Key.ctrl_l in pressed_keys or keyboard.Key.ctrl_r in pressed_keys:
        if key == keyboard.Key.tab:
            actions.append("pyautogui.hotkey('ctrl', 'tab')")
            return

    # Regular keys
    try:
        if hasattr(key, 'char') and key.char:
            actions.append(f"pyautogui.typewrite('{key.char}')")
        elif key == keyboard.Key.enter:
            actions.append("pyautogui.press('enter')")
        elif key == keyboard.Key.backspace:
            actions.append("pyautogui.press('backspace')")
        elif key == keyboard.Key.tab:
            actions.append("pyautogui.press('tab')")
        elif key == keyboard.Key.esc:
            return False  # allow early stop with ESC
    except Exception:
        pass

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

def main():
    print("Starting in 3 seconds... get ready!")
    time.sleep(3)

    print(f"Recording for {recording_time} seconds...")

    with mouse.Listener(on_click=on_click) as mouse_listener, \
         keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:

        time.sleep(recording_time)  # <-- change this if you want a longer/shorter record time

    with open("macro_playback.py", "w") as f:
        f.write("import pyautogui\nimport time\n\n")
        f.write("print('Starting playback in 3 seconds...')\n")
        f.write("time.sleep(3)  # wait before starting playback\n\n")

        f.write("for i in range(10):\n")  # <-- change this if you want to repeat the actions more or less times

        for action in actions:
            f.write("   " + action + "\n")
            f.write("   time.sleep(0.3)\n")

        f.write("   print(f'Completed {i+1} iterations')\n\n")
        f.write("print('Playback complete.')\n")

    print("Recording complete. Saved as macro_playback.py")



if __name__ == "__main__":
    main()
