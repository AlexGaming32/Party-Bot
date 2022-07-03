from ast import AsyncWith
from cProfile import label
from contextlib import AsyncExitStack
import datetime
from email import message
from email.errors import MissingHeaderBodySeparatorDefect
from fileinput import close
from http import server
from operator import le
from pickletools import read_unicodestringnl
from platform import release
from pydoc import cli, describe
from re import A, I
from sqlite3 import enable_shared_cache
from telnetlib import AYT
from tkinter import image_types
from tkinter.font import names
from tkinter.ttk import LabelFrame
from turtle import title
from typing_extensions import Required
from unicodedata import name
from unittest import async_case
from webbrowser import get
from xml.dom.minidom import getDOMImplementation
from aiohttp import ClientTimeout
from click import option
import discord
from discord import Embed, Emoji, Forbidden, InputText, LoginFailure, Option, Role
from datetime import timedelta
from discord.ext import commands
from discord.ext import tasks
import os
import random
import discord.ext.tasks
import json
from discord import Interaction
import random
from discord.ui import Button, View
import asyncio
import discord.utils
import time
from discord.utils import get
import greenlet
from interactions import Modal
from pyparsing import Opt, empty, opAssoc
import requests
import re


intents = discord.Intents.all()
client = discord.Bot(command_prefix='!', intents=intents)
edit_guilds=[981237860734742539]
bad_words=['nigger', 'schwanz', 'hurre', 'huhren', 'nigg', 'dick', 'peni', 'pimmel', 'tit', 'niger', 'wixx', 'basta', 'fuck', 'nude', 'hitl', 'missge', 'nigar', 'fick', 'hure', 'arsch', 'dummkopf', 'brezelesser', 'porn', 'nogger', 'suck', 'balls', 'cock']

@client.slash_command(name = 'setup', description = 'sets the server up for the bot')
async def setup(ctx):
    if not ctx.author.guild_permissions.administrator:
        embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        async def button_call(inter):
                if not ctx.author.guild_permissions.administrator:
                    embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
                    await ctx.respond(embed=embed, ephemeral=True)
                else:
                    async def button_call2(inter):
                            if not ctx.author.guild_permissions.administrator:
                                embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
                                await ctx.respond(embed=embed, ephemeral=True)
                            else:
                                async def nocall3(inter):
                                    async def nocall4(inter):
                                            if not ctx.author.guild_permissions.administrator:
                                                embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
                                                await ctx.respond(embed=embed, ephemeral=True)
                                            else:
                                                embed=discord.Embed(title=":envelope_with_arrow: | Important Infos", color=0xb994ff)
                                                embed.add_field(name=":information_source: | Suggestion Channel", value="Users will be able to suggest things if an admin sets it up with **/setsuggest**", inline=False)
                                                # embed.add_field(name=":trophy: | Premium", value="The server can get premium if the owner joins the **Coding and Chill** Server for free!", inline=False)
                                                embed.add_field(name=":map: | Globalchat", value="Admins can choose a globalchat channel using **/setglobal**", inline=False)
                                                embed.add_field(name=":tada: | Member joins", value="Admins can choose a channel where new members will be announced with **/setwelcome**", inline=False)
                                                embed.set_footer(text="Party Bot // Setup complete")
                                                view4 = View()
                                                complete = Button(label="Setup complete!", emoji="😎")
                                                complete.disabled = True
                                                view4.add_item(complete)
                                                await inter.response.edit_message(embed=embed, view=view4)
                                    async def yescall4(inter):
                                                with open('inviteguild.json', 'r') as f:
                                                    data = json.load(f)
                                                data[str(inter.guild.id)] = 0
                                                with open('inviteguild.json', 'w') as f:
                                                    data = json.dump(data, f)
                                                await nocall4(inter)

                                
                                    view4 = View()
                                    yesbutton4 = Button(label="Turn on", style=discord.ButtonStyle.green)
                                    nobutton4 = Button(label="Turn off", style=discord.ButtonStyle.red)
                                    yesbutton4.callback = yescall4
                                    nobutton4.callback = nocall4
                                    view4.add_item(yesbutton4)
                                    view4.add_item(nobutton4)
                                    embed=discord.Embed(title="👮‍♂️ | Anti Invite", description="This bot has an anti invite feature that deletes invites from others (without manage messages). You can always toggle it for each channel with **/toggleinvite**. This will only effect the default.", color=0x87ff85)
                                    await inter.response.edit_message(embed=embed, view=view4)


                                async def yescall3(inter):
                                        if not ctx.author.guild_permissions.administrator:
                                            embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
                                            await ctx.respond(embed=embed, ephemeral=True)
                                        else:
                                            with open('spamguild.json', 'r') as f:
                                                data = json.load(f)
                                            data[str(inter.guild.id)] = 0
                                            with open('spamguild.json', 'w') as f:
                                                data = json.dump(data, f)
                                            await nocall3(inter)

                                guild = inter.guild
                                await guild.create_role(name="🎉 | Party Bot Fun")
                                embed=discord.Embed(title="👮‍♂️ | Anti spam", description="This bot has an anti spam feature that allows members (without manage messages) to only send 4 messages before getting timed out for 30s. You can always toggle it for each channel with **/togglespam**. This will only effect the default.", color=0x87ff85)
                                yesbutton3 = Button(label="Turn on", style=discord.ButtonStyle.green)
                                nobutton3 = Button(label="Turn off", style=discord.ButtonStyle.red)
                                yesbutton3.callback = yescall3
                                nobutton3.callback = nocall3
                                view3 = View()
                                view3.add_item(yesbutton3)
                                view3.add_item(nobutton3)
                                await inter.response.edit_message(embed=embed, view=view3)



                    embed=discord.Embed(title=":tada: | Fun Role", description="To use commands like **/sudo** or **/spam**, the user needs the **Party Bot fun role**. Click the button to create it.", color=0x87ff85)
                    view2 = View()
                    continue_button2 = Button(label="Create", style=discord.ButtonStyle.blurple, emoji="▶️")
                    view2.add_item(continue_button2)
                    continue_button2.callback = button_call2
                    await inter.response.edit_message(embed=embed, view=view2)


                        
    continue_button = Button(label="Continue", style=discord.ButtonStyle.blurple, emoji="▶️")
    continue_button.callback = button_call
    view = View()
    view.add_item(continue_button)
    embed=discord.Embed(title=":tada: | Party Bot Setup", description="Thanks for using Party Bot! This is the setup for the bot to make sure everything works correct. Just click through the buttons to continue.", color=0xd485ff)
    await ctx.respond(embed=embed, view=view)


        

