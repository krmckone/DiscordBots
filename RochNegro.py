
import discord
import asyncio

kwajBot = discord.Client()


@kwajBot.event
async def on_ready():
    print('Logged in as')
    print(kwajBot.user.name)
    print(kwajBot.user.id)
    print(kwajBot.user.mention)
    print('------')
    await kwajBot.change_presence(game=discord.Game(name='FSU!!!!!'))

@kwajBot.event
async def on_message(message):
    if message.content.startswith('!Is josh a negro?'):
        await kwajBot.send_message(message.channel, 'Yes!')
    if message.content.startswith("!WhoIsNegro?"):
        await kwajBot.send_message(message.channel, "Josh is the big 'ol freakin negro!")
    if message.content.startswith("!WhoIsFuklur?"):
        await kwajBot.send_message(message.channel, "NATE IS THE FUKLUR!")

    if message.content.startswith("!hello"):
        await kwajBot.send_message(message.channel, "{0}, hello".format(message.author.mention))
    if message.content.startswith("!bitch"):
        await kwajBot.send_message(message.channel, "{0}, ur a bitch".format(message.author.mention))
    if message.content.startswith('!everyoneBitch'):
        serverIter = kwajBot.servers
        serverList = list(serverIter)
        currentServer = serverList[0]
        currentMembers = currentServer.members
        for member in currentMembers:
            if member.mention == currentServer.get_member(kwajBot.user.id).mention:
                pass
            else:
                await kwajBot.send_message(message.channel, "{0}, ur a big bitch!".format(member.mention))

kwajBot.run('MzM0MTQ0MjE4NjA2MDc1OTA2.DE7buQ.4jL9Lo1Nr1S1mEQ3GS74pUzjla4')