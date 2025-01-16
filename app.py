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

clark = get(client.emojis, name='hubris')

def increment_hex(color):
    return discord.Color(color.value + 1)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if str(message.channel) == 'mod-chat' and '/roles' in message.content:
        print(message.guild.roles)
        await message.add_reaction(clark)

    if str(message.author.id) == amelia:
        roles = message.author.roles
        role = roles[len(roles) - 1]
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
