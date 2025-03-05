import discord

def increment_hex(color):
    return discord.Color(color.value + 1)

def increment_red(color):
    return discord.Color.from_rgb(color.r, max(color.g - 5, 0), max(color.b - 5, 0))

def increment_blue(color):
    return discord.Color.from_rgb(max(color.r - 5, 0), max(color.g - 5, 0), color.b)

def increment_green(color):
    return discord.Color.from_rgb(max(color.r - 5, 0), color.g, max(color.b - 5, 0))

def increment_cyan(color):
    return discord.Color.from_rgb(max(color.r - 5, 0), color.g, color.b)

def increment_magenta(color):
    return discord.Color.from_rgb(color.r, max(color.g - 5, 0), color.b)

def increment_yellow(color):
    return discord.Color.from_rgb(color.r, color.g, max(color.b - 5, 0))

def increment_white(color):
    return discord.Color.from_rgb(min(color.r + 5, 255), min(color.g + 5, 255), min(color.b + 5, 255))

def updateTSV(color):
    f = open('colour.tsv', 'a')
    f.write(f'{color.r}\t{color.g}\t{color.b}\n')
    f.close()