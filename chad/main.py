import keyboard
from chad.reply_generator import generate_reply
from chad.logger import log

def main_loop():
    print("Chad is listening. Press your hotkey to speak.")
    while True:
        keyboard.wait('F9')
        try:
            print("🎤 Listening...")
            reply = generate_reply()
            print("🧠 Chad says:", reply)
        except Exception as e:
            log(f"Error in main loop: {e}")

if __name__ == "__main__":
    main_loop()
