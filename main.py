import discord
from discord import Option
from datetime import timedelta
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import os
import random
import discord.ext.tasks
import json
from keep_alive import keep_alive

intents = discord.Intents.all()
client = discord.Bot(command_prefix='!', intents=intents)

servers = [981237860734742539]


@client.slash_command(guild_ids = servers, name = 'reveal', description = 'Gibt einen Link zum Source Code des Bots')
async def source(ctx):
    embed=discord.Embed(title="Github Repo: https://github.com/AlexGaming32/Party-Bot :cold_face:", color=0xA020F0)
    await ctx.respond(embed=embed)
  
@client.event
async def on_ready():
    print("Bot ist nun online!")


@client.slash_command(guild_ids=servers,
                      name='ping',
                      description='Macht pong und zeigt die Verzögerung an!')
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!",
        description=
        f"{round(client.latency * 1000)} ms Verzögerung :slight_smile:",
        color=0xA020F0)
    await ctx.respond(embed=embed)


@client.slash_command(
    guild_ids=servers,
    name='ben',
    description='Stell Talking Ben eine Frage! :slight_smile: ')
async def ball(ctx, frage: Option(str, Required=True)):
    antworten = [
        'Ja schon', 'no', 'maybe nicht? susy baka', 'Nein du bozo',
        'Jap :thumbsup:', 'Stimme zu! :)', 'Nope', 'Frag ma später nochmal',
        'Nein bruh :skull:', 'Ja defenetiv',
        'Ne, füll deez nuts in dein Mund :sunglasses:',
        'Ja natürlich ||nicht||', 'Ja, klingt gut :flushed:',
        'Nein, so cringe das ich net ma antworten wollte', 'bruh nein :skull:',
        'Iwie hab ich net mal bock zu antworten :yawning_face:'
    ]
    embed = embed = discord.Embed(
        title="Talking Ben:",
        description=
        f"**Deine Frage:** {frage} \n**Bens Antwort:** {random.choice(antworten)}",
        color=0xA020F0)
    await ctx.respond(embed=embed)


@client.slash_command(
    guild_ids=servers,
    name='münzenwurf',
    description='Wirft eine Münze! Entweder du hast Glück oder nicht.')
async def coinflip(ctx):
    varianten = [
        'Du hast Glück gehabt! :four_leaf_clover:',
        'Du hast Pech gehabt! :slight_frown:'
    ]
    embed = discord.Embed(title="Münzenwurf :coin:",
                          description=f"Müzenwurf: {random.choice(varianten)}",
                          color=0xA020F0)
    await ctx.respond(embed=embed)


@client.slash_command(guild_ids=servers,
                      name='random',
                      description='Gibt dir eine zufällige Zahl!')
async def rng(ctx, max: Option(int)):
    embed = discord.Embed(
        title="Random Number",
        description=f"Deine Random Zahl ist: {random.randrange(max)}",
        color=0xbc50eb)
    await ctx.respond(embed=embed)


@client.slash_command(guild_ids=servers,
                      name='clear',
                      description='[Mod] Löscht Nachrichten aus dem Kanal')
@commands.has_role("Party-Bot Admin 😎" or "Admin" or "Party-Bot Mod 🚀")
async def purge(ctx, nachrichten: Option(int, max_value=200, Required=True)):
    if nachrichten < 1:
        embed = discord.Embed(
            title="Fehler!",
            description="Gebe bitte einen Wert zwischen 1-200 an!",
            color=0xfc3003)
        await ctx.respond(embed=embed)
    else:
        nachrichten += 2
        embed = discord.Embed(
            title="Nachrichten Clear!",
            description=
            f"{nachrichten -2} Nachrichten werden gelöscht! Bitte warte kurz :ok_hand:",
            color=0x03adfc)
        await ctx.respond(embed=embed)
        await ctx.channel.purge(limit=nachrichten)


@client.slash_command(guild_ids=servers,
                      name='dm',
                      description='[Fun] Schickt eine DM zum ausgewählten User')
@commands.has_role("Party-Bot Admin 😎" or "Admin" or "Party-Bot Mod 🚀"
                   or "Party-Bot Fun 🎉")
