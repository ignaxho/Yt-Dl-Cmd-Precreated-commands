import sys
import distro
import subprocess

apt = []
pacman = []
errorflag = False

so = sys.platform # linux // darwin // win32 #

if so == "linux" or "linux2":
    distroid = distro.id()
    print(distroid)
    if distroid in apt:
        print("Apt")
    elif distroid in pacman:
        print("Pacman")
    else:
        print("Other")

elif so == "win32" or "win64":
    print(so)
    
elif so == "darwin":
    errorflag = True
    print("Mac not supported")

print(so)