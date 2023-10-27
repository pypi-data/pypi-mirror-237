#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : chatbot
# @Time         : 2023/10/27 14:31
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : https://nicedouble-streamlitantdcomponentsdemo-app-middmy.streamlit.app/

from meutils.pipe import *
from meutils.ai_cv.latex_ocr import latex_ocr

import streamlit as st
import streamlit_antd_components as sac


class ChatMessage(BaseModel):
    name: str = "user"  # "user", "assistant", or str
    avatar: Optional[str] = None
    generator: Iterable = '我是一条内容'


def chat_message(message: ChatMessage, help: Optional[str] = None, message_hook: Optional[Callable] = None):
    """
        chat_message(ChatMessage())
        chat_message(ChatMessage(name='assistant'))

        def chat_messages(messages: List[ChatMessage]):
            for msg in messages:
                chat_message(msg)

        chat_messages([ChatMessage()] * 10)
    """
    with st.chat_message(name=message.name, avatar=message.avatar):
        message_placeholder = st.empty()
        response = ''
        for token in message.generator:
            # Display robot response in chat message container
            # time.sleep(0.1)
            response += token
            message_placeholder.markdown(response + "▌")

        message_placeholder.markdown(response, unsafe_allow_html=True, help=help)


        if message_hook: message_hook()



if __name__ == '__main__':
    st.markdown('### 🔥解题小助手')

    prompt = st.chat_input("    🤔 你可以问我任何问题")

    file = st.file_uploader('上传题目图片', type=[".jpg", ".jpeg", '.png'])
    if file:
        # _ = latex_ocr(file)
        # st.markdown(_)
        st.image(file)
    # st.image('ocr.png')
    chat_message(ChatMessage(generator='😘😘😘我是你的答题小助手！\n\n **参考示例**：'), message_hook=lambda: st.image('ocr.png'))

