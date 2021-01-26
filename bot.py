import asyncio
from time import sleep
import discord
from discord import Member
from datetime import date
from keep_alive import keep_alive

intents = discord.Intents.all()
client = discord.Client(intents=intents)


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
    if message.author.bot:
        return
    if message.content.startswith('>help'):
        embed0 = discord.Embed(
            title=f'Bem vindo ao embed de ajuda do [nome do seu bot]!',
            description=f' ',
            color=0xFFFAFA)
        embed0.set_thumbnail(url='[link da thumbnail do seu embed]')
        embed0.set_footer(
            text='Staff do servidor [nome do seu servidor].',
            icon_url='[link da imagem do seu footer.]')
        embed0.add_field(
            name='>Hello',
            value='Esse comando serve para comprimentar o Bot.',
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
                await mensagemsugestoes.add_reaction('✅')
                await mensagemsugestoes.add_reaction('❎')
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

    channel0 = client.get_channel([id do canal em que todas as mensagens recebem uma reação predefinida])
    if message.channel == channel0:
        await message.add_reaction('[\emoji da reação que você quer que seja adicionada]')


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
