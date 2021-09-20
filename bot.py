import os
import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
load_dotenv()


client = commands.Bot(command_prefix="!")

# print(os.environ.get('TOKEN'))
TOKEN = os.environ.get('TOKEN')

# client = discord.Client()


@client.event 
async def on_ready():
    print(f'{client.user} connecté')

@client.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
   if amount == None:
       await ctx.channel.purge(limit=1000000)
   else:
       await ctx.channel.purge(limit=amount)

@client.command(name='btc_price')
async def btcprice(ctx):
    re = 0
    re = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    ret = re.text
    await ctx.send(ret)
client.run(TOKEN)

