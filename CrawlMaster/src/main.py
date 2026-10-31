#crawler https://www.baidu.com st <xpath>
#open https://www.baidu.com
"""模块导入部分"""
from commands import command
from instruction import *
"""函数部分"""
def processing_user_input():
    return 0
"""main loop"""
while True:
    user_input = input("./>").strip()
    parts = user_input.split(" ")
    if parts == "exit":
        import sys
        sys.exit(0)

    action = command.get(parts[0])

    if action is None:
        continue

    if parts[0] and len(parts) >= 2:
        arg_1 = parts[1]
#        print(parts[1]) https://www.baidu.com
#        print(arg_1)    https://www.baidu.com
#        print(parts[0]) open
        action(arg_1)
    if parts[0] and len(parts) == 1:
        action()