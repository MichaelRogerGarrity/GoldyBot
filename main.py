import discord
import os
import requests
import json
import random
import pip
import youtube_dl
import contextvars
import asyncio
import functools
import itertools
from replit import db
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


name = contextvars.ContextVar("name", default = 'Hello')
client = discord.Client()


sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing", "tilted"]

starter_encouragements = ["Cheer up buddy!", "Hang in there.", "You are better than you believe."]

if "responding" not in db.keys():
  db["responding"] = True

# Will get a random inspirational quote from the ZenQuotes API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_bitcoin():
  URL = "https://api.coindesk.com/v1/bpi/currentprice/CNY.json"
  r = requests.get(URL)
  data = r.json()
  price = data['bpi']['USD']['rate']
  return(price)

def get_joke():
  url = "https://joke3.p.rapidapi.com/v1/joke"

  querystring = {"nsfw":"true"}

  headers = {
  'x-rapidapi-key': "6bedbb7641msh96d615409cbcf1ap1dbc38jsn0e716cabbbee",
  'x-rapidapi-host': "joke3.p.rapidapi.com"
  }
  response = requests.get(url, headers=headers, params=querystring)
  response = response.json()
  response = response['content']
  return(response)

def get_meme():
  url = "https://some-random-api.ml/meme"

  response = requests.get(url)
  response = response.json()
  response = response['image']
  return(response)

def get_wink():
  url = "https://some-random-api.ml/animu/wink"

  response = requests.get(url)
  response = response.json()
  response = response['link']
  return(response)

def get_pat():
  url = "https://some-random-api.ml/animu/pat"

  response = requests.get(url)
  response = response.json()
  response = response['link']
  return(response)

def get_koala():
  url = "https://some-random-api.ml/img/koala"

  response = requests.get(url)
  response = response.json()
  response = response['link']
  return(response)

def get_fox():
  url = "https://some-random-api.ml/img/fox"

  response = requests.get(url)
  response = response.json()
  response = response['link']
  return(response)

def get_bird():
  url = "https://some-random-api.ml/img/birb"

  response = requests.get(url)
  response = response.json()
  response = response['link']
  return(response)

def get_panda():
  url = "https://some-random-api.ml/img/panda"

  response = requests.get(url)
  response = response.json()
  response = response['link']
  return(response)

def get_cat():
  url = "https://some-random-api.ml/img/cat"

  response = requests.get(url)
  response = response.json()
  response = response['link']
  return(response)  

def get_pikachu():
  url = "https://some-random-api.ml/img/pikachu"

  response = requests.get(url)
  response = response.json()
  response = response['link']
  return(response)  

def get_kanye():
  URL = "https://api.kanye.rest"
  r = requests.get(URL)
  data = r.json()
  quote = data['quote']
  return(quote)

# Will return the name of an anime based off a screenshot from said anime using trace.moe API
def get_anime_name(image):
  url = "https://trace.moe/api/search?url=" + image
  response = requests.get(url) 
  json_data = json.loads(response.text)
  anime_name = json_data['docs'][0]['title_english']
  anime_name = str(anime_name)
  return(anime_name)

# Will return the episode of the anime in which the screenshot appeared, once again with trace.moe API
def get_anime_episode(image):
  url = "https://trace.moe/api/search?url=" + image
  response = requests.get("https://trace.moe/api/search?url=" + image) 
  json_data = json.loads(response.text)
  anime_episode = json_data['docs'][0]['episode']
  anime_episode = str(anime_episode)
  return(anime_episode)