@client.slash_command(name = 'kick', description = 'Kicks a member from the server and sends DM')
async def kick(ctx, user: Option(discord.Member), reason: Option(str)):
    if not ctx.author.guild_permissions.kick_members:
            embed=discord.Embed(title=":warning: | You do not have the permission to do that!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)
    elif user.guild_permissions.kick_members:
        embed=discord.Embed(title=":warning: | You can't kick a mod!", color=0xff6b6b)
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        #Kick command
        try:
            guild_icon = ctx.guild.icon.url
            embed=discord.Embed(title=f":cry: | Kicked from **{ctx.guild.name}**", description=f"You have been kicked from **{ctx.guild.name}**. \n**Moderator:** {ctx.author} \n**Reason:** {reason}", color=0xff6b6b)
            embed.set_thumbnail(url=f"{guild_icon}")
            await user.send(embed=embed)
        except Forbidden:
            pass
        try:
            await user.kick(reason=reason)
            embed=discord.Embed(title=f":skull: | Kicked **{user}**", color=0x61ffa5)
            await ctx.respond(embed=embed)
        except Forbidden:
            embed=discord.Embed(title=":warning: | The bot doesn't have enough perms!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)


@client.slash_command(name = 'ban', description = 'Banns a member from the server and sends DM')
async def ban(ctx, user: Option(discord.Member), reason: Option(str)):
    if not ctx.author.guild_permissions.ban_members:
            embed=discord.Embed(title=":warning: | You do not have the permission to do that!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)
    elif user.guild_permissions.ban_members:
        embed=discord.Embed(title=":warning: | You can't ban a mod!", color=0xff6b6b)
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        #Kick command
        try:
            guild_icon = ctx.guild.icon.url
            embed=discord.Embed(title=f":cry: | Banned from **{ctx.guild.name}**", description=f"**Moderator:** {ctx.author} \n**Reason:** {reason}", color=0xff6b6b)
            embed.set_thumbnail(url=f"{guild_icon}")
            await user.send(embed=embed)
        except Forbidden:
            pass
        try:
            await user.ban(reason=reason)
            embed=discord.Embed(title=f":skull: | Banned **{user}**", color=0x61ffa5)
            await ctx.respond(embed=embed)
        except Forbidden:
            embed=discord.Embed(title=":warning: | The bot doesn't have enough perms!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)



@client.slash_command(name = 'clear', description = 'Clears a amount of messages in the channel')
async def kick(ctx, amount: Option(int, max_value=1000, min_value=1)):
    if not ctx.author.guild_permissions.manage_messages:
            embed=discord.Embed(title=":warning: | You do not have the permission to do that!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)
    else:
        await ctx.channel.trigger_typing()
        await ctx.channel.purge(limit=amount)
        embed=discord.Embed(title=f":white_check_mark: | Cleared {amount} messages!", color=0x75ff91)
        await ctx.respond(embed=embed, delete_after=4)


@client.slash_command(name = 'timeout', description = 'Times a member from the server out')
async def timeout(ctx, user: Option(discord.Member), mins: Option(int, min_value=0, max_value=60, Required=False), hours: Option(int, min_value=0, max_value=23, Required=False), days: Option(int, min_value=0, max_value=27, Required=False), reason: Option(str, Required=False)):
    if not ctx.author.guild_permissions.kick_members:
            embed=discord.Embed(title=":warning: | You do not have the permission to do that!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)
    elif user.guild_permissions.kick_members:
        embed=discord.Embed(title=":warning: | You can't timeout a mod!", color=0xff6b6b)
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        #Kick command
        try:
            guild_icon = ctx.guild.icon.url
            embed=discord.Embed(title=f":cry: | Timeout from **{ctx.guild.name}**", description=f"**Moderator:** {ctx.author} \n**Reason:** {reason}", color=0xff6b6b)
            embed.set_thumbnail(url=f"{guild_icon}")
            await user.send(embed=embed)
        except Forbidden:
            pass
        try:
            lange = timedelta(days = days, hours = hours, minutes = mins)
            await user.timeout_for(lange, reason=reason)
            embed=discord.Embed(title=f":skull: | Timeout **{user}**", color=0x61ffa5, description=f"{days}d {hours}h {mins}min")
            await ctx.respond(embed=embed)
        except Forbidden:
            embed=discord.Embed(title=":warning: | The bot doesn't have enough perms!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)


time_window_milliseconds = 4000
max_msg_per_window = 4
author_msg_times = {}



async def antispam(message):
    global author_msg_counts

    author_id = message.author.id
    # Get current epoch time in milliseconds
    curr_time = datetime.datetime.now().timestamp() * 1000

    # Make empty list for author id, if it does not exist
    if not author_msg_times.get(author_id, False):
        author_msg_times[author_id] = []

    # Append the time of this message to the users list of message times
    author_msg_times[author_id].append(curr_time)

    # Find the beginning of our time window.
    expr_time = curr_time - time_window_milliseconds

    # Find message times which occurred before the start of our window
    expired_msgs = [
        msg_time for msg_time in author_msg_times[author_id]
        if msg_time < expr_time
    ]

    # Remove all the expired messages times from our list
    for msg_time in expired_msgs:
        author_msg_times[author_id].remove(msg_time)
    # ^ note: we probably need to use a mutex here. Multiple threads
    # might be trying to update this at the same time. Not sure though.

    if len(author_msg_times[author_id]) > max_msg_per_window:
        if not message.author.guild_permissions.manage_messages:
            lange = timedelta(seconds=30)
            reason = "Anti spam"
            with open('spamguild.json', 'r') as f:
                servers = json.load(f)
            with open('spamchannels.json', 'r') as f:
                channels = json.load(f)
            if str(message.guild.id) in servers and not str(message.channel.id) in channels:
                embed=discord.Embed(title=":triumph: | Antispam", description=f"**{message.author}**, you are not allowed to spam here. Admins can toggle that with **/togglespam**!", color=0xff8585)
                await message.reply(embed=embed)
                await message.author.timeout_for(lange, reason=reason)
                await message.delete()
                return
            elif not str(message.guild.id) in servers and str(message.channel.id) in channels:
                embed=discord.Embed(title=":triumph: | Invites are banned here", description=f"**{message.author}**, you are not allowed spam here. Admins can toggle that with **/togglespam**!", color=0xff8585)
                await message.reply(embed=embed)
                await message.author.timeout_for(lange, reason=reason)
                await message.delete()
                return
            else:
                return
    else:
        pass



async def antinvite(message):
    if not message.author.guild_permissions.manage_messages:
        if 'discord.gg/' in message.content.lower():
            with open('inviteguild.json', 'r') as f:
                servers = json.load(f)
            with open('invite_channels.json', 'r') as f:
                channels = json.load(f)
            if str(message.guild.id) in servers and not str(message.channel.id) in channels:
                embed=discord.Embed(title=":triumph: | Invites are banned here", description=f"**{message.author}**, you are not allowed to send invites here. Admins can toggle invites with **/toggleinvites**!", color=0xff8585)
                await message.reply(embed=embed)
                await message.delete()
            elif not str(message.guild.id) in servers and str(message.channel.id) in channels:
                embed=discord.Embed(title=":triumph: | Invites are banned here", description=f"**{message.author}**, you are not allowed to send invites here. Admins can toggle invites with **/toggleinvites**!", color=0xff8585)
                await message.reply(embed=embed)
                await message.delete()
            else:
                return
    else:
        pass
            
            

async def savegif(message):
    if 'tenor.com/' in message.content.lower():
        with open('gifs.json', 'r') as f:
            data = json.load(f)
        data[str(message.content)] = 0
        with open('gifs.json', 'w') as f:
            data = json.dump(data, f)



@client.event
async def on_message(message):
    await savegif(message)
    await globalchat(message)
    await antispam(message)
    await antinvite(message)
    



@client.slash_command(name="togglespam", description = 'Toggles spam in a channel')
async def togglespam(ctx):
        if not ctx.author.guild_permissions.administrator:
            embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)
        else:
            with open('spamchannels.json', 'r') as f:
                data = json.load(f)
            with open('spamguild.json', 'r') as f:
                guilds = json.load(f)
            if not str(ctx.channel.id) in data:
                data[str(ctx.channel.id)] = 0
                with open('spamchannels.json', 'w') as f:
                    data = json.dump(data, f)
                if str(ctx.guild.id) in guilds:
                    embed=discord.Embed(title=":pencil: | Toggled spam", description="Anti spam is now **disabled** in this channel!", color=0x6bffab)
                    await ctx.respond(embed=embed)
                else:
                    embed=discord.Embed(title=":pencil: | Toggled spam", description="Anti spam is now **enabled** in this channel. Non staff will now be punished for spamming!", color=0x6bffab)
                    #toggled on
                    await ctx.respond(embed=embed)       
            else:
                data.pop(str(ctx.channel.id))
                with open('spamchannels.json', 'w') as f:
                    data = json.dump(data, f)
                if not str(ctx.guild.id) in guilds:
                    embed=discord.Embed(title=":pencil: | Toggled spam", description="Anti spam is now **disabled** in this channel!", color=0x6bffab)
                    await ctx.respond(embed=embed)
                else:
                    embed=discord.Embed(title=":pencil: | Toggled spam", description="Anti spam is now **enabled** in this channel. Non staff will now be punished for spamming!", color=0x6bffab)
                    #toggled on
                    await ctx.respond(embed=embed)



# @client.slash_command(name = 'nick', description = 'Nicks a users. Or /unnick')
# async def nick(ctx, user: Option(discord.Member, Required=True), new_name: Option(str, Required=True)):
#     if not ctx.author.guild_permissions.kick_members:
#         embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
#         await ctx.respond(embed=embed, ephemeral=True)
#     else:
#         await user.edit(nick=f'{new_name}')
#         embed=discord.Embed(title="User nicked!", description=f"**{user}** name has been changed to **{new_name}**! :ok_hand:", color=0xff4d4d)
#         await ctx.respond(embed=embed)

# @client.slash_command(name = 'unnick', description = 'unnicks a user. Or /nick')
# async def unnick(ctx, user: Option(discord.Member, Required=True)):
#     if not ctx.author.guild_permissions.kick_members:
#         embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
#         await ctx.respond(embed=embed, ephemeral=True)
#     else:
#         await user.edit(nick=f'{user.name}')
#         embed=discord.Embed(title="User genickt!", description=f"Unnicked **{user}** to his normal name! :ok_hand:", color=0xff4d4d)
#         await ctx.respond(embed=embed)

@client.slash_command(name="toggleinvites", description = 'Toggles server invites in a channel')
async def togglespam(ctx):
        if not ctx.author.guild_permissions.administrator:
            embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)
        else:
            with open('invite_channels.json', 'r') as f:
                data = json.load(f)
            with open('inviteguild.json', 'r') as f:
                guilds = json.load(f)
            if not str(ctx.channel.id) in data:
                data[str(ctx.channel.id)] = 0
                with open('invite_channels.json', 'w') as f:
                    data = json.dump(data, f)
                if str(ctx.guild.id) in guilds:
                    embed=discord.Embed(title=":pencil: | Toggled invites", description="Anti invite is now **disabled** in this channel!", color=0x6bffab)
                    await ctx.respond(embed=embed)
                else:
                    embed=discord.Embed(title=":pencil: | Toggled invites", description="Anti invite is now **enabled** in this channel. Non staff will now be prevented from sending invites in this channel!", color=0x6bffab)
                    #toggled on
                    await ctx.respond(embed=embed)       
            else:
                data.pop(str(ctx.channel.id))
                with open('invite_channels.json', 'w') as f:
                    data = json.dump(data, f)
                if not str(ctx.guild.id) in guilds:
                    embed=discord.Embed(title=":pencil: | Toggled invites", description="Anti invite is now **disabled** in this channel!", color=0x6bffab)
                    await ctx.respond(embed=embed)
                else:
                    embed=discord.Embed(title=":pencil: | Toggled invites", description="Anti invite is now **enabled** in this channel. Non staff will now be prevented from sending invites in this channel!", color=0x6bffab)
                    #toggled on
                    await ctx.respond(embed=embed)

@client.slash_command(name = 'randomgif', description = 'gets you a random gif')
async def rangif(ctx):
    async def closegif(inter):
        if inter.user == ctx.author:
            await inter.message.delete()
        else:
            embed=discord.Embed(title=":warning: | You aren't the creator of this menu!", color=0xff6161)
            await inter.response.send_message(embed=embed, ephemeral=True)

    async def anothergif(inter):
        randoms = ['Feeling brave!', 'gimme more', 'MORE', 'Lets go', 'we need more', 'more epicness here']
        emos = ['🔥', '👻', '💩', '🎉', '😎', '🥶', '💀', '🤡', '😳']
        view = View()
        another = Button(label=f"{random.choice(randoms)}", emoji=f"{random.choice(emos)}", style=discord.ButtonStyle.blurple)
        another.callback = anothergif
        close = Button(label="Exit")
        close.callback = closegif
        view.add_item(another)
        view.add_item(close)
        if inter.user == ctx.author:
            with open('gifs.json', 'r') as f:
                data = json.load(f)
            gifs = []
            for gif in data:
                gifs.append(gif)
            random_gif = random.choice(gifs)
            await inter.response.edit_message(content=f"{random_gif}", view=view)
        else:
            embed=discord.Embed(title=":warning: | You aren't the creator of this menu!", color=0xff6161)
            await inter.response.send_message(embed=embed, ephemeral=True)

    with open('gifs.json', 'r') as f:
        data = json.load(f)
    gifs = []
    for gif in data:
        gifs.append(gif)

    random_gif = random.choice(gifs)
    view = View()
    another = Button(label="Another one!", emoji="🔥", style=discord.ButtonStyle.blurple)
    close = Button(label="Exit")
    close.callback = closegif
    another.callback = anothergif
    view.add_item(another)
    view.add_item(close)
    await ctx.respond(f'{random_gif}', view=view)






@client.slash_command(name = 'reactiontime', description = 'A reactiontime minigame with 3 buttons')
async def minigame_rr(ctx):
    async def win(inter):
        embed=discord.Embed(title=":game_die: | Minigame: Reactiontime", description=f"**{inter.user}**, has clicked the button the fastest and won the game! :trophy:", color=0xffb35c)
        await inter.response.edit_message(embed=embed, view=None)
    embed=discord.Embed(title=":game_die: | Minigame: Reactiontime", description="Select the button in 3s. (Message will be edited)", color=0xffb35c)
    view = View()
    blue = Button(label="Blue", style=discord.ButtonStyle.blurple)
    green = Button(label="Green", style=discord.ButtonStyle.green)
    red = Button(label="Red", style=discord.ButtonStyle.red)
    view.add_item(blue)
    view.add_item(green)
    view.add_item(red)
    await ctx.respond(embed=embed)
    buttons = ['blue', 'green', 'red']
    real_button = random.choice(buttons)
    if real_button == 'blue':
        blue.callback = win
    if real_button == 'green':
        green.callback = win
    if real_button == 'red':
        red.callback = win
    await asyncio.sleep(3)
    embed=discord.Embed(title=":game_die: | Minigame: Reactiontime", description=f"Click the **{real_button}** button now!!", color=0xffb35c)
    await ctx.edit(embed=embed, view=view)

@client.slash_command(name = 'setglobal', description = 'Toggles globalchat in a text channel')
async def setglobal(ctx, chat: Option(discord.TextChannel)):
    if not ctx.author.guild_permissions.administrator:
            embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)
    else:
        with open('gl.json', 'r') as f:
            data = json.load(f)
        data[str(ctx.guild.id)] = chat.id
        with open('gl.json', 'w') as f:
            data = json.dump(data, f)
        embed=discord.Embed(title=":white_check_mark: | Done! To undo run **/removeglobal**", color=0x66ffa8)
        await ctx.respond(embed=embed)



@client.slash_command(name = 'removeglobal', description = 'Removes globalchat from the server')
async def setglobal(ctx):
    if not ctx.author.guild_permissions.administrator:
            embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
            await ctx.respond(embed=embed, ephemeral=True)
    else:
        with open('gl.json', 'r') as f:
            data = json.load(f)
        data[str(ctx.guild.id)] = 0
        with open('gl.json', 'w') as f:
            data = json.dump(data, f)
        embed=discord.Embed(title=":white_check_mark: | Done! Removed globalchat.", color=0x66ffa8)
        await ctx.respond(embed=embed)

@client.slash_command(guild_ids=edit_guilds, name = 'makestaff', description = 'Makes a person staff')
async def setglobal(ctx, user: Option(discord.Member)):
    if ctx.author.id == 904666156772757524:
        with open('glstaff.json', 'r') as f:
            data = json.load(f)
        data[str(user.id)] = 0
        with open('glstaff.json', 'w') as f:
            data = json.dump(data, f)
        embed=discord.Embed(title=":white_check_mark: | Member made staff!", color=0x66ffa8)
        await ctx.respond(embed=embed)
    else:
        embed=discord.Embed(title=":warning: | You don't have perms!", color=0x66ffa8)
        await ctx.respond(embed=embed, ephemeral=True)


async def globalchat(message):
    if not message.author.bot:
        pic_url=message.author.avatar.url
        try:
            guild_icon = message.guild.icon.url
        except AttributeError:
            guild_icon = 'https://mpng.subpng.com/20180804/bve/kisspng-earth-world-emoji-day-globe-world-emoji-day-file-twemoji2-1f30e-svg-wikimedia-commons-5b65d19d1524f4.2381951915333994530866.jpg'
            
        with open('gl.json', 'r') as f:
            data = json.load(f)
        with open('bannned.json', 'r') as f:
            bans = json.load(f)
        with open('glstaff.json', 'r') as f:
            staff = json.load(f)
        channels = []
        for server in data:
            rn = data[server]
            channels.append(rn)
        embed=discord.Embed(description=f"{message.content} \n\n", color=0x6b84ff)
        embed.set_author(name=f"{message.author}", icon_url=pic_url)
        embed.set_footer(text=f"{message.guild.name} | Channels: {len(data)}", icon_url=guild_icon)




        if message.channel.id in channels:
            if not str(message.author.id) in staff and 'discord.gg/' in message.content.lower():
                embed=discord.Embed(title=":rotating_light: | Message blocked", description="Invites are blocked in globalchat!", color=0xff8080)
                await message.reply(embed=embed, delete_after=4)
                await message.delete()
                return
            for word in bad_words:
                if word in message.content.lower():
                    embed=discord.Embed(title=":rotating_light: | Message blocked", description="Your message contained a word that is banned in the globalchat!", color=0xff8080)
                    await message.reply(embed=embed, delete_after=4)
                    await message.delete()
                    return
            if str(message.author) in bans:
                embed=discord.Embed(title=":rotating_light: | Banned from globalchat", description=f"Reason for your ban: **{bans[str(message.author)]}**", color=0xff8080)
                await message.reply(embed=embed, delete_after=5)
                await message.delete()
            if 'tenor.com/' in message.content.lower():
                embed=discord.Embed(color=0x6b84ff)
                embed.set_author(name=f"{message.author}", icon_url=pic_url)
                embed.set_footer(text=f"{message.guild.name} | Channels: {len(data)}", icon_url=guild_icon)
                fr = get_gif_url(message.content)
                embed.set_image(url=f"{fr}")
                await message.channel.send(embed=embed)
                for ids in channels:
                    if message.channel.id != ids:
                        await client.get_channel(int(ids)).send(embed=embed)
                        await message.delete()
                        return
            with open('glnews.json', 'r') as f:
                glusers = json.load(f)
            if not str(message.author.id) in glusers:
                glusers[str(message.author.id)] = 0
            with open('glnews.json', 'w') as f:
                glusers = json.dump(glusers, f)
            with open('glnews.json', 'r') as f:
                glusers = json.load(f)
            value = glusers[str(message.author.id)]
            if value > 1:
                view = View()
                pass
            else:
                async def welcome_callback(inter):
                    view = View()
                    if inter.user.id in welcomes:
                        embed=discord.Embed(title=":warning: | You can't welcome someone twice!", color=0xffcf24)
                        await inter.response.send_message(embed=embed, ephemeral=True)
                    else:
                        welcomes.append(inter.user.id)
                    if inter.user == message.author:
                        embed=discord.Embed(title=":warning: | You can't welcome yourself", color=0xffcf24)
                        await inter.response.send_message(embed=embed, ephemeral=True)
                    for ids in channels:
                        if message.channel.id != ids:
                            wembed=discord.Embed(title=f":wave: | Welcome {message.author}!", description=f"**{inter.user}** has welcomed you!", color=0xfff266)
                            await inter.response.send_message(embed=wembed, view=None)
                            await client.get_channel(int(ids)).send(embed=wembed, view=None)
                            await message.delete()
                embed.add_field(name=":wave: | New in globalchat", value=f"Click to welcome **{message.author}**!", inline=False)
                view = View()
                welcome = Button(label="Welcome", emoji="👋", style=discord.ButtonStyle.blurple)
                welcome.callback = welcome_callback
                view.add_item(welcome)
                welcomes = []
                welcomes.clear
                with open('glnews.json', 'r') as f:
                    news = json.load(f)
                value = value +1
                news[str(message.author.id)] = value
                with open('glnews.json', 'w') as f:
                    news = json.dump(news, f)
                
            await message.channel.send(embed=embed, view=view)
            for ids in channels:
                if message.channel.id != ids:
                    await client.get_channel(int(ids)).send(embed=embed, view=view)
                    await message.delete()

@client.slash_command(guild_ids=edit_guilds, name = 'gban', description = 'banns a user from globalchat')
async def ban_global(ctx, username: Option(str), reason: Option(str)):
    with open('glstaff.json', 'r') as f:
        staffs = json.load(f)
    if str(ctx.author.id) in staffs:
        with open('bannned.json', 'r') as f:
            bans = json.load(f)
        bans[str(username)] = reason
        with open('bannned.json', 'w') as f:
            bans = json.dump(bans, f)
        embed=discord.Embed(title=f":white_check_mark: | Banned **{username}** from globalchat!", color=0x75ffa3)
        await ctx.respond(embed=embed)
    else:
        await ctx.respond('Only globalchat staff can do that!', ephemeral=True)

@client.slash_command(name = 'rpc', description = 'Invite someone to play rock paper scissors')
async def rpc(ctx):
    async def rpc_rock(inter):
        with open('rpc.json', 'r') as f:
            data = json.load(f)
        if str(inter.message.id) in data:
            if data[str(inter.message.id)] == 'rock':
                embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"Nobody won! Both player chose rock :sob:", color=0xd780ff)
                await inter.response.edit_message(embed=embed, view=None)
            if data[str(inter.message.id)] == 'paper':
                embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"**{inter.user}**, has lost the game! The enemy picked paper :skull:", color=0xd780ff)
                await inter.response.edit_message(embed=embed, view=None)
            if data[str(inter.message.id)] == 'sc':
                embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"**{inter.user}**, has won the game! The enemy picked scissors :trophy:", color=0xd780ff)
                await inter.response.edit_message(embed=embed, view=None, content=None)
        else:
            data[str(inter.message.id)] = 'rock'
            with open('rpc.json', 'w') as f:
                data = json.dump(data, f)
            await inter.response.edit_message(content="1 more player has to choose!")

    async def rpc_paper(inter):
        with open('rpc.json', 'r') as f:
            data = json.load(f)
        if str(inter.message.id) in data:
            if data[str(inter.message.id)] == 'paper':
                embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"Nobody won! Both player chose paper :sob:", color=0xd780ff)
                await inter.response.edit_message(embed=embed, view=None)
            if data[str(inter.message.id)] == 'sc':
                embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"**{inter.user}**, has lost the game! The enemy picked scissors :skull:", color=0xd780ff)
                await inter.response.edit_message(embed=embed, view=None)
            if data[str(inter.message.id)] == 'rock':
                embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"**{inter.user}**, has won the game! The enemy picked rock :trophy:", color=0xd780ff)
                await inter.response.edit_message(embed=embed, view=None, content=None)
        else:
            data[str(inter.message.id)] = 'paper'
            with open('rpc.json', 'w') as f:
                data = json.dump(data, f)
            await inter.response.edit_message(content="1 more player has to choose!")

    async def rpc_sc(inter):
        with open('rpc.json', 'r') as f:
            data = json.load(f)
        if str(inter.message.id) in data:
            if data[str(inter.message.id)] == 'sc':
                embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"Nobody won! Both player chose scissors :sob:", color=0xd780ff)
                await inter.response.edit_message(embed=embed, view=None)
            if data[str(inter.message.id)] == 'rock':
                embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"**{inter.user}**, has lost the game! The enemy picked rock :skull:", color=0xd780ff)
                await inter.response.edit_message(embed=embed, view=None)
            if data[str(inter.message.id)] == 'paper':
                embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"**{inter.user}**, has won the game! The enemy picked paper :trophy:", color=0xd780ff)
                await inter.response.edit_message(embed=embed, view=None, content=None)
        else:
            data[str(inter.message.id)] = 'sc'
            with open('rpc.json', 'w') as f:
                data = json.dump(data, f)
            await inter.response.edit_message(content="1 more player has to choose!")




        
    async def cancel(inter):
        if inter.user != ctx.author:
            embed=discord.Embed(title=":warning: | You aren't the host of the game!", color=0xff7070)
            await inter.response.send_message(embed=embed, view=None, ephemeral=True)
        else:
            await inter.message.delete()

    async def accept(inter):
        if inter.user == ctx.author:
            embed=discord.Embed(title=":warning: | No friends?", color=0xff7070)
            await inter.response.send_message(embed=embed, view=None, ephemeral=True)
        else:
            embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"Play by choosing one of the buttons bellow!", color=0xd780ff)
            view = View()
            rock = Button(label="Rock", emoji="🪨", style=discord.ButtonStyle.blurple)
            paper = Button(label="Paper", emoji="📰", style=discord.ButtonStyle.blurple)
            schere = Button(label="Scissors", emoji="✂️", style=discord.ButtonStyle.blurple)
            rock.callback = rpc_rock
            paper.callback = rpc_paper
            schere.callback = rpc_sc
            view.add_item(rock)
            view.add_item(schere)
            view.add_item(paper)
            await inter.response.edit_message(embed=embed, view=view)
        

    embed=discord.Embed(title=":game_die: | Minigame: RPC", description=f"Click accept to play a game of rock paper scissors with **{ctx.author}**!", color=0xd780ff)
    view = View()
    accept_rpc = Button(label="Accept", emoji="🔍", style=discord.ButtonStyle.green)
    cancel_rpc = Button(label="Cancel", style=discord.ButtonStyle.red)
    cancel_rpc.callback = cancel
    accept_rpc.callback = accept
    view.add_item(accept_rpc)
    view.add_item(cancel_rpc)
    await ctx.respond(embed=embed, view=view)



