from sqlite3 import connect
import os
import time
import schedule
from discord import *
from dotenv import load_dotenv
from discord.ext import commands
import discord
import math
import random
import sqlite3
key_Youtube="AIzaSyCbIbEKCKWOU4YJJlnyGkgURGPI71vJ7qE"
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
Dragon=commands.Bot(command_prefix='!', intents=Intents.all())
class Estado():
 @Dragon.event
 async def on_ready():
    Estado.on_ready()
    Active_Bot
    print("En funcionamiento!")
    print(f"User:{Dragon.user.name}")
    print(f"Id:{Dragon.user.id}")

    
def Active_Bot():
  schedule.every().monday.at("08:00").do(Active_Bot)
  while True:
   schedule.run_pending()
   time.sleep(1)
def is_admin():
    def predicate(ctx):
        return ctx.guild is not None and ctx.author.guild_permissions.administrator
    return commands.check(predicate)
#Basicos
@Dragon.command(name="S")
async def add(ctx, a: int, b: int):
    try:
      await ctx.send(f"El resultado de la suma es: {a + b}")
    except discord.ext.commands.errors.BadArgument:
       return "No"
       
@Dragon.command(name="R")       
async def res(ctx,a:int,b:int):
   try:
      await ctx.send(f"El resultado de la resta es: {a - b}")
   except discord.ext.commands.errors.BadArgument:
      return "No"
      
@Dragon.command(name="D")
async def div(ctx,a:int,b:int):
   try:
    await ctx.send(f"El resultado de la Division es: {a / b}")
   except discord.ext.commands.errors.BadArgument:
      return "No"

@Dragon.command(name="M")
async def mul(ctx,a:int,b:int):
    try:
     await ctx.send(f"El resultado de la Multplicacion es: {a*b}")
    except discord.ext.commands.errors.BadArgument:
      return "No"
      
@Dragon.command(name="Raiz")
async def raiz(ctx,a:int):
   if a > 0:
      await ctx.send(f"La raiz cuadrada de {a} es: {math.sqrt(a)}")
   else:
      await ctx.send("El numero no es valido")
   pass
@commands.has_permissions(administrator=True)
@is_admin()
@Dragon.command(name="Del",hidden=True)
async def delete(ctx):
    deleted = await ctx.channel.purge(limit=None)
    await ctx.send(f'Se han borrado {len(deleted)} mensajes')

@Dragon.command(name="Redes")
async def youtube(ctx,*,arg):
   if arg=="Y" or arg=="y":
    await ctx.send(f"https://www.youtube.com/channel/UC3DL-9IFD6-0BJO-cjllksQ \nCanal Oficial de la Biblioteca del Infinito!")
   elif arg=="T" or arg=="t" :
      await ctx.send("https://www.tiktok.com/@labibliotecadelinfinito \nTiktok oficial de la biblioteca del infinito")

#Funcion en desarrollo 
@Dragon.command(name="Datos")
async def Random(ctx,*,arg):
     if arg == "Curiosidades" or arg == "curiosidades":
        Conexion = sqlite3.connect("Base_Datos/Curiosidades.db")
        Mi_Cursor = Conexion.cursor()
        sql = "SELECT * FROM Curiosidades ORDER BY RANDOM() LIMIT 1"
        Mi_Cursor.execute(sql)
        row = Mi_Cursor.fetchone()
        Mi_Cursor.close()
        await ctx.send(f'Aqui tienes una curiosidad aleatorio  {ctx.author.mention}: {row[1]}')
     elif arg=="economia" or arg=="Economia":
        Conexion = sqlite3.connect("Base_Datos/Economia.db")
        Mi_Cursor = Conexion.cursor()
        sql = "SELECT * FROM Economia ORDER BY RANDOM() LIMIT 1"
        Mi_Cursor.execute(sql)
        row = Mi_Cursor.fetchone()
        Mi_Cursor.close()
        await ctx.send(f'Aquí tienes un dato aleatorio sobre economia {ctx.author.mention}: {row[1]}')
     elif arg=="Backrooms" or "backrooms":
      Conexion = sqlite3.connect("Base_Datos/Backrooms.db")
      Mi_Cursor = Conexion.cursor()
      sql = "SELECT * FROM Backrooms_Niveles ORDER BY RANDOM() LIMIT 1"
      Mi_Cursor.execute(sql)
      row = Mi_Cursor.fetchone()
      Mi_Cursor.close()
      await ctx.send(f"Aqui tienes un nivel aleatorio  {ctx.author.mention}: {row[1]}")
     elif arg=="Personajes_Historicos":
        lista_Terror_Analogico=[]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(lista_Historia)}")
     elif arg=="Lovecraft":
        Lista_Random=[]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(lista_Historia)}")
     elif arg==" suscesos_historicos":
        lista_Historia=[]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(lista_Historia)}")
     elif arg=="Terror_analogico":
        lista_Terror_Analogico=[]
        await ctx.send(f"Aquí tienes un dato random:  {random.choice(Lista_Backrooms)}")
     elif arg=="economia":
        Lista_Economia=["c"]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(Lista_Economia)}")
     elif arg==" suscesos_historicos":
        lista_Historia=["b"]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(lista_Historia)}")
     elif arg=="Terror_analogico":
        lista_Terror_Analogico=["a"]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(lista_Terror_Analogico)}")
     elif arg=="Backrooms":
       Lista_Backrooms=[]
     elif arg=="Niveles_Backrooms":
        Lista_Terror_Analogico=[]
     elif arg=="":
       Lista_Economia=[]
     else:
        await ctx.send(f"Introduce Alguno de los temas que tenemos disponibles, Seguimos trabajando para poner mas!!!!!")

@Dragon.command("Palabra_Random")
async def Palabras_Random(ctx):
    Conexion = sqlite3.connect("Base_Datos/Palabras.db")
    Mi_Cursor = Conexion.cursor()
    sql = "SELECT * FROM Palabras ORDER BY RANDOM() LIMIT 1"
    Mi_Cursor.execute(sql)
    row = Mi_Cursor.fetchone()
    Mi_Cursor.close()
    await ctx.send(f'Aqui tienes una palabra aleatoria: {row[1]}')

@Dragon.command(name="def")    
async def definiciones(ctx,*,arg):
   if arg=="Def":
      Lista_Random=[]
   elif arg=="Def_Backrooms":
      Lista_Backrooms=[]
   elif arg=="Def_Terror_Analogico":
      Lista_Terror_Analogico=[]
   elif arg=="Def_Economia":
      Lista_Economia=[]

@Dragon.command(name="A")
async def Answerd(ctx,arg):
   if arg=="D" or arg=="d":
      await ctx.send(f"Buenos dias a ti tambien")
   elif arg== "T" or arg== "t":
      await ctx.send(f"Buenas tardes A Ti tambien")
   elif arg== "N" or arg== "n":
      await ctx.send(f"Buenas Noches Para ti tambien {ctx.author.mention}")

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return f'{ctx.author} slapped {to_slap} because *{argument}*'


@commands.has_any_role('Hola',"Messi","A")
@Dragon.command(name="Slap")
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)

Dragon.run(TOKEN)
Dragon(Active_Bot()) 