async def send(ctx, user: Option(discord.Member, Required=True),
               msg: Option(str, Required=True)):
    embed = discord.Embed(title="Get Dmed!",
                          description=f"{msg}",
                          color=0xA020F0)
    embed.set_footer(text=f"Geschickt von {ctx.author}")
    await user.send(embed=embed)
    obama = discord.Embed(
        title="Ok!",
        description=f"Benutzer wurde mit einer DM benachrichtigt! :ok_hand:",
        color=0xA020F0)
    await ctx.respond(embed=obama)


@client.slash_command(guild_ids=servers,
                      name='embed',
                      description='[Fun] Schickt ein Embed in dem Channel')

async def embed(ctx, title: Option(str, Required=True),
                msg: Option(str, Required=True)):
    embed = discord.Embed(title=f'{title}',
                          description=f"{msg}",
                          color=0xA020F0)
    embed.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)


@client.slash_command(guild_ids=servers,
                      name='avatar',
                      description='Gibt dir das Profilbild eines Mitglieds')
async def picture(ctx, member: Option(discord.Member, Required=False)):
    member = ctx.author if not member else member
    embed = discord.Embed(title=member)
    embed.set_image(url=member.avatar.url)
    await ctx.respond(embed=embed)


@client.slash_command(guild_ids=servers,
                      name='help',
                      description='Zeigt alle Befehle vom Bot an')
async def help(ctx):
    embed = discord.Embed(
        title='Bot Command Help',
        description=
        '!ping - Macht Pong und zeigt Delay an \n!Ben [Frage] - frag Ben was \n!coin - wirft ne Münze \n!rng [max Zahl] - gibt dir ne zufälligr Zahl \n!dm [user] [msg] - dmed user',
        color=0xd4482c)
    await ctx.respond(embed=embed)
    embed = discord.Embed(
        title='Admin Befehle',
        description=
        '!kick/Ban [@user] [optional: Grund] - kickt User \n!purge [Anzahl] - löscht Anzahl an Nachrichten \n!embed [Nachricht] - schickt n Embed \n!setup - erstellt Rollen für den Bot',
        color=0xf7d219)
    embed.set_footer(text="Bot erstellt von Imposter#9309 // Party Bot")
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    content_raw = message.content.lower()
    with open('words.json', 'r') as f:
        blacklist = json.load(f)
        for word in blacklist:
            if word in content_raw:
                await message.delete()
                embed=discord.Embed(title="Blacklist", description=f"**{message.author}**, Deine Nachricht wurde gelöscht weil sie ein Wort enthielt das ein Admin auf die Blacklist gesetzt hat!", color=0xA020F0)
                await message.channel.send(embed=embed)

        if 'discord.gg/' in message.content:
            embed=discord.Embed(title="Blacklist", description=f"**{message.author}**, Einladungen sind hier verboten!", color=0xA020F0)
            await message.delete()
            await message.channel.send(embed=embed) 

@client.slash_command(guild_ids = servers, name = 'banword', description = '[Admin] Bannt ein Wort vom Server!')
@commands.has_role("Party-Bot Admin 😎")
async def banword(ctx, wort: Option(str, Required=True)):
    with open('words.json', 'r') as f:
        data=json.load(f)
    data[wort] = ctx.guild.name
    with open('words.json', 'w') as f:
        json.dump(data, f)
        embed=discord.Embed(title="Blacklist", description=f"**{ctx.author}**, Du hast das Wort erfolgreich gebannt!", color=0xA020F0)
    await ctx.respond(embed=embed)


