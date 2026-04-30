import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot Casa Sustentável logado como {bot.user}')

    canal_geral = discord.utils.get(bot.get_all_channels(), name="geral")
    
    if canal_geral: 
        await canal_geral.send("🟢 **Opa, cheguei! O bot está online e pronto para uso!**")
    else:
        print("Aviso: Não encontrei nenhum canal com o nome 'geral'.")

@bot.command()
async def dica_casa(ctx):
    dicas = [
        "Separe um cantinho na cozinha apenas para embalagens secas (plástico, vidro e papelão). Facilita muito a reciclagem! ♻️",
        "Trocar as lâmpadas antigas por LED não só ajuda o meio ambiente, como reduz muito a sua conta de luz no fim do mês. 💡📉",
        "Antes de ir ao mercado, deixe sacolas retornáveis (ecobags) no porta-malas do carro ou perto da porta. 🛍️🚗"
    ]
    await ctx.send(random.choice(dicas))

@bot.command()
async def economia(ctx):
    await ctx.send("Dica de economia: Feche a torneira enquanto ensaboa a louça. Isso pode economizar até 100 litros de água por lavagem! 🚰💰")

bot.run("")
