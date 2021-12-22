# bot.py
import os
import asyncio
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()

client = discord.Client(intents=intents)

channelId=os.getenv('Meal_Polls')

admin =['ramit','sujoy','ujjaldas','lolwakiholwa']


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD :
            break

    print(
            f'{client.user} has connected to Discord!\n'
            f'{guild.name}(id: {guild.id})\n'
            )


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hi {member.name}, welcome to IMSc, Mess!'
            )
    for guild in client.guilds:
        if guild.name == GUILD :
            break
        
    members ='\n - '.join([member.name for member in guild.members]) 
    print(f'Guild Members :\n -{members}')

@client.event
async def on_message(message):
    if message.author==client.user :
       return  
    sorig=message.content
    str=sorig.lower()
    slist=str.split(' ')
    if 'hi' == slist[0] or 'hey' == slist[0]:
       print(message)
       await message.channel.send(f'Hey {message.author.mention} :eyes:')
    if '!poll' == slist[0] :
      if message.channel.id == int(channelId) :
         #print(f'{message} author is {message.author}')
         if message.author.name in admin or message.author.nick in admin :
            msg= await message.channel.send(sorig.split(' ',1)[1]+' Tomorrow?')
            await msg.add_reaction('\N{THUMBS UP SIGN}')
            #await msg.add_reaction('\N{THUMBS DOWN SIGN}')
            await asyncio.sleep(10)
            users=[]
            updated_message = await msg.channel.fetch_message(msg.id)
            for r in updated_message.reactions:
               print(r.count)

               if r.emoji == "\N{THUMBS UP SIGN}":
                  u = await r.users().flatten()
                  users.extend(u)
            n=[]
            for u in users :
                n.append(u.name)
            print(n)


client.run(TOKEN)
