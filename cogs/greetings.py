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

    """
    hi コマンド
    prefix + hi で呼び出される

    on_hi イベントを呼び出す
    """
    @commands.command()
    async def hi(self, ctx):
        self.bot.dispatch("hi", ctx)

def setup(bot):
    bot.add_cog(Greetings(bot))