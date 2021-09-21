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
arrr = "pirate-chain"
btc = "bitcoin"

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



@client.command(name='price')
async def arrrprice(ctx, arg):
    
    r = requests.get("https://api.coingecko.com/api/v3/coins/list")
    re = json.loads(r.text)
    ret =  re                                                                                                   
    jsonString = json.dumps(ret)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    if not arg: 
        print("pas arg")
    # for i in range(len(ret)): e =  print("Notation: ","coins: ", r.json()[i]["name"], "| |","Symboles: ", r.json()[i]["symbol"])
    # json.dump(e, "monfichier.json")
    re = 0
    re = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={arg}&vs_currencies=usd")
    ret = re.json()
    rete = ret[f"{arg}"]
    retex = rete["usd"]
    print(rete)
    await ctx.send(f'```Le {arg} vaut actuellement:  {retex} $```')

@client.command(name='blague')
async def blague(ctx):
    re = 0
    re = requests.get("https://api.chucknorris.io/jokes/random")
    ret = re.json()
    rete = ret["value"]
    retex = rete
    print(rete)
    await ctx.send(f'```{retex}```')









client.run(TOKEN)


