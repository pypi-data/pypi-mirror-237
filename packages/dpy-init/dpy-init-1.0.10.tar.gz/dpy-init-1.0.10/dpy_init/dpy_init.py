import click

@click.command()
@click.option('--library', type=click.Choice(['discord.py', 'disnake.py']), prompt='Choose a library')
def dpy_init(library):
    # Create the main.py file with content based on user choices
    content = ""

    if library == 'discord.py':
        command_type = click.prompt('Choose a command type', type=click.Choice(['normal-commands', 'hybrid-commands']))

        if command_type == 'normal-commands':
            varname = click.prompt('Choose a variable name', type=click.Choice(['bot', 'client']))
            if varname == 'bot':

                content = """# Importing libraries...
import discord
from discord.ext import commands

# Setting up intents...
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

# Creating the client...
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot has logged in.")

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"PONG! The client latency is `{latency}`ms. ")

bot.run("Your token here")
"""
            elif varname == "client":
                content = """import discord
from discord.ext import commands

# Setting up intents...
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

# Creating the client...
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot has logged in.")

@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"PONG! The client latency is `{latency}`ms. ")

client.run("Your token here")
"""

        elif command_type == 'hybrid-commands':
            varname = click.prompt('Choose a variable name', type=click.Choice(['bot', 'client']))
            if varname == 'bot':

                content = """# Importing libraries...
import discord
from discord.ext import commands
import time

# Creating a custom client...
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
        # Setting up intents...
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.reactions = True
        self.intents = intents

    async def setup_hook(self):
        time.sleep(5)
        await self.tree.sync()
        print("Synced slash commands for the bot.")

bot = Bot()

@bot.event
async def on_ready():
    print("Bot has logged in.")
    time.sleep(1)
    print("Ready to roll!")

@bot.hybrid_command(name="ping", description="Shows the bot's ping to Discord.")
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"PONG! The client latency is `{latency}`ms.")

bot.run("Your token here")
"""
            elif varname == 'client':
                content = """# Importing libraries...
import discord
from discord.ext import commands
import time

# Creating a custom client...
class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
        # Setting up intents...
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.reactions = True
        self.intents = intents

    async def setup_hook(self):
        time.sleep(5)
        await self.tree.sync()
        print("Synced slash commands for the bot.")

client = Client()

@client.event
async def on_ready():
    print("Bot has logged in.")
    time.sleep(1)
    print("Ready to roll!")

@client.hybrid_command(name="ping", description="Shows the bot's ping to Discord.")
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"PONG! The client latency is `{latency}`ms.")

client.run("Your token here")
"""

    elif library == 'disnake.py':
        command_type = click.prompt('Choose a command type', type=click.Choice(['normal-commands', 'slash-commands']))

        if command_type == 'normal-commands':
            content = """
# Coming soon :/ 
"""

        elif command_type == 'slash-commands':
            content = """
# Coming soon :/ 
"""

    if content:
        with open('main.py', 'w') as file:
            file.write(content)
        print(f"Successfully created main.py for {library} with {command_type}. ")
    else:
        print("Invalid library or command type choice. ")

if __name__ == '__main__':
    dpy_init()
