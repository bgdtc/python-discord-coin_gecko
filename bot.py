from logging import error
import os
import discord
from discord import colour
from discord.ext import commands
import requests
from dotenv import load_dotenv
import json
load_dotenv()


client = commands.Bot(command_prefix="!")

# print(os.environ.get('TOKEN'))
TOKEN = os.environ.get('TOKEN')


client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "!help",colour=0xE5E242, description = "```Affiche ce panneau d'aide```")
    em.add_field(name = "!help <arg>", value = "```Affiche l'aide de la commande```")
    em.add_field(name = "!price <arg>", value = "```Affiche la valeur du Token en USD```")
    em.add_field(name = "!blague", value = "```Je vous fait une blague de Chuck Norris```")
    
    await ctx.send(embed = em)




@client.event 
async def on_ready():

    print(f'{client.user} connecté')
    r = requests.get("https://api.coingecko.com/api/v3/coins/list")
    re = json.loads(r.text)

    ret =  re                                                                                                   
    jsonString = json.dumps(ret)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
@client.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
   if amount == None:
       await ctx.channel.purge(limit=1000000)
   else:
       await ctx.channel.purge(limit=amount)



@client.command(name='price')
async def arrrprice(ctx, arg):
    
    
    with open('data.json') as file_object:
         data = json.load(file_object)
         for i in range(len(data)): e= print("Coins: ", data[i]["name"])
         print(e)
    
    
    # for i in range(len(ret)): e =  print("Notation: ","coins: ", r.json()[i]["name"], "| |","Symboles: ", r.json()[i]["symbol"])
    # json.dump(e, "monfichier.json")
         re = 0
         re = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={arg}&vs_currencies=usd")
         ret = re.json()
    # if (arg in data  ):
    #     print("error")
    #     await ctx.send("error")
    #     await ctx.send("voici la liste des tokens: ")
    #     for i in range(len(data)): await ctx.send(f'```{data[i]["name"]}```')
        
    # else:
         data = ret
         coin = f"{arg}" in data
         print(coin)
         if coin == True:
               rete = ret[f"{arg}"]
               retex = rete["usd"]
               print(rete)
               await ctx.send(f'```Le {arg} vaut actuellement:  {retex} $```')
         else:
             await ctx.send(f'{arg} n\'est pas dans la liste des Tokens (utilisez le nom complet et non le ticker )')
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


