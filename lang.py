import requests
import os
import contextlib
from rich import print as rp

# import your addons here

# from addons.file import functions
from addons.general import *
from extras.addons.filecontrol import *

# key is the character that runs the function, value is the function, imported above
# generaladdonfunctions in general

addonfunctions = {}
addonfunctions.update(generaladdonfunctions)
addonfunctions.update(fileaddonfunctions)

# import your addons here

filesfolder = "packets"
packetfiles = os.listdir(filesfolder)
packeturls = []

packetcur = 0

mainrunner = "main.123"

eventrunner = "main.456"
eventfunctions = {}

memamt = 50
mem = [0 for i in range(memamt)]
cur = 0

alt = False
altvar = 0

skipln = False
altskipln = 0

def sendevent(target):
    global eventfunctions

    runlater = False
    with contextlib.suppress(Exception):
        with open("hidden/placeholder.123", "w") as file:
            file.write(eventfunctions[target][0])
            if len(eventfunctions[target]) == 2:
                runlater = True
        run("hidden/placeholder.123", origin="event")
        if runlater:
            sendevent(eventfunctions[target][1], origin="event")
            runlater = False

# event listeners #
with open(eventrunner) as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    line = line.split("~")[0]
    
    if line == "":
        continue

    node = line[0]

    if node == "*":
        target = line[1]
        func = line[1:].split(":")[1]
        
        output = [func]

        eventfunctions[target] = output
    elif node == "#":
        target = line[1:4]
        func = line[1:].split(":")[1]

        output = [func]

        eventfunctions[target] = output
        
    elif node == "&":
        target = line[1:].split(":")[0]
        func = line[1:].split(":")[1]

        output = [func]

        eventfunctions[target] = output

def run(fname=mainrunner, ignore=[],  origin="", ignoreEvent=False):
    global mem, memamt, packetcur, packeturls, packetfiles, alt, altvar, cur, eventfunctions
    
    if origin == "event" and not ignoreEvent:
        sendevent("EVN")
    if origin == "event":
        ignoreEvent = True
    
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
            memamt = int(memamt)
            if memamt > len(mem):
                for i in range(memamt - len(mem)):
                    mem.append(0)
            if memamt < len(mem):
                for i in range(len(mem) - memamt):
                    mem.pop()
            lines = lines[1:]
        except Exception as e:
            rp(f"[red]{e}[/red]")
            exit()

    for line in lines:
        line = line.strip()

        for i in ignore:
            line.replace(i, "")

        if "~" in line:
            line = line.split("~")[0]

        for i in line:
            if i in eventfunctions and not ignoreEvent:
                sendevent(i)

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
                if not ignoreEvent:
                    sendevent("OUT")

                if alt:
                    print(altvar)
                    continue
                print(mem[cur])
            elif i == "6":
                if not ignoreEvent:
                    sendevent("OUT")

                if alt:
                    print(chr(altvar))
                    continue
                txt = ""
                for x in mem:
                    txt += chr(x)
                print(txt)
            elif i == "7":
                if not ignoreEvent:
                    sendevent("PAC")

                if alt:
                    packetcur -= 1
                    continue
                packetcur += 1
            elif i == "8":
                if not ignoreEvent:
                    sendevent("PAC")

                if alt:
                    res = requests.get(packeturls[packetcur])
                    with open("hidden/placeholder.123", "w") as file:
                        file.write(res.text)
                    run("hidden/placeholder.123")
                    continue
                run(f"{filesfolder}/{packetfiles[packetcur]}", ignore_reset=True)
            elif i == "9":
                if not ignoreEvent:
                    sendevent("CLR")

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
input("Press ENTER to end")

"""
EVENTS

EVN - event triggered
OUT - something printed
PAC - something about packets
CLR - mem cleared
"""