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

--_-_-_-_-_-_-_-_-

### alt conditional

```
h133.9.
6
6
6

#9
the 6 on line 4 decides whether it outputs or not, because this skips the first two lines. the smiley is the memory equal to 2
```

no packets
general.py

--_-_-_-_-_-_-_-_-

### get request

```
h33331
.h3.44441
.h3.44441
.h.331
.h.333331
.333333.441
.33333.4441
.33333.4441
h33331
.h3.44441
.h3.44441
.h.331
h441
h333331
.h.1
.33333.44441
.h.31
.h.33331
h3331
.33333.4441
h3331
h31
.h3.44441
6
._.
```

no packets
general.py

--_-_-_-_-_-_-_-_-