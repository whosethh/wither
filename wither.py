# imports start 

import discord, rich, fade, colorama, os, random, requests

from discord.ext import commands
from colorama import Fore, init
from rich.console import Console

# imports end

console = Console(
    color_system="auto"
)

wither = commands.Bot(command_prefix="$", activity = discord.Streaming(name="prefix `$`", url="https://twitch.tv/elraenn"), status=discord.Status.dnd)

for root,directory,files in os.walk('.'):
    for file in files:
        if file.endswith('.py') and file != 'wither.py':
            wither.load_extension(f'{root[2:]}.{file[:-3]}')


@wither.event
async def on_ready():
    colorama.init(convert=True)

    version = "1.0"

    motd = requests.get('https://raw.githubusercontent.com/probablynothate/days/master/motd')
    
    mtext = ""

    if motd.status_code == 404:
        mtext = "No MOTD found"
    else:
        mtext = motd.text

    colors = [fade.purpleblue, fade.blackwhite, fade.greenblue, fade.purplepink]

    botloadfull = random.choice(colors)(f'''
                ██╗    ██╗██╗████████╗██╗  ██╗███████╗██████╗ 
                ██║    ██║██║╚══██╔══╝██║  ██║██╔════╝██╔══██╗
                ██║ █╗ ██║██║   ██║   ███████║█████╗  ██████╔╝
                ██║███╗██║██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
                ╚███╔███╔╝██║   ██║   ██║  ██║███████╗██║  ██║
                 ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n
                 v{version}
                Connected as: {wither.user}
                Prefix: {wither.command_prefix}
                Guild Count: {len(wither.guilds)}
                Cogs Count: {len(wither.cogs)}
                ┌───────────────────────────────┐
                motd: {mtext}
                └───────────────────────────────┘
    ''')

    



   # console.print(botloadfull) #justify="center")
    console.print(botloadfull, justify="center", end="")


token = "OTM1OTY3NjM1OTIzOTI3MDkw.YfGVyQ.ld06qjko95CDowrFULsbWI3LoqU"


@wither.command(aliases=["cc"])
@commands.is_owner()
async def cogc(ctx):
    emb = discord.Embed(description="Total Cogs Loaded.", color=0xfbb4f3)
    emb.add_field(name="Total Cog Count", value=f"`{len(wither.cogs)}`")
    await ctx.send(embed=emb)

@wither.command(aliases=["lsc"])
@commands.is_owner()
async def listcogs(ctx):
    embl = discord.Embed(description="Listing the Cogs.", color=0xfbb4f3)
    embl.add_field(name="Total Cogs List", value=f"`{list(wither.cogs)}`")
    await ctx.send(embed=embl)

wither.run(token)