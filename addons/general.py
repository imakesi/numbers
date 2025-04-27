import sys
import requests
import math
import random
import importlib.util
from pathlib import Path
from rich import print as rp
from time import sleep

s = sys.modules["__main__"]

def rand():
    if s.alt:
        s.altvar = random.randint(1, 10)
        return
    s.mem[s.cur] = random.randint(1, 10)

def inp():
    if s.alt:
        try:
            s.altvar = int(input(" > "))
        except ValueError:
            rp("[red]Please input a number.[/red]")
        return
    try:
        s.mem[s.cur] = int(input(" > "))
    except ValueError:
        rp("[red]Please input a number.[/red]")

def ordinp():
    if s.alt:
        try:
            for i in str(int(input(" > "))):
                s.mem[s.cur] = ord(i)
                s.cur += 1
            s.cur -= 1
        except ValueError:
            rp("[red]Please input a number.[/red]")
        return
    try:
        s.mem[s.cur] = ord(str(int(input(" > "))))
    except ValueError:
        rp("[red]Please input a 1-digit number.[/red]")

def strinp():
    if s.alt:
        s.altvar = input(" > ")
        return
    for i in input(" > "):
        s.mem[s.cur] = ord(i)
        s.cur += 1
    s.cur -= 1

def infinite():
    s.run()

def get():
    if s.alt:
        txt = ""
        for i in s.mem:
            txt += chr(i)
        res = requests.get(txt)
        print(res.text)
        return
    res = requests.get(s.packeturls[s.packetcur])
    print(res.text)

def alttransfer():
    if s.alt:
        s.mem[s.cur] = ord(str(s.altvar))
        return
    s.mem[s.cur] = s.altvar

def plus():
    if s.alt:
        s.altvar = s.mem[s.cur] + s.mem[s.cur+1]
        return
    s.mem[s.cur] += s.mem[s.cur+1]

def minus():
    if s.alt:
        s.altvar = s.mem[s.cur] - s.mem[s.cur+1]
        return
    s.mem[s.cur] -= s.mem[s.cur+1]

def mult():
    if s.alt:
        s.altvar = s.mem[s.cur] * s.mem[s.cur+1]
        return
    s.mem[s.cur] *= s.mem[s.cur+1]

def div():
    if s.alt:
        s.altvar = s.mem[s.cur] / s.mem[s.cur+1]
        return
    s.mem[s.cur] /= s.mem[s.cur+1]

def exp():
    if s.alt:
        s.altvar = s.mem[s.cur] ** s.mem[s.cur+1]
        return
    s.mem[s.cur] **= s.mem[s.cur+1]

def root():
    if s.alt:
        s.altvar = math.sqrt(s.mem[s.cur])
        return
    s.mem[s.cur] = math.sqrt(s.mem[s.cur])

def hundred():
    if s.alt:
        s.mem[s.cur] += 110
        return
    s.mem[s.cur] += 100

generaladdonfunctions = {
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
    ":": alttransfer,
    "h": hundred,
    "i": infinite,

    ";": exit
}