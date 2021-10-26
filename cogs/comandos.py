import disnake
import operator
import embeds
import resources
from disnake.ext import commands
from replit import db


class Commands(commands.Cog):
  def __init__(self, client):
    self.bot = client
  
  @commands.command()
  async def ajuda(self, ctx):
    embeds.ajuda.set_author(
      name = ctx.author.display_name,
      icon_url = ctx.author.display_avatar)  
    await ctx.channel.send(embed=embeds.ajuda)

  @commands.command()
  async def cargo(self, ctx, role:commands.RoleConverter):
    """Recebe um nome de um cargo com caracteres sensíveis e mostra uma lista daqueles que fazem parte deste cargo."""
    if role == Exception:
      await ctx.send(f'_Não foi possível encontrar tal cargo._')
      return

    mentionList = []
    memberlist = role.members
    memberlist = sorted(memberlist,key=operator.attrgetter('display_name'))
    for member in memberlist: #role.members é uma lista de Members.
      mentionList.append(member.mention)
    string = "aaa".join([element for element in mentionList])
    string = string.replace("aaa", "\n")

    embed = disnake.Embed(
      title=role.name.upper(),
      description= f'Usuários que são **{role.name.upper()}** no servidor!',
      colour=embeds.cor
      )
    embed.add_field(name=f'Lista de {role.name} [{len(mentionList)}]', value=string, inline=True)
    embed.set_thumbnail(url=embeds.thumb_ic)
    embed.set_author(
      name = ctx.author.display_name,
      icon_url = ctx.author.display_avatar)  
    
    await ctx.send(embed=embed)

  @commands.command()
  async def helloworld(self, ctx):
    await ctx.send(embed=embeds.helloworld)

  @commands.command()
  async def convite(self, ctx):
    await ctx.reply(
      f'Olá {ctx.author.mention}, aqui está o link de convite para o servidor:\n https://discord.gg/TBKwV2BKQg')

  @commands.command()
  async def Lista(self, ctx):
    lista = disnake.Embed(title='Lista de coisas a fazer', description='Reagir com o emote 🔴 pra "pendente", 🟡 pra "em progresso" e 🟢 "pra concluído"', colour=embeds.cor)
    lista.set_thumbnail(url=embeds.thumb_ic)
    lista.add_field(name=f"{resources.semaforo[0]}", value=f'{db["r"]}z', inline=False)
    lista.add_field(name=f"{resources.semaforo[1]}", value=f'{db["y"]}z', inline=False)
    lista.add_field(name=f"{resources.semaforo[2]}", value=f'{db["g"]}z', inline=False)
    await ctx.send(embed=lista)
          

  @commands.command()
  async def grupo(self, ctx, title:str, description:str, amount:int, data:str='sem data'): 
    embed = embeds.ourEmbed(title, description, ctx)
    embed.set_footer(text=f'entragar em {data}')
    for x in range(amount):
      embed.add_field(name=f'grupo{x+1}', value='participantes: ', inline=False)

    msg = await ctx.send(embed=embed)

    for x in range(amount):
      await msg.add_reaction(emoji=resources.emoji[x])

def setup(bot):
  bot.add_cog(Commands(bot))

