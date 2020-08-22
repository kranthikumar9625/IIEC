import os

print("welcome to Application ")
print("please give your input: ", end='')

choice = input().lower()

if ('start' in choice) or('launch' in choice) or ('open' in choice):
    if 'chrome' in choice:
        os.system("start chrome")
    elif 'notepad' in choice:
        if ('notepad++' in choice) or ('notepad ++' in choice):
            os.system('start notepad++.exe')
        else:
            os.system("notepad")
    elif 'calculator' in choice:
        os.system("calc")
    elif 'internet explorer' in choice:
        os.system("start iexplore")
    elif ('ms word' in choice) or ('word' in choice):
        os.system("start winword")
    elif ('ms excel' in choice) or ('excel' in choice):
        os.system("start excel")
    elif 'outlook' in choice:
        os.system('start outlook')
    elif 'onenote' in choice:
        os.system('start onenote')
    elif 'sublime' in choice:
        os.system('start sublime_text')
    elif ('media player' in choice) or ('wm player' in choice):
        os.system('start wmplayer')
    elif 'slack' in choice:
        os.system('slack')
    else:
        print("Please enter valid app")
else:
    print("please include start/open/launch in your input to start the app")


