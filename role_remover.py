async def clear_roles(message):
    guild = message.author.guild
    role_names = ['Decoy', 'Lookout', 'Driver', 'Accomplice', 'Thief', 'Mastermind', 'Double Mastermind', 'Double Mastermind... 2! (insert peggle 2 gif here)', 'One Job From Retirement', 'Successfully Retired', 'Coming Back For One Last Heist', 'You, and Shoe Thievery, Ascend', 'Ascended Decoy', 'Ascended Ascended Decoy', 'Spooky Decoy', 'Spooky Lookout', 'Spooky Driver', 'Spooky Accomplice', 'Spooky Thief', 'Ego', 'Ego+', 'Ego++', 'Ego+++', 'Ego++++', 'THE VAULT', 'THE TRUE VAULT', 'The Modern Day Sisyphus']

    for role in guild.roles:
        print('Checking ' + role.name)
        if role.name in role_names:
            print('Locking in to ' + role.name)
            report = 'Report for: ' + role.name
            for member in role.members:
                print('Removing ' + role.name + ' from ' + member.name)
                await member.remove_roles(role)
                print('Removed ' + role.name + ' from ' + member.name)
                report += '\nRemoved ' + role.name + ' from ' + member.name
            await message.reply(report)