import os
import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import json
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
    ret = re.json()
    rete = ret["bitcoin"]
    retex = rete["usd"]
    print(rete)
    await ctx.send(f'```Le bitcoin vaut actuellement:  {retex} $```')


@client.command(name='arrr_price')
async def arrrprice(ctx):
    re = 0
    re = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=pirate-chain&vs_currencies=usd")
    ret = re.json()
    rete = ret["pirate-chain"]
    retex = rete["usd"]
    print(rete)
    await ctx.send(f'```Le ARRR vaut actuellement:  {retex} $```')

@client.command(name='blague')
async def blague(ctx):
    re = 0
    re = requests.get("https://api.chucknorris.io/jokes/random")
    ret = re.json()
    rete = ret["value"]
    retex = rete
    print(rete)
    await ctx.send(f'```{retex}```')

@client.command(name='trad')
async def trad(ctx):
    payload = "[{\"Text\": \"I would really like to drive your car around the block a few times.\"}]"
    querystring = {"api-version":"3.0","to":"french","textType":"plain","profanityAction":"NoAction"}
    headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com",
    'x-rapidapi-key': "undefined"
    }
    re = 0
    re = requests.post("https://microsoft-translator-text.p.rapidapi.com/translate",data=payload, headers=headers, params=querystring)
    ret = re.json()
    rete = ret
    retex = rete
    retexe = requests.post(f'https://context.reverso.net/traduction/anglais-francais/{retex}')
    retexex = retexe.text
    retexexe = retexex 

    await ctx.send(f'```{retexexe}```')








client.run(TOKEN)


