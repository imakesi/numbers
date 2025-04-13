import requests
import os
from rich import print as rp

# import your addons here

# from addons.file import functions
from addons.general import *

# key is the character that runs the function, value is the function, imported above

addonfunctions = {
    "@": rand,
    ">": inp,
    "<": ordinp,
    "=": strinp,
    "_": get,
    "+": plus,
    "-": minus,
    "*": mult,
    "/": div,
    "^": exp,
    "%": root,
    "h": hundred,
    ":": alttransfer,

    ";": exit
}

# import your addons here

filesfolder = "packets"
packetfiles = os.listdir(filesfolder)
packeturls = []

packetcur = 0

memamt = 50
mem = [0 for i in range(memamt)]
cur = 0

alt = False
altvar = 0

skipln = False
altskipln = 0

def run(fname="main.123"):
    global mem, memamt, packetcur, packeturls, packetfiles, alt, altvar, cur
    with open(fname) as file:
        lines = file.readlines()

    if lines == []:
        return

    if lines[0].strip().startswith("!"):
        if len(lines[0]) == 1:
            rp(f"[red]Line 1, {fname}\nDesired memory length not found.[/red]")
            exit()
        try:
            memamt = lines[0].strip()[1:]
            mem = [0 for i in range(int(memamt))]
            lines = lines[1:]
        except TypeError:
            rp("[red]Memory length is not a number.[/red]")
            exit()

    for line in lines:
        line = line.strip()

        if line.startswith("~"):
            continue

        for i in line:
            if i == "0":
                if alt:
                    mem[cur] = 0
                    continue
                cur = 0
            elif i == "1":
                if alt:
                    altvar += 1
                    continue
                cur += 1
            elif i == "2":
                if alt:
                    altvar -= 1
                    continue
                cur -= 1
            elif i == "3":
                if alt:
                    mem[cur] += 10
                    continue
                mem[cur] += 1
            elif i == "4":
                if alt:
                    mem[cur] -= 10
                    continue
                mem[cur] -= 1
            elif i == "5":
                if alt:
                    print(altvar)
                    continue
                print(mem[cur])
            elif i == "6":
                if alt:
                    print(chr(altvar))
                    continue
                txt = ""
                for x in mem:
                    txt += chr(x)
                print(txt)
            elif i == "7":
                if alt:
                    packetcur -= 1
                    continue
                packetcur += 1
            elif i == "8":
                if alt:
                    res = requests.get(packeturls[packetcur])
                    with open("hidden/placeholder.123", "w") as file:
                        file.write(res.text)
                    run("hidden/placeholder.123")
                    continue
                run(f"{filesfolder}/{packetfiles[packetcur]}")
            elif i == "9":
                if alt:
                    altvar = 0
                    continue
                mem = [0 for i in range(int(memamt))]
            elif i == ".":
                alt = not alt
            elif i in addonfunctions.keys():
                addonfunctions[i]()

# cursor = 0 / value = 0
# cursor += 1 / altvar += 1
# cursor -= 1 / altvar -= 1
# value += 1 / value += 10
# value -= 1 / value -= 10
# print value / print altvar
# print chr values of mem / print chr value of altvar
# packet pointer += 1 / packet pointer -= 1
# use packet file / use packet from url
# skip next line if value is 0 / skip next value lines if altvar is 0
# toggle alt

run()
