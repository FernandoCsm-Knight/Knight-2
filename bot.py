import asyncio
from time import sleep
import discord
from discord import Member
from datetime import date
from keep_alive import keep_alive
from random import choice, randint
import json
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.all()
client = discord.Client(intents=intents)

inspiração = [['Não vemos as coisas como elas são, mas como nós somos.', '**Anaïs Nin**'], ['A moral é a debilidade do cérebro.', '**Arthur Rimbaud**'], 
['Há livros escritos para evitar espaços vazios na estante.', '**Carlos Drummond de Andrade**'], 
['Engolimos de uma vez a mentira que nos adula e bebemos gota a gota a verdade que nos amarga.', '**Denis Diderot**'], 
['Políticos e fraldas devem ser trocados de tempos em tempos pelo mesmo motivo.', '**Eça de Queiróz**'], ['Felicidade em pessoas inteligentes é a coisa mais rara que conheço.', '**Ernest Hemingway**'], 
['Em tempos de embustes universais, dizer a verdade se torna um ato revolucionário.', '**George Orwell**'], ['É permissível a cada um de nós morrer pela sua fé, mas não matar por ela.', '**Hermann Hesse**'],
['Algo deve mudar para que tudo continue como está.', '**Giuseppe Tomasi di Lampedusa**'], ['Tenha cuidado com a tristeza. É um vício.', '**Gustave Flaubert**'], 
['Não há mentira pior do que uma verdade mal compreendida por aqueles que a ouvem.', '**Henry James**'], ['A graça de cair é se machucar!', '**Fernando Dal Maria**'], 
['A democracia é um erro estatístico, porque na democracia decide a maioria e a maioria é formada de imbecis.', '**Jorge Luis Borges**'], 
['A solidão é a mãe da sabedoria.', '**Laurence Sterne**'], ['Aquele que lê maus livros não leva vantagem sobre aquele que não lê livro nenhum.', '**Mark Twain**']]

@client.event
async def on_ready():
    print(f'O bot está logado como {client.user}')
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(
            activity=discord.Game('discord.gg/[código do convite]'),
            status=discord.Status.online)
        await asyncio.sleep(4)
        await client.change_presence(
            activity=discord.Game('no [nome do seu servidor]!'),
            status=discord.Status.online)
        await asyncio.sleep(4)


