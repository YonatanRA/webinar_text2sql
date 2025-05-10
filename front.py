import chainlit as cl
from tools import logger
from chatbot.chatclass import Text2SQL


chatbot = Text2SQL()

@cl.on_message
async def on_message(message: cl.Message):

    msg = cl.Message(content='')

    response = ''

    async with cl.Step(type='run'):
    
        for chunk in chatbot.main(prompt=message.content):
            await msg.stream_token(chunk)

            response += chunk

        await msg.send()

    logger.info(response)
    