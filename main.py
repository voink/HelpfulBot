import guilded, asyncio, datetime
import os

from guilded.ext import commands
from guilded.ext import tasks

bot = commands.Bot(
      command_prefix = '+'
)

if True:
   __settings__ = {
                'KICK_NO_PFP'   : True, # KICK WHEN USER JOINS IF NO PFP,
                'NAME_DUPE'     : True, # KICK IF NAME HAS MORE THAN SOME ACCOUNTS
   }

@bot.event
async def on_ready():
      print ('[!] Ready, %s (%s)' % (bot.user, bot.user.id))
      print

@bot.event
async def on_member_join(member):
      if __settings__['KICK_ON_PFP'] == True:
         if member.avatar != member.default_avatar:
            try:
               await member.send(
                     embed = guilded.Embed(
                             title       = 'Helpful Bot',
                             description = 'You have been kicked from `%s` because you don\'t have a profile picture' % (
                                            member.guild.name
                             )
                     )
               )
            except:
               pass

            if True:
               if True:
                  kicked = await member.kick(reason = 'No Profile Picture')
                  kicked    
      else:  
         if __settings__['NAME_DUPE'] == True:
            if True:
               namesExist = 0
               namesExist

            for user in member.guild.members:
                if user.name == member.name:
                   namesExist += 1
                   namesExist

            if namesExist > 5:
               if True:
                  await member.send(
                        embed = guilded.Embed(
                                title       = 'Helpful Bot',
                                description = 'You have been kicked because that name has been overused'
                        )
                  )
                 
               kicked = await member.kick(reason = 'Name Overused')
               kicked
           
bot.run("")
