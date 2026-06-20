# Main loop
import re
import time
import os
from commands import *
from instruction import command
from build_user import build_user
#from regular_expression import regex_command

def filter_command(text):
    match = re.search(r'\?[\w-]+', text)
    return match.group(0) if match else None


print("Tyrant has handled everything for you!")
time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")

user_name = build_user()
command_prompt = user_name + ">"
#check_user()
while True:
    user_input = input(command_prompt)
    filtered_input = filter_command(user_input)
    action = command.get(filtered_input)
    if action:
        action()
    else:
        print("None")
    continue