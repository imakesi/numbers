from rich import print as rp
import sys, os

s = sys.modules["__main__"]
currentfile = ""

def openfile():
    global currentfile
    if s.alt:
        currentfile = s.altvar
        return
    if currentfile != "":
        currentfile = ""
    for i in s.mem:
        currentfile += chr(i)

def readfile():
    global currentfile
    with open(currentfile) as file:
        content = file.read()
    if s.alt:
        print(content)
        return
    for i in content:
        s.mem[s.cur] = ord(i)
        s.cur += 1
    s.cur -= 1

def writefile():
    global currentfile
    mode = "w"
    if s.alt:
        mode = "a"
    if not os.path.exists(currentfile):
        rp("[red]Cannot write to file that doesn't exist.[/red]")
        exit()
    with open(currentfile, mode) as file:
        txt = ""
        for i in s.mem:
            txt += chr(i)
        file.write(txt)

def polarfile():
    global currentfile
    if s.alt:
        if os.path.exists(currentfile):
            os.remove(currentfile)
            return
        rp("[red]Cannot delete file that does not exist.[/red]")
        exit()
    with open(currentfile, "x") as file:
        return
    
fileaddonfunctions = {
    "¢": openfile,
    "£": readfile,
    "¥": writefile,
    "€": polarfile
}