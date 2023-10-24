import click

@click.command()
@click.option('--library', type=click.Choice(['discord.py', 'disnake.py']), prompt='Choose a library')
def dpy_init(library):
    # Create the main.py file with content based on user choices
    content = ""

    if library == 'discord.py':
        command_type = click.prompt('Choose a command type', type=click.Choice(['normal-commands', 'hybrid-commands']))

        if command_type == 'normal-commands':
            content = """
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(f"{client.user.name} has logged in.")

@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"PONG! The client latency is `{latency}`ms.")

client.run("Your token here :)")

"""
        elif command_type == 'hybrid-commands':
            content = """
import discord
from discord.ext import commands

class Client(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.reactions = True
        super().__init__(command_prefix=get_prefix, intents=intents)

    async def setup_hook(self):
        time.sleep(5)
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}.")


client = Client()

@client.event
async def on_ready():
    print(f"{client.user.name} has logged in.")

@client.hybrid_command(name="ping", description="Shows the ping of the bot to discord.")
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"PONG! The client latency is `{latency}`ms.")

client.run("Your token here :)")

"""
    elif library == 'disnake.py':
        command_type = click.prompt('Choose a command type', type=click.Choice(['normal-commands', 'slash-commands']))

        if command_type == 'normal-commands':
            content = """
# Coming soon :/
# Sorryy!


"""
        elif command_type == 'slash-commands':
            content = """
# Coming soon :/
# Sorryy!


"""

    if content:
        with open('main.py', 'w') as file:
            file.write(content)
        print(f"Successfully created main.py for {library} with {command_type}.")
    else:
        print("Invalid library or command type choice.")

if __name__ == '__main__':
    dpy_init()