@client.event
async def on_raw_reaction_add(payload):
    msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    with open('rr.json', 'r')as f:
        data = json.load(f)
    if str(payload.message_id) in data:

        member = payload.member
        guild = member.guild


        roleid = data[str(payload.message_id)] # Gets role id and role object
        role = get(guild.roles, id=roleid)

        await member.add_roles(role) # Adds the role to the member

@client.event
async def on_raw_reaction_remove(payload):
    msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    with open('rr.json', 'r')as f:
        data = json.load(f)
    if str(payload.message_id) in data:   
        guild2 = client.get_guild(payload.guild_id)
        member2 = guild2.get_member(payload.user_id)
        guild = await client.fetch_guild(payload.guild_id)
        roleid = data[str(payload.message_id)] # Gets role id and role object
        role = get(guild.roles, id=roleid)
        await member2.remove_roles(role) # Adds the role to the member






@client.slash_command(name = 'reactionrole', description = 'Creates a reactionrole')
async def rr(ctx, role: discord.Role):
    if not ctx.author.guild_permissions.administrator:
        embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
        await ctx.respond(embed=embed, ephemeral=True)
    else:
        class MyModal(discord.ui.Modal):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(
                    discord.ui.InputText(
                        label="Embed title",
                        placeholder="E.x. Funny reactionrole",
                    ),
                    discord.ui.InputText(
                        label="Embed Description",
                        placeholder="E.x. React to get the funny role! You can always unreact if you wish!",
                        style=discord.InputTextStyle.long,
                    ),
                    *args,
                    **kwargs,
                )

            async def callback(self, interaction: discord.Interaction):
                    title = value=self.children[0].value
                    desc = value=self.children[1].value
                    embed=discord.Embed(title=f"{title}", description=f"{desc}", color=0x8a92ff)
                    msg = await ctx.send(embed=embed)
                    msg_id = msg.id
                    with open('rr.json', 'r') as f:
                        rr = json.load(f)
                    rr[str(msg_id)] = role.id
                    with open('rr.json', 'w') as f:
                        rr = json.dump(rr, f)
                    msg = client.get_message(msg_id)
                    await msg.add_reaction("🟩")
                    embed=discord.Embed(title=":white_check_mark: | Reactionrole created!", color=0x8a92ff)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
        modal = MyModal(title="Reactionrole Embed")
        await ctx.send_modal(modal)


