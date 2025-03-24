# PROGRAM ARCHIVE

### "hello"

```
!5
8333318318.3.4418.3.4418.3.36
```

(packets: "plus100.123")
```
.3333333333.
```

no addons

--_-_-_-_-_-_-_-_-

### raw "hello"

```
!5
.3333333333.33331
.3333333333.31
.33333333333.441
.33333333333.441
.33333333333.36
```

no packets, no addons

--_-_-_-_-_-_-_-_-

### add-on test

```
!1
/6
```

no packets

```python
# addons #
def test():
    s = sys.modules["__main__"]
    s.mem[s.cur] += 101

# "/": test #
```

--_-_-_-_-_-_-_-_-

### the adder

```
!2

>1>2.+.#.5.
```

no packets

```python
# addons #
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
```