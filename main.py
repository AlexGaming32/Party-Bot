import discord
from discord import Option
from datetime import timedelta
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import os
import random
import discord.ext.tasks
import json
from webserver import keep_alive
import asyncio


intents = discord.Intents.all()
client = discord.Bot(command_prefix='!', intents=intents)

servers = [977632897840349204]


@client.slash_command(name = 'reveal', description = 'Gibt einen Link zum Source Code des Bots')
async def source(ctx):
    embed=discord.Embed(title="Github Repo: https://github.com/AlexGaming32/Party-Bot :cold_face:", color=0xA020F0)
    await ctx.respond(embed=embed)
  



@client.slash_command(
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


@client.slash_command(
                      name='random',
                      description='Gibt dir eine zufällige Zahl!')
async def rng(ctx, max: Option(int)):
    embed = discord.Embed(
        title="Random Number",
        description=f"Deine Random Zahl ist: {random.randrange(max)}",
        color=0xbc50eb)
    await ctx.respond(embed=embed)


@client.slash_command(
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


@client.slash_command(
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


@client.slash_command(
                      name='embed',
                      description='[Fun] Schickt ein Embed in dem Channel')

async def embed(ctx, title: Option(str, Required=True),
                msg: Option(str, Required=True)):
    embed = discord.Embed(title=f'{title}',
                          description=f"{msg}",
                          color=0xA020F0)
    await ctx.respond(embed=embed)


@client.slash_command(
                      name='avatar',
                      description='Gibt dir das Profilbild eines Mitglieds')
async def picture(ctx, member: Option(discord.Member, Required=False)):
    member = ctx.author if not member else member
    embed = discord.Embed(title=member)
    embed.set_image(url=member.avatar.url)
    await ctx.respond(embed=embed)

@client.slash_command(name = 'kick', description = '[Mod] Kickt ein Mitglied vom Server')
@commands.has_role("Party-Bot Mod 🚀")
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

@client.slash_command(name = 'ban', description = '[Admin] Bannt ein Mitglied vom Server')
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

@client.slash_command(name = 'spam', description = '[Fun] Spammt eine Nachricht in den Kanal')
@commands.has_role("Party-Bot Fun 🎉" or "Party-Bot Admin 😎" or "Admin" or "Party-Bot Mod 🚀")
async def spam(ctx, nachricht: Option(str, Required = True), anzahl: Option(int, max_value=10)):
    embed=discord.Embed(title="Spam :)", description=f"**{ctx.author}** hat einen Spam gestartet, deal with it.", color=0xb243d0)
    await ctx.respond(embed=embed)
    for i in range(anzahl): 
        await ctx.send(nachricht)
      
@client.slash_command(name = 'timeout', description = "[Mod] Timed einen Benutzer aus")
@commands.has_role("Party-Bot Mod 🚀")
async def timeout(ctx, mitglied: Option(discord.Member, required = True), grund: Option(str, required = False), tage: Option(int, max_value = 27, default = 0, required = False), stunden: Option(int, default = 0, required = False), min: Option(int, default = 0, required = False), sec: Option(int, default = 0, required = False)): 
    lange = timedelta(days = tage, hours = stunden, minutes = min, seconds = sec)
    await mitglied.timeout_for(lange, reason = grund)
    embed=discord.Embed(title=f"**Moderation**", description=f"**{mitglied}** wurde vom Server gestummt! \nMod: **{ctx.author}** \nGrund: **{grund}**\nLänge: {tage}T {stunden}H {min}M {sec}S", color=0xdb0000)
    await ctx.respond(embed=embed)
    embed=discord.Embed(title=f"**Gemuted!**", description=f"Du wurdest von {ctx.guild.name} gestummt! \nMod: **{ctx.author}** \nGrund: **{grund}**\nLänge: {tage}T {stunden}H {min}M {sec}S", color=0xdb0000)
    embed.set_footer(text=f"Party Bot Moderation")
    await mitglied.send(embed=embed)

@client.slash_command(name = 'realmrang', description = "Gibt dir den MC Rang im DC Server")
async def rang(ctx, code: Option(str, Required=True)):
    dia_role = discord.utils.get(ctx.author.guild.roles, name = 'Diamond')
    znow_role = discord.utils.get(ctx.author.guild.roles, name = 'Znowunity')
    iron_role = discord.utils.get(ctx.author.guild.roles, name = 'Eisen')
    with open('znow.json', 'r') as f:
        znow = json.load(f)
    with open('dia.json', 'r') as f:
        dia = json.load(f)
    with open('iron.json', 'r') as f:
        iron = json.load(f)
    with open('used.json', 'r') as f:
        used = json.load(f)

    if code in used:
        embed=discord.Embed(title="Fehler!", description="Der Code den du gerade angegeben hast wurde schon von einem Benutzer eingelöst! Wenn du denkst dies sei ein Fehler melde dich beim Support!", color=0xed0202)
        await ctx.respond(embed=embed)
        return
    if code in znow:
        embed=discord.Embed(title="Rang Eingelöst!", description="Du hast den Code erfolgreich einglöst und hast den **Znowunity** Rang erhalten! :tada:", color=0x02ed06)
        await ctx.respond(embed=embed)
        await ctx.author.edit(nick=f'[Znowunity] {ctx.author.name}')
        await ctx.author.add_roles(znow_role)
        await use_rank(code)
        return
    if code in dia:
        embed=discord.Embed(title="Rang Eingelöst!", description="Du hast den Code erfolgreich einglöst und hast den **Diamond** Rang erhalten! :tada:", color=0x02ed06)
        await ctx.respond(embed=embed)
        await ctx.author.edit(nick=f'[Diamond] {ctx.author.name}')
        await ctx.author.add_roles(dia_role)
        await use_rank(code)
        return
    if code in iron:
        embed=discord.Embed(title="Rang Eingelöst!", description="Du hast den Code erfolgreich einglöst und hast den **Eisen** Rang erhalten! :tada:", color=0x02ed06)
        await ctx.respond(embed=embed)
        await ctx.author.edit(nick=f'[Eisen] {ctx.author.name}')
        await ctx.author.add_roles(iron_role)
        await use_rank(code)
        return
    else:
        embed=discord.Embed(title="Fehler!", description="Der Code den du gerade angegeben hast ist entweder ungültig! Wenn du denkst dies sei ein Fehler melde dich beim Support!", color=0xed0202)
        await ctx.respond(embed=embed)
        return

async def use_rank(code):
    with open('used.json', 'r') as f:
        data = json.load(f)
    data[code] = 0
    with open('used.json', 'w') as f:
        data = json.dump(data, f)

@client.command()
async def vcspam(ctx):
    vc = ctx.author.voice.channel
    await vc.connect()
    await ctx.voice_client.disconnect()

@client.event
async def on_message(message):
    content_raw = message.content.lower()
    with open('words.json', 'r') as f:
        blacklist = json.load(f)
        if message.guild.id == 981237860734742539:
            for word in blacklist:
                if word in content_raw:
                        await message.delete()
                        embed=discord.Embed(title="Blacklist", description=f"**{message.author}**, Deine Nachricht wurde gelöscht weil sie ein Wort enthielt das ein Admin auf die Blacklist gesetzt hat!", color=0xA020F0)
                        await message.channel.send(embed=embed)

    if 'discord.gg/' in message.content:
    	if message.guild.id == 981237860734742539:
            embed=discord.Embed(title="Blacklist", description=f"**{message.author}**, Einladungen sind hier verboten!", color=0xA020F0)
            await message.delete()
            await message.channel.send(embed=embed)


@client.slash_command(name = 'banword', description = '[Admin] Bannt ein Wort vom Server!')
@commands.has_role("Party-Bot Admin 😎")
async def banword(ctx, wort: Option(str, Required=True)):
    with open('words.json', 'r') as f:
        data=json.load(f)
    data[wort] = ctx.guild.name
    with open('words.json', 'w') as f:
        json.dump(data, f)
        embed=discord.Embed(title="Blacklist", description=f"**{ctx.author}**, Du hast das Wort erfolgreich gebannt!", color=0xA020F0)
    await ctx.respond(embed=embed)



@client.slash_command(name = 'invite', description = 'Läst dich einen Bot mit seiner ID einladen!')
async def invite(ctx, bot_id: Option(str, Required=True)):
    embed=discord.Embed(title="Bot Invite", description="Hier sind die Einladungen zu den Bot den du in der ID angegeben hast! Falls du mich zu deinem Server einladen möchtest, schaue bei meinem Profil vorbei!", color=0x8a5cf5)
    embed.add_field(name=":busts_in_silhouette: Invite ohne Rechte", value=f"https://discord.com/api/oauth2/authorize?client_id={bot_id}&permissions=0&scope=applications.commands%20bot", inline=False)
    embed.add_field(name=":shield: Invite + Admin", value=f"https://discord.com/api/oauth2/authorize?client_id={bot_id}&permissions=8&scope=applications.commands%20bot", inline=False)
    embed.add_field(name=":closed_book: ID von Bots", value="Falls du die ID von einem Bot nicht weißt: rechts klicke auf den Bot und unten ID kopieren, auf Handy: Bot halten und ID kopieren. Du muss dafür Entwicklermodus an haben: Einstellungen > Erweitert > Entwicklermodus", inline=False)
    await ctx.respond(embed=embed)

@client.slash_command(name='help', description='Zeigt alle Befehle vom Bot an')
async def help(ctx):
    embed=discord.Embed(title="Party Bot Commands", description="**Hier sind alle Befehle für den Bot!**\n\nAdmin braucht die 'Party-Bot Admin 😎' Rolle \nMod braucht die : 'Party-Bot Mod 🚀' Rolle \nFun braucht die : 'Party-Bot Fun 🎉' Rolle \n ", color=0xb870ff)
    embed.add_field(name="Admin", value="/ban - Bannt User \n/banword - Sperrt ein Wort vom Server", inline=False)
    embed.add_field(name="Moderator", value="/kick - Kickt User \n/timeout - timed User aus \n/clear - Löscht Nachrichten aus Kanal", inline=False)
    embed.add_field(name="Fun", value="/dm - Schickt eine DM zu einen User\n/embed - Erstellt ein Embed \n/spam - Spammt eine Nachricht", inline=False)
    embed.add_field(name="User", value="/avatar - Gibt dir ein Profilbild\n/help - Alle Befehle Liste\n/münzenwurf - wirft ne Münze\n/random - gibt dir eine random Zahl\n/reveal - Gibt den Quellcode des Bots \n/ping - Zeigt Verzögerung an\n/ben - frag Ben eine Frage\n/realmrang - Gibt dir einen Rang vom Realm auf DC\n/invite - Gibt dir n Invite Link zu einem Bot deiner Wahl", inline=False)

    await ctx.respond(embed=embed)


@client.event
async def on_ready():
    print("Bot ist nun online!")
  


keep_alive()

token = os.environ['TOKEN']

client.run(token)