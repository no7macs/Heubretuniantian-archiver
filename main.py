#!/usr/bin/python3.7.9
import json
import os
import requests
from datetime import date
import discord as discord

client = discord.Client()

@client.event
async def on_message(message):
    print(message)
    if message.author.bot == False:
        if message.content[0:2] == 'h ' and  message.author.id in [548571901916610560, 301489793714618368]:
            content = message.content[2:]
            #Adds new channel to archive
            if content.split(' ')[0] == 'add':
                if not os.path.isdir('./content/' + message.channel.name):
                    os.mkdir('./content/' + message.channel.name)
                    await message.channel.send('creating archive and adding past posts')
                    for a in (await message.channel.history().flatten()):
                        print(a.attachments)
                        if a.attachments != []:
                            for b in a.attachments:
                                fileDat = requests.get(b.url)
                                filename = './content/' + message.channel.name + '/' + (date.today().strftime("%Y-%m-%d-%H-%M-%S") if os.path.isfile(b.filename) else b.filename)
                                with open(filename, 'wb') as savedFile:
                                    savedFile.write(fileDat.content)
                                    savedFile.close
                    await message.channel.send('done creating archive')
                else: await message.channel.send('already in archive')  
            #Rebuilds all files
            elif content.split(' ')[0] == 'rebuild':
                #Checks if category exists and if it doesn't creates it
                for a in message.guild.categories:
                    if a.name == 'Heubretuniantian archives': exists=True
                    else: exists=False
                if exists == False:
                    category = await message.guild.create_category('Heubretuniantian archives')
                #Puts all files in the category if it is the category
                for a in message.guild.categories:
                    print(a)
                    if a.name == 'Heubretuniantian archives':
                        for b in os.listdir('content'):
                            for a in category.channels:
                                if a.name in os.listdir('./content/'):
                                    channel = await message.guild.create_text_channel(b, category=a, nsfw=True)
                                else: pass
                            print(channel)
                            for c in os.listdir('./content/' + b):
                                await channel.send(file=discord.File('./content/' + b + '/' + c))
        elif message.author.id in [548571901916610560, 301489793714618368] and message.channel.name in loadedjsonsettings['channels']:
            print(message.attachments)
            print(message.attachments[0].url)
            #saves file
            for a in message.attachments:
                if a != []:
                    fileDat = requests.get(a.url)
                    filename = './content/' + message.channel.name + '/' + (date.today().strftime("%Y-%m-%d-%H-%M-%S") if os.path.isfile(a.filename) else a.filename)
                    with open(filename, 'wb') as savedFile:
                        savedFile.write(fileDat.content)
                        savedFile.close

client.run(open('./token.txt', 'r').read())