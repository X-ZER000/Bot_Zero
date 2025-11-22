import discord
from discord.ext import commands

# ===================================== EXPLICACIÓN ==========================================================
# intents: 
# Da permisos para que el bot pueda ver cosas dentro del Discord: estados, imágenes, reacciones, etc.
# intents = discord.Intents.all()  significa:
# “Dale todos los permisos permitidos a mi bot”
# Funciona porque el bot tiene activado: presence intent, server members intent y message content intent.
# =============================================================================================================

intents = discord.Intents.all()

# ===================================== EXPLICACIÓN ==========================================================
# Aquí estás creando tu bot.
# command_prefix="¡" significa que los comandos se activan con ¡comando
# Ej: ¡hola, ¡ping, ¡boss
# intents=intents conecta los permisos que configuraste arriba.
# =============================================================================================================

bot = commands.Bot(command_prefix="¡", intents=intents)


# ===================================== EVENTO: BOT LISTO =====================================================
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
# =============================================================================================================


# ===================================== CANAL BOSS – RETO A – CATEGORÍA C ===================================
#
# FUNCIONALIDAD:
# - Comando: ¡boss
# - El bot crea un CANAL llamado "boss" si no existe.
# - Envía un mensaje de introducción.
# - Activa modo de ENTREGA: el usuario puede enviar un texto y el bot lo recibe.
#
# Versión 1: Simple. Solo texto como entrega.
# Versión 2 será más profesional (archivos, embeds, repaso, registro, etc.)
# =============================================================================================================

@bot.command()
async def boss(ctx):
    guild = ctx.guild

    # Ver si el canal ya existe
    existing_channel = discord.utils.get(guild.channels, name="boss")

    # Si no existe, lo creamos
    if not existing_channel:
        channel = await guild.create_text_channel("boss")
    else:
        channel = existing_channel

    await ctx.send(f"El canal BOSS está listo, {ctx.author.mention}. Ve al canal **#boss** para enviar el RETO A.")

    # Mensaje inicial dentro del canal Boss
    await channel.send(
        "🔥 **RETO A – CATEGORÍA C ACTIVADO** 🔥\n\n"
        "Puedes enviar tu entrega aquí mismo.\n"
        "Solo escribe tu texto y lo registraré.\n\n"
        "Cuando quieras enviar algo, solo mándalo como mensaje normal."
    )


# ===================================== SISTEMA DE ENTREGA (simple) ===========================================
# Todo mensaje enviado dentro del canal Boss cuenta como entrega.
# Versión 1: se imprime la entrega en consola.
# Versión 2: se almacenará en base de datos / archivos / embeds.
# =============================================================================================================

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Si el mensaje está en el canal Boss
    if message.channel.name == "boss":
        print(f"[ENTREGA - {message.author}]: {message.content}")

        await message.channel.send("✔️ Tu entrega fue recibida.")

    # MUY IMPORTANTE: permitir que los comandos funcionen después de este on_message
    await bot.process_commands(message)

# ---- INICIAR BOT ----
bot.run("Your Token")
