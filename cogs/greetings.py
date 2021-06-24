from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    """
    このクラスのコマンド一覧を表示
    """
    @commands.command()
    async def all(self, ctx):
        cog = self.bot.get_cog("Greetings")
        commands = cog.get_commands()
        await ctx.send([c.name for c in commands])

    """
    hello コマンド
    prefix + hello で呼び出される
    """
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("hello")

def setup(bot):
    bot.add_cog(Greetings(bot))