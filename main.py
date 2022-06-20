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
from discord.ui import Button, View

noperms=discord.Embed(title="Fehler!", description="**{ctx.author}**, du hast nicht die Berechtigung diesen Befehl auszuführen!", color=0xff2e2e)

intents = discord.Intents.all()
client = discord.Bot(command_prefix='!', intents=intents)

servers = [977632897840349204]


@client.slash_command(name = 'reveal', description = 'Gibt einen Link zum Source Code des Bots')
async def source(ctx):
    embed=discord.Embed(title="Command offline wegen Bug!", color=0xA020F0)
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
                      name='dm',
                      description='[Fun] Schickt eine DM zum ausgewählten User')
async def send(ctx, user: Option(discord.Member, Required=True),
               msg: Option(str, Required=True)):
               if ctx.author != 937870654869499955:
                    embed = discord.Embed(title="Get Dmed!",
                                        description=f"{msg}",
                                        color=0xA020F0)
                    embed.set_footer(text=f"Geschickt von {ctx.author}")
                    await user.send(embed=embed)
                    obama = discord.Embed(
                        title="Ok!",
                        description=f"Benutzer wurde mit einer DM benachrichtigt! :ok_hand:",
                        color=0xA020F0)
                    await ctx.respond(embed=obama, ephemeral=True)






@client.slash_command(
                      name='avatar',
                      description='Gibt dir das Profilbild eines Mitglieds')
async def picture(ctx, member: Option(discord.Member, Required=False)):
    member = ctx.author if not member else member
    embed = discord.Embed(title=member)
    embed.set_image(url=member.avatar.url)
    await ctx.respond(embed=embed)





@client.slash_command(name = 'spam', description = '[Fun] Spammt eine Nachricht in den Kanal')
@commands.has_role("Party-Bot Fun 🎉" or "Party-Bot Admin 😎" or "Admin" or "Party-Bot Mod 🚀")
async def spam(ctx, nachricht: Option(str, Required = True), anzahl: Option(int, max_value=10)):
    embed=discord.Embed(title="Spam :)", description=f"**{ctx.author}** hat einen Spam gestartet, deal with it.", color=0xb243d0)
    await ctx.respond(embed=embed)
    for i in range(anzahl): 
        await ctx.send(nachricht)
    




@client.slash_command(name = 'button', description = 'Erstellt n epischen Knopf')
@commands.has_role("Party-Bot Fun 🎉" or "Party-Bot Admin 😎" or "Admin" or "Party-Bot Mod 🚀")
async def vbux(ctx, url: Option(str, Required=True), text: Option(str, Required=True)):
    button = Button(label="Drück", url=f"{url}", emoji="😎")
    view = View()
    view.add_item(button)
    await ctx.send(f"{text}", view=view)

@client.slash_command(name = 'umfrage', description = 'useless feature')
async def source(ctx):
    embed=discord.Embed(title="Command offline wegen Bug!", color=0xA020F0)
    await ctx.send(embed=embed)






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
  if isinstance(message.channel, discord.channel.DMChannel):
        if message.author.id != 980078681911337001:
            await message.reply(':exploding_head:')
        else:
            pass
  else:
        content_raw = message.content.lower()
        with open('words.json', 'r') as f:
            blacklist = json.load(f)
            if message.guild.id == 981237860734742539:
                if message.channel.id != 985881293470445568:
                    if message.channel.id != 981239866459320450:
                        for word in blacklist:
                            if word in content_raw:
                                embed=discord.Embed(title="Blacklist", description=f"**{message.author}**, Deine Nachricht wurde gelöscht weil sie ein Wort enthielt was ein Admin auf die Blacklist gesetzt hat!", color=0xA020F0)
                                await message.delete()
                                await message.channel.send(embed=embed)
                            else:
                                    if message.channel.id == 985881293470445568:
                                        await message.add_reaction("<:Yes:985891312874172466>")
                                        await message.add_reaction("<:No:985891311410348062>")
                                        embed=discord.Embed(title="Blacklist", description=f"**{message.author}**, Deine Nachricht wurde gelöscht weil sie ein Wort enthielt das ein Admin auf die Blacklist gesetzt hat!", color=0xA020F0)
                                        await message.channel.send(embed=embed)
            
        if 'discord.gg/' in message.content:
            if message.guild.id == 981237860734742539:
                    if message.channel.id != 981239866459320450:
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
    while 1 + 1 == 2:
        await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} Server | /help"))
        await asyncio.sleep(13)
        await client.change_presence(activity=discord.Game(name="Susy stuff | /help"))
        await asyncio.sleep(6)
        await client.change_presence(activity=discord.Game(name="Python | /help"))
        await asyncio.sleep(6)


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "🎉・member-joins":
            embed=discord.Embed(title="Neues Mitglied! :tada:", description=f"**{member}**, ist dem Server nun beigetreten! Viel Spaß hier. Vergiss nicht <#984871989770608730> und <#981239068006428722> zu lesen.")
            embed.set_footer(text="Party Bot // Member Joins")
            await channel.send(embed=embed)
    role_id = 981248663466680390
    role = member.guild.get_role(role_id)
    await member.add_roles(role)

