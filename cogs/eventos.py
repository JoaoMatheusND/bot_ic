from disnake.ext import commands
import embeds
import resources

class Events(commands.Cog):
  def __init__(self, client):
    self.bot = client

  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{resources.bot_on}')
    print(self.bot.user)

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot: return

    if "hello" in message.content.lower().split():
      msg = await message.reply('Helloworld!')

    if "factorio" in message.content.lower().split():
      msg = await message.reply(
      '***"Alguém falou em Factorio?"***\n- Ancelmo, 2021')

    if "recursão" in message.content.lower().split():
      msg = await message.reply('**Você quis dizer: *recursão*.**')
      await msg.add_reaction(emoji="<:PepeReee:859293051562098728>")
        
    if "f" == message.content.lower():
      await message.add_reaction(emoji="<:f_:859311264098025533>")
    
    if "teste" in message.content.lower():
      
      await message.channel.send(embed=embeds.bem_vindo)    

    if any(word in message.content.lower() for word in resources.agradecimentos):
      if str(self.bot.user.id) in message.content:
        msg = await message.reply('_De nada! Você é um amigo(a), amigo(a)!_')
        #await msg.add_reaction(emoji="🗑️")

    """if any(word in message.content.lower()
      for word in resources.bad_words):  #passar depois para os comandos
      await message.delete()
      msg = await message.channel.send(
      f'{message.author.mention}, se você continuar, vai ser mutado permanentemente no servidor.'
      )
      await msg.delete(delay=120)"""
  
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    channel = await self.bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = await self.bot.fetch_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)
    member_react = await guild.fetch_member(payload.member.id)
    roles = member.roles
    reaction = payload.emoji

    if payload.user_id == self.bot.user.id or channel in resources.channel_block: return

    if str(reaction) in resources.emoji:
      for x in range(resources.num_emoji):
        if resources.emoji[x] == str(reaction):
          grupo = []
          embed = message.embeds[0]
          users = await message.reactions[x].users().flatten()
          users.pop(users.index(self.bot.user))
          for pessoa in users:
            grupo.append(pessoa.mention)
          user = " ".join(grupo)

          embed.set_field_at(index=x, name=f'grupo{x+1}', value=f'participantes: {user}', inline=False)
          await message.edit(embed=embed)
    
    if str(reaction) == "📌":
      for x in message.reactions:
        if x.emoji == "📌":
          Q_users = await x.users().flatten()
          if len(Q_users) >= 3:
            await message.pin()
  
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self,payload):
    channel = await self.bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id) 
    guild = await self.bot.fetch_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)
    roles = member.roles
    reaction = payload.emoji
  
    if payload.user_id == self.bot.user.id or channel in resources.channel_block: return

    if str(reaction) in resources.emoji:
      for x in range(resources.num_emoji):
        if resources.emoji[x] == str(reaction):
          grupo = []
          embed = message.embeds[0]
          users = await message.reactions[x].users().flatten()
          users.pop(users.index(self.bot.user))
          for pessoa in users:
            grupo.append(pessoa.mention)
          user = " ".join(grupo)

          embed.set_field_at(index=x, name=f'grupo{x+1}', value=f'participantes: {user}', inline=False)
          await message.edit(embed=embed)

  @commands.Cog.listener()
  async def on_member_join(ctx, member):
    embed = embeds.ourEmbed('Bem vindo ao servidor IC/UFAL', 'bem vindos ao servidor, o servidor foi criado com intuito de ajudar os alunos, com foco nos calouros, a aprenderem como a ufal funciona, além disso você pode interagir com outros alunos dos curso de CC e EC, participar de estudos em grupo e monitorias', ctx)
    embed.set_thumbnail(url=embeds.thumb_ic)
    embed.set_image(url=embeds.thumb)
    embed.add_field(name='Geral', value='qualquer dúvida use os comandos "!comandos" e/ou "!ajuda"', inline=False)
    msg = await member.send(embed=embed)
    await msg.add_reaction(emoji="👍")

def setup(bot):
  bot.add_cog(Events(bot))




  
    