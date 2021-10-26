import disnake
from embeds import thumb_ic, cor
from disnake.ext import commands
from replit import db

"""db["r"]="\n" #key to red
db["y"]="\n" #key to yellow
db["g"]="\n" #key to green"""

emoji = ['🔴', '🟡', '🟢']

class List(commands.Cog):
  def __init__(self, client):
    self.bot = client

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    channel = await self.bot.fetch_channel(893309560322924575)
    #message = await channel.fetch_message(902262750934364190)
    message_now = await channel.fetch_message(payload.message_id)
    react = str(payload.emoji)

    if payload.channel_id == 875926997455503440:#893309560322924575:

      async for x in self.bot.logs_from(channel):
        if x.embeds:
          await self.bot.message_delete(x)
      
      if react == emoji[0]:
        value = db["r"]
        value.join(message_now.content)

      if react == emoji[1]:
        value = db["y"]
        value.join(message_now.content)

      if react == emoji[2]:
        value = db["g"]
        value.join(message_now.content)
    await message_now.channel.send(embed=lista)
    
def setup(bot):
  bot.add_cog(List(bot))