@client.slash_command(name = 'vorschlag', description = 'Erstellt ein Vorschlag für den Server')
async def vorschlag(ctx, vorschlag: Option(str, Required=True)):
    for channel in ctx.guild.channels:
        if str(channel) == "✅・vorschläge":
            embed=discord.Embed(title=f"{ctx.author}'s Vorschlag", description=f"``{vorschlag}``", color=0x7094ff)
    embed.add_field(name="Wie schlage ich vor?", value="Gehe zu einem Chat und mache /vorschlag (dein Vorschlag). Er wird anschließend hier gepostet!", inline=True)
    await channel.send(embed=embed)
    embed=discord.Embed(title="Ok!", description="Danke für den Vorschlag das Team wird entscheiden ob deine Idee umgesetzt wird! Mitglieder können im Vorschläge Kanal abstimmen! :ok_hand: ", color=0x8170ff)
    await ctx.respond(embed=embed)

@client.command()
async def vbux(ctx):
    button = Button(label="Useless", url="https://www.youtube.com/watch?v=XgUB3lF9IQA", emoji="😎")
    
    async def button_callback(interaction):
        await interaction.response.send_message('sus!')

    button.callback = button_callback

    view = View()
    view.add_item(button)
    await ctx.respond("Heheheha", view=view)
    
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
    embed = embed = discord.Embed(description=
        f"**Deine Frage:** {frage} \n**Bens Antwort:** {random.choice(antworten)}",
        color=0xA020F0)
    embed.set_author(name="Talking Ben", icon_url="https://mobimg.b-cdn.net/v2/fetch/d1/d1d4deb5edf432a65ae4fb7f123faba2.jpeg?w=1000")
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


@client.slash_command(name='clear', description='[Mod] Löscht Nachrichten aus dem Kanal')
async def purge(ctx, nachrichten: Option(int, max_value=200, Required=True)):
    if ctx.author.guild_permissions.manage_messages:
        if nachrichten < 1:
            embed = discord.Embed(
                title="Fehler!",
                description="Gebe bitte einen Wert zwischen 1-200 an!",
                color=0xfc3003)
            await ctx.respond(embed=embed)
        else:
            nachrichten += 1
            embed = discord.Embed(
                title="Nachrichten Clear!",
                description=
                f"{nachrichten -1} Nachrichten werden gelöscht! Bitte warte kurz :ok_hand:",
                color=0x03adfc)
            await ctx.respond(embed=embed)
            await ctx.channel.purge(limit=nachrichten)
    else:
        await ctx.respond(embed=noperms)

@client.slash_command(name='embed', description='[Fun] Schickt ein Embed in dem Channel')
async def embed(ctx, title: Option(str, Required=True), msg: Option(str, Required=True)):
    if ctx.author.guild_permissions.manage_messages:
        embed = discord.Embed(title=f'{title}',
                            description=f"{msg}",
                            color=0xA020F0)
        await ctx.respond(embed=embed)
    else:
        await ctx.respond(embed=noperms)


@client.slash_command(name = 'kick', description = '[Mod] Kickt ein Mitglied vom Server')
async def kick(ctx, mitglied: Option(discord.Member, Required = True), grund: Option(str, Required = False)):
    if ctx.author.guild_permissions.kick_members:
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
    else:
        await ctx.respond(embed=noperms)

