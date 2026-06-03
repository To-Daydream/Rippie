import discord
import os
from dotenv import load_dotenv
from discord import ApplicationContext, Embed, ui

load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_IDS = [int(id.strip()) for id in os.getenv("GUILD_IDS", "").split(",") if id.strip()]
ABOUT_THUMBNAIL_URL = os.getenv("ABOUT_THUMBNAIL_URL")

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=GUILD_IDS, description="View what Rippie's all about!")
async def about(ctx : ApplicationContext):
    """shows basic information about rippie"""

    owner_url = 'https://discord.com/users/'
    github_project = 'https://github.com/'
    support_url = 'https://discord.gg/'

    embed = Embed(color=0xFFFFFF)
    embed.set_author(name='Rippie', url=github_project)
    embed.set_thumbnail(url=ABOUT_THUMBNAIL_URL)
    embed.add_field(name='DEV:',
                    value=f'[vie]({owner_url})',
                    inline=False,)
    #embed.add_field(name='ᴄᴏɴᴛʀɪʙᴜᴛᴏʀꜱ:',
                    #value='[empty](https://github.com/)\n'
                    #'[person2](https://github.com/)',
                    #inline=False)
    
    view = ui.View()
    view.add_item(ui.Button(label='GITHUB', url=github_project, row=0))
    view.add_item(ui.Button(label='SUPPORT SERVER', url=support_url,
                            row=0))

    print(f'Sending about embed...')

    await ctx.respond(embed=embed, view=view)

bot.run(TOKEN)