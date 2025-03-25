import sys
import requests
import math

s = sys.modules["__main__"]

def inp():
    if s.alt:
        s.altvar = int(input(" > "))
        return
    s.mem[s.cur] = int(input(" > "))

def clear():
    s.mem = [0 for i in range(int(s.memamt))]

def get():
    res = requests.get(s.packeturls[s.packetcur])
    print(res.text)

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