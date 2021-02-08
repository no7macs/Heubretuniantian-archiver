#!/usr/bin/python3.7.9
import json
import os
import requests
from datetime import date
import discord as discord

client = discord.Client()

with open('channels.json', 'r') as jsonFile:
    loadedjsonsettings = json.load(jsonFile)
    jsonFile.close()

@client.event
async def on_message(message):
    if message.author.bot == False:
        if message.content[0:2] == 'h ':
            content = message.content[2:]
            #Adds new channel to archive
            if content.split(' ')[0] == 'add':
                print('kek lmao')
                if not os.path.isdir('./contents/' + message.channel.name):
                    os.mkdir('./content/' + message.channel.name)
            #Rebuilds all files
            elif content.split(' ')[0] == 'rebuild':
                #Checks if category exists and if it doesn't creates it
                for a in message.guild.categories:
                    if a.name == 'Heubretuniantian archives': exists=True
                    else: exists=False
                if exists == False:
                    await message.guild.create_category('Heubretuniantian archives')
                #Puts all files in the category if it is the category
                for a in message.guild.categories:
                    print(a)
                    if a.name == 'Heubretuniantian archives':
                        for b in os.listdir('content'):
                            await message.guild.create_text_channel(b, category=a, nsfw=True)
        elif message.author.id in [548571901916610560] and message.channel.name in loadedjsonsettings['channels']:
            print(message.attachments)
            print(message.attachments[0].url)
            #saves file
            for a in message.attachments:
                fileDat = requests.get(a.url)
                filename = './content/' + message.channel.name + '/' + (date.today().strftime("%Y-%m-%d-%H-%M-%S") if os.path.isfile(a.filename) else a.filename)
                with open(filename, 'wb') as savedFile:
                    savedFile.write(fileDat.content)
                    savedFile.close

client.run(open('./token.txt', 'r').read())