# imports start 

import discord, rich, fade, colorama, os, random, requests

from discord.ext import commands
from colorama import Fore, init
from rich.console import Console

# imports end

console = Console(
    color_system="auto"
)

class economy(commands.Cog):

    def  __init__(self, wither):
        self.wither = wither




def setup(wither):
    wither.add_cog(economy(wither))
