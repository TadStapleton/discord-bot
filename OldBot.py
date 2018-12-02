
import random
import asyncio
import requests
import discord
import time
from collections import Counter
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "NDM5Mjc0MDYxNjk3MTIyMzA2.DcQxYQ.uiK4QCrR_WbkWTX6yE1Y2Hdu2LI01"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

target = "00000000000"

#startup text
@client.event
async def on_ready():
    print("Bot is now running")

@client.event
async def on_member_join(member):

    general = client.get_channel("439251606333030414")
    balanced = discord.utils.get(member.server.roles, name="Balanced")

    await client.add_roles(member, balanced)

    await client.send_message(general, "Hey " + member.display_name + " thanks for joining the server! You have been given the Balanced role by default. Type '!Optional Roles' to check out some of the extra roles on the server.")

@client.event
async def on_message(message):

    global target

    if message.author.id != "439274061697122306":



    #  if "youtu" and "." in message.content and message.channel.id != "439268035422060544":

    #            videos = client.get_channel("439268035422060544")
    #            await client.delete_message(message)
    #            await client.send_message(videos, "This video was posted by " + message.author.nick)
    #            await client.send_message(videos, message.content)






        if "!Iam 18+" in message.content:

            eightteen = discord.utils.get(message.author.server.roles, name="18+")

            age = discord.utils.get(message.author.server.roles, name="<<<<<<<Age>>>>>>>")

            await client.add_roles(message.author, age, eightteen)

            await client.send_message(message.channel, "role added")

        if "!Iam Under 18" in message.content:

            undereightteen = discord.utils.get(message.author.server.roles, name="Under 18")

            age = discord.utils.get(message.author.server.roles, name="<<<<<<<Age>>>>>>>")

            await client.add_roles(message.author, age, undereightteen)

            await client.send_message(message.channel, "role added")

        if "!Iam Left" in message.content:

            left = discord.utils.get(message.author.server.roles, name="Left")

            politics = discord.utils.get(message.author.server.roles, name="<<<<<<<Politics>>>>>>>")

            await client.add_roles(message.author, politics, left)

            await client.send_message(message.channel, "role added")

        if "!Iam Center" in message.content:

            Center = discord.utils.get(message.author.server.roles, name="Center")

            politics = discord.utils.get(message.author.server.roles, name="<<<<<<<Politics>>>>>>>")

            await client.add_roles(message.author, politics, Center)

            await client.send_message(message.channel, "role added")

        if "!Iam Right" in message.content:

            right = discord.utils.get(message.author.server.roles, name="Right")

            politics = discord.utils.get(message.author.server.roles, name="<<<<<<<Politics>>>>>>>")

            await client.add_roles(message.author, politics, right)

            await client.send_message(message.channel, "role added")

        if "!Iam He/Him" in message.content:

            he = discord.utils.get(message.author.server.roles, name="He/Him")

            pro = discord.utils.get(message.author.server.roles, name="<<<<<<<Pronouns>>>>>>>")

            await client.add_roles(message.author, pro, he)

            await client.send_message(message.channel, "role added")

        if "!Iam She/Her" in message.content:

            she = discord.utils.get(message.author.server.roles, name="She/Her")

            pro = discord.utils.get(message.author.server.roles, name="<<<<<<<Pronouns>>>>>>>")

            await client.add_roles(message.author, pro, she)

            await client.send_message(message.channel, "role added")

        if "!Iam They/Them" in message.content:

            they = discord.utils.get(message.author.server.roles, name="They/Them")

            pro = discord.utils.get(message.author.server.roles, name="<<<<<<<Pronouns>>>>>>>")

            await client.add_roles(message.author, pro, they)

            await client.send_message(message.channel, "role added")

        if "!Iamnot 18+" in message.content:

            eightteen = discord.utils.get(message.author.server.roles, name="18+")

            age = discord.utils.get(message.author.server.roles, name="<<<<<<<Age>>>>>>>")

            await client.remove_roles(message.author, age, eightteen)

            await client.send_message(message.channel, "role removed")

        if "!Iamnot Under 18" in message.content:

            undereightteen = discord.utils.get(message.author.server.roles, name="Under 18")

            age = discord.utils.get(message.author.server.roles, name="<<<<<<<Age>>>>>>>")

            await client.remove_roles(message.author, age, undereightteen)

            await client.send_message(message.channel, "role removed")

        if "!Iamnot Left" in message.content:

            left = discord.utils.get(message.author.server.roles, name="Left")

            politics = discord.utils.get(message.author.server.roles, name="<<<<<<<Politics>>>>>>>")

            await client.remove_roles(message.author, politics, left)

            await client.send_message(message.channel, "role removed")

        if "!Iamnot Center" in message.content:

            Center = discord.utils.get(message.author.server.roles, name="Center")

            politics = discord.utils.get(message.author.server.roles, name="<<<<<<<Politics>>>>>>>")

            await client.remove_roles(message.author, politics, Center)

            await client.send_message(message.channel, "role removed")

        if "!Iamnot Right" in message.content:

            right = discord.utils.get(message.author.server.roles, name="Right")

            politics = discord.utils.get(message.author.server.roles, name="<<<<<<<Politics>>>>>>>")

            await client.remove_roles(message.author, politics, right)

            await client.send_message(message.channel, "role removed")

        if "!Iamnot He/Him" in message.content:

            he = discord.utils.get(message.author.server.roles, name="He/Him")

            pro = discord.utils.get(message.author.server.roles, name="<<<<<<<Pronouns>>>>>>>")

            await client.remove_roles(message.author, pro, he)

            await client.send_message(message.channel, "role removed")

        if "!Iamnot She/Her" in message.content:

            she = discord.utils.get(message.author.server.roles, name="She/Her")

            pro = discord.utils.get(message.author.server.roles, name="<<<<<<<Pronouns>>>>>>>")

            await client.remove_roles(message.author, pro, she)

            await client.send_message(message.channel, "role removed")

        if "!Iamnot They/Them" in message.content:

            they = discord.utils.get(message.author.server.roles, name="They/Them")

            pro = discord.utils.get(message.author.server.roles, name="<<<<<<<Pronouns>>>>>>>")

            await client.remove_roles(message.author, pro, they)

            await client.send_message(message.channel, "role removed")



        if "fag" in message.content.lower():

            await client.delete_message(message)

        if "nigger" in message.content:

            await client.delete_message(message)

        if "alexa kill this clown" in message.content.lower():

            if message.author.id == "117456270859960322" :

                await client.kick(target)
                await client.send_message(message.channel, "bye bye")

            if message.author.id ==  "258081755158937610":

                await client.kick(target)
                await client.send_message(message.channel, "bye bye")

        if "!Optional Roles" in message.content.lower():

            emb = (discord.Embed(description="```\nOptional Roles: \n<<<<<<<Age>>>>>>> \n18+ \nUnder 18 \n<<<<<<<Politics>>>>>>> \nLeft \nCenter \nRight \n<<<<<<<Pronouns>>>>>>> \nHe/Him \nShe/Her \nThey/Them``` \n \nType !Iam <role> to add a role \nType !Iamnot <role> to remove it", color=0xfb4654))

            await client.send_message(message.channel, embed=emb)


        target = message.author


    print(message.author.display_name + ", channel: " + message.channel.name + ", content: " + message.content)


client.run(TOKEN)
