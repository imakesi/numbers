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