#crawler https://www.baidu.com st <xpath>
#open https://www.baidu.com
"""open函数部分"""
def cmd_open():
    global cmd_args_1
    url = cmd_args_1
    import webbrowser
    webbrowser.open(url)

"""模块导入部分"""
from commands import command
"""函数部分"""
def processing_user_input():
    return 0
"""main loop"""
while True:
    user_input = input("./>")
    processing_user_input()
