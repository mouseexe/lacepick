import discord

from color_modification import *
from util import *


async def seize(guild, message, stocks, tomato):
    target = message.content.split(' ')[2]
    if contains('me', target.lower()):
        target_user = message.author
    else:
        target_user = next(x for x in guild.members if str(x.id) in target)
    print('Seizing ' + str(target_user))
    await tomato.edit(color=discord.Color.from_rgb(255, 255, 255))
    f = open('colour.tsv', 'a')
    f.write(f'-1\-1\-1\n')
    f.write(f'255\t255\t255\n')
    f.close()
    for member in tomato.members:
        await member.remove_roles(stocks)
        await member.remove_roles(tomato)
        print(str(target_user) + ' seized')
    await target_user.add_roles(stocks)
    await target_user.add_roles(tomato)
    await message.add_reaction('🤏')


async def release(message, stocks):
    print('Releasing prisoner')
    for member in stocks.members:
        print(str(member) + ' released')
        await member.remove_roles(stocks)
        await message.add_reaction('🫳')


async def throw(message, tomato):
    # Throw a tomato at someone in the stocks
    if contains('tomato', message.content):
        color = increment_red(tomato.color)
        print('Tomato thrown! Color updated from ' + str(tomato.color) + ' to ' + str(color))
        updateTSV(color)
        await tomato.edit(color=color)
        await message.add_reaction('🍅')

    # Throw a blueberry at someone in the stocks
    if contains('blueberry', message.content):
        color = increment_blue(tomato.color)
        print('Blueberry thrown! Color updated from ' + str(tomato.color) + ' to ' + str(color))
        updateTSV(color)
        await tomato.edit(color=color)
        await message.add_reaction('🫐')

    # Throw an avocado at someone in the stocks
    if contains('avocado', message.content):
        color = increment_green(tomato.color)
        print('Avocado thrown! Color updated from ' + str(tomato.color) + ' to ' + str(color))
        updateTSV(color)
        await tomato.edit(color=color)
        await message.add_reaction('🥑')

    # Throw ice  at someone in the stocks
    if contains('ice', message.content):
        color = increment_cyan(tomato.color)
        print('Ice thrown! Color updated from ' + str(tomato.color) + ' to ' + str(color))
        updateTSV(color)
        await tomato.edit(color=color)
        await message.add_reaction('🧊')

    # Throw a grape at someone in the stocks
    if contains('grape', message.content):
        color = increment_magenta(tomato.color)
        print('Grape thrown! Color updated from ' + str(tomato.color) + ' to ' + str(color))
        updateTSV(color)
        await tomato.edit(color=color)
        await message.add_reaction('🍇')

    # Throw a banana at someone in the stocks
    if contains('banana', message.content):
        color = increment_yellow(tomato.color)
        print('Banana thrown! Color updated from ' + str(tomato.color) + ' to ' + str(color))
        updateTSV(color)
        await tomato.edit(color=color)
        await message.add_reaction('🍌')

    # Throw water at someone in the stocks
    if contains('water', message.content):
        color = increment_white(tomato.color)
        print('Water thrown! Color updated from ' + str(tomato.color) + ' to ' + str(color))
        updateTSV(color)
        await tomato.edit(color=color)
        await message.add_reaction('💧')