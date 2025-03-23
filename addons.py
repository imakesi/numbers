import sys

def test():
    s = sys.modules["__main__"]
    s.mem[s.cur] += 101