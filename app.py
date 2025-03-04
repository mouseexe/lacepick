import os
import discord
import re
import random

# Token is a secret stored on okd
TOKEN = os.environ.get('DISCORDTOKEN', 'default value')

client = discord.Client(intents=discord.Intents.all())

kay = '149029488938713089'
dan = '184367491345022977'
sleve = '266363683741892619'
eli = '387042210106966016'
amelia = '135402844567240704'

def updateTSV(color):
    f = open('colour.tsv', 'a')
    f.write(f'{color.r}\t{color.g}\t{color.b}\n')
    f.close()

def contains(word, string): return bool(re.search(r'\b' + re.escape(word.lower()) + r'\b', string.lower()))

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

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if str(message.channel) == 'mod-log':
        return

    if str(message.channel) == 'town-square':
        guild = message.author.guild
        stocks = next(x for x in guild.roles if x.name == 'In The Stocks')
        tomato = next(x for x in guild.roles if x.name == 'tomatoed')

        # Put someone in the stocks
        if 'guards! seize ' in message.content.lower():
            target = message.content.split(' ')[2]
            target_user = next(x for x in guild.members if str(x.id) in target)
            print('Seizing ' + str(target_user))
            await tomato.edit(color=discord.Color.from_rgb(255, 255, 255))
            for member in tomato.members:
                await member.remove_roles(stocks)
                await member.remove_roles(tomato)
                print(str(target_user) + ' seized')
            await target_user.add_roles(stocks)
            await target_user.add_roles(tomato)

        # Remove someone from the stocks
        if 'guards! release' in message.content.lower():
            print('Releasing prisoner')
            for member in stocks.members:
                print(str(member) + ' released')
                await member.remove_roles(stocks)

        # Only throw produce if someone is in the stocks
        if len(stocks.members) > 0:

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

        if 'history' in message.content.lower():
            with open('colour.tsv') as f:
                count = sum(1 for _ in f)
            await message.channel.send(f'{count} fruit thrown since last update!',file=discord.File('./colour.tsv'))

    # Amelia color increment on message
    if str(message.author.id) == amelia:
        if random.randint(1, 1000) == 1000:
            await message.reply('Hi Amelia! It\'s me, Lacepick. I hope you\'re having a great day.')
        else :
            roles = message.author.roles
            role = roles[len(roles) - 1]
            if str(role.color) != '#ffffff':
                color = increment_hex(role.color)
                print('Amelia spoke! Color updated from ' + str(role.color) + ' to ' + str(color))
                await role.edit(color=color)

    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
