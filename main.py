from datetime import datetime, timedelta
from threading import Timer
from pathlib import Path
import os
#import webbrowser

USER_NAME = "name"
FOLDER_PATH = Path("C:/Users/"+USER_NAME+"/Documents/journal/")


# Add function to create a folder if not found 
# Also create a folder for each month

def create_entry():
    now = datetime.now()
    date_str = str(now.day) +'_'+ str(now.month) + '_' +str(now.year)
    file_name = date_str + "_daily_goal.txt"
    file_open = FOLDER_PATH / file_name
    with open(file_open, "w") as f:
        f.write("Today is " + str(now.weekday()) + "\n")
        f.write("Today's work goals" + "\n")
        f.write("*** Enter work goals here ***" + "\n")
        f.write("Today's personal goals" + "\n")
        f.write("*** Enter personal goals here ***" + "\n")

    
# TODO
# Make a list of alarms for each event
# but for now just use on as set_time
curr_time = datetime.today()
set_time = curr_time.replace(day=curr_time.day, hour=7, minute=0, second=0, microsecond=0) + timedelta(seconds=20)
# Time till next trigger in sec 
delta_t = (set_time - curr_time).total_seconds()
print("Time till alarm: "+str(delta_t)+" seconds")
t = Timer(delta_t, create_entry)
t.start()
