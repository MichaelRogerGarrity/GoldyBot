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
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix='$')

req = requests.get("https://discord.com/api/path/to/the/endpoint")
print(req)

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
  response = requests.get(url) 
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




@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='duffy', help='Monkey time')
async def duffy(ctx):
  response = 'oo aa oo aa'
  await ctx.send(response)

@bot.command(name='inspire', help='Randomly chosen inspirational quote')
async def inspire(ctx):
  response = get_quote()
  await ctx.send(response)

@bot.command(name='anime', help='When used as "$anime URL" with a link to an image, it will identify the source anime and episode for that image')
async def anime(ctx, URL):
  anime_name = get_anime_name(URL)
  anime_episode = get_anime_episode(URL)
  await ctx.send("This image is from episode " + anime_episode + " of " + anime_name +"!")

@bot.command(name='kanye', help='Returns a random Kanye West quote/Tweet')
async def kanye(ctx):
  response = get_kanye()
  await ctx.send("\""+response+"\" - Kanye West")

@bot.command(name='dog', help='Returns a randomly chosen picture of a dog')
async def dog(ctx):
  response = get_dog()
  await ctx.send(response)

@bot.command(name='bitcoin', help='Returns the current value of bitcoin in USD')
async def bitcoin(ctx):
  response = get_bitcoin()
  await ctx.send("One Bitcoin is currently worth $"+response)

@bot.command(name='monke', help='Monke time')
async def monke(ctx):
  await ctx.send('monke')

@bot.command(name='meme', help='Returns a randomly chosen meme')
async def meme(ctx):
  response = get_meme()
  await ctx.send(response)

@bot.command(name='wink', help='Returns a randomly chosen anime wink gif')
async def wink(ctx):
  response = get_wink()
  await ctx.send(response)

@bot.command(name='pat', help='Returns a randomly chosen anime headpat gif')
async def pat(ctx):
  response = get_pat()
  await ctx.send(response)

@bot.command(name='koala', help='Returns a randomly chosen image of a koala')
async def koala(ctx):
  response = get_koala()
  await ctx.send(response)

@bot.command(name='fox', help='Returns a randomly chosen image of a fox')
async def fox(ctx):
  response = get_fox()
  await ctx.send(response)

@bot.command(name='bird', help='Returns a randomly chosen image of a bird')
async def bird(ctx):
  response = get_bird()
  await ctx.send(response)

@bot.command(name='panda', help='Returns a randomly chosen image of a panda')
async def panda(ctx):
  response = get_panda()
  await ctx.send(response)

@bot.command(name='cat', help='Returns a randomly chosen image of a cat')
async def cat(ctx):
  response = get_cat()
  await ctx.send(response)

@bot.command(name='pikachu', help='Returns a randomly chosen gif of Pikachu')
async def pikachu(ctx):
  response = get_pikachu()
  await ctx.send(response)

@bot.command(name='no', help='Yes')
async def no(ctx):
  await ctx.send('Yes')

@bot.command(name='yes', help='No')
async def yes(ctx):
  await ctx.send('No')

@bot.command(name='sus', help='Among Us')
async def sus(ctx):
  await ctx.send("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣻⣯⣽⣟⠿⠟⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⡿⣫⣾⣿⣿⣿⡹⢁⣴⣷⣿⣿⣷⣆⣤⡀⠠⢬⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⢱⣿⣿⣿⠿⠩⢠⣿⣿⣿⣿⣿⣏⣿⢸⣿⡖⣄⠹⣷⡌⢿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⡸⣿⣿⣿⣼⠂⢸⣿⣿⣾⠯⢟⠋⠿⣿⡿⣳⡿⣳⣿⣷⡈⢿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣷⣌⡻⣿⢡⣿⡀⢻⣿⣿⣷⣭⣯⡆⢰⣤⣥⣶⣿⣿⣿⣷⠈⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣤⡈⠛⠛⠙⠛⠁⣸⣿⣿⣿⣿⣿⡿⠉⣤⣤⡉⢻⣿⣿ \n⣿⣿⣿⣿⣿⠿⠛⢋⣉⣁⣈⣉⣀⣈⣉⣉⣉⣁⡐⠚⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡀⢿⣿ \n⣿⣿⣿⠏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⢿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡇⢸⣿ \n⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡇⢸⣿ \n⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠇⣸⣿ \n⣿⣿⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣧⡈⠛⠿⠋⢠⣿⣿ \n⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣾⣿⣿⣿ \n⣿⣿⣿⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿ \n⣿⣿⣿⣆⠘⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿ \n⣿⣿⣿⠋⣠⣶⣶⣶⣶⣶⣶⠂⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿ \n⣿⣿⠃⣰⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⣿⣿⣿⣿ \n⣿⡏⠀⣿⣿⣿⣿⣿⣿⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿ \n⣿⣇⠀⣿⣿⣿⣿⣿⣿⣿⣧⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⣿⣿⣿ \n⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⣿⣆⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣿⣿⣿ \n⣿⣿⣷⣄⠙⠿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿ \n⣿⣿⣿⣿⣷⡄⢀⣉⣩⣿⣿⣿⠋⢠⣄⣀⣀⣀⣀⡀⢶⣿⣿⣿⣿⣿⣿⣿⣿⡏⢁⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣧⠈⣿⣿⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣷⡈⠻⣿⣿⣿⣿⣿⣿⡿⢁⣼⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣆⠘⣿⣿⡿⠃⣰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠉⠛⠻⠿⠏⣠⣾⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣦⣈⠉⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿")



keep_alive()
bot.run(os.getenv('TOKEN'))