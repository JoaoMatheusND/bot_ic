from disnake.ext import commands

class Slash(commands.Cog):
  def __init_(self,bot):
    self.bot = bot

  @commands.slash_command(description="Responds with 'World'")
  async def hello(self, inter):
    await inter.response.send_message("World")

  @commands.slash_command(description="Responds with 'World'")
  async def hello(self, inter):
    await inter.response.send_message("World")  
  

  

def setup(bot):
  bot.add_cog(Slash(bot))  