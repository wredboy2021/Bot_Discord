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
#Posible Funcion Cuando se posean mas Subs
#@Dragon.command(name="Subs")
#async def subscriptores(ctx,username):
    #data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + key_Youtube).read()
    #subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    #response = username + " tiene " + "{:,d}".format(int(subs)) + " suscriptores!"
    #await ctx.send(response)
def is_admin():
    def predicate(ctx):
        return ctx.guild is not None and ctx.author.guild_permissions.administrator
    return commands.check(predicate)