import discord
from discord.ext import commands
import platform
import os

class LogOnReady(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        self.client.logger.info(f"Logged in as {self.client.user.name}")
        self.client.logger.info(f"discord.py API version: {discord.__version__}")
        self.client.logger.info(f"Python version: {platform.python_version()}")
        self.client.logger.info(f"Running on: {platform.system()} {platform.release()} ({os.name})")
        self.client.logger.info("-------------------")

# add cog extension to "client" (the bot)
# NOTE: THIS CODE RUNS FROM THE DIRECTORY THAT "main.py" IS IN
async def setup(client):
    await client.add_cog(LogOnReady(client))