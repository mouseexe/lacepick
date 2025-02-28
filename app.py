import os
import discord
from discord.utils import get

# Token is a secret stored on okd
TOKEN = os.environ.get('DISCORDTOKEN', 'default value')

client = discord.Client(intents=discord.Intents.all())

kay = '149029488938713089'
dan = '184367491345022977'
sleve = '266363683741892619'
eli = '387042210106966016'
amelia = '135402844567240704'

def increment_hex(color):
    return discord.Color(color.value + 1)

def increment_red(color):
    return discord.Color.from_rgb(color.r + 1, 0, 0)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    roles = message.author.roles
    role = roles[len(roles) - 1]
    role_name = role.name

    # Put someone in the stocks
    if role_name == 'Moderator' and 'Guards! Seize ' in message.content:
        print('attempting to seize')
        guild = message.author.guild
        target = message.content.split(' ')[2]
        target_user = next(x for x in guild.members if str(x.id) in target)
        print('seizing ' + target_user)
        role = next(x for x in guild.roles if x.name == 'In The Stocks')
        tomato = next(x for x in guild.roles if x.name == 'tomatoed')
        for member in role.members:
            await member.remove_roles(role)
            await member.remove_roles(tomato)
        await target_user.add_roles(role)
        await target_user.add_roles(tomato)

    # Remove someone from the stocks
    if role_name == 'Moderator' and 'Guards! Release ' in message.content:
        guild = message.author.guild
        target = message.content.split(' ')[2]
        target_user = next(x for x in guild.members if str(x.id) in target)
        role = next(x for x in guild.roles if x.name == 'In The Stocks')
        await target_user.remove_roles(role)

    # Throw a tomato at someone in the stocks
    if str(message.channel) == 'town-square' and '!tomato' in message.content:
        guild = message.author.guild
        tomato = next(x for x in guild.roles if x.name == 'tomatoed')
        color = increment_red(tomato.color)
        await tomato.edit(color=color)

    # Amelia color increment on message
    if str(message.author.id) == amelia:
        if str(role.color) != '#ffffff':
            color = increment_hex(role.color)
            print('Color updated from ' + str(role.color) + ' to ' + str(color))
            await role.edit(color=color)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
