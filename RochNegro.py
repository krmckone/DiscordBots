
import discord
import asyncio

newClient = discord.Client()

@newClient.event
async def on_ready():
    print('Logged in as')
    print(newClient.user.name)
    print(newClient.user.id)
    print('------')

@newClient.event
async def on_message(message):
    if message.content.startswith('Is josh a negro?'):
        await newClient.send_message(message.channel, 'Yes!')
    if message.content.startswith("How big of a negro is he?"):
        await newClient.send_message(message.channel, "He's a big 'ol freakin negro")
    if message.content.startswith("Who is the fuklur?"):
        await newClient.send_message(message.channel, "NATE IS THE FUKLUR!")

newClient.run('MzM0MTQ0MjE4NjA2MDc1OTA2.DEXMgA.fuVHIdSqKhPv6lj3sIkrcLNZciQ')