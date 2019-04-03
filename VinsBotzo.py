import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name="Making a bot"))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if "mij niet bellen" in message.content.lower():
		await client.send_message(message.channel, "OK :telephone:")

@client.event
async def on_message_delete(message):
	if message.author == client.user:
		return
	else:
		await client.send_message(message.channel, "%s said: %s" %(message.author, message.content))

@client.event
async def on_member_update(before, after):
	#if before.status == offline & after.status == online:
	channel = discord.utils.get(client.get_all_channels(), name='general')
	if channel:
		print('{}: {}'.format(channel.name, channel.id))
		fmt = '{0.mention} is now {0.status}.'
		await client.send_message(channel, fmt.format(after))

client.run("NTYzMTE4MDY5NTg1Njc0MjUw.XKUsvw.ChE2gGyba20FfKv6g1eiyC9zIJE")
