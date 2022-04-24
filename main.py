import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
import random
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

load_dotenv()

Ds_Token = os.getenv('TOKEN')
Prefix = os.getenv('PREFIX')
GIDS = os.getenv('GIDS')

client = discord.Client()
bot = commands.Bot(command_prefix=Prefix)
slash = SlashCommand(bot, sync_commands=True)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
    print('Bot ready')

@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    await bot.process_commands(message)

@bot.command(pass_context=True, aliases=['orso','Orso'])
async def cmd1(ctx):
    orso1 = random.randint(1,8)
    orso2 = str(orso1)
    embed1 = discord.Embed(title="Ecco un orso a caso (Orso numero " + orso2 + ")")
    embed1.set_image(url="https://raw.githubusercontent.com/Fredbear07/Bears/main/Bears/Bear" + orso2 + ".png")
    await ctx.send(embed=embed1)

@slash.slash(
    name="Orso",
    description="8 Foto di orsi casuali",
    guild_ids=[GIDS]    
)    
async def _orso(ctx: SlashContext):
    orso1 = random.randint(1,8)
    orso2 = str(orso1)
    embed1 = discord.Embed(title="Ecco un orso a caso (Orso numero " + orso2 + ")")
    embed1.set_image(url="https://raw.githubusercontent.com/Fredbear07/Bears/main/Bears/Bear" + orso2 + ".png")
    await ctx.send(embed=embed1)
    
@slash.slash(
    name="Github",
    description="Codice sorgente e repo del bot",
    guild_ids=[GIDS]    
)    
async def _orso(ctx: SlashContext):
    await ctx.send("https://github.com/Fredbear07/BearBot")

@slash.slash(
    name="?",
    description="Le Info Del Server",
    guild_ids=[GIDS]    
)    
async def _orso(ctx: SlashContext):
    embed1 = discord.Embed(title="")
    embed1.set_image(url="https://raw.githubusercontent.com/Fredbear07/Bears/main/Bears/Bear" + orso2 + ".png")
    await ctx.send(embed=embed1)
    await ctx.send("https://github.com/Fredbear07/BearBot")

bot.run(Ds_Token)