@client.slash_command(name = 'embed', description = 'send an embed from the bot')
async def embed(ctx):
    role = discord.utils.get(ctx.guild.roles, name="🎉 | Party Bot Fun")
    if not role in ctx.author.roles:
        embed=discord.Embed(title=":warning: | You need the FUN role for that", description="If you're an admin you need to give yourself the role or create it with **/setup**!", color=0xffa55c)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    class embedmodal(discord.ui.Modal):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(
                    discord.ui.InputText(
                        label="Embed title",
                        placeholder="E.x. Epic embed",
                    ),
                    discord.ui.InputText(
                        label="Embed Description",
                        placeholder="E.x. Here is the long awaited embed",
                        style=discord.InputTextStyle.long,
                    ),
                    *args,
                    **kwargs,
                )

            async def callback(self, interaction: discord.Interaction):
                title = value=self.children[0].value
                desc = value=self.children[1].value
                embed=discord.Embed(title=f"{title}", description=f"{desc}", color=0x7a83ff)
                await interaction.response.send_message(embed=embed)

    modal = embedmodal(title="Embed builder")
    await ctx.send_modal(modal)



@client.slash_command(name = 'setwelcome', description = 'select a welcome message channel')
async def setwelcome(ctx, channel: discord.TextChannel):
    if not ctx.author.guild_permissions.administrator:
        embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    with open('welcome.json', 'r')as f:
        data = json.load(f)
        class welcomemodal(discord.ui.Modal):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(
                    discord.ui.InputText(
                        label="Message",
                        placeholder="E.x. Welcome to our server! Don't forget the rules!",
                    ),
                    *args,
                    **kwargs,
                )

            async def callback(self, interaction: discord.Interaction):
                msg = value=self.children[0].value
                with open('welcome.json', 'r')as f:
                        data = json.load(f)
                data[str(channel.id)] = msg
                with open('welcome.json', 'w') as f:
                    data = json.dump(data, f)
                embed=discord.Embed(title=":white_check_mark: | All done! New members will be welcomed!", color=0x66ff70)
                await interaction.response.send_message(embed=embed)
    modal = welcomemodal(title="Welcome message")
    await ctx.send_modal(modal)


