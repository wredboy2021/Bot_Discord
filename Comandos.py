import os
import time
import schedule
from discord import *
from dotenv import load_dotenv
from discord.ext import commands
Dragon=commands.Bot(command_prefix='!', intents=Intents.all())
@Dragon.event()
async def on_Ready():
    print("Tamos ready")
    print("Logiado como\n")
    pass
@Dragon.command()
async def test(ctx, *,args):
    arguments = ' '.join(args)
    await ctx.send(f'{len(args)} Palabras escritas: {arguments}')