import discord
from discord import app_commands


client = discord.Client(intents=discord.Intents.all())
token = open('token.txt', 'r').read()


@client.event
async def on_ready():
    await app_commands.CommandTree(client).sync()
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


client.run(token)
