import time
from colorama import Fore, init

init(autoreset=True)

def animate_line(text, delay=0.014):
    for c in text:
        print(Fore.RED + c, end='', flush=True)
        time.sleep(delay)
    print()

lyrics = [
    ("That should be me holding' your hand", 0.09),
    ("That should be me making' you laugh", 0.09),
    ("That should be me, this is so sad", 0.09),
    ("That should be me", 0.09),
    ("That should be me", 0.09),
    ("That should be me feelin' your kiss", 0.09),
    ("That should be me buyin you gifts", 0.09),
    ("This is so wrong, I can't go on", 0.08),
    ("Til you believe", 0.10),
    ("That should be me", 0.08),
]

for line, speed in lyrics:
    animate_line(line, speed)
    time.sleep(0.04)