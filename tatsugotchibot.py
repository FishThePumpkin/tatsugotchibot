import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
import os

enabled = False

client = commands.Bot(command_prefix = "-")
client.remove_command('help')
status = ['Cat\'s', 'voice', 'is', 'so', 'nice', 'owo']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(2)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Online!'))
    print("Bot is ready")

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


@client.command(pass_context=True)
async def tg(ctx, *train):
    tgstr = ''
    for word in train:
        tgstr += word
    #await client.say(tgstr)
    if tgstr == 'train':
        ran = random.randint(110,200)/10
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

@client.command()
async def enable():
    if enabled == False:
        enabled = True
        await client.say("Timer is now enabled!")
    else:
        await client.say("Timer is already enabled!")

@client.command()
async def disable():
    if enabled == True:
        enabled = False
        await client.say("Timer is now disabled!")
    else:
        await client.say("Timer is already disabled!")
    
    
    
client.loop.create_task(change_status())
client.run(os.environ['BOT_TOKEN'])    
