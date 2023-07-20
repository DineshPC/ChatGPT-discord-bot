# import necessary modules
from dotenv import load_dotenv
import discord
import os
import asyncio
from app.chatgpt_ai.openai import chatgpt_response

# initialize dotenv or load dotenv
load_dotenv()

# getting discord token from environment 
discord_token = os.getenv('DISCORD_TOKEN')

# Define a class for Discord bot
class MyClient(discord.Client):
    


    # Method to run when the bot is ready
    async def on_ready(self):
        print("Successfully logged in as: ", self.user)

    # Method to run when a message is sent in the channel
    async def on_message(self, message):
        print(message.content)
        
        # Ignore if the message is sent by the bot itself
        if message.author == self.user:
            return
        
        command, user_message = None, None
        
        # Check if the message contains any of the specified commands
        for text in ['/ai', '/bot', '/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)
                
        # If the command is valid, get the response from the OpenAI chatbot and send it to the channel
        if command in ['/ai', '/bot', '/chatgpt']:
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")
            
# Define the intents and specify that the bot should listen to message content
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot client and run it
client = MyClient(intents=intents)
client.run(discord_token)