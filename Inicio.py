
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
from discord.utils import get
key_Youtube="AIzaSyCbIbEKCKWOU4YJJlnyGkgURGPI71vJ7qE"
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
Dragon=commands.Bot(command_prefix='/', intents=Intents.all())
class Estado():
    @Dragon.event
    async def on_ready():
        Active_Bot
        print("En funcionamiento!")
        print(f"User:{Dragon.user.name}")
        print(f"Id:{Dragon.user.id}")
        canal = discord.utils.get(Dragon.get_all_channels(), id=1092477049941262348)
        await canal.send('@here ¡Ya Estoy Activo!')

    
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
async def Random(ctx,*,args):
     if args == "Curiosidades" or args == "curiosidades":
        Conexion = sqlite3.connect("Base_Datos/Curiosidades.db")
        Mi_Cursor = Conexion.cursor()
        sql = "SELECT * FROM Curiosidades ORDER BY RANDOM() LIMIT 1"
        Mi_Cursor.execute(sql)
        row = Mi_Cursor.fetchone()
        Mi_Cursor.close()
        await ctx.send(f'Aqui tienes una curiosidad aleatorio  {ctx.author.mention}: {row[1]}')
     elif args=="economia" or args=="Economia":
        Conexion = sqlite3.connect("Base_Datos/Economia.db")
        Mi_Cursor = Conexion.cursor()
        sql = "SELECT * FROM Economia ORDER BY RANDOM() LIMIT 1"
        Mi_Cursor.execute(sql)
        row = Mi_Cursor.fetchone()
        Mi_Cursor.close()
        await ctx.send(f'Aquí tienes un dato aleatorio sobre economia {ctx.author.mention}: {row[1]}')
     elif args=="Terroranalogico" or args=="terroranalogico":
       Conexion = sqlite3.connect("Base_Datos/TerrorAnalogico.db")
       Mi_Cursor = Conexion.cursor()
       sql = "SELECT * FROM Terroranalogico ORDER BY RANDOM() LIMIT 1"
       Mi_Cursor.execute(sql)
       row = Mi_Cursor.fetchone()
       Mi_Cursor.close()
       await ctx.send(f'Aqui tienes un dato Aleatorio sobre terror analogico{ctx.author.mention}: {row[1]}')
     elif args=="Backrooms" or args=="backrooms":
        Conexion = sqlite3.connect("Base_Datos/Backrooms.db")
        Mi_Cursor = Conexion.cursor()
        sql = "SELECT * FROM Backrooms_Niveles ORDER BY RANDOM() LIMIT 1"
        Mi_Cursor.execute(sql)
        row = Mi_Cursor.fetchone()
        Mi_Cursor.close()
        await ctx.send(f'Aqui tienes un nivel aleatorio de los backrooms {ctx.author.mention} : {row[1]}')
     elif args=="PersonajesHistoricos":
        Conexion = sqlite3.connect("Base_Datos/PersonajesHistoricos.db")
        Mi_Cursor = Conexion.cursor()
        sql = "SELECT * FROM Personaje ORDER BY RANDOM() LIMIT 1"
        Mi_Cursor.execute(sql)
        row = Mi_Cursor.fetchone()
        Mi_Cursor.close()
        await ctx.send(f'Aqui Tienes un Personaje Historico y una curiosidad sobre el {ctx.author.mention} : {row[1]}')
     elif args=="Lovecraft":
        Conexion = sqlite3.connect("Base_Datos/Lovecraft.db")
        Mi_Cursor = Conexion.cursor()
        sql = "SELECT * FROM Lovecraft ORDER BY RANDOM() LIMIT 1"
        Mi_Cursor.execute(sql)
        row = Mi_Cursor.fetchone()
        Mi_Cursor.close()
        await ctx.send(f'Aqui tienes un dato curioso sobre la literatura lovecraftiana{ctx.author.mention} : {row[1]}')
     elif args=="Scp":
         Conexion = sqlite3.connect("Base_Datos/Palabras.db")
         Mi_Cursor = Conexion.cursor()
         sql = "SELECT * FROM Palabras ORDER BY RANDOM() LIMIT 1"
         Mi_Cursor.execute(sql)
         row = Mi_Cursor.fetchone()
         Mi_Cursor.close()
         await ctx.send(f'Aqui tienes una palabra aleatoria: {row[1]}')
     elif args=="A":
          Conexion = sqlite3.connect("Base_Datos/Palabras.db")
          Mi_Cursor = Conexion.cursor()
          sql = "SELECT * FROM Palabras ORDER BY RANDOM() LIMIT 1"
          Mi_Cursor.execute(sql)
          row = Mi_Cursor.fetchone()
          Mi_Cursor.close()
          await ctx.send(f'Aqui tienes una palabra aleatoria: {row[1]}')
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

