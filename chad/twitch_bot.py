from twitchio.ext import commands
import json
from chad.logger import log

with open("config.json") as f:
    config = json.load(f)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=config["twitch_token"], prefix="!", initial_channels=[config["twitch_channel"]])
        self.tone = "neutral"

    async def event_ready(self):
        print(f"Twitch bot ready as {self.nick}")

    @commands.command()
    async def tone(self, ctx):
        tone = ctx.message.content.split(" ", 1)[-1]
        self.tone = tone
        await ctx.send(f"Chad's tone set to {tone}.")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