@client.slash_command(guild_ids = servers, name = 'kick', description = '[Mod] Kickt ein Mitglied vom Server')
@commands.has_role("Party-Bot Admin 😎" or "Admin" or "Party-Bot Mod 🚀")
async def kick(ctx, mitglied: Option(discord.Member, Required = True), grund: Option(str, Required = False)):
    try:
        embed=discord.Embed(title=f"Kicked!", description=f"Du wurdest von **{ctx.guild.name}** gekickt! \nVon: **{ctx.author}** \nGrund: **{grund}**", color=0xdb0000)
        embed.set_footer(text=f"Party Bot Moderation")
        await mitglied.send(embed=embed)
        await mitglied.kick(reason=grund)
        embed=discord.Embed(title=f"**Moderation**", description=f"**{mitglied}** wurde vom Sever gekickt und hat eine DM erhalten! \nMod: **{ctx.author}** \nGrund: **{grund}**", color=0xdb0000)
        await ctx.respond(embed=embed)
    except discord.Forbidden:
        await mitglied.kick(reason=grund)
        embed=discord.Embed(title=f"**Moderation**", description=f"**{mitglied}** wurde vom Sever gekickt, konnte aber wegen seinen Einstellungen keine DM erhalten! :sob: \nMod: **{ctx.author}** \nGrund: **{grund}**", color=0xdb0000)
        await ctx.respond(embed=embed)

@client.slash_command(guild_ids = servers, name = 'ban', description = '[Admin] Bannt ein Mitglied vom Server')
@commands.has_role("Party-Bot Admin 😎" or "Admin")
async def ban(ctx, mitglied: Option(discord.Member, Required = True), grund: Option(str, Required = False)):
    try:
        embed=discord.Embed(title=f"Gebannt!", description=f"Du wurdest von **{ctx.guild.name}** gebannt! \nVon: **{ctx.author}** \nGrund: **{grund}**", color=0xdb0000)
        embed.set_footer(text=f"Party Bot Moderation")
        await mitglied.send(embed=embed)
        await mitglied.ban(reason=grund)
        embed=discord.Embed(title=f"**Moderation**", description=f"**{mitglied}** wurde vom Sever gebannt und hat eine DM erhalten! \nMod: **{ctx.author}** \nGrund: **{grund}**", color=0xdb0000)
        await ctx.respond(embed=embed)
    except discord.Forbidden:
        await mitglied.kick(reason=grund)
        embed=discord.Embed(title=f"**Moderation**", description=f"**{mitglied}** wurde vom Sever gebannt, konnte aber wegen seinen Einstellungen keine DM erhalten! :sob: \nMod: **{ctx.author}** \nGrund: **{grund}**", color=0xdb0000)
        await ctx.respond(embed=embed)

@client.slash_command(guild_ids = servers, name = 'spam', description = '[Fun] Spammt eine Nachricht in den Kanal')
@commands.has_role("Party-Bot Fun 🎉" or "Party-Bot Admin 😎" or "Admin" or "Party-Bot Mod 🚀")
async def spam(ctx, nachricht: Option(str, Required = True), anzahl: Option(int, max_value=10)):
    embed=discord.Embed(title="Spam :)", description=f"**{ctx.author}** hat einen Spam gestartet, deal with it.", color=0xb243d0)
    await ctx.respond(embed=embed)
    for i in range(anzahl): 
        await ctx.send(nachricht)
      
@client.slash_command(guild_ids = servers, name = 'timeout', description = "[Mod] Timed einen Benutzer aus")
@commands.has_role("Party-Bot Mod 🚀")
async def timeout(ctx, mitglied: Option(discord.Member, required = True), grund: Option(str, required = False), tage: Option(int, max_value = 27, default = 0, required = False), stunden: Option(int, default = 0, required = False), min: Option(int, default = 0, required = False), sec: Option(int, default = 0, required = False)): 
    lange = timedelta(days = tage, hours = stunden, minutes = min, seconds = sec)
    await mitglied.timeout_for(lange, reason = grund)
    embed=discord.Embed(title=f"**Moderation**", description=f"**{mitglied}** wurde vom Server gestummt! \nMod: **{ctx.author}** \nGrund: **{grund}**\nLänge: {tage}T {stunden}H {min}M {sec}S", color=0xdb0000)
    await ctx.respond(embed=embed)
    embed=discord.Embed(title=f"**Gemuted!**", description=f"Du wurdest von {ctx.guild.name} gestummt! \nMod: **{ctx.author}** \nGrund: **{grund}**\nLänge: {tage}T {stunden}H {min}M {sec}S", color=0xdb0000)
    embed.set_footer(text=f"Party Bot Moderation")
    await mitglied.send(embed=embed)

keep_alive()

token = os.environ['TOKEN']

client.run(token)