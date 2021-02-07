#!/usr/bin/python3.7.9
import json
import os
import requests
import time
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
            if content.split(' ')[0] == 'add':
                print('kek lmao')
                if not 'channels' in loadedjsonsettings:
                    loadedjsonsettings['channels'] = []
                if not message.channel.id in loadedjsonsettings['channels']:
                    loadedjsonsettings['channels'].append(message.channel.name)
                    os.mkdir('./content/' + message.channel.name)
                with open('channels.json', 'w') as jsonFile:
                    json.dump(loadedjsonsettings, jsonFile, indent=4)
                    jsonFile.close()
        elif message.author.id in [548571901916610560] and message.channel.name in loadedjsonsettings['channels']:
            print(message.attachments)
            #saves file
            fileDat = requests.get(message.attachments.url)
            with open('./contents/' + message.channel.name + '/' + (strftime("%Y-%m-%d-%H-%M-%S", gmtime() if os.path.isfile(message.attachments.filename) else message.attachments.filename)), 'wb') as savedFile:
                savedFile.write(fileDat.contents)
                savedFile.close

client.run(open('./token.txt', 'r').read())