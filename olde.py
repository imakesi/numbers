# (0123456789!?.,/)

import requests
import re
import toml

settings = ""
with open("settings.toml") as file:
  settings = toml.loads(file.read())

packets = []
packeturls = settings["lang"]["packets"]
for i in packeturls:
  packets.append(requests.get(i).text)

stuffamt = 50
stuff = [0 for i in range(stuffamt)]
altvar = 0
cursor = 0

alt = False
skipln = False

def run(fname=settings["lang"]["run"]):
  global cursor, stuff, stuffamt, alt, altvar, skipln
  with open(fname, "r") as file:
    lines = file.readlines()
    if lines[0].startswith("!"):
      newlen = int(lines[0][1:])
      stuffamt = newlen
      stuff = [0 for k in range(stuffamt)]

      lines = lines[1:]
      for i in lines:
        for j in i.strip():
          if j == "0":
            if not alt:
              cursor = 0
            if alt and cursor > 0:
              stuff[cursor] = 0
          if j == "1":
            if not alt:
              if cursor > stuffamt:
                print(f"CursorError: cursor value {cursor} exceeds maximum {stuffamt}")
                break
              cursor += 1
            else:
              altvar += 1
          if j == "2":
            if not alt:
              if cursor <= 0:
                print(f"CursorError: cursor value {cursor} is less than 0")
                break
              cursor -= 1
            else:
              altvar -= 1
          if j == "3":
            if not alt:
              stuff[cursor] += 1
            else:
              stuff[cursor] += 5
          if j == "4":
            if not alt:
              stuff[cursor] += 10
            else:
              stuff[cursor] += 50
          if j == "5":
            if not alt:
              stuff[cursor] -= 1
            else:
              stuff[cursor] -= 5
          if j == "6":
            if not alt:
              print(stuff[cursor])
            else:
              print(altvar)
          if j == "7":
            astr = ""
            if not alt:
              for k in stuff:
                if k != 0:
                  astr += chr(k)
            else:
              for k in stuff:
                astr += chr(k)
            print(astr)
          if j == "8":
            if not alt:
              for k in stuff:
                if k != 0:
                  print(k)
            else:
              for k in stuff:
                print(k)
          if j == "9":
            inp = input(" > ")
            if re.search(r"[^0-9]", inp):
              for k in inp:
                if not alt:
                  stuff[cursor] = ord(k)
                else:
                  altvar = ord(k)
                cursor += 1
            else:
              if not alt:
                stuff[cursor] = int(inp)
              else:
                altvar = int(inp)
          if j == "(":
            if not alt:
              stuff = [0 for k in range(stuffamt)]
            if alt:
              altvar = 0
          if j == ")":
            astr = ""
            for k in stuff:
              if k != 0:
                astr += chr(int(k))
            res = requests.get(astr)
            if not alt:
              for k in res.text:
                if k.isdecimal():
                  stuff[cursor] = int(k)
                else:
                  stuff[cursor] = ord(k)
                cursor += 1
            if alt and cursor > 0:
              if res.text.isdecimal():
                altvar = int(res.text)
              else:
                altvar = res.text
            if alt and cursor <= 0:
              print(res.text)
          if j == "!":
            if not alt:
              stuff[cursor] = ord(str(stuff[cursor]))
            else:
              altvar = ord(str(altvar))
          if j == "?":
            if not alt:
              if stuff[cursor] <= 0:
                skipln = True
            else:
              if altvar <= 0:
                skipln = True
          if j == ".":
            alt = not alt
          if j == ",":
            with open(settings["lang"]["packetrun"], "w") as file2:
              file2.write(packets[cursor])
            print(f"running... {settings['lang']['packetrun']}")
            run(settings["lang"]["packetrun"])
          if j == "/":
            if not alt:
              astr = ""
              for k in stuff:
                if k != 0:
                  astr += chr(k)
              if astr.strip():
                settings["lang"]["packets"].append(astr)
            else:
              settings["lang"]["packets"] = []
            with open("settings.toml", "w") as file2:
              toml.dump(settings, file2)

if __name__ == "__main__":
  run()