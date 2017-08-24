
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
    await kwajBot.send_message(kwajBot.get_channel("204728912209641472"), "KWAJ BOT IS ONLINE >:o")



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
        currentServer = "204728912209641472"
        currentMembers = currentServer.members
        for member in currentMembers:
            if member.mention == currentServer.get_member(kwajBot.user.id).mention:
                pass
            else:
                await kwajBot.send_message(message.channel, "{0}, ur a big bitch!".format(member.mention))



#Gives updates on status changes and when players get on games
@kwajBot.event
async def on_member_update(memberBefore, memberAfter):
    currentChannel = kwajBot.get_channel("204728912209641472")
    if memberBefore.status != memberAfter.status:
        await kwajBot.send_message(currentChannel, f"{memberBefore.mention}, the bitch, was {memberBefore.status} and now {memberAfter.status}!")
    else:
        pass
    if memberBefore.game == None and memberAfter.game != None:
        await kwajBot.send_message(currentChannel, f"{memberBefore.mention}, the bitch, got on {memberAfter.game.name}")
    if memberAfter.game == None and memberBefore.game != None:
        await kwajBot.send_message(currentChannel, f"{memberAfter.mention}, the bitch, got off {memberBefore.game.name}")



kwajBot.run('MzM0MTQ0MjE4NjA2MDc1OTA2.DE7buQ.4jL9Lo1Nr1S1mEQ3GS74pUzjla4')



