# numbers
 a little esolang i made for fun


### coding in numbers

(cursor is the memory pointer, value is the value at the pointer in the memory)

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
| 9 | skip next line if value = 0 | skip next value lines if alt var = 0 |
| . | toggle alt                  | toggle alt                           |

now, you may be wondering what a "packet" is

basically, a packet file is a function in a different numbers file

it's just useful for compacting code

a packet url is a get request that returns numbers code

you put your packet files in the packets folder, and your packet urls in the packeturls list in "lang.py"


### great, packets, but what about addons?

addons are basically custom commands

if you're looking at "lang.py" currently, you can see that at the top, there's a dictionary for addonfunctions

if you want to test that, try using the addon test in "ARCHIVE.md"

if you want to make your own addon, clear the value in the dictionary and prepare a function, then go to "addons.py"

keep the `s = sys.modules\["__main__"]`, and write out your function using `s.var` to access variables from lang

then write out a program in "main.123", using "/" as your function

# im a bad teacher so probably just tell ai to explain the code to you
