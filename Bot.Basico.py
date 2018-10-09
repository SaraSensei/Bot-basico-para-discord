
import discord
import asyncio
import time
import logging
from logging.handlers import RotatingFileHandler
import random
import sqlite3
import traceback
import time
import datetime
import sys
import os
import hashlib
import asyncio
import aiohttp
from discord.ext.commands import bot
from discord.ext import commands
client = discord.Client()


 

@client.event
async def on_ready():
      print("Ready")


# Event para dar la bienvenida a un usuario en el servidor
@client.event
async def on_member_join(member):

    channel = member.server.get_channel("Token del canal")


    await client.send_message(channel, 'Poneis el mensaje que querais'+member.mention)

client.run("Poneis el token del bot")
