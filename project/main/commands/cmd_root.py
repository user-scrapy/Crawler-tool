#Root permission command
from build_user import check_user
def root_command():
    global root_status_code
    root_status_code = 0
    if root_status_code == 0:
        check_user()
        import os
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("root status code is 1, you have root permission now")

    return 0