@Dragon.command(name="Rol")
@is_admin()
@commands.has_permissions(administrator=True)    
async def Rol(ctx, usuario: discord.Member):
    rol = discord.utils.get(ctx.guild.roles, name='Messi')
    await usuario.add_roles(rol)
    await ctx.send(f"Se ha asignado el rol {rol.name} a {usuario.mention}")

@Rol.error
async def rol_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("No se ha encontrado al usuario mencionado.")
@Dragon.command(name="Web")
async def Answerd(ctx):
      Conexion = sqlite3.connect("Base_Datos/Web.db")
      Mi_Cursor = Conexion.cursor()
      sql = "SELECT * FROM Web ORDER BY RANDOM() LIMIT 1"
      Mi_Cursor.execute(sql)
      row = Mi_Cursor.fetchone()
      Mi_Cursor.close()
      await ctx.send(f'Espero te parezca interesante esta pagina web{ctx.author.mention} : {row[1]}')
      
class MemberRoles(commands.Converter):
    async def convert(self, ctx, argument):
        member = ctx.author
        return [role.name for role in member.roles[1:]]

@Dragon.command(name="RolesUser")
async def roles(ctx, *, member: MemberRoles = None):
    if not member:
        member = ctx.author
    roles = await MemberRoles().convert(ctx, member)
    if len(roles) == 0:
        await ctx.send("No tienes roles asignados por el momento.")
    else:
        await ctx.send(f"Tienes los siguientes roles {ctx.author.mention} : {', '.join(roles)}")



class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return f'{ctx.author.mention} Abofeteo a {to_slap} Porque *{argument}*'
@commands.has_any_role('Hola',"Messi","A")
@Dragon.command(name="Slap")
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)
@Dragon.command(name="Call")
async def joke(ctx,*,args):
   if args=="Chiste" or args=="Chistes":
       Conexion = sqlite3.connect("Base_Datos/Chistes.db")
       Mi_Cursor = Conexion.cursor()
       sql = "SELECT * FROM Chistes ORDER BY RANDOM() LIMIT 1"
       Mi_Cursor.execute(sql)
       row = Mi_Cursor.fetchone()
       Mi_Cursor.close()
       await ctx.send(f'Espero te guste el chiste que te contare{ctx.author.mention} : {row[1]}')
   elif args=="Anecdota" or args=="anecdota":
        Conexion = sqlite3.connect("Base_Datos/Anecdotas.db")
        Mi_Cursor = Conexion.cursor()
        sql = "SELECT * FROM Anecdotas ORDER BY RANDOM() LIMIT 1"
        Mi_Cursor.execute(sql)
        row = Mi_Cursor.fetchone()
        Mi_Cursor.close()
        await ctx.send(f'Disfruta la anecdota que te contare{ctx.author.mention} : {row[1]}')  
   else:
         await ctx.send(f"Este comando solo funciona para los chistes y anecdotas, prueba denuevo {ctx.author.mention}")


Dragon.run(TOKEN)
Dragon(Active_Bot()) 