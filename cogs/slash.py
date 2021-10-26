import disnake
import operator
import embeds
import resources
from disnake.ext import commands
from replit import db

class Slash(commands.Cog):
  def __init__(self, client):
        self.bot = client

  @commands.slash_command(description="Mostra uma mensagem de ajuda")
  async def ajuda(self, inter):
      embeds.ajuda.set_author(name=inter.author.display_name,
                              icon_url=inter.author.display_avatar)
      await inter.response.send_message(embed=embeds.ajuda)

  @commands.slash_command(description="Multiplies the number by 7")
  async def multiply(self, inter, number: float):
      await inter.response.send_message(f'{float(number * 7)}')

  @commands.slash_command(description = "mostra uma lista daqueles que fazem parte deste cargo.")
  async def cargo(self, inter, role: disnake.Role): 
      if role == Exception:
          await inter.response.send_message(
              f'_Não foi possível encontrar tal cargo._')
          return

      mentionList = []
      memberlist = role.members
      print(memberlist)
      memberlist = sorted(memberlist,
                          key=operator.attrgetter('display_name'))
      for member in memberlist:  #role.members é uma lista de Members.
          mentionList.append(member.mention)
      string = "aaa".join([element for element in mentionList])
      string = string.replace("aaa", "\n")

      embed = disnake.Embed(
          title=role.name.upper(),
          description=
          f'Usuários que são **{role.name.upper()}** no servidor!',
          colour=embeds.cor)
      embed.add_field(name=f'Lista de {role.name} [{len(mentionList)}]',
                      value=string,
                      inline=True)
      embed.set_thumbnail(url=embeds.thumb_ic)
      embed.set_author(name=inter.author.display_name,
                        icon_url=inter.author.display_avatar)

      await inter.response.send_message(embed=embed)

  @commands.slash_command(description="Exempo de 'hello world' em C")
  async def helloworld(self, inter):
      await inter.response.send_message(embed=embeds.helloworld)

  @commands.slash_command(description="Convite para p server")
  async def convite(self, inter):
      await inter.reply(
          f'Olá {inter.author.mention}, aqui está o link de convite para o servidor:\n https://discord.gg/TBKwV2BKQg'
      )

  @commands.slash_command(description="Em Obras")
  async def lista(self, inter):
      lista = disnake.Embed(
          title='Lista de coisas a fazer',
          description=
          'Reagir com o emote 🔴 pra "pendente", 🟡 pra "em progresso" e 🟢 "pra concluído"',
          colour=embeds.cor)
      lista.set_thumbnail(url=embeds.thumb_ic)
      lista.add_field(name=f"{resources.semaforo[0]}",
                      value=f'{db["r"]}z',
                      inline=False)
      lista.add_field(name=f"{resources.semaforo[1]}",
                      value=f'{db["y"]}z',
                      inline=False)
      lista.add_field(name=f"{resources.semaforo[2]}",
                      value=f'{db["g"]}z',
                      inline=False)
      await inter.response.send_message(embed=lista)

  @commands.slash_command(description="Cria um organizador de grupos")
  async def grupo(self,
                  inter,
                  title: str,
                  description: str,
                  amount: int,
                  data: str = 'sem data'):
      embed = embeds.ourEmbed(title, description, inter)
      embed.set_footer(text=f'entregar em {data}')
      for x in range(amount):
          embed.add_field(name=f'grupo{x+1}',
                          value='participantes: ',
                          inline=False)

      msg = await inter.response.send_message(embed=embed)

      for x in range(amount):
          await msg.add_reaction(emoji=resources.emoji[x])

  @commands.slash_command(description='Mosta a latência do bot')
  async def latency(self, inter):
      embed = disnake.Embed(description=f'🏓 Pong! {round(self.bot.latency * 1000)}ms', colour=embeds.cor)
      await inter.response.send_message(embed=embed)


def setup(bot):
  bot.add_cog(Slash(bot))  