# chainlit run app.py -w

from chatbot.user_manager import user_state_manager
from tools import logger
import chainlit as cl

user_state = user_state_manager.get_user_state('Yona')

@cl.on_message
async def on_message(message: cl.Message):

    msg = cl.Message(content='')

    response = ''

    async with cl.Step(type='run'):
    
        for chunk in user_state['chatbot'].main(prompt=message.content, user_state=user_state):
            await msg.stream_token(chunk)

            response += chunk

        await msg.send()

    logger.info(response)