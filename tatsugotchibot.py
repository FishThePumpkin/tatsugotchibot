import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
from random import *
import os

client = commands.Bot(command_prefix = "-")
client.remove_command('help')
status = ['COONS','COOOOONS']

coons = [":1_:",":2_:",":3_:",":4_:",":5_:",":6_:",":7_:",":8_:",":7_:",":8_:",":9_:",":10:",":11:",":12:"]

coonsdict = {
  ":1_:": "585367557674893313",
  ":2_:": "585369785446039572",
  ":3_:": "585369809395384320",
  ":4_:": "585369829826101248",
  ":5_:": "585369847974723584",
  ":6_:": "585369865632612352",
  ":7_:": "585369881885802497",
  ":8_:": "585369903851241482",
  ":9_:": "585369922922741760",
  ":10:": "585369941545451530",
  ":11:": "585369960646443018",
  ":12:": "585369979638251524"
}

async def get_reaction(message,i):
    index = randint(0,len(reactionsdict[inmsg[i]]) - 1)
    try:
       await client.add_reaction(message,reactionsdict[inmsg[i]][index])
    except:
        if message.content.find('EMOJI_NAME'):
            for x in client.get_all_emojis():
                if x.id == reactionsdict[inmsg[i]][index]:
                    await client.add_reaction(message, x)
           
        

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(2)
#

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Online!'))
    print("Bot is ready")
    
    
@client.event
async def on_message(message):
    mess = message.content.lower()
    auth = message.author
    rnd = randint(0,100)
    if not auth.id == "585341561345409044":
        if rnd in range(10):
            rnd = randint(0,len(coonsdict) - 1)
            if message.content.find('EMOJI_NAME'):
                for x in client.get_all_emojis():
                    if x.id == coonsdict[coons[rnd]]:
                        await client.add_reaction(message, x)
        if "hi" in mess:
            await client.send_message(message.channel, "hi")
            


    
    
    
client.loop.create_task(change_status())
client.run(os.environ['BOT_TOKEN'])    