def get_dog():
  URL = "https://dog.ceo/api/breeds/image/random"
  r = requests.get(URL)
  data = r.json()
  image = data['message']
  return(image)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if msg.startswith('$duffy'):
    await message.channel.send('oo aa oo aa')
  
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new encouragement"):
    encouraging_message = msg.split("$new encouragement ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del encouragement"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del encouragement",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list encouragements"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is now enabled.")

    else:
      db["responding"] = False
      await message.channel.send("Responding is now disabled.")
  
  if msg.startswith("$search anime"):
    image = msg.split("$search anime ",1)[1]
    anime_name = get_anime_name(image)
    anime_episode = get_anime_episode(image)
    await message.channel.send("This image is from episode " + anime_episode + " of " + anime_name +"!")
    
  if msg.startswith("$kanye"):
    quote = get_kanye()
    await message.channel.send("\""+quote+"\" - Kanye West")
  
  if msg.startswith("$dog"):
    image = get_dog()
    await message.channel.send(image)
  
  if msg.startswith("$bitcoin"):
    price = get_bitcoin()
    await message.channel.send("One Bitcoin is currently worth $"+price)
  
  #if msg.startswith("$joke"):
  #  joke = get_joke()
  #  await message.channel.send(joke)

  if msg.startswith('$monke'):
    await message.channel.send('monke')

  if msg.startswith("$meme"):
    meme = get_meme()
    await message.channel.send(meme)

  if msg.startswith("$wink"):
    wink = get_wink()
    await message.channel.send(wink)

  if msg.startswith("$pat"):
    meme = get_pat()
    await message.channel.send(meme)

  if msg.startswith("$koala"):
    meme = get_koala()
    await message.channel.send(meme)

  if msg.startswith("$fox"):
    meme = get_fox()
    await message.channel.send(meme)

  if msg.startswith("$bird"):
    meme = get_bird()
    await message.channel.send(meme)

  if msg.startswith("$panda"):
    meme = get_panda()
    await message.channel.send(meme)

  if msg.startswith("$cat"):
    meme = get_cat()
    await message.channel.send(meme)

  if msg.startswith("$pikachu"):
    meme = get_pikachu()
    await message.channel.send(meme)

  if msg.startswith("$help"):
    await message.channel.send("Command List:\n$duffy - Monkey time\n$monke - Monke time\n$inspire - Randomly chosen inspirational quote\n$search anime [link to image] - Identifies the name of the anime and episode in which a screenshot appeared\n$kanye - Returns a random Kanye quote/tweet\n$dog - Returns a randomly chosen picture of a dog\n$bitcoin - Returns the current value of one bitcoin in USD\n$joke - Returns a randomly generated joke\n$meme - Returns a randomly chosen meme\n$wink - Returns a randomly chosen anime wink gif\n$pat - Returns a randomly chosen anime headpat gif\n$koala - Returns a randomly chosen image of a koala\n$fox - Returns a randomly chosen image of a fox\n$bird - Returns a randomly chosen image of a bird\n$panda - Returns a randomly chosen image of a panda\n$cat - Returns a randomly chosen image of a cat\n$pikachu - Returns a randomly chosen gif of Pikachu\n$yes - No\n$no - Yes\n$sus - Among Us")

  if msg.startswith("$no"):
    await message.channel.send("Yes")

  if msg.startswith("$yes"):
    await message.channel.send("No")  

  if msg.startswith("$sus"):
    await message.channel.send("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣻⣯⣽⣟⠿⠟⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⡿⣫⣾⣿⣿⣿⡹⢁⣴⣷⣿⣿⣷⣆⣤⡀⠠⢬⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⢱⣿⣿⣿⠿⠩⢠⣿⣿⣿⣿⣿⣏⣿⢸⣿⡖⣄⠹⣷⡌⢿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⡸⣿⣿⣿⣼⠂⢸⣿⣿⣾⠯⢟⠋⠿⣿⡿⣳⡿⣳⣿⣷⡈⢿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣷⣌⡻⣿⢡⣿⡀⢻⣿⣿⣷⣭⣯⡆⢰⣤⣥⣶⣿⣿⣿⣷⠈⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣤⡈⠛⠛⠙⠛⠁⣸⣿⣿⣿⣿⣿⡿⠉⣤⣤⡉⢻⣿⣿ \n⣿⣿⣿⣿⣿⠿⠛⢋⣉⣁⣈⣉⣀⣈⣉⣉⣉⣁⡐⠚⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡀⢿⣿ \n⣿⣿⣿⠏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⢿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡇⢸⣿ \n⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡇⢸⣿ \n⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠇⣸⣿ \n⣿⣿⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣧⡈⠛⠿⠋⢠⣿⣿ \n⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣾⣿⣿⣿ \n⣿⣿⣿⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿ \n⣿⣿⣿⣆⠘⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿ \n⣿⣿⣿⠋⣠⣶⣶⣶⣶⣶⣶⠂⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿ \n⣿⣿⠃⣰⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⣿⣿⣿⣿ \n⣿⡏⠀⣿⣿⣿⣿⣿⣿⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿ \n⣿⣇⠀⣿⣿⣿⣿⣿⣿⣿⣧⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⣿⣿⣿ \n⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⣿⣆⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣿⣿⣿ \n⣿⣿⣷⣄⠙⠿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿ \n⣿⣿⣿⣿⣷⡄⢀⣉⣩⣿⣿⣿⠋⢠⣄⣀⣀⣀⣀⡀⢶⣿⣿⣿⣿⣿⣿⣿⣿⡏⢁⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣧⠈⣿⣿⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣷⡈⠻⣿⣿⣿⣿⣿⣿⡿⢁⣼⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣆⠘⣿⣿⡿⠃⣰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠉⠛⠻⠿⠏⣠⣾⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣦⣈⠉⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿")

  
  
  
    


keep_alive()
client.run(os.getenv('TOKEN'))