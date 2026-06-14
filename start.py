from Classes.os_check import oscheck
from Classes.linux_class import mainlin
from Classes.win_class import mainwin
from subprocess import run

check = oscheck()
linux = mainlin()
win = mainwin()

def update_dlp():
    
    if check.checkos() == "Linux":
        run("./yt-dlp-linux -U", shell=True)
    elif check.checkos() == "Darwin":
        print("Error: MacOS not supported")
    elif check.checkos() == "Windows":
        run("./yt-dlp -U", shell=True)

def start():

    update_dlp()
    if check.checkos() == "Linux":
        linux.mainfunc()
    elif check.checkos() == "Windows":
        win.mainfunc()
        
if __name__ == "__main__":
    start()
