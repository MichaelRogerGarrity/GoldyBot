import discord
import os
from dotenv import load_dotenv
import requests
from requests import get
import json
import random
import pip
import youtube_dl
import contextvars
import asyncio
import functools
import itertools
import nacl
import ffmpeg
import re
import time
from discord.ext import commands
from discord.ext import tasks
from youtube_dl import YoutubeDL
import genshinstats as gs
#from SimpleEconomy import Seco
load_dotenv('vscode.env')
gs.set_cookie(ltuid=os.getenv('ltuid'), ltoken=os.getenv('ltoken'))


#intents = discord.Intents(messages=True, guilds=True,members=True)
#bot = commands.Bot(command_prefix="!",intents=intents)
#seco=Seco(bot, os.getenv('SIMPLE_ECON_API'), "goldybot", def_bal = 0, def_bank = 0, logs=True)


bot = commands.Bot(command_prefix='$')

req = requests.get("https://discord.com/api/path/to/the/endpoint")
print(req)

youtube_dl.utils.bug_reports_message = lambda: ''

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '/music_files/%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'source_address': '0.0.0.0' ,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

def youtubesearch(arg):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            get(arg) 
        except:
            video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        else:
            video = ydl.extract_info(arg, download=False)
    result = video['webpage_url']
    return result


  

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

def get_ethereum():
  URL = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,CNY,JPY,GBP"
  r = requests.get(URL)
  data = r.json()
  price = data['USD']
  price = "{:.2f}".format(price)
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
    cryptoLoop.start()


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

@bot.command(name='slap', help='Sends a video of a slap that ends by crashing the recipient\'s discord client')
async def no(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/777379028654227500/845179288805703710/Slap.mp4')

@bot.command(name='sus', help='Among Us')
async def sus(ctx):
  await ctx.send("sus")

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='play', help='To play song')
async def play(ctx, *, arg):
  youtube_dl_opts = {}
  url = youtubesearch(arg)
  
  with YoutubeDL(youtube_dl_opts) as ydl:
      info_dict = ydl.extract_info(url, download=False)
      video_url = info_dict.get("url", None)
      video_id = info_dict.get("id", None)
      video_title = info_dict.get('title', None)
  try :
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(video_title))
  except:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@bot.command(name='vengabus', help='To play song')
async def vengabus(ctx):
  
  try :
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            filename = "J:\Other stuff\Code Projects\GoldyBot\music_files\permanent songs\\vengabus.mp3"
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))     
  except:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='eth', help='Returns the current value of Ethereum in USD')
async def eth(ctx):
  response = get_ethereum()
  await ctx.send("One Ether is currently worth $"+response)

@bot.command(name='duck', help='Shuba shuba')
async def duck(ctx):
  await ctx.send(file=discord.File(r'J:\Other stuff\Code Projects\GoldyBot\music_files\videos\duck.mp4'))

#@bot.command(name='bal', help='Displays the balance of GoldyCoin in your wallet.')
#async def bal(ctx):
#    balance=await seco.get_balance(ctx.author.id)
#    
#    e=discord.Embed(
#        title="Balance",
#        description=f"Your balance is: {balance}"
#    )
#    await ctx.send(embed=e)

@bot.command(name='bank', help='Displays the balance of GoldyCoin in your bank account.')
async def bank(ctx):
    balance=await bot.seco.get_bank(ctx.author.id)
    
    e=discord.Embed(
        title="Bank",
        description=f"Your Bank balance is: {balance}"
    )
    await ctx.send(embed=e)

@bot.command(name='genshin', help='Get Genshin data. Example: \"$genshin michael characters\" Acceptable parameters for last word: characters, stats')
async def genshin(ctx, name, arg):
  uid = 1
  output = ''
  if name=='michael':
    uid = 626923400
    name2 = 'Michael'
  if name=='liam':
    uid = gs.get_uid_from_community(18666797)
    name2 = 'Liam'
  if name=='savannah':
    uid = 616103451
    name2 = 'Savannah'
  if name=='nicole':
    uid = 602438360
    name2 = 'Nicole'
  if arg=='characters':
    characters = gs.get_all_characters(uid)
    output = '**List of '+name2+'\'s Characters:**\n'
    for char in characters:
      output = output+(f"**{char['rarity']}☆ {char['name']:10}** | lvl {char['level']:2}    C{char['constellation']}")+'\n'
    await ctx.send(output)
  if arg=='stats':
    stats = gs.get_user_info(uid)['stats']
    output = '**List of all '+name2+'\'s Stats:**\n'
    for field,value in stats.items():
      output=output+(f"{field.replace('_',' ')}: {value}")+'\n'
    await ctx.send(output)

@bot.command(name='rng', help='Returns a random number from 0 to the input number')
async def rng(ctx, num):
  temp = random.randrange(int(num))
  response = temp+1
  await ctx.send(response)

gs.sign_in()
gs.get_daily_rewards()
  
@bot.command(name='timer', help='Functions as a timer for a set number of hours, minutes, and/or seconds.')
async def timer(ctx, timeString):
  validTime = True
  # checks for any letters A-Z
  if timeString.upper().isupper():
    validTime = False

  # can't be empty, and hh:mm:ss is the max size, which is 8 characters
  if len(timeString) == 0 or len(timeString) > 8:
    validTime = False

  if timeString.isnumeric():
    total_time = int(timeString)
  elif validTime:
    #regex to check formatting of string
    if not re.match("^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$", timeString):
      validTime = False
    
    if len(timeString) == 8:
      total_time = int(timeString[0:2])*3600 + int(timeString[3:5])*60 + int(timeString[6:8])
    elif len(timeString) == 5:
      total_time = int(timeString[0:2])*60 + int(timeString[3:5])
    elif len(timeString) <= 2:
      total_time = int(timeString)
  if validTime:
    await ctx.send("Beginning " + str(total_time) + " second timer now!")
    while total_time > 0:
      time.sleep(1)
      total_time -= 1
      if total_time%5 == 0 and 0 < total_time < 20:
        await ctx.send(str(total_time) + " seconds left!")
      if total_time == 60:
        await ctx.send("1 minute left!")
      if total_time == 30:
        await ctx.send("30 seconds left!")
      if 0 < total_time < 5:
        await ctx.send(str(total_time) + " seconds left!")
    await ctx.send("Time's up! Timer has reached zero.")
  else:
    await ctx.send("Please enter a valid time format. Either a number of seconds or hh:mm:ss is acceptable.")
  
@bot.command(name='roll', help='Rolls a random number ranging from 1 to the entered max.')
async def roll(ctx, max):
  randNum = random.randrange(1, int(max)+1)
  await ctx.send(str(randNum))
   
  
@tasks.loop(hours=1)
async def cryptoLoop():
 btc = get_bitcoin()
 eth = get_ethereum()
 channel = bot.get_channel(839986437553651764)
 await channel.send('**Hourly Crypto Update:**\nBitcoin is currently worth: **$'+btc+'**\nEthereum is currently worth: **$'+eth+'**')

@cryptoLoop.before_loop
async def before():
    await bot.wait_until_ready()

bot.run(os.getenv('TOKEN'))