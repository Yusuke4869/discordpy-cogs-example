import discord
from discord.ext import commands
import random

class Dice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    """
    親コマンド dice

    invoke_without_command = True
        サブコマンドがなかったときに実行される

    case_insensitive = True
        大文字小文字の区別なし（親コマンドは区別あり）
    """
    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def dice(self, ctx):
        embed = discord.Embed(title="サイコロ", color=0xf4a460)
        embed.add_field(name="dice shake [N]", value="1-6までのサイコロをN回振ります. 最大10回", inline=False)
        embed.add_field(name="dice random [N] [a] [b] [c] ... [f]", value="数字をいじったサイコロをN回振ります\nサイコロに設定できる数字は最大6種類(重複可)\n10回まで振ることができます", inline=False)
        await ctx.send(embed=embed)

    """
    diceコマンドのサブコマンド shake
    """
    @dice.command()
    async def shake(self, ctx, n=None):
        embed = discord.Embed(title="サイコロ結果", color=0xf4a460)

        if n == None:
            embed.add_field(name="Error", value="引数が足りません")
            await ctx.send(embed=embed)
            return

        try:
            n = int(n)
        except ValueError:
            embed.add_field(name="Error", value="引数は整数にしてください")
            await ctx.send(embed=embed)
            return

        if n < 1 or n > 10:
            embed.add_field(name="Error", value="サイコロは10回までしか振れません")
            await ctx.send(embed=embed)
            return

        result = [random.randint(1, 6) for i in range(n)]
        embed.add_field(name=f"結果", value=result, inline=False)
        await ctx.send(embed=embed)

    """
    diceコマンドのサブコマンド random
    """
    @dice.command()
    async def random(self, ctx, n=None, *nums):
        embed = discord.Embed(title="サイコロ結果", color=0xf4a460)

        if n == None or len(nums) == 0:
            embed.add_field(name="Error", value="引数が足りません")
            await ctx.send(embed=embed)
            return

        if len(nums) > 6:
            embed.add_field(name="Error", value="サイコロに設定できる数字は最大6です")
            await ctx.send(embed=embed)
            return

        try:
            n = int(n)
        except ValueError:
            embed.add_field(name="Error", value="引数は整数にしてください")
            await ctx.send(embed=embed)
            return

        if n < 1 or n > 10:
            embed.add_field(name="Error", value="サイコロは10回までしか振れません")
            await ctx.send(embed=embed)
            return

        result = [random.choice(nums) for i in range(n)]
        embed.add_field(name=f"結果", value=result, inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Dice(bot))