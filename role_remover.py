async def clear_roles(message):
    guild = message.author.guild
    role_names = ['Decoy', 'Lookout', 'Driver', 'Accomplice', 'Thief', 'Mastermind', 'Double Mastermind', 'Double Mastermind... 2! (insert peggle 2 gif here)', 'One Job From Retirement', 'Successfully Retired', 'Coming Back For One Last Heist', 'You, and Shoe Thievery, Ascend', 'Ascended Decoy', 'Ascended Ascended Decoy', 'Spooky Decoy', 'Spooky Lookout', 'Spooky Driver', 'Spooky Accomplice', 'Spooky Thief', 'Ego', 'Ego+', 'Ego++', 'Ego+++', 'Ego++++', 'THE VAULT', 'THE TRUE VAULT', 'The Modern Day Sisyphus']

    report = 'Report:'

    for role in guild.roles:
        if role.name in role_names:
            for member in role.members:
                await member.remove_roles(role)
                report += '\nRemoved ' + role.name + ' from ' + member.name
    await message.reply(report)