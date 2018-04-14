
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
    if message.content.startswith('!Is josh a good friend?'):
        await kwajBot.send_message(message.channel, 'Yes!')
    if message.content.startswith("!WhoIsTheBestFriend?"):
        await kwajBot.send_message(message.channel, "Josh is the big 'ol best friend!")
    if message.content.startswith("!WhoIsNate?"):
        await kwajBot.send_message(message.channel, "Nate is also one of the best friends!")

    if message.content.startswith("!hello"):
        await kwajBot.send_message(message.channel, "{0}, hello".format(message.author.mention))
    if message.content.startswith("!friend"):
        await kwajBot.send_message(message.channel, "{0}, you're a good friend".format(message.author.mention))
    if message.content.startswith('!everyoneFriend'):
        currentServer = "204728912209641472"
        currentMembers = currentServer.members
        for member in currentMembers:
            if member.mention == currentServer.get_member(kwajBot.user.id).mention:
                pass
            else:
                await kwajBot.send_message(message.channel, "{0}, you're a great friend!".format(member.mention))



#Gives updates on status changes and when players get on games
@kwajBot.event
async def on_member_update(memberBefore, memberAfter):
    currentChannel = kwajBot.get_channel("204728912209641472")
    if memberBefore.status != memberAfter.status:
        await kwajBot.send_message(currentChannel, f"{memberBefore.mention}, our friend, was {memberBefore.status} and now {memberAfter.status}!")
    else:
        pass
    if memberBefore.game == None and memberAfter.game != None:
        await kwajBot.send_message(currentChannel, f"{memberBefore.mention}, our friend, got on {memberAfter.game.name}")
    if memberAfter.game == None and memberBefore.game != None:
        await kwajBot.send_message(currentChannel, f"{memberAfter.mention}, our friend, got off {memberBefore.game.name}")