@client.event
async def on_member_join(member):
    with open('welcome.json') as f:
        data = json.load(f)
    for channel in data:
        ch = discord.utils.get(member.guild.text_channels, id=int(channel))
        embed=discord.Embed(title=":tada: | Member join", description=f"{data[channel]}", color=0x8870ff)
        await ch.send(content=f"<@{member.id}>", embed=embed)



@client.slash_command(name = 'setsuggest', description = 'select a suggestions channel')
async def sel_suggestions(ctx, channel: discord.TextChannel):
    if not ctx.author.guild_permissions.administrator:
        embed=discord.Embed(title=":warning: | You aren't an admin!", color=0xff6b6b)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    with open('suggest.json', 'r') as f:
        data = json.load(f)
    data[str(ctx.guild.id)] = channel.id
    with open('suggest.json', 'w') as f:
        data = json.dump(data, f)
    embed=discord.Embed(title=":white_check_mark: | Suggestion channel set up! ", description="Members will now be able to suggest things with **/suggest**!", color=0x70ffa0)
    await ctx.respond(embed=embed)


@client.slash_command(name = 'suggest', description = 'suggest something for the server')
async def suggest(ctx):
    with open('suggest.json', 'r') as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        embed=discord.Embed(title=":warning: | Suggestions aren't set up!", color=0xff6b6b, description="Before you can suggest an Admin needs to set it up with **/setsuggest**")
        await ctx.respond(embed=embed)
        return
    class suggestionmodal(discord.ui.Modal):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(
                    discord.ui.InputText(
                        label="Suggestion",
                        placeholder="E.x. Fix da server.",
                        style=discord.InputTextStyle.long,
                    ),
                    *args,
                    **kwargs,
                )
            async def callback(self, interaction: discord.Interaction):
                suggestion = value=self.children[0].value
                with open('suggest.json', 'r') as f:
                    data = json.load(f)
                ch = discord.utils.get(ctx.guild.text_channels, id=data[str(ctx.guild.id)])
                embed=discord.Embed(title=f":pencil: | Suggestion by {interaction.user}", description=f"{suggestion}\n \n ", color=0xffdd61)
                embed.add_field(name=":information_source: How to suggest?", value=f"Use **/suggest**, there you can enter your suggestion.", inline=False)
                msg = await ch.send(embed=embed)
                embed=discord.Embed(title=f":pencil: | Send suggestion!", color=0xffdd61, description=f"Send in <#{ch.id}>, others can vote on it now!")
                await interaction.response.send_message(embed=embed)
                await msg.add_reaction("👍")
                await msg.add_reaction("👎")
                


    modal = suggestionmodal(title=f"Suggest to {ctx.guild.name}")
    await ctx.send_modal(modal)