@client.event
async def on_message(message):

    if message.guild.id != [id do seu server]:
        return
    
    if message.author.bot:
        return
    
    canal12 = client.get_channel([id do canal em que seerá permitido o comando >G1])
    if message.channel == canal12:
        alo = message.content.split()
        if alo[0] not in ['>G1', '>clear', '>BBC']:
            alo1 = await message.channel.send(
                f'{message.author.mention} nesse canal você só pode utilizar o comando >G1[mensagem]. Para saber mais sobre esse comando utilize >help em outro canal de texto do servidor.'
            )
            await message.delete()
            await alo1.delete(delay=5)

        if message.content.startswith('>G1'):
            canalg1 = client.get_channel([id do canal onde esse comando será usado])
            if message.channel != canalg1:
                return
            args = message.content.split()
            listag1 = []
            try:
                if len(args) == 1:
                    site = requests.get('https://g1.globo.com')
                    content = site.content
                    sitenovo = BeautifulSoup(content, 'html.parser')
                    noticia = sitenovo.find_all('div',
                                                attrs={'class': 'feed-post-body'})
                    for x in range(0, 5):
                        link0 = noticia[x].find(
                            'a',
                            attrs={
                                'class':
                                'feed-post-link gui-color-primary gui-color-hover'
                            })
                        titulo = link0.text
                        link1 = link0.attrs
                        link2 = link1['href']
                        subtitulo = noticia[x].find(
                            'div', attrs={'class': 'feed-post-body-resumo'})
                        if subtitulo == None:
                            listag1.append(
                                f'`G1` \n \n __**{titulo}**__ \n \n LINK: {link2} \n 🗒️'
                            )
                        else:
                            subtitulo1 = subtitulo.text
                            listag1.append(
                                f'`G1` \n \n __**{titulo}**__ \n {subtitulo1} \n \n LINK: {link2} \n 🗒️'
                            )
                    embednoticias = discord.Embed(title='☕ Notícias do dia! 🗞️',
                                                  description='',
                                                  color=0xa80000)
                    embednoticias.set_thumbnail(
                        url='[link da imagem da thumbnail]')
                    for arquivo in range(0, len(listag1)):
                        embednoticias.add_field(name=f'📰 Notícia {arquivo + 1}',
                                                value=f'{listag1[arquivo]}',
                                                inline=False)
                    embednoticias.set_footer(
                        text='Staff do servidor [nome do seu servidor]',
                        icon_url='[link da imagem do seu footer]')
                    await message.channel.send(embed=embednoticias)
                if len(args) >= 2:
                    args.pop(0)
                    busca = '+'.join(args)
                    embedtitle = ' '.join(args)
                    site = requests.get(f'https://g1.globo.com/busca/?q={busca}')
                    content = site.content
                    sitenovo = BeautifulSoup(content, 'html.parser')
                    noticia = sitenovo.find_all(
                        'li', attrs={'class': 'widget widget--card widget--info'})
                    for x in range(0, 5):
                        link0 = noticia[x].find(
                            'div', attrs={'class': 'widget--info__text-container'})
                        info = noticia[x].find('div',
                                               attrs={
                                                   'class': 'widget--info__header'
                                               }).text
                        link1 = link0.find('a', href=True)
                        link2 = link1.attrs
                        link3 = link2['href']
                        titulo = noticia[x].find(
                            'div',
                            attrs={
                                'class': 'widget--info__title product-color'
                            }).text.strip()
                        subtitulo = noticia[x].find(
                            'p', attrs={'class': 'widget--info__description'})
                        subtitulo1 = subtitulo.text
                        listag1.append(
                            f'`{info}` \n \n __**{titulo}**__ \n {subtitulo1} \n \n LINK: https:{link3} \n 📢'
                        )
                    embedg1 = discord.Embed(
                        title=f'🔎 Notícias no G1 sobre {embedtitle} 🔍',
                        description='',
                        color=0xa80000)
                    for arquivo in range(0, len(listag1)):
                        embedg1.add_field(name=f'📰 Notícia {arquivo + 1}',
                                          value=f'{listag1[arquivo]}',
                                          inline=False)
                    embedg1.set_thumbnail(url='[link da imagem da thumbnail]')
                    embedg1.set_footer(text='Staff do servidor [nome do seu servidor]',
                                       icon_url='[link da imagem do seu footer]')
                    await message.channel.send(embed=embedg1)
            except IndexError as erro:
                msgg1 = await message.channel.send(
                    f'{message.author.mention} **não há resultados para essa pesquisa no G1.** `{erro}`'
                )
                sleep(5)
                await msgg1.delete()
                await message.delete()    
                
        if message.content.startswith('>BBC'):
            args = message.content.split()
            listaBBC = []
            try:
                if len(args) == 1:
                    siteBBC = requests.get(
                        'https://www.bbc.com/portuguese/topics/cz74k717pw5t')
                    contentBBC = siteBBC.content
                    sitenovoBBC = BeautifulSoup(contentBBC, 'html.parser')
                    noticiaBBC = sitenovoBBC.find_all(
                        'li', attrs={'class': 'lx-stream__post-container'})
                    noticia1 = sitenovoBBC.find(
                        'li',
                        attrs={
                            'class':
                            'lx-stream__post-container placeholder-animation-finished'
                        })
                    imagem = noticia1.find('img')
                    imagem2 = imagem['src']

                    for x in range(0, 5):
                        titulolinkBBC = noticiaBBC[x].find(
                            'a',
                            attrs={
                                'class':
                                'qa-heading-link lx-stream-post__header-link'
                            })
                        titulo = titulolinkBBC.find(
                            'span',
                            attrs={
                                'class':
                                'lx-stream-post__header-text gs-u-align-middle'
                            }).text
                        link2 = titulolinkBBC['href']
                        subtitulo = noticiaBBC[x].find(
                            'p',
                            attrs={
                                'class':
                                'lx-stream-related-story--summary qa-story-summary'
                            }).text
                        info = noticiaBBC[x].find(
                            'span',
                            attrs={
                                'class': 'gs-u-vh qa-visually-hidden-meta'
                            }).text
                        if subtitulo == None:
                            listaBBC.append(
                                f'`{info}`\n \n__**{titulo}**__\n \nLINK: https://www.bbc.com{link2} \n 🗒️'
                            )
                        else:
                            listaBBC.append(
                                f'`{info}`\n \n__**{titulo}**__\n{subtitulo}\n \nLINK: https://www.bbc.com{link2} \n 🗒️'
                            )
                    embedBBC = discord.Embed(
                        title='☕ Notícias do dia na BBC News Brasil! 🗞️',
                        description='',
                        color=0xb80000)
                    embedBBC.set_author(
                        name='Ir para a BBC News Brasil.',
                        url=
                        'https://www.bbc.com/portuguese/topics/cz74k717pw5t',
                        icon_url=[link da imagem do seu author])
                    for arquivo in range(0, len(listaBBC)):
                        embedBBC.add_field(name=f'📰 Notícia {arquivo + 1}',
                                           value=f'{listaBBC[arquivo]}',
                                           inline=False)
                    embedBBC.set_thumbnail(url=f'{imagem2}')
                    embedBBC.set_footer(
                        text='Staff do servidor [nome do seu servidor].',
                        icon_url=[link da imagem do seu footer])
                    await message.channel.send(embed=embedBBC)

                if len(args) == 2:
                    if args[1] == 'world':
                        siteBBC = requests.get(
                            'https://www.bbc.com/news/world')
                        contentBBC = siteBBC.content
                        sitenovoBBC = BeautifulSoup(contentBBC, 'html.parser')
                        noticiaBBC = sitenovoBBC.find_all(
                            'div',
                            attrs={
                                'class':
                                'gs-c-promo gs-t-News nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-c-promo--inline gs-c-promo--stacked@m gs-c-promo--flex'
                            })
                        noticia1 = sitenovoBBC.find(
                            'div',
                            attrs={
                                'class':
                                'gs-c-promo gs-t-News nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-c-promo--inline@m gs-c-promo--stacked@xxl gs-c-promo--flex'
                            })
                        info = noticia1.find('span',
                                             attrs={
                                                 'class': 'gs-u-vh'
                                             }).text
                        link = noticia1.find(
                            'a',
                            attrs={
                                'class':
                                'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor'
                            })
                        link2 = link['href']
                        titulo = noticia1.find(
                            'h3',
                            attrs={
                                'class':
                                'gs-c-promo-heading__title gel-paragon-bold gs-u-mt+ nw-o-link-split__text'
                            }).text
                        subtitulo = noticia1.find(
                            'p',
                            attrs={
                                'class':
                                'gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary'
                            }).text
                        imagem = noticia1.find('img')
                        imagem2 = imagem['src']
                        if subtitulo == None:
                            listaBBC.append(
                                f'`{info}`\n \n__**{titulo}**__\n \nLINK: https://www.bbc.com{link2} \n 🗒️'
                            )
                        else:
                            listaBBC.append(
                                f'`{info}`\n \n__**{titulo}**__\n{subtitulo}\n \nLINK: https://www.bbc.com{link2} \n 🗒️'
                            )

                        for x in range(0, 4):
                            titulolinkBBC = noticiaBBC[x].find(
                                'a',
                                attrs={
                                    'class':
                                    'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'
                                })
                            titulo = titulolinkBBC.find(
                                'h3',
                                attrs={
                                    'class':
                                    'gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text'
                                }).text
                            link2 = titulolinkBBC['href']
                            subtitulo = noticiaBBC[x].find(
                                'p',
                                attrs={
                                    'class':
                                    'gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary gs-u-display-none gs-u-display-block@m'
                                }).text
                            info = noticiaBBC[x].find('span',
                                                      attrs={
                                                          'class': 'gs-u-vh'
                                                      }).text
                            if subtitulo == None:
                                listaBBC.append(
                                    f'`{info}`\n \n__**{titulo}**__\n \nLINK: https://www.bbc.com{link2} \n 🗒️'
                                )
                            else:
                                listaBBC.append(
                                    f'`{info}`\n \n__**{titulo}**__\n{subtitulo}\n \nLINK: https://www.bbc.com{link2} \n 🗒️'
                                )
                        embedBBC = discord.Embed(
                            title='☕ Notícias do dia na BBC News World! 🗞️',
                            description='',
                            color=0xb80000)
                        embedBBC.set_author(
                            name='Ir para a BBC World.',
                            url='https://www.bbc.com/news/world',
                            icon_url=[link da imagem do seu author])
                        for arquivo in range(0, len(listaBBC)):
                            embedBBC.add_field(name=f'📰 Notícia {arquivo + 1}',
                                               value=f'{listaBBC[arquivo]}',
                                               inline=False)
                        embedBBC.set_thumbnail(url=f'{imagem2}')
                        embedBBC.set_footer(
                            text='Staff do servidor [nome do seu servidor].',
                            icon_url=[link da imagem do seu footer])
                        await message.channel.send(embed=embedBBC)
                    else:
                        msgBBC = await message.channel.send(
                            f'{message.author.mention} **não há resultados para essa pesquisa na BBC.**'
                        )
                        await message.delete()
                        await msgBBC.delete(delay=5)

            except IndexError as erro:
                msgBBC = await message.channel.send(
                    f'{message.author.mention} **não há resultados para essa pesquisa na BBC.** `{erro}`'
                )
                await message.delete()
                await msgBBC.delete(delay=5)

    else:
    
        if message.content.startswith('>help'):
            embed0 = discord.Embed(
                title=f'Bem vindo ao embed de ajuda do [nome do seu bot]!',
                description=f' ',
                color=0xFFFAFA)
            embed0.set_thumbnail(url='[link da imagem da sua thumbnaill]')
            embed0.set_footer(
                text='Staff do servidor [nome do seu servidor].',
                icon_url='[link da imagem do seu footer.]')
            embed0.add_field(
                name='>Hello',
                value='Esse comando serve para comprimentar o Bot.',
                inline=False)
            embed0.add_field(
                name='>formatação',
                value=
                'Esse comando retorna algumas diocas sobre formatação de texto no discord.',
                inline=False)
            embed0.add_field(
                name='>G1',
                value=
                'Esse comando só pode ser usado no canal de notícias do servidor. Com >G1 [mensagem] você pode pesquisar a mensagem no site do G1, ao digitar somente >G1 você receberá as notícias do dia.',
                inline=False)        
            embed0.add_field(
                name='>sugestões [mensagem]',
                value=
                'Esse comando pode ser utilizado para fazer uma sugestão para o servidor, tanto para implementar novos canais ou funcionalidades no servidor, quanto para alterar/criar regras e/ou comandos.',
                inline=False)
            embed0.add_field(
                name='>denúncias [mensagem]',
                value=
                'Esse comando pode ser utilizado para realizar uma denúncia com relação a algum membro ou ação que você achou injusta no servidor. QUALQUER ACUSAÇÃO SEM PROVAS ACARRETARA EM BANIMENTO.',
                inline=False)
            embed0.add_field(
                name='>userinfo [Nome do usuário]',
                value=
                'Devolve algumas informações a respeito do usuário citado no comando.',
                inline=False)
            embed0.add_field(
                name='>weather [nome da Cidade ou Estado ou País]',
                value='Retorna as informações do tempo no local mensionado.',
                inline=False)
            await message.channel.send(embed=embed0)

        if message.content.startswith('>clear'):
            if message.author.permissions_in(message.channel).manage_messages:
                args = message.content.split()
                if len(args) == 2:
                    if args[1].isdigit():
                        count = int(args[1]) + 1
                        deleted = await message.channel.purge(limit=count)
                        msg = await message.channel.send(
                            f'{len(deleted) - 1} mensagens foram deletadas.')
                        sleep(2)
                        await msg.delete()
            else:
                msg = await meszage.content.send(f'{message.author.mention} você não tem permissão para usar esse comando.')
                await message.delete()
                await msg.delete(delay=5)

        if message.content.startswith('>userinfo'):
            args = message.content.split(' ')
            if len(args) == 2:
                member: Member = discord.utils.find(lambda m: args[1] in m.name,
                                                    message.guild.members)
                if member:
                    embed = discord.Embed(
                        title=f'Informações do usuário {member.name}',
                        description=
                        f'Aqui estão as informações {message.author.mention}',
                        color=0x00BFFF)
                    embed.add_field(
                        name='Entrou no servidor:',
                        value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                        inline=True)
                    embed.add_field(
                        name='Criou a conta no discord:',
                        value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                        inline=True)
                    cargos = ''
                    for role in member.roles:
                        if not role.is_default():
                            cargos += f'{role.mention} \r\n'
                    if cargos:
                        embed.add_field(name='Cargo:', value=cargos, inline=True)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_footer(
                        text='Staff do servidor [nome do seu servidor].',
                        icon_url='[link da imagem do seu footer]')
                    await message.channel.send(embed=embed)

        if message.content.startswith('>Hello'):
            member = message.author
            embed1 = discord.Embed(
                title=f'Olá {member.name}',
                description=f'Gostaria de algo antes de começarmos?',
                color=0x902AE4)
            msg = await message.channel.send(embed=embed1)
            await msg.add_reaction('🍹')
            await msg.add_reaction('🫐')
            await msg.add_reaction('❎')
            if message.author.name == '[seu nome no discord]':
                await msg.add_reaction('☕')

            @client.event
            async def on_reaction_add(reaction, user):
                iddamensagem = msg.id
                if reaction.message.id != iddamensagem:
                    return
                if user == client.user:
                    return
                if reaction.emoji == '🍹':
                    await message.channel.send('Um drink tropical saindo...')
                    sleep(2)
                    await message.channel.send(':tropical_drink:')
                if reaction.emoji == '☕':
                    if user.name == '[seu nome no discord]':
                        await message.channel.send('Iniciando sistema 1...')
                        sleep(2)
                        await message.channel.send('Iniciado com sucesso!')
                    else:
                        await message.channel.send(
                            'Você não é meu criador, não posso iniciar o sistema!')
                if reaction.emoji == '❎':
                    msg1 = await message.channel.send('Tudo bem.')
                    await msg1.add_reaction('❤️')
                if reaction.emoji == '🫐':
                    await message.channel.send('Vc é muito saudável...')

        if message.content.startswith('>sugestões'):
            args = message.content.split()
            if len(args) >= 2:
                a = len(message.content)
                if a <= 1010:
                    await message.delete()
                    channel = client.get_channel([id do canal para onde devem ir as sugestões não aprovadas])
                    args.pop(0)
                    newargs = ' '.join(args)
                    embed2 = discord.Embed(
                        title=f'{message.author.name} enviou uma sugestão:',
                        description=
                        f'**Mensão:** {message.author.mention}\n \n**Conteúdo:**\n{newargs.capitalize()}',
                        color=0x31E349)
                    embed2.set_thumbnail(url=message.author.avatar_url)
                    embed2.add_field(
                        name='Mensagem enviada em:',
                        value=
                        f'{date.today().day}/{date.today().month}/{date.today().year}'
                    )
                    mensagemsugestoes = await channel.send(embed=embed2)
                    await mensagemsugestoes.add_reaction('❎')
                    await mensagemsugestoes.add_reaction('✅')
                    await mensagemsugestões.add_reaction('❗')
                    await message.channel.send(
                        f'{message.author.mention} sua mensagem foi enviada com secesso!'
                    )

                    @client.event
                    async def on_reaction_add(reaction, user):
                        if reaction.message.channel != channel:
                            return
                        if user == client.user:
                            return
                        if reaction.count >= [número de votos necessários para aprovar ou negar uma sugestão]:
                            canalsugestoes1 = client.get_channel([id do canal para onde devem ir as sugestões aprovadas])
                            if reaction.emoji == '✅':
                                embed3 = reaction.message.embeds[0]
                                msg2 = await canalsugestoes1.send(embed=embed3)
                                await msg2.add_reaction('✅')
                                await msg2.add_reaction('❎')
                            if reaction.emoji == '❎':
                                await reaction.message.delete()
                else:
                    await message.channel.send(
                        f'{message.author.mention} você só pode enviar mensagens com até 1000 caractéres.'
                    )
            else:
                await message.channel.send(
                    f'{message.author.mention}Você precisa digitar a sugestão após digitar o comando, exemplo:\n'
                    '```>sugestões Quero fazer uma sugestão.```')

        if message.content.startswith('>denúncias'):
            args = message.content.split()
            if len(args) >= 2:
                a = len(message.content)
                if a <= 1010:
                    await message.delete()
                    channel = client.get_channel([id do canal para onde devem ir as denúncias])
                    args.pop(0)
                    newargs = ' '.join(args)
                    embed3 = discord.Embed(
                        title=f'{message.author.name} enviou uma denúncia:',
                        description=
                        f'**Mensão:**{message.author.mention}\n \n**Conteúdo:**\n{newargs.capitalize()}',
                        color=0xFF0000)
                    embed3.set_thumbnail(url=message.author.avatar_url)
                    embed3.add_field(
                        name='Mensagem enviada em:',
                        value=
                        f'{date.today().day}/{date.today().month}/{date.today().year}'
                    )
                    mensagemdenuncias = await channel.send(embed=embed3)
                    await mensagemdenuncias.add_reaction('✅')
                    await mensagemdenuncias.add_reaction('❎')
                    await mensagemdenuncias.add_reaction('❗')
                    await message.channel.send(
                        f'{message.author.mention} sua mensagem foi enviada com secesso!'
                    )
                else:
                    await message.channel.send(
                        f'{message.author.mention} você só pode enviar mensagens com até 1000 caractéres.'
                    )
            else:
                await message.channel.send(
                    f'{message.author.mention}Você precisa digitar a denúncia após digitar o comando, exemplo:\n'
                    '```>denúncia Quero fazer uma denúncia.```')

        if message.content.startswith('>inspiração'):
            meinspire = choice(inspiração)
            embed5 = discord.Embed(title=f'{meinspire[1]} disse:',
                                   description=f'{meinspire[0]}',
                                   color=0x27E320)
            embed5.set_footer(text='Staff do servidor Jealous King.',
                              icon_url='https://imgur.com/GMWIN4J.jpg')
          if meinspire[0] == 'A democracia é um erro estatístico, porque na democracia decide a maioria e a maioria é formada de imbecis.':
                embed5 = discord.Embed(title=f'{meinspire[1]} disse:',
                                       description=f'{meinspire[0]}',
                                       color=0x008000)
                embed5.set_footer(text='Esse aqui é um bom easter egg!',
                                  icon_url='https://imgur.com/GMWIN4J.jpg')
          await message.channel.send(embed=embed5)            

        if message.content.startswith('>formatação'):
            embed6 = discord.Embed(title='Formatação Básica de mensagens.',
                                   description='Para aprender a escrevere colorido procure o **[seu nome]**.',
                                   color=0x5F9EA0) \\aqui a descrição é opcional
            embed6.set_author(name='Para mais informações você pode clicar aqui!',
                              url='https://support.discord.com/hc/pt-br/articles/210298617-No%C3%A7%C3%B5es-b%C3%A1sicas-de-marca%C3%A7%C3%A3o-de-texto-Formata%C3%A7%C3%A3o-do-chat-negrito-it%C3%A1lico-e-sublinhado-')
            embed6.set_image(url='https://imgur.com/IasLmjN.jpg')
            embed6.set_thumbnail(url='[link da imagem thumbnail]')
            embed6.add_field(name='Negrito, Itálico e Sublinhado.',
                             value='Seguem na tabela abaixo.',
                             inline=False)
            embed6.add_field(name='Mensagens escondidas: ||Alo!||',
                             value='Digite `||` [mensagem] `||`.',
                             inline=False)
            embed6.add_field(name='Blocos de código.',
                             value="1 linha = utilize `[crase]` [mensagem] `[crase]`.\n 2 linhas ou mais = utilize `[3 crases]` [mensagem] `[3 crases]`.",
                             inline=False)
            embed6.add_field(name='Mensagem riscada: ~~Alo!~~',
                             value='Digite `~~` [mensagem] `~~`.',
                             inline=False)
            embed6.set_footer(text='Staff do servidor [nome do seu servoidor]!',
                              icon_url='[link da imagem do seu footer]')
            await message.channel.send(embed=embed6)   

        if message.content.startswith('>ping'):
            args = message.content.split()
            if len(args) == 1:
                p = (client.latency) * 1000
                await message.channel.send(f'Pong! [{p:.0f}ms]') 

        if message.content.startswith('>weather'):
            args = message.content.split()
            if len(args) >= 2:
                args.pop(0)
                argsweather = ' '.join(args)
                key = '[chave de acesso]'
                url = f'http://api.openweathermap.org/data/2.5/weather?q={argsweather}&appid={key}&units=metric'
                data = json.loads(requests.get(url).content)
                nome = data['name']
                pais = data['sys']['country']
                coordenadaslon = data['coord']['lon']
                coordenadaslat = data['coord']['lat']
                climaestado = data['weather'][0]['description']
                climamain = data['weather'][0]['main']
                temperatura1 = data['main']['temp']
                temperatura2 = data['main']['feels_like']
                humidade = data['main']['humidity']
                velocidadevento = data['wind']['speed']
                pressao = data['main']['pressure']
                visibilidade = data['visibility']
                urlid = data['id']
                embed7 = discord.Embed(title=' ',
                                       description=f'Tempo em {nome}-{pais}',
                                       color=0xF62A71)
                embed7.set_author(name='Bot Knight [>weather].',
                                  url=f'https://openweathermap.org/city/{urlid}',
                                  icon_url='[link do icone do autor]')
                embed7.set_thumbnail(url='[link da imagem da thumbnail]')
                embed7.set_footer(text='Staff do servidor [nome do seu servidor].',
                                  icon_url='[link da imagem do seu footer]')
                embed7.add_field(
                    name='Longitude(lon) e Latitude(lat).',
                    value=f'lon = {coordenadaslon} \nlat = {coordenadaslat}.',
                    inline=True)
                embed7.add_field(
                    name='Tempo:',
                    value=f'{climamain.title()} with {climaestado.title()}',
                    inline=True)
                embed7.add_field(
                    name='Temperatura:',
                    value=f'{temperatura1:.0f}°C/{(temperatura1 * 9/5) + 32:.0f}°F',
                    inline=True)
                embed7.add_field(
                    name='Sensação Térmica:',
                    value=f'{temperatura2:.0f}°C/{(temperatura2 * 9/5) + 32:.0f}°F',
                    inline=True)
                embed7.add_field(name='Humidade:',
                                 value=f'{humidade}%',
                                 inline=True)
                embed7.add_field(name='Vento (velocidade):',
                                 value=f'{velocidadevento:.2f} m/s',
                                 inline=True)
                embed7.add_field(name='Pressão atmosférica:',
                                 value=f'{pressao * 0.000986923266716013:.2f} atm',
                                 inline=True)
                embed7.add_field(name='Visibilidade:',
                                 value=f'{visibilidade / 1000:.2f} km',
                                 inline=True)
                await message.channel.send(embed=embed7)
        
        if message.content.startswith('>$<'):
            argsd = message.content.split()
            try:
                if len(argsd) == 1:
                    response = requests.get(
                        'https://v6.exchangerate-api.com/v6/[your API key]/latest/USD'
                    )
                    data = response.json()
                    valor = data['conversion_rates']['BRL']
                    embeddolar = discord.Embed(
                        title='Conversão Dólar - Real.',
                        description=f'1,00 USD = {valor:.2f} BRL',
                        color=0x1F870D)
                    embeddolar.set_footer(
                        text='Staff do servidor [nome do seu servidor].',
                        icon_url='[link da imagem do seu footer]')
                    await message.channel.send(embed=embeddolar)
                if len(argsd) == 2:
                    response = requests.get(
                        'https://v6.exchangerate-api.com/v6/[your API key]/latest/USD'
                    )
                    data = response.json()
                    argsd1 = argsd[1].upper()
                    valor = data['conversion_rates'][f'{argsd1}']
                    embeddolar1 = discord.Embed(
                        title=f'Conversão USD - {argsd1}.',
                        description=f'1,00 USD = {valor:.2f} {argsd1}',
                        color=0x1F870D)
                    embeddolar1.set_footer(
                        text='Staff do servidor [nome do seu servidor].',
                        icon_url='[link da imagem do seu footer]')
                    await message.channel.send(embed=embeddolar1)
            except KeyError as erro:
                dolar = await message.channel.send(
                    f'{message.author.mention} a moeda {erro} não foi encontrada, por favor confira sua abreviação.'
                )
                await message.delete()
                await dolar.delete(delay=5)        

        if message.content.startswith('>fox'):
            sitefox = requests.get('https://randomfox.ca/floof')
            dicionariofox = sitefox.json()
            link = dicionariofox['image']
            embed8 = discord.Embed(title='🦊 Fox!',
                                   description='',
                                   url=f'{link}',
                                   color=0x92481a)
            embed8.set_image(url=f'{link}')
            await message.channel.send(embed=embed8)

        if message.content.startswith('>bird'):
            num = randint(1, 100)
            sitebird = requests.get(f'http://shibe.online/api/birds?count={num}&urls=true&httpsUrls=true')
            listabird = sitebird.json()
            link = listabird[0]
            embed8 = discord.Embed(title='🐦 Bird!',
                                   description='',
                                   url=f'{link}',
                                   color=0xdd2e44)
            embed8.set_image(url=f'{link}')
            await message.channel.send(embed=embed8)

        if message.content.startswith('>duck'):
            sitefox = requests.get('https://random-d.uk/api/v2/quack')
            dicionarioduck = sitefox.json()
            link = dicionarioduck['url']
            embed8 = discord.Embed(title='🦆 Duck!',
                                   description='',
                                   url=f'{link}',
                                   color=0x8ea031)
            embed8.set_image(url=f'{link}')
            await message.channel.send(embed=embed8)
                
        channel0 = client.get_channel([id do canal em que todas as mensagens recebem uma reação predefinida])
        if message.channel == channel0:
            await message.add_reaction('[\emoji da reação que você quer que seja adicionada]')

        
@client.event
async def on_raw_reaction_add(payload):
    channel = [id do canal para onde irão as sugestões ainda sem aprovação]
    if payload.member.id == client.user.id:
        return
    if payload.channel_id != channel:
        return
    channel01 = client.get_channel(channel)
    msg00 = await channel01.fetch_message(payload.message_id)
    if payload.emoji.name == '✅':
        msg01 = msg00.reactions
        contagem = msg01[1].count
        if contagem >= 3:
            channel02 = client.get_channel([id do canal de sugestões aprovadas])
            msg02 = msg00.embeds[0]
            msg03 = await channel02.send(embed=msg02)
            await msg03.add_reaction('✅')
            await msg03.add_reaction('❎')
            await msg00.clear_reaction('✅')
    if payload.emoji.name == '❎':
        msg01 = msg00.reactions
        contagem = msg01[0].count
        if contagem >= 3:
            await msg00.delete()
 

@client.event
async def on_member_join(member):
    if member.bot:
        return
    else:
        channel = client.get_channel([id do canal de novos membros])

        embed4 = discord.Embed(
            title='',
            description=f'Olá {member.mention}! Bem vindo ao Jealous King!',
            color=0x25BCC7)
        embed4.add_field(
            name='**Regras**',
            value=
            'Saiba mais sobre nossas diretrizes no canal <#[id do canal de regras]>.',
            inline=False)
        embed4.add_field(
            name='**Cargos**',
            value=
            'Você pode escolher seu cargo no canal <#[id do canal de bem-vindos]>.',
            inline=False)
        embed4.set_author(
            name='🔰 Bem-Vindo! ⚔️', icon_url='[link da imagem que vai aparecer no icone do autor]')
        embed4.set_thumbnail(url=member.avatar_url)
        embed4.set_footer(
            text='Staff do servidor Jealous King.',
            icon_url='[link da imagem do seu footer]')
        embed4.set_image(url='[link da imagem do seu embed]')
        await channel.send(embed=embed4)


keep_alive()
client.run('[O Token do bot vai aqui!]')
