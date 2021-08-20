# Discord notifier bot

If you're using Discord for chatting, it's a free and super handy way to also receive useful notifications on your PC or phone.

This is a simple bot that checks messages.txt in the same folder, for example once per minute. Any messages placed in this file (by other programs) will be sent to you via a Discord private message.

It requires Python 3, discord.py (pip install discord.py) and some way, such as screen in Linux, to stay always on.

Firstly, you'll need to set up a bot in the Discord developer portal. A good tutorial is [here](https://realpython.com/how-to-make-a-discord-bot-python/), for example. You'll only need the bot token you'll get when the bot is created. All the other functionality and code in the tutorial, although good to know, are not needed for using this bot.

Secondly, you'll need to know what the numeric ID of your own Discord account is. [This is how you'll find it.](https://techswift.org/2020/04/22/how-to-find-your-user-id-on-discord/)

When you have these, insert them in discordbot_config.txt, start up the program, and leave it running. Try writing something in "messages.txt" and see if you receive the message personally within a minute.

If you have any questions, or found this useful, I'd be happy to know. :)
