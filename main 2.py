from time import sleep
import random

h = "hello world"
t, c = "", 0
while t != h:
    n = random.randint(ord("a"), ord("z"))

    if chr(n) in h and h[c] == chr(n):
            t += chr(n)
            c += 1
    elif h[c] == " ":
            t += " "
            c += 1

print(t + f'{chr(n)}' if c < len(h) else t)

sleep(0.05)