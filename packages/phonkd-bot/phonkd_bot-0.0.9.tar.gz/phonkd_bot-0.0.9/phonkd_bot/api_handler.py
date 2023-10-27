# external imports
import discord
from discord.ext import commands
import inspect
import json
import sys
import os

# local imports
from phonkd_bot.logger import logger

class DiscordAPIHandler():
    def __init__(self) -> None:
        # aliases
        self.LOGGER = logger()
        self.CALLER_FILE = self.get_caller_file()
        self.CALLER_DIRECTORY = self.get_caller_directory(self.CALLER_FILE)

        # attributes
        self.config = self.load_config_file(self.CALLER_DIRECTORY)
        self.client = self.load_client()

    """ Initializer methods """
    def get_caller_file(self) -> str:
        fname = inspect.currentframe()
        while fname.f_back:
            fname = fname.f_back
        caller_file = fname.f_globals['__file__']
        return caller_file

    def get_caller_directory(self, caller_file: str):
        caller_directory = os.path.dirname(os.path.abspath(caller_file))
        return caller_directory

    def load_config_file(self, directory: str) -> dict:
        config_path = directory + "/config.json"
        if not os.path.isfile(config_path):
            self.LOGGER.error(f"Failed to locate config.json, please create it and try again")
            sys.exit()
        else:
            with open(config_path) as file:
                return json.load(file)

    def load_client(self) -> commands.Bot:
        client = commands.Bot(command_prefix=commands.when_mentioned_or(self.config["prefix"]), intents=discord.Intents.all())
        client.logger = self.LOGGER
        client.callables = {}
        return client

    async def load(self) -> None:
        # get the path of hte current file
        path = os.path.realpath(f"{os.path.dirname(__file__)}/cogs")

        # loop through every python file in the cogs directory
        for filename in os.listdir(path):
            if filename.endswith(".py"):
                extension = filename[:-3]
                try:
                    # load the cog and log the information
                    await self.client.load_extension(f"phonkd_bot.cogs.{extension}")
                    self.LOGGER.info(f"Loaded extension '{extension}'")
                except Exception as e:
                    # print the exception if there is one
                    exception = f"{type(e).__name__}: {e}"
                    self.LOGGER.error(f"Failed to load extension {extension}\n{exception}")

    async def main(self) -> None:
        async with self.client:
            await self.load()

            try:
                await self.client.start(self.config["token"])
            except Exception as e:
                self.LOGGER.error(f"{type(e).__name__}: {e}")
                sys.exit()