
import random

import os.path
if os.path.isfile("colour.tsv"):
    waiting=True
    while waiting:
        confirm = input("Override colour.tsv? y/n\n>")
        if confirm.lower() == "y":
            waiting = False
        elif confirm.lower() == "n":
            exit()
        else:
            print("Unknown Response: "+confirm)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--steps", help="Steps to generate", type=int, default=1000)
args = parser.parse_args()

s = args.steps
x = 255#random.randrange(0,255,5)
y = 255#random.randrange(0,255,5)
z = 255#random.randrange(0,255,5)
f = open('colour.tsv', 'w')

def colour_overflow(num):
    # if num < 0:
    #     num += 255
    return num

for i in range(0, s):
    x = colour_overflow(x+random.choice((0,-5)))
    y = colour_overflow(y+random.choice((0,-5)))
    z = colour_overflow(z+random.choice((0,-5)))
    if x < 0 or y < 0 or z < 0:
        x=y=z=255
        f.write(f'-1\t-1\t-1\n')
    f.write(f'{x}\t{y}\t{z}\n')
f.close()

print(f'Wrote {s} lines to colour.tsv')

