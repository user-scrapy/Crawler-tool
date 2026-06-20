def get_time_command():
    import datetime
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)
    return 0