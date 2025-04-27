import sys
s = sys.modules["__main__"]

def lgt():
    guess = int(chr(s.mem[s.cur]))
    print(guess)
    secret = int(s.altvar)
    if guess == secret:
        print("CORRECT! press CTRL+C to exit")
    elif guess > secret:
        print("guess is too large...")
    elif guess < secret:
        print("guess is too small...")

apiaddonfunctions = {
    "ƒ": lgt
}