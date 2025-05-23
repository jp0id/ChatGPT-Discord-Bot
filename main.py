import os

import discord
from dotenv import load_dotenv

from src.chatgpt import ChatGPT
from src.discordBot import DiscordClient, Sender
from src.logger import logger
from src.memory import Memory
from src.models import OpenAIModel
from src.server import keep_alive

load_dotenv()

models = OpenAIModel(api_key=os.getenv('OPENAI_API'), model_engine=os.getenv('OPENAI_MODEL_ENGINE'),
                     base_url=os.getenv('BASE_URL'))

memory = Memory(system_message='you are a helpful assistant.')
chatgpt = ChatGPT(models, memory)


def run():
    client = DiscordClient()
    sender = Sender()

    @client.tree.command(name="chat", description="与 AI BOT 聊天")
    async def chat(interaction: discord.Interaction, *, message: str):
        user_id = interaction.user.id
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        receive = chatgpt.get_response(user_id, message)
        await sender.send_message(interaction, message, receive)

    @client.tree.command(name="reset", description="清除与 BOT 的历史聊天记录")
    async def reset(interaction: discord.Interaction):
        user_id = interaction.user.id
        logger.info(f"resetting memory from {user_id}")
        try:
            chatgpt.clean_history(user_id)
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(f'> 已经清除了与BOT的历史聊天记录 < - <@{user_id}>')
        except Exception as e:
            logger.error(f"Error resetting memory: {e}")
            await interaction.followup.send('> Oops! Something went wrong. <')

    client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
    keep_alive()
    run()
