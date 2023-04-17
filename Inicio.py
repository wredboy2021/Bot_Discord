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
from Base_Datos import *
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
async def delete(ctx):
    deleted = await ctx.channel.purge(limit=None)
    await ctx.send(f'Se han borrado {len(deleted)} mensajes')

@Dragon.command(name="Redes")
async def youtube(ctx,*,arg):
   if arg=="Y" or arg=="y":
    await ctx.send(f"https://www.youtube.com/channel/UC3DL-9IFD6-0BJO-cjllksQ \nCanal Oficial de la Biblioteca del Infinito!")
   elif arg=="T" or arg=="t" :
      await ctx.send("https://www.tiktok.com/@labibliotecadelinfinito \nTiktok oficial de la biblioteca del infinito")


@Dragon.command(name="Datos_Random")
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
        Conexion=sqlite3.connect("Economia")
        Mi_Cursor=Conexion.cursor()
        sql = "SELECT * FROM table ORDER BY RANDOM() LIMIT 1"
        Mi_Cursor.execute(sql)
        row = Mi_Cursor.fetchone()
        await ctx.send(f'Aquí tienes un dato aleatorio: {row[0]}')
     elif arg==" suscesos_historicos":
        lista_Historia=[]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(random_list)}")
     elif arg=="Terror_analogico":
        lista_Terror_Analogico=[]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(random_list)}")
     elif arg=="economia":
        Lista_Random=[]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(random_list)}")
     elif arg==" suscesos_historicos":
        lista_Historia=[]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(random_list)}")
     elif arg=="Terror_analogico":
        lista_Terror_Analogico=[]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(random_list)}")
     elif arg=="economia":
        Lista_Economia=["c"]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(Lista_Economia)}")
     elif arg==" suscesos_historicos":
        lista_Historia=["b"]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(lista_Historia)}")
     elif arg=="Terror_analogico":
        lista_Terror_Analogico=["a"]
        await ctx.send(f"Aquí tienes un dato random: {random.choice(lista_Terror_Analogico)}")
     else:
        await ctx.send(f"Introduce Alguno de los temas que tenemos disponibles, Seguimos trabajando para poner mas!!!!!")
@Dragon.command("Palabra_Random")
async def Palabras_Random(ctx):
   mention = ctx.message.author.mention
   Random=["Hola","Paqui","Eto","Clamor", 
           "Frenesí", "Brumoso", "Mofle", "Bruñido", "Caprichoso", 
           "Chorrear", "Desfallecer", "Engolosinado", "Fulgor", "Garbo", 
           "Gazmoño", "Gesticular", "Hilar", "Incendio", "Intrigar", "Jovial", 
           "Lacónico", "Lisonjero", "Mascullar", "Mitigar", "Nimio", "Oliscar", "Pertinaz", "Querellante", "Regocijo", "Sibilante", "Titubeante", 
           "Ungüento", "Vago", "Voluble", "Zafarrancho", "Abulia", "Bache", "Chamuscar", "Desparpajo", "Encrespado", "Fervor", "Garabato", "Gazmoñería", "Gruñido", 
           "Herir", "Inaudito", "Jugarreta", "Lambiscón", "Lívido", "Mascara", "Mordacidad", "Nimiedad", "Oliscar", "Perturbación", "Quemarropa", "Risueño", 
           "Sibaritismo", "Titánico", "Ufano", "Vanagloria", "Zarandear", "Acicalar", "Badulaque", "Chillar", "Despabilado", "Enfervorizar", "Fervoroso", "Garabatear", 
           "Gazmoñerías", "Gruñón", "Heráldico", "Incendiar", "Jugarretear", "Lambiscar", "Luminoso", "Masoquista", "Mormullo", "Noveno", "Ostentoso", "Perplejidad", 
           "Quedar atónito", "Rizar el rizo", "Sibarita", "Tiznar", "Ufano", "Vaporoso", "Zozobrar","Buenos dias", "Buenas tardes", "Buenas noches", "Adios", "Saludos", 
           "Hola de nuevo", "Hasta pronto", "Gracias", "Por favor", "Disculpa", "Perdon", "Cuidado", "Alegria", "Felicidad", "Amor", "Cariño", "Bienvenida", "Bienvenido", 
           "Suerte", "Exitos", "Divertido", "Aventura", "Disfruta", "Sabes", "Creo", "Piensa", "Intenta", "Comprende", "Comparte", "Ayuda", "Emocion", "Tristeza", 
           "Tension", "Tiempo", "Realidad", "Imagina", "Fantasia", "Idea", "Proyecto", "Pasatiempo", "Razon", "Luchar", "Poder", "Riqueza", "Creativo", "Inspiracion",
             "Alegria", "Verdad", "Mentira", "Mundo", "Universo", "Unido", "Individual", "Cambio", "Futuro", "Vida", "Muerto", "Vivo", "Movimiento", "Siempre", "Nunca", 
             "Nada", "Todo", "Aqui", "Alli", "Ahora", "Siempre", "Ayer", "Mañana", "Razonable", "Irrazonable", "Corto", "Largo", "Ligero", "Pesado", "Clima", "Tierra", 
             "Mar", "Cielo", "Naturaleza", "Animales", "Plantas", "Cultura", "Civilizacion", "Arte", "Musica", "Cine", "Viajes", "Deportes", "Juegos", "Cocina", "Comida", 
             "Bebida", "Lectura", "Escritura", "Ciencia", "Tecnologia", "Oportunidad", "Confianza", "Respeto", "Honestidad", "Integridad", "Libertad", "Justicia", "Global", "Local", "Positivo", "Negativo", "Habilidad", "Desventaja", 
             "Historia", "Mitos", "Leyendas", "Fantasmas", "Encuentro", "Despedida", "Rutina", "Cambio", "Verano", "Invierno", "Primavera", "Otoño", "Amanecer", "Atardecer", 
             "Alegria", "Tristeza", "Aprendizaje", "Enseñanza", "Protocolo", "Libertad", "Dinero", "Salud", "Familia", "Amigos", "Confianza", "Magia", "Sorpresa", "Misterio","xertz", "xystus", "xanthosis", "xenelasy", "xerarch", "xerography", 
             "xoanon", "xenoglossy", "xemeroid", "xylogenous", "xenophobia", "xylology", "xenodochy", "xyster", "xenia", "xylomancy", "xiphias", "xenogenesis", "xerasia", 
             "xenomancy", "xyster", "xylophone", "xeranthemum", "xerlin", "xyloid", "xenogenesis", "xenon", "xylography", "xenoparasite", "xenolith", "xerophile", 
             "xenogenesis", "xylomelum", "xenomorph", "xenopos", "xylophagous", "xenius", "xerasia", "xenodochy", "xylomancy", "xerampelina", "xanthic", "xenia", "xanthine", 
             "xenogenesis", "xeromancy", "xenotropic", "xenotime", "xenogamy", "xeroderma", "xenogenesis", "xylorcin", "xerotripsis"]
   await ctx.send(f"{mention} Tu Palabra Random es:{random.choice(Random)}")



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