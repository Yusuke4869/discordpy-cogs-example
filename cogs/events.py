from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    """
    イベント
    """
    @commands.Cog.listener()
    async def on_message(self, ctx):

        if ctx.author.bot:
            return

        content = ctx.content

        if content == "こんにちは":
            await ctx.channel.send(f"こんにちは！ {ctx.author.display_name} さん！")

        # オウム返し
        else:
            await ctx.channel.send(content)

    """
    オリジナルイベント
    """
    @commands.Cog.listener()
    async def on_hi(self, ctx):
        await ctx.channel.send(f"Hi!, {ctx.author.name}")

def setup(bot):
    bot.add_cog(Events(bot))