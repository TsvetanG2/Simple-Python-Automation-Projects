import os
import sqlite3
import time


# define a function to save the data
def save_data(data):
    # open the file in write mode
    with open("data.txt", "w") as file:
        # write the data to the file
        file.write(data)

# define a function to get the browser history
def get_browser_history():
    # get the current user profile directory
    dir = os.getenv("USERPROFILE")

    # concatenate the path to the history database
    path = os.path.join(dir, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "History")

    # connect to the history database
    conn = sqlite3.connect(path)

    # query the database for the browser history
    cursor = conn.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC")

    # create a list to store the history data
    history = []

    # iterate over the query results
    for row in cursor:
        # get the URL, title, and last visit time
        url = row[0]
        title = row[1]
        time = row[2]

        # format the data as a string
        data = f"{url} - {title} - {time}"

        # add the data to the history list
        history.append(data)

    # close the database connection
    conn.close()

    # return the history data as a string
    return "\n".join(history)

# define a function to run the application
def run_application():
    while True:
        # get the browser history
        history = get_browser_history()

        # save the history to the file
        save_data(history)

        # pause for 5 seconds before running again
        time.sleep(1)

# run the application
run_application()
