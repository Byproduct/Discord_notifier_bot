import os
import sys
import discord     # requires pip install discord.py
from discord.ext import tasks
from discord import Client

discord_bot: Client = discord.Client()

try:
    with open ("discordbot_config.txt", "r") as f:
        data = f.readlines()
except:
    print("Error reading configuration file (discordbot_config.txt).")
    sys.exit(0)

# configuration loaded from discordbot_config.txt
bot_token = data[4].rstrip()
owner_id = data[6].rstrip()
message_check_interval = int(data[8].rstrip())

print("\nDiscord bot configuration")
print(f"bot token: {bot_token}")
print(f"bot owner's discord user id': {owner_id}")
print(f"message check interval': {message_check_interval}\n\n")


#   Things to do immediately after the bot has connected to Discord (nothing important for now)
@discord_bot.event
async def on_ready():
    for guild in discord_bot.guilds:
        server = guild
    print(f'{discord_bot.user} has connected to {server}!')
    user = await discord_bot.fetch_user(owner_id)
    await user.send('I\'m alive!')


#   periodically check if there are any messages (left by other programs) to send to the bot owner
@tasks.loop(seconds=message_check_interval)         # set this interval in the configuration file. There's probably no need to poke in the file system too often. Default interval is one minute.
async def check_for_queued_messages():
    # if messages.txt exists, read it into one string and then delete the file
    try:
        with open("messages.txt", "r") as f:
            data = f.readlines()
        messages = ""
        for line in data:
            messages = messages + line
        os.remove("messages.txt")

        # ...and send the messages to the bot owner
        user = await discord_bot.fetch_user(owner_id)
        await user.send(messages)

    except:
        # print("No messages.")
        pass

check_for_queued_messages.start()


# bot startup command
try:
    discord_bot.run(bot_token)
except:
    print("Error connecting to discord (probably no network)")
    sys.exit(1)