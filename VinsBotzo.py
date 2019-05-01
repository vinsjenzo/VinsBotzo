import discord
import logging
import os
import random 

access_token= os.environ["ACCESS_TOKEN"]

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


gameNames = ["Making a bot", "Fixing chiemies", "Smoking some dank weed", "Popping a molly", "Making some dinner", "Banging your mom"]

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(f"""Discord.py version {discord.__version__}""")
    await client.change_presence(game=discord.Game(name="Making a bot"))
    
##@client.event
##async def on_server_join(server):
##    channel = discord.utils.get(server.channels, name='status-reports')
##    if channel:
##        return
##    else:
##        await client.create_channel(server, 'status-reports', type=discord.ChannelType.text)

@client.event 
async def on_typing(channel, user, when):
    await client.change_presence(game=discord.Game(name=random.choice(gameNames)))
	
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "mij niet bellen" in message.content.lower():
        await client.send_message(message.channel, "OK BRUUR :telephone:")
    if message.author.id == "390555869273915394":
        await client.send_message(message.channel, "Kk bek houde rick!")
    if message.author.id == "250738667772051460":
        await client.send_message(message.channel, "Diëgo ga mannen pijpen, pijpsletje!")
    

##@client.event
##async def on_message_delete(message):
##    if message.author == client.user:
##        return
##    else:
##        await client.send_message(message.channel, "%s said: %s" %(message.author, message.content))
##
##@client.event
##async def on_member_update(before, after):
##    #if before.status == offline & after.status == online:
##    channel = discord.utils.get(after.server.channels, name='status-reports')
##    if channel:
##        print('{}: {}'.format(channel.name, channel.id))
##        fmt = '{0.mention} is now {0.status}.'
##        await client.send_message(channel, fmt.format(after))

client.run(access_token)
