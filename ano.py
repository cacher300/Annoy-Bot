import discord
from discord.ext import commands, tasks
import asyncio

TOKEN = 'OTY5MDUyNTQyNg1MONKEYI4ODY0.GVOOs1.NFrey5_lgeiHeSIQhJ_EeLnADV7qZ1EQaDM'
GUILD_ID = '1089696359436257814'
CATEGORY_NAME = 'TEDDYS HOUSE'

client = commands.Bot(command_prefix='!')


async def add_remove_channels():
    await client.wait_until_ready()
    guild = client.get_guild(int(GUILD_ID))
    while not client.is_closed():
        category = discord.utils.get(guild.categories, name=CATEGORY_NAME)
        if category is None:
            category = await guild.create_category(CATEGORY_NAME)

        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel) and channel.category == category:
                await channel.delete()
            elif isinstance(channel, discord.VoiceChannel) and channel.category == category:
                await channel.delete()

        text_channel = await category.create_text_channel('MAIN')

        await asyncio.sleep(0)

@client.event
async def on_ready():
    print('Bot is ready.')
    client.loop.create_task(add_remove_channels())

client.run(TOKEN)
