# GoldyBot
This is a bot for Discord. In case you are unfamiliar with it, Discord is a voice and instant messaging platform centered around creating community-oriented servers. These servers can be as large as thousands of people, or just a small group of close friends. Bots can be added to servers to do all sorts of cool things and enhance the general experience of using Discord (or in most cases, just goof around). As for how the bot functions: in short, it reads messages sent in the text chat channels and parses them, looking for specific commands. The bot then responds accordingly to the commands with a wide variety of behaviors (for now, only in the form of text messages and embedded images). 

Here is an example of what one particular command would look like:

![alt text](https://i.imgur.com/Lgll6dt.png)

This bot was my first project using Python code. I had never tried it before, having used primarily Java and C in the past, so I figured it would be a fun project to familiarize myself with the language. I also learned quite a bit about using API and reading .json data. The bot is a whole lot of fun to use in my private servers with my friends, and is already full of inside jokes. I'm sure that there are all sorts of loose ends that need to be tied up (such as a few declared variabled that never get used due to constant changes in implementation) but at least as of writing this, it's in a pretty solid state. I do hope to continue working on it periodically. One future plan is to implement voice functionality to interact with the bot over voice using wake words and voice to text, but that's a pretty long-term goal.

A (nearly) full list of the commands used to control the bot can be found below:

$duffy - Monkey time (inside joke)

$monke - Monke time (also an inside joke)

$inspire - Randomly chosen inspirational quote

$anime [link to image] - Identifies the name of the anime and number of the episode in which a screenshot appeared

$kanye - Returns a random Kanye West quote/tweet

$dog - Returns a randomly chosen picture of a dog

$bitcoin - Returns the current value of one bitcoin in USD

$meme - Returns a randomly chosen meme

$wink - Returns a randomly chosen anime wink gif

$pat - Returns a randomly chosen anime headpat gif

$koala - Returns a randomly chosen image of a koala

$fox - Returns a randomly chosen image of a fox

$bird - Returns a randomly chosen image of a bird

$panda - Returns a randomly chosen image of a panda

$cat - Returns a randomly chosen image of a cat

$pikachu - Returns a randomly chosen gif of Pikachu

$yes - No (just says "No")

$no - Yes (just says "Yes")

$sus - Among Us (inside joke)

In addition to commands, there is one continuous function running on a one hour loop which simply prints a feed of Bitcoin and Ethereum prices in a text channel on a Discord server. We got tired of constantly typing the commands to print the prices!