def get_gif_url(view_url):

    # Get the page content
    page_content = requests.get(view_url).text

    # Regex to find the URL on the c.tenor.com domain that ends with .gif
    regex = r"(?i)\b((https?://c[.]tenor[.]com/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))[.]gif)"

    # Find and return the first match
    return re.findall(regex, page_content)[0][0]


@client.slash_command(
    name='ben',
    description='Aks ben any question you want')
async def ball(ctx, frage: Option(str, Required=True)):
    antworten = ['Yes', 'No', 'Hohohoooo', 'UGhhhh', 'ofc yes']
    embed = embed = discord.Embed(description=
        f"**Your question:** {frage} \n**Bens reply:** {random.choice(antworten)}",
        color=0xA020F0)
    embed.set_author(name="Talking Ben", icon_url="https://mobimg.b-cdn.net/v2/fetch/d1/d1d4deb5edf432a65ae4fb7f123faba2.jpeg?w=1000")
    await ctx.respond(embed=embed)

@client.slash_command(name = 'sudo', description = 'Force a user to send a message')
async def sudo(ctx, user: Option(discord.Member), msg: Option(str, Required=True)):
    role = discord.utils.get(ctx.guild.roles, name="🎉 | Party Bot Fun")
    if not role in ctx.author.roles:
        embed=discord.Embed(title=":warning: | You need the FUN role for that", description="If you're an admin you need to give yourself the role or create it with **/setup**!", color=0xffa55c)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    embed=discord.Embed(title=":ok_hand: | Sending message...",
        color=0xA020F0)
    await ctx.respond(embed=embed, ephemeral=True)
    webhook = await ctx.channel.create_webhook(name="Sudo webhook...", reason=f"By: {ctx.author} message: {msg}")
    await webhook.send(username=f"{user.name}", avatar_url=f"{user.avatar.url}", content=f"{msg}")
    await webhook.delete()

