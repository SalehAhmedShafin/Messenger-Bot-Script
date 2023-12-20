import time
import pyautogui

def send_message(message, count):
    print("Switch to Messenger and focus on the chat input field...")
    time.sleep(5)  # Give you some time to switch to Messenger

    for _ in range(count):
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        time.sleep(1)  # Adjust the sleep duration if needed

if __name__ == "__main__":
    message_to_send = "Hey, me Saleh Ahmed Shafin"
    messages_count = 100

    send_message(message_to_send, messages_count)
