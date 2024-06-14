import discord
import os 
import random
intents = discord.Intents.default()
intents.message_content = True
bot = discord.bot(intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.event
async def on_message(ctx): 
  tips = os.listdir('tips')
  if tips:
      tip_name = random.choice(tips)
      with open(f'tips/{tip_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
bot.run ("MTI0ODc1NDY4NzA4NDIwNDAzNQ.GQ_c-Y.2dtG_fGIg0CN3QywGkVHxmLPtcTZQA9BhKPTnA")