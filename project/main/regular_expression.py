
def regex_open_url():
    import re
    import webbrowser
    #"?crawler -https://www.douban/top250  -<span class=\"title\"> -pages=10"
    text = input("enter:")
    pattern = r'-(.*?) '
    try:
        matches = re.findall(pattern,text)
        matches = matches[0]
        matches = matches.strip()
        webbrowser.open(matches)
    except:
        print("error")
    print(matches)
#regex_open_url()

def regex_command():
    import re
    text = "?crawler asdadwad"
    pattern = r'?(.*?) '
    matches = re.findall(pattern,text)
    print(matches)
regex_command()
