#!/usr/bin/python3.7.9
import json
import discord as discord

client = discord.Client()

with open('channels.json', 'r') as jsonFile:
    loadedjsonsettings = json.load(jsonFile)
    jsonFile.close()

@client.event
async def on_message(message):
    if message.content[0:2] == 'h ':
        content = message.content[2:]
        if message.author.bot == False:
            if content.split(' ')[0] == 'add':
                print('kek lmao')
                if not message.channel.category_id in loadedjsonsettings:
                    loadedjsonsettings[message.channel.category_id] = {}
                if not message.channel.id in loadedjsonsettings[message.channel.category_id]:
                    loadedjsonsettings[message.channel.category_id][message.channel.name] = {} 
                with open('channels.json', 'w') as jsonFile:
                    json.dump(loadedjsonsettings, jsonFile, indent=4)
                    jsonFile.close()

client.run(open('./token.txt', 'r').read())