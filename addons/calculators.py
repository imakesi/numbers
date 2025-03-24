import sys

s = sys.modules["__main__"]

def inp():
    if s.alt:
        s.altvar = int(input(" > "))
        return
    s.mem[s.cur] = int(input(" > "))

def plus():
    if s.alt:
        s.altvar = s.mem[s.cur] + s.mem[s.cur+1]
        return
    s.mem[s.cur] += s.mem[s.cur+1]

def clear():
    s.mem = [0 for i in range(int(s.memamt))]

# ">": inp #
# "+": plus #
# "#": clear #