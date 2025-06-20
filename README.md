# numbers
 a little esolang i made for fun
 one character, one command

make sure to run "lang.py"

### coding in numbers

(cursor is the memory pointer, value is the value at the pointer in the memory, alternate variable is a little seperated number)

the commands:

| x | function                    | alternate function                   |
|---|-----------------------------|--------------------------------------|
| 0 | set cursor to 0             | set value to 0                       |
| 1 | increment cursor            | increment alternate var              |
| 2 | decrement cursor            | decrement alternate var              |
| 3 | increment value             | increment value by 10                |
| 4 | decrement value             | decrement value by 10                |
| 5 | print value                 | print alternate var                  |
| 6 | print chr values of memory  | print chr value of alternate var     |
| 7 | increment packet cursor     | decrement packet cursor              |
| 8 | run packet file             | run packet url                       |
| 9 | clear memory                | clear alternate var                  |
| . | toggle alt                  | toggle alt                           |

hopefully you can figure out what's going on here

also, a special little clause, you can set the length of the memory. to do this, go to the first line, type "!", then your memory length as a number (the first line will be ignored if it starts with "!", because of my bad coding, so please don't do that error)

another note is that "~" is used to initiate a comment (but only at the start)

now these packets in the table are basically just functions, they are written in numbers itself, and can be in a file or sent back from a URL. the cursor memory system is mirrored for these as you can see in the table

packets cousin, addons, are basically custom commands. they are written in python and are like the interpreter in "lang.py". i recommend either using the addons in "addons/general.py" or no addons at all, as sometimes addons can be overwritten as packets

### how to write a program


if you haven't already, open vscode and use `git clone https://github.com/imakesi/numbers` and Ctrl+K Ctrl+O the folder 

go to "main.123", this is the esolang code that "lang.py" interprets

for this example, i'll just make it output "hello". the way this works is `6` outputs the chr values of all of the memory, so if we fill up the memory with the ascii values for "hello" (104 101 108 108 111), we can use command `6` to output "hello" into the console.

if you use the table, you can see that alternate `3` adds 10 to the value, so that's an easy way to get to 100, which is common in the ascii value of lowercase letters

let's just start with getting to the ascii value for "h", 104.

```
.3333333333.
3333
6
```

alternate 3 adds 10 to the value, so the top gives 100

then regular 3 adds 1 to the value, so the middle gives 4

this is good, but only one out of the five letters, so if we apply the same logic to the other numbers, we get this

```
.3333333333.
3333
1
~ ^ 104, h

.3333333333.
3
1
~ ^ 101, e

.3333333333.
33333333
1
~ ^ 108, l

.3333333333.
33333333
1
~ ^ 108, l

.33333333333.
3
1
~ ^ 111, o

6
```

`1` here goes to the next character, and `6` prints out it as text

now, compacted:

`.3333333333.33331.3333333333.31.3333333333.333333331.3333333333.333333331.33333333333.316`

and we made "hello", but this has lots and lots of `.3333333333.`

"general.py" includes a plus 100 addon, so replace `.3333333333.` with `h`, the +100 addon command in "general.py"

you can change the "h" by editing the `addonfunctions` dictionary, but i like to use the ones i set

`h33331h31h333333331h333333331.33333333333.316`

and instead of +110, alternate h:

`h33331h31h333333331h333333331.h.316`

now i compacted this further logic wise, (instead of +8, +10 then -2, which is less characters and removing the last `1`):

`h33331h31.h.441.h.441.h.36`

and we get "hello"!

---

### how to write an addon


let's start at "addons/template.py". either copy it, or overwrite it on your copy entirely. in the command, test, we will be making an addon.

the example addon i will be using, is to set the value to 727. usually, the value is `mem[cur]`, but because we are on a different script, we will be utilizing the `s` variable to use variables from "lang.py". so, in this case, to reference the value, we would use `s.mem[s.cur]`. so our code is:

```python
import sys

s = sys.modules["__main__"]

def test():
    # your code here...
    s.mem[s.cur] = 727
```

but, as you already know, commands tend to have an alternate mode. if you're looking at "general.py", you can see i used:

```python
if s.alt:
    # alt mode
    return
# regular mode
```

if we apply this logic to our previous command, and fufill an alternate mode, (i'll be switching the value for the altvar), we get:

```python
import sys

s = sys.modules["__main__"]

def test():
    # your code here...
    if s.alt:
        s.altvar = 727
        return
    s.mem[s.cur] = 727
```

add the specified command names

```python
import sys

s = sys.modules["__main__"]

def test():
    # your code here...
    if s.alt:
        s.altvar = 727
        return
    s.mem[s.cur] = 727

testaddonfunctions = {
    "!": test
}
```

in this example, i used "!" to represent the test command, so if you run "!" in the language, you will get the desired function (setting value to 727).

now, add that to "lang.py" with this:

```python
from addons.template import test, testaddonfunctions

addonfunctions = {}
addonfunctions.update(testaddonfunctions)
```

if you're making an addon, don't repeat commands, as it will overwrite or be overwritten (make sure to not conflict with "general.py" addons)
if you're using an addon, and it conflicts with other ones you're using, change the values

good practice is also using events

---

### events

the file extension 123's sibling is 456, and this file is basically the event listener

go to main.456

right now, the only 3 nodes are *, #, and &. the * node takes one character as input and takes commands as target. # takes 3 characters and is stuff like "REQ", "CLR", you can find at the bottom of any file with functions (addons, or lang.py). & is like # but dynamic

the target is what it looks for and after the colon is in the language and what it runs

the syntax is:

\[node\] \[target\] : \[function\]

so basically, if you're gonna link it so that every time 3 is ran, 5 is ran:

*3:5

whenever 3 runs in the main script, it runs 5

if you want to take a different approach, so that when it clears the memory, it adds 5:

\#CLR:33333

another thing is that, if you want events to run in one of your event triggers, allowing loops, toggle it like this

UNIGNORE \[node and code\] ~ allows loops

then start ignoring again like this

IGNORE \[node and code\] ~ stops loops

also after your node and code, you can do emit. building off `*3:5` for example:

&COOLEVENTNAME:333333333333333333333333333333333333333333333335
*3:5 emit COOLEVENTNAME

you can probably do something wild with this, but i haven't found it yet

go wild

---

if you want to know some programs, go to "ARCHIVE.md" or "archivebutdumb.txt"
