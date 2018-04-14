
import discord
import asyncio

bigHoss = discord.Client()

@bigHoss.event
async def on_ready():
    print('Logged in as')
    print(bigHoss.user.name)
    print(bigHoss.user.id)
    print(bigHoss.user.mention)
    print('------')
    await bigHoss.change_presence(game=discord.Game(name="NAM '67"))
    await bigHoss.send_message(bigHoss.get_channel("247243512519720961"), 
        "BIG HOSS IS ONLINE, WELCOME TO THE NAM >:o")



@bigHoss.event
async def on_message(message):

    if message.content.startswith('!BigHoss'):
        await bigHoss.send_message(message.channel, 'HEY')
    if message.content.startswith("!NAM"):
        await bigHoss.send_message(message.channel, "SHIT WERE IN THE NAM!!")
    if message.content.startswith("!BirdDog"):
        await bigHoss.send_message(message.channel, "WE WE GOT A NEW GUY TODAY, call em bird dog.")

    if message.content.startswith("!Charlie"):
        await bigHoss.send_message(message.channel, "Get down {0}!, It's charlie!!".format(message.author.mention))
    if message.content.startswith("!Heck"):
        await bigHoss.send_message(message.channel, "Heck,{0}, I don't know if we're ganna make it".format(message.author.mention))


    if message.content.startswith("!CallSeth"):
        server = bigHoss.get_server("247243512519720961")
        seth = server.get_member("192844733746380801")
        await bigHoss.send_message(message.channel, "{0}, you're a lil bich".format(seth.mention))




