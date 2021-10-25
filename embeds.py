import disnake
import datetime

client = disnake.Client()

# Imagens
thumb = "https://cdn.discordapp.com/attachments/857312584525152329/872578503344807946/Asset_9.png"

thumb_ic = "https://cdn.discordapp.com/attachments/859388961490468864/876909859734437908/IC_-_Icone_Pequeno.png"
cor = 11701855 

class ourEmbed(disnake.Embed):
  """Nosso Embed modificado. Ele recebe o título, a descrição, e o contexto.
  exemplo:
  ourEmbed("Título", "Descrição", ctx)
  """
  #TODO verificar como age sem contexto e como resolver isso
  def __init__(self,title,description, ctx=None): 
    super().__init__(title=title,description=description,colour=cor)
    super().set_thumbnail(url=thumb_ic)
    super().set_author(name=ctx.author.display_name,           
                       icon_url=ctx.author.display_avatar)

class action_log(disnake.Embed):
  def __init__(self, event:str, member=None, ctx=None):
    super().__init__(title=f"Evento {event.upper()}", description=f"o membro {member.display_name} executou {event.upper()} em {ctx.channel.mention}", timestamp=datetime.datetime.now() , colour=cor)
    super().set_thumbnail(url=thumb_ic)
    super().set_author(name=member.display_name,                                             icon_url=member.display_avatar)
    super().set_footer(text=f"querem colocar alguma coisa?")
    

##############################--------------------------------##############################

# Ajuda
ajuda = disnake.Embed(
    title='Ajuda',
    description=
    'Caso tenha dúvidas com alguma matéria, marque um **monitor** dessa matéria no canal referente a ela.\nMas se sua dúvida seja relacionada a algo do servidor, marque alguém da **Organização** do servidor no canal #geral, que a gente responde assim que possível.',
    colour=cor)
ajuda.add_field(name='Monitores', value="Use o comando **!monitores**", inline=True)
ajuda.add_field(name='Organização', value="Tercio\nOliver", inline=True)
ajuda.set_thumbnail(url=thumb_ic)

# Hello World
helloworld = disnake.Embed(
    title='Hello world!',
    description=
    'Aqui está um exemplo de **Hello world!**, um código básico escrito em **C**, criado para exibir uma única mensagem:\n```c\n#include <stdio.h>\nint main(){\n\n    printf("kakaka iai men");\n    return 0;\n}```',
    colour=cor)
helloworld.set_thumbnail(url=thumb_ic)

