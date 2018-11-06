import discord
from time import localtime, strftime
import asyncio

TOKEN = 'XXXXXXXXXXXXXX'

client = discord.Client()

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='Working Hard'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='Super Buggy'))
        await asyncio.sleep(5)

async def time_task():
    while True:
        hours = int(strftime("%H", localtime()))
        minutes = int(strftime("%M", localtime()))
        seconds = int(strftime("%S", localtime()))
        if minutes == 0 and seconds == 0:
            if hours >= 12:
                await client.send_message(discord.Object(id='445036133961826315'), "The hour is: " + strftime("%H", localtime()) + " PM")
            else:
                await client.send_message(discord.Object(id='445036133961826315'), "The hour is: " + strftime("%H", localtime()) + " AM")
        await asyncio.sleep(1)

@client.event
async def on_ready():
    print('Bot is running')
    client.loop.create_task(time_task())
    client.loop.create_task(status_task())

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if "!optional roles" in message.content.lower():
        await client.send_message(message.channel, "The Automod that handles role changes is currently offline, sorry!")
        return
    if "!iam" in message.content.lower():
        await client.send_message(message.channel, "The Automod that handles role changes is currently offline, sorry!")
    if "!time" in message.content.lower():
        hours = strftime("%H", localtime())
        minutes = strftime("%M", localtime())
        seconds = strftime("%S", localtime())
        await client.send_message(message.channel, "The time is: " + hours + ":" + minutes + ":" + seconds)
    if "!tester" in message.content.lower():
        hours = int(strftime("%H", localtime()))
        if hours >= 12:
            await client.send_message(discord.Object(id='445036133961826315'), "The hour is: " + strftime("%H", localtime()) + " PM")
        else:
            await client.send_message(discord.Object(id='445036133961826315'), "The hour is: " + strftime("%H", localtime()) + " AM")

@client.event
async def on_member_join(member):
    print("test")
    role = discord.utils.get(member.server.roles, id="439252203950178304")
    await client.add_roles(member, role)
    mention = member.mention
    msg = "Hello " + mention + "welcome to the server! You\'ve been given the balanced role by default."
    await client.send_message(discord.Object(id='439251606333030414'), msg)

client.run(TOKEN)