@client.slash_command(name = 'ban', description = '[Admin] Bannt ein Mitglied vom Server')
async def ban(ctx, mitglied: Option(discord.Member, Required = True), grund: Option(str, Required = False)):
    if ctx.author.guild_permissions.ban_members:
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
    else:
        ctx.respond(embed=noperms)

@client.slash_command(name = 'timeout', description = "[Mod] Timed einen Benutzer aus")
async def timeout(ctx, mitglied: Option(discord.Member, required = True), grund: Option(str, required = False), tage: Option(int, max_value = 27, default = 0, required = False), stunden: Option(int, default = 0, required = False), min: Option(int, default = 0, required = False), sec: Option(int, default = 0, required = False)):
    if ctx.author.guild_permissions.kick_members:
        lange = timedelta(days = tage, hours = stunden, minutes = min, seconds = sec)
        await mitglied.timeout_for(lange, reason = grund)
        embed=discord.Embed(title=f"**Moderation**", description=f"**{mitglied}** wurde vom Server gestummt! \nMod: **{ctx.author}** \nGrund: **{grund}**\nLänge: {tage}T {stunden}H {min}M {sec}S", color=0xdb0000)
        await ctx.respond(embed=embed)
        embed=discord.Embed(title=f"**Gemuted!**", description=f"Du wurdest von {ctx.guild.name} gestummt! \nMod: **{ctx.author}** \nGrund: **{grund}**\nLänge: {tage}T {stunden}H {min}M {sec}S", color=0xdb0000)
        embed.set_footer(text=f"Party Bot Moderation")
        await mitglied.send(embed=embed)
    else:
        ctx.respond(embed=noperms)

@client.slash_command(name = 'nick', description = '[Mod] nickt einen User')
@commands.has_role("Party-Bot Mod 🚀")
async def nick(ctx, user: Option(discord.Member, Required=True), neuer_name: Option(str, Required=True)):
    await user.edit(nick=f'{neuer_name}')
    embed=discord.Embed(title="User genickt!", description=f"Der Name von **{user}** wurde erfolgreich zu **{neuer_name}** geändert! :ok_hand:", color=0xff4d4d)
    await ctx.respond(embed=embed)


@client.slash_command(name = 'unnick', description = '[Mod] unnickt einen User')
@commands.has_role("Party-Bot Mod 🚀")
async def nick(ctx, user: Option(discord.Member, Required=True)):
    await user.edit(nick=f'{user.name}')
    embed=discord.Embed(title="User genickt!", description=f"Der Name von **{user}** wurde erfolgreich zurück zu seinen normalen Namen zurückgesetzt! :ok_hand:", color=0xff4d4d)
    await ctx.respond(embed=embed)




@client.slash_command(name = 'sudo', description = '[Fun] Sendet eine Nachricht vom anderen User')
@commands.has_role("Party-Bot Fun 🎉" or "Party-Bot Admin 😎" or "Admin" or "Party-Bot Mod 🚀")
async def sudo(ctx, user: Option(discord.Member), msg: Option(str, Required=True)):
    embed=discord.Embed(title=":ok_hand: | Sende Nachricht, bitte warte...")
    await ctx.respond(embed=embed, ephemeral=True)
    webhook = await ctx.channel.create_webhook(name="Bitte warten...", reason=f"Von: {ctx.author} msg: {msg}")
    await webhook.send(username=f"{user.name}", avatar_url=f"{user.avatar.url}", content=f"{msg}")
    await webhook.delete()
  

@client.slash_command(name = 'serverlist', description = 'Zeigt an auf wie vielen Server ich bin')
async def serverlist(ctx):
    embed=discord.Embed(title=f"{len(client.guilds)} Server", description=f'Ich bin auf {len(client.guilds)} Servern aktiv! Liste: \n', color=0x66ffa1)
    await ctx.respond(embed=embed)
    await ctx.channel.send('\n'.join(guild.name for guild in client.guilds))

@client.slash_command(name = 'createinv', description = 'Erstellt Invites')
async def createinv(ctx):
    if ctx.author.id == 904666156772757524:
        await ctx.respond('Gebe invites...', ephemeral=True)
        for guild in client.guilds:
            discord_guild = client.get_guild(int(guild.id))
            link = await discord_guild.text_channels[0].create_invite()
            await ctx.send(link)
    else:
        await ctx.respond('Nur Imposter#9309 kann das tuen.')


keep_alive()

token = os.environ['TOKEN']

client.run(token)
