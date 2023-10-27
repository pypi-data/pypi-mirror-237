"""
This class acts as the front end to the user. I seperated it from the main class to prevent the user
from seeing internal methods that may be confusing
"""

# external imports
from collections.abc import Callable
from discord import Message as message
import asyncio
import sys

# local import
from .api_handler import DiscordAPIHandler

class DiscordBot:
    def __init__(self) -> None:
        self.api_handler = DiscordAPIHandler()
        self.logger = self.api_handler.LOGGER

    def start(self) -> None:
        """
        Starts the bot client and loads dependencies.
        """
        asyncio.run(self.api_handler.main())
    
    def call_on_message(self, function: Callable[[message], str]) -> None:
        """
        The bot will call the parameter passed into this method whenever it receives a message
        """
        if callable(function):
            self.api_handler.client.callables["on_message"] = function
        else:
            self.api_handler.LOGGER.error(f"Invalid function '{function}'")
            sys.exit()