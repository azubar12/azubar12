from ast import Try
from distutils import command
from email import message
import json
from distutils.log import error
from multiprocessing.connection import Client
from turtle import update
from async_timeout import asyncio
import discord
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='.')

#Start bot
@client.event
async def on_ready(self):
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Bar server!'))
    print('Bot is online.')

#PingPong
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#Clear
@client.command()
async def clear5(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clear10(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clear15(ctx, amount=15):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clear20(ctx, amount=20):
    await ctx.channel.purge(limit=amount)

#Kick+Ban
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def massunban(ctx):
    banlist = await ctx.guild.ban()
    for users in banlist:
        try:
            await ctx.guild.unban(user=users.user)
        except:
            pass
    await ctx.send("Mass unbanning")

#SlowMode
@client.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

#Nickname
@client.command(pass_content=True)
async def changenick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

#Suggestion
@client.command()
async def suggestion(ctx,*,message):
    emb=discord.Embed(title="suggestion", description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('✅')
    await msg.add_reaction('✖️')

#Mute
@client.command()
async def mute(ctx, member:discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    guild = ctx.guild
    if role not in guild.rules:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", premissions=perms)
        await member.add_roles(role)
        await ctx.send(f"{member} was muted.")
    else:
        await member.add_roles(role)
        await ctx.send(f"{member} was mutrd.")

#Token
client.run('OTMzNjg2OTUwMTIzMTYzNjU4.YelJuw.tmrwF7SrX2z0x27V4FrWGUaZs00')