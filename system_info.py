import os
import getpass
from datetime import datetime

current_username = getpass.getuser()
current_datetime = datetime.now()
current_directory = os.getcwd()

output = (
    f"User: {current_username}\n"
    f"Date and Time: {current_datetime}\n"
    f"Current directory : {current_directory}"
)

print(output)

with open("system_report.txt", "w") as file:
    file.write(output)
