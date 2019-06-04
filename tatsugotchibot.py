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
            

@client.command()
async def ping():
    await client.say('Pong!')


@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        color = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='**-ping**', value='Returns Pong!', inline=False)
    
    embed.add_field(name='**-say <string>**', value='Tells the bot to say something.', inline=False)
    

    await client.say(embed=embed) #send_message(author, embed=embed)

@client.command()
async def enable():
    global enabled
    if enabled == "false":
        enabled = "true"
        await client.say("Timer is now enabled!")
    else:
        await client.say("Timer is already enabled!")

@client.command()
async def disable():
    global enabled
    if enabled == "true":
        enabled = "false"
        await client.say("Timer is now disabled!")
    else:
        await client.say("Timer is already disabled!")


@client.command(pass_context=True)
async def tg(ctx, *train):
    global enabled
    if enabled == "true":
        tgstr = ''
        for word in train:
            tgstr += word
        #await client.say(tgstr)
        if tgstr == 'train':
            ran = random.randint(140,200)/10
            time.sleep(ran)
            await client.say("Training is available! <@{}>".format(ctx.message.author.id))
            
        if tgstr == 'feed':
            await client.say("I will remind you to feed your pet in 8 hours!")
            time.sleep(28800)
            await client.say("You should feed your pet! <@{}>".format(ctx.message.author.id))
            
        if tgstr == 'clean':
            await client.say("I will remind you to clean after your pet in 8 hours!")
            time.sleep(28800)
            await client.say("You should clean after your pet! <@{}>".format(ctx.message.author.id))
            
        if tgstr == 'play':
            await client.say("I will remind you to play with your pet in 8 hours!")
            time.sleep(28800)
            await client.say("You should play with your pet! <@{}>".format(ctx.message.author.id))
        

@client.command()
async def say(*args):
    output = ' '
    for word in args:
        output += word
        output += ' '
    await client.say(output)
    
    
    
client.loop.create_task(change_status())
client.run(os.environ['BOT_TOKEN'])    