@client.slash_command(name = 'addtag', description = 'Creates tag that anyone can view via /tag')
async def tagrr(ctx, name: Option(str, Required=True)):
    with open('tags.json', 'r') as f:
        data=json.load(f)
    try:
            inhalt = data[name]
            print(inhalt)
            embed=discord.Embed(title=":warning: | Name unavaible", description=f"The name is already in use by someone else! If you want to view the tag use **/tag {name}**", color=0xffb561)
            await ctx.respond(embed=embed, ephemeral=True)
    except KeyError:
            class tagmodal(discord.ui.Modal):
                def __init__(self, *args, **kwargs) -> None:
                    super().__init__(
                        discord.ui.InputText(
                            label="Tag name",
                            placeholder="E.x. serverinfo",
                            value=f"{name}"
                        ),
                        discord.ui.InputText(
                            label="Tag content",
                            placeholder="E.x. our server is amazing!",
                            style=discord.InputTextStyle.long,
                        ),
                        *args,
                        **kwargs,
                    )

                async def callback(self, interaction: discord.Interaction):
                    title = value=self.children[0].value
                    desc = value=self.children[1].value
                    embed=discord.Embed(title=f"Tag created!", description=f"Anyone can view it with **/{title}**", color=0x7a83ff)
                    await interaction.response.send_message(embed=embed)
                    with open('tags.json', 'r') as f:
                        data = json.load(f)
                    data[title] = f'{desc}\n**Created by: {interaction.user}**'
                    with open('tags.json', 'w') as f:
                        data = json.dump(data, f, indent=4)
            modal = tagmodal(title="Create tag")
            await ctx.send_modal(modal)



