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
import nacl
import ffmpeg
from discord.ext import commands
from discord.ext import tasks


bot = commands.Bot(command_prefix='$')

req = requests.get("https://discord.com/api/path/to/the/endpoint")
print(req)

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
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

@bot.command(name='sus', help='Among Us')
async def sus(ctx):
  await ctx.send("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣻⣯⣽⣟⠿⠟⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⡿⣫⣾⣿⣿⣿⡹⢁⣴⣷⣿⣿⣷⣆⣤⡀⠠⢬⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⢱⣿⣿⣿⠿⠩⢠⣿⣿⣿⣿⣿⣏⣿⢸⣿⡖⣄⠹⣷⡌⢿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⡸⣿⣿⣿⣼⠂⢸⣿⣿⣾⠯⢟⠋⠿⣿⡿⣳⡿⣳⣿⣷⡈⢿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣷⣌⡻⣿⢡⣿⡀⢻⣿⣿⣷⣭⣯⡆⢰⣤⣥⣶⣿⣿⣿⣷⠈⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣤⡈⠛⠛⠙⠛⠁⣸⣿⣿⣿⣿⣿⡿⠉⣤⣤⡉⢻⣿⣿ \n⣿⣿⣿⣿⣿⠿⠛⢋⣉⣁⣈⣉⣀⣈⣉⣉⣉⣁⡐⠚⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡀⢿⣿ \n⣿⣿⣿⠏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⢿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡇⢸⣿ \n⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡇⢸⣿ \n⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠇⣸⣿ \n⣿⣿⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣧⡈⠛⠿⠋⢠⣿⣿ \n⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣾⣿⣿⣿ \n⣿⣿⣿⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿ \n⣿⣿⣿⣆⠘⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿ \n⣿⣿⣿⠋⣠⣶⣶⣶⣶⣶⣶⠂⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿ \n⣿⣿⠃⣰⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⣿⣿⣿⣿ \n⣿⡏⠀⣿⣿⣿⣿⣿⣿⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿ \n⣿⣇⠀⣿⣿⣿⣿⣿⣿⣿⣧⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⣿⣿⣿ \n⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⣿⣆⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣿⣿⣿ \n⣿⣿⣷⣄⠙⠿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿ \n⣿⣿⣿⣿⣷⡄⢀⣉⣩⣿⣿⣿⠋⢠⣄⣀⣀⣀⣀⡀⢶⣿⣿⣿⣿⣿⣿⣿⣿⡏⢁⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣧⠈⣿⣿⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣷⡈⠻⣿⣿⣿⣿⣿⣿⡿⢁⣼⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣆⠘⣿⣿⡿⠃⣰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠉⠛⠻⠿⠏⣠⣾⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣦⣈⠉⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿")

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
async def play(ctx,url):
    try :
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
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

@bot.command(name='eth', help='Returns the current value of Ethereum in USD')
async def eth(ctx):
  response = get_ethereum()
  await ctx.send("One Ether is currently worth $"+response)

@tasks.loop(hours=1)
async def cryptoLoop():
 btc = get_bitcoin()
 eth = get_ethereum()
 channel = bot.get_channel(839986437553651764)
 await channel.send('**Hourly Crypto Update:**\nBitcoin is currently worth: $'+btc+'\nEthereum is currently worth: $'+eth)

@cryptoLoop.before_loop
async def before():
    await bot.wait_until_ready()


bot.run(os.getenv('TOKEN'))