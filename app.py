import os
import random

from guard_actions import *
from role_remover import *

# Token is a secret stored on okd
TOKEN = os.environ.get('DISCORDTOKEN', 'default value')

client = discord.Client(intents=discord.Intents.all())

kay = '149029488938713089'
dan = '184367491345022977'
sleve = '266363683741892619'
eli = '387042210106966016'
amelia = '135402844567240704'

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user or str(message.channel) == 'mod-log':
        stop_teeth = random.randint(1, 3)
        if contains('TEETH', message.content) and stop_teeth != 2:
            print('Rolled ' + str(stop_teeth) + ', chaining TEETH')
        else:
            return

    if contains('TEETH', message.content):
        await message.channel.send('TEETH')
        return

    if str(message.channel) == 'mod-chat' and contains('!lacepick-role-reset', message.content):
        print('Clearing roles.')
        await clear_roles(message)
        return

    if str(message.channel) == 'lacepick-control-panel':
        target_channel = message.content.split(' ')[0]
        target_message = message.content.split(' ', 1)[1]

        for channel in message.author.guild.channels:
            if str(channel) == target_channel:
                await channel.send(target_message)
                return


    if str(message.channel) == 'town-square':
        guild = message.author.guild
        stocks = next(x for x in guild.roles if x.name == 'In The Stocks')
        tomato = next(x for x in guild.roles if x.name == 'tomatoed')

        # Put someone in the stocks
        if 'guards! seize ' in message.content.lower():
            await seize(message, stocks, tomato)

        # Remove someone from the stocks
        if 'guards! release' in message.content.lower():
            await release(message, stocks)

        # Only throw produce if someone is in the stocks
        if len(stocks.members) > 0:
            await throw(message, tomato)
            if str(tomato.color) == '#000000':
                await release(message, stocks)

        # Share color history
        if 'history' in message.content.lower():
            with open('colour.tsv') as f:
                count = sum(1 for _ in f)
            await message.channel.send(f'{count} fruit thrown since last update!',file=discord.File('./colour.tsv'))

    # Amelia color increment on message
    if str(message.author.id) == amelia:
        if random.randint(1, 1000) == 666:
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
