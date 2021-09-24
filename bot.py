# -> IMPORT DES MODULES
import os
from sys import stderr, stdout
import discord
from twilio.rest import Client
import shlex
from discord import colour
from discord.ext import commands
import requests
from dotenv import load_dotenv
import json
import subprocess
load_dotenv()


# -> SETUP TWILIO  not required

account_sid = os.environ['TWILIO_SID']
auth_token  = os.environ['TWILIO_TOKEN']

twil = Client(account_sid, auth_token)



# -> SETUP BOT
client = commands.Bot(command_prefix="!")

# -> TOKEN BOT
TOKEN = os.environ.get('TOKEN')

# -> PERSONNALISATION COMMANDE HELP
client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "!help",colour=0xE5E242, description = "```Affiche ce panneau d'aide```")
    em.add_field(name = "!help <arg>", value = "```Affiche l'aide de la commande```")
    em.add_field(name = "!price <arg>", value = "```Affiche la valeur du Token en USD```")
    em.add_field(name = "!blague", value = "```Je vous fait une blague de Chuck Norris```")
    em.add_field(name = "!meteo <arg>", value = "```J'Affiche la météo du lieu sélectionné```")
    em.add_field(name = "!insulte", value = "```Préparez vous pour une insulte fleurie```")
    
    await ctx.send(embed = em)



# -> EXECUTION AU CHARGEMENT DU BOT
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

# -> COMMANDE PURGE DES MESSAGES 
@client.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
   if amount == None:
       await ctx.channel.purge(limit=1000000)
   else:
       await ctx.channel.purge(limit=amount)


# -> RÉCUPÉRATION DES PRIX DEPUIS L'API COINGECKO
@client.command(name='price')
async def arrrprice(ctx, arg):
    
    
    with open('data.json') as file_object:
         data = json.load(file_object)
         for i in range(len(data)): e= print("Coins: ", data[i]["name"])
         print(e)
         re = 0
         re = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={arg}&vs_currencies=usd")
         ret = re.json()
         data = ret
         coin = f"{arg}" in data
         print(coin)
         if coin == True:
               rete = ret[f"{arg}"]
               retex = rete["usd"]
               print(rete)
               await ctx.send(f'```Le {arg} vaut actuellement:  {retex} $```')
         else:
              em = discord.Embed(title = "Error",colour=0x900C2C, description = f"```{arg} N'est pas dans la liste des tokens. Utilisez le nom complet plutôt que le ticker```")    
              await ctx.send(embed = em)


# -> RÉCUPÉRATION D'UNE BLAGUE ALÉATOIRE DE L'API DE CHUCK NORRIS
@client.command(name='blague')
async def blague(ctx):
    re = 0
    re = requests.get("https://api.chucknorris.io/jokes/random")
    ret = re.json()
    rete = ret["value"]
    retex = rete
    print(rete)
    em = discord.Embed(title = "Blague !",colour=0x38A3A5, description = f'```{retex}```')    
    await ctx.send(embed = em)

# -> RÉCUPÉRATION DE LA MÉTÉO EN FONCTION DE L'ARGUMENT
@client.command(name='meteo')
async def meteo(ctx, arg):
    re = 0
    re = requests.get(f"https://api.weatherapi.com/v1/current.json?key=8280fb7707c1498baf281757212409&q={arg}&aqi=no")
    ret = re.json()
    test = str(ret["location"]["name"]) 
    test1 = str(ret["location"]["region"])
    test2 =  str(ret["location"]["country"])
    test3 =  str(ret["current"]["temp_c"])
    await ctx.send(test + " " + test1 + " " + test2 + " " + test3 + " C°")


# ->  INSULTE AVEC INSULTRON 
@client.command(name='insulte')
async def insulte(ctx):
    proc = subprocess.Popen(['./insultron'], stdin=subprocess.PIPE,
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.STDOUT)
   
    with subprocess.Popen(['./insultron'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:   output, errrors = p.communicate()
    lines = output.decode('utf-8')
    em = discord.Embed(title = "Dans Ta Geule !",colour=0x925C2C, description = f"```{lines}```")    
    await ctx.send(embed = em)


# -> NMAP 
@client.command(name='nmap')
async def nmap(ctx, target):
   with subprocess.Popen(['./nmap', f'{target}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as p: output, err = p.communicate()
   lines = output
   em = discord.Embed(title = 'Nmap Scan Results: ',colour=0x985D2C, description= f'```{lines}```')
   await ctx.send(embed = em)   

#  -> FLOOD 
@client.command(name='flood')
async def flood(ctx):
    for i in range(1000): 
        await ctx.send([i])

# -> SMS MON TEL 
@client.command(name='message')
async def message(ctx, to, messages):
    message = twil.messages \
             .create(
                 body=f"{messages}",
                 from_='+19044743902',
                 to=f'{to}'
             )
    print(message.sid)
    await ctx.send(f'```{message.sid}```')
    await ctx.send(f'```envoyé a {to}```')

# ->  LANCEMENT DU BOT
client.run(TOKEN)


