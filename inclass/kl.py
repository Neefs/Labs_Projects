from inputs import get_gamepad
from pynput import keyboard
from datetime import datetime



def on_press(key):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Key pressed: {key}")

# Start keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()
while True:
    pass

# Gamepad loop
# while True:
#     events = get_gamepad()
#     for event in events:
#         print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Gamepad: {event.code} = {event.state}")sSssssssssswwwwwwwaawaaaddwdwdwdwdwassAWDWadsaWDSAWDsAWDSAw