import os
import time
import schedule
from discord import *
from dotenv import load_dotenv
from discord.ext import commands
import discord
import math
import random


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
   
#Basicos
@Dragon.command(name="Test")
async def test(ctx, *, arg):
    await ctx.send(arg)

@Dragon.command(name="Dilo")
async def dilo(ctx, member: discord.Member, *,arg):
    await ctx.send(f'Le has dicho a {member.mention} '+ ''.join(arg))
    await ctx.message.delete()

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
     await ctx.send(f"El resultado de la Multplicacion es: {a**b}")
    except discord.ext.commands.errors.BadArgument:
      return "No"
      
@Dragon.command(name="Raiz")
async def raiz(ctx,a:int):
   if a > 0:
      await ctx.send(f"La raiz cuadrada de {a} es: {math.sqrt(a)}")
   else:
      await ctx.send("El numero no es valido")
   pass

@Dragon.command(name="Del")
async def delete(ctx,member:discord.Member):
   member:discord.Member
   await ctx.channel.purge(limit=None)
   await ctx.send(f'Has borrado Todos los mensajes{member.mention}')

@Dragon.command(name="Random")
async def Random(ctx,*,arg):
     if arg == "random":
      random_list = ["La tasa de supervivencia del cáncer de pulmón es del 17%, la menor de todos los tipos de cáncer.", 
                     "El caballo más rápido de todos los tiempos fue el caballo de carreras norteamericano, Secretariat, que corrió una milla en 1 minuto y 59 segundos.",
                     "Los bebés tienen más de 100 huesos más que los adultos, porque algunos se fusionan a medida que crecen.",
                     "Una sola hoja de una alfilera de árbol de cedro rojo contiene más de 10.000 semillas.",
                     "Los tiburones tienen más de 20.000 filas de dientes a lo largo de su vida.",
                     "La temperatura de la superficie del sol es de aproximadamente 9.340 °F (5.160 °C)."]
      await ctx.send(f"Aquí tienes un dato random: {random.choice(random_list)}")
     elif arg=="economia":
        Lista_Random=[]
     elif arg==" suscesos_historicos":
        lista_Historia=[]
     elif arg=="Terror_analogico":
        lista_Terror_Analogico=[]
     elif arg=="economia":
        Lista_Random=[]
     elif arg==" suscesos_historicos":
        lista_Historia=[]
     elif arg=="Terror_analogico":
        lista_Terror_Analogico=[]
     elif arg=="economia":
        Lista_Random=[]
     elif arg==" suscesos_historicos":
        lista_Historia=[]
     elif arg=="Terror_analogico":
        lista_Terror_Analogico=[]
     else:
        await ctx.send(f"Introduce Alguno de los temas que tenemos disponibles, Seguimos trabajando para poner mas!!!!!")



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
   


class Advanced():
   def __init__(self,ctx,arg):
      self.ctx=ctx
      self.arg=arg
   def Answerd():
      pass      



Dragon.run(TOKEN)
Dragon(Active_Bot()) 