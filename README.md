# python-discord-coin_gecko



# python-discord-coingecko

# Pour run le bot, dans votre terminal saissisez

npx nodemon --exec "clear;python3" bot.py
##### Dans un premier temps créer un environnement 

python3.8 -m venv .env
## ATTENTION
##### Linux risque de vous demander d'installer venv

apt install python3.8-venv
##### Il faut donc relancer la commande pour créer l'environnement

##### Activer en sourçant

source .env/bin/activate
##### Pour l'utilisation de l'API de Discord, on installe discord.py avec pip

pip install -U discord.py
##### Après cela, il faut se rendre sur le portail des développeurs de discord
https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications

##### Il est très facile de trouver ce lien par vous-mêmes

##### Cliquer sur New Application et donner un nom à votre application

##### Aller dans l'onglet Bot et cliquer sur 'Add Bot' pour créer le bot dans l'application

## Ajouter le bot à un serveur
##### pour l'inviter sur votre serveur, il faut générer une URL d'authorisation avec OAuth2

##### Cliquer sur l'onglet OAuth2, cochez la case 'bot' et donnez lui les permissions que vous voulez
##### Ensuite, copiez l'URL générée et accédez-y depuis un nouvel onglet, vous permettant d'ajouter le bot aux serveurs dont vous disposez des droits suffissants

##### Sélectionnez votre serveur et appuyez sur continuer, là vous devrez valider les droits que vous voulez donner au bot > cliquer sur 'Autoriser'

## Maintenant vous devez voir votre bot sur votre serveur

# Connexion du BOT

init dev
