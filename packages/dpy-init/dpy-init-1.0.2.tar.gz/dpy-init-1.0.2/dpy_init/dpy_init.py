import click

@click.command()
@click.option('--library', type=click.Choice(['discord.py', 'disnake.py']), prompt='Choose a library')
def dpy_init(library):
    # Create the main.py file with content based on user choices
    content = ""

    if library == 'discord.py':
        command_type = click.prompt('Choose a command type', type=click.Choice(['normal-commands', 'hybrid-commands']))

        if command_type == 'normal-commands':
            content = """import discord

# Your code for discord.py with normal commands here


"""
        elif command_type == 'hybrid-commands':
            content = """import discord

# Your code for discord.py with hybrid commands here


"""
    elif library == 'disnake.py':
        command_type = click.prompt('Choose a command type', type=click.Choice(['normal-commands', 'slash-commands']))

        if command_type == 'normal-commands':
            content = """import disnake

# Your code for disnake.py with normal commands here


"""
        elif command_type == 'slash-commands':
            content = """import disnake

# Your code for disnake.py with slash commands here


"""

    if content:
        with open('main.py', 'w') as file:
            file.write(content)
        print(f"Successfully created main.py for {library} with {command_type}.")
    else:
        print("Invalid library or command type choice.")

if __name__ == '__main__':
    dpy_init()