@client.slash_command(name = 'tag', description = 'view a tag')
async def tag(ctx, name: Option(str, Required=True)):
    with open('tags.json', 'r') as f:
        data=json.load(f)
        try:
            inhalt = data[name]
            embed=discord.Embed(title=f"/tag **{name}**", description = f'{inhalt} \n\nIf you would like to create your own tag use **/addtag**! Or view all created tags with **/taglist**', color=0xffb561)
            await ctx.respond(embed=embed)
        except KeyError:
            embed=discord.Embed(title=":warning: | Tag not found!", description = 'You can create a tag with /addtag!', color=0xffb561)
            await ctx.respond(embed=embed, ephemeral=True)

@client.slash_command(name = 'taglist', description = 'Lists all globally created tags.')
async def listtag(ctx):
    with open('tags.json', 'r') as f:
        data = json.load(f)
    tag_names = []
    for tag in data:
        tag_names.append(tag)
    tag_names = str(tag_names).strip('')
    embed=discord.Embed(title=":pencil: | Taglist", description=f"{str(tag_names)}", color=0xffea61)
    embed.add_field(name=":information_source: | View a tag", value="Use **/tag (name)** to view a tags content", inline=False)
    embed.add_field(name=":information_source: | Creating a tag", value="Use **/createtag** to create a tag that anyone can view here and with /tag", inline=False)
    await ctx.respond(embed=embed)

@client.slash_command(guild_ids=edit_guilds, name = 'removetag', description = 'Deletes a tag from the JSON file')
async def tagdel(ctx, name: Option(str, Required=True)):
    if ctx.author.id == 904666156772757524:
        button = Button(label="Confirm", style=discord.ButtonStyle.red)
        async def confirmdel(inter):
            if inter.user == ctx.author:
                try:
                    with open('tags.json', 'r') as f:
                        data = json.load(f)
                    data.pop(str(name))
                    with open('tags.json', 'w') as f:
                        data = json.dump(data, f)
                    embed=discord.Embed(title="Tag deleted!", description=f"The tag **{name}** has been deleted from the JSON file! To create a tag use /addtag.", color=0x80ff9f)
                    await inter.response.edit_message(view=None, embed=embed)
                except KeyError:
                     embed=discord.Embed(title=":warning: | Tag not found!", description = 'Maybe the tag already has been deleted...', color=0xffb561)
                     await inter.response.send_message(embed=embed, ephemeral=True)
            else:
                embed=discord.Embed(title=":warning: | You did not create this button!", color=0xff7a7a)
                await inter.response.send_message(embed=embed, ephemeral=True)
        button.callback = confirmdel
        view = View()
        view.add_item(button)
        with open('tags.json', 'r') as f:
            data=json.load(f)
        inhalt = data[name]
        embed=discord.Embed(title=f"Delete **{name}**?", description = f"{inhalt} \n\n**Please press confirm to delete the tag! This can't be undone.**", color=0xffb561)
        await ctx.respond(embed=embed, view=view)
    else:
        embed=discord.Embed(title=":warning: | Only **Imposter#9309** can do that!", color=0xff7a7a)
        await ctx.respond(embed=embed, ephemeral=True)


client.run(os.getenv('DEV_TOKEN'))