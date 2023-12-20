import time
import pyautogui

def send_messages(base_message, count):
    print("Switch to Apps and focus on the chat input field...")
    time.sleep(5)

    for i in range(1, count + 1):
        message = f"{base_message} {i}"
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        time.sleep(1) 

if __name__ == "__main__":
    base_message_to_send = "I love you"
    messages_count = 100

    send_messages(base_message_to_send, messages_count)
