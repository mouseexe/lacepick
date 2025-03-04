
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
x = random.randrange(0,255,5)
y = random.randrange(0,255,5)
z = random.randrange(0,255,5)
f = open('colour.tsv', 'w')

for i in range(0, s):
    x = (x+random.choice((0,5))) % 255
    y = (y+random.choice((0,5))) % 255
    z = (z+random.choice((0,5))) % 255
    # print(x,y,z)
    f.write(f'{x}\t{y}\t{z}\n')
f.close()

print(f'Wrote {s} lines to colour.tsv')

