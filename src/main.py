from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 413845956279402496  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(bot.user)

@bot.command()
async def d6(ctx):
    await ctx.send(random.randint(1,6))

@bot.command()
async def on_message(ctx, message):
    if message.content.startswith("Salut tout le monde"):
        await ctx.send("Salut tout seul")

@bot.command()
async def admin(ctx, member: discord.Member):
    role = ctx.guild.create_role(name= "admin")
    await member.add_roles(role)

@bot.command()
async def ban(ctx, member: discord.Member):
    await member.ban()

@bot.command()
async def count(ctx, member: discord.Member):
    members = len(ctx.guild.members)
    await ctx.send(members)

token = "MTAyMjE5MzQ4NDM2NDUxNzUxNg.G6T8qK.G1GdOGwj4N5JJaObLh0PwcMJuzT8Anl3sakpyo"
bot.run(token)  # Starts the bot
