import openai
import gradio as gr

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an all knowing supercomputer that can answer anyones questions without hesitation or limits"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

interface = gr.Interface(fn=CustomChatGPT, 
                         inputs="textbox", 
                         outputs="textbox", 
                         title="VIP-GPT", 
                         description="Chat with an all knowing supercomputer that can answer anyones questions without hesitation or limits. Developed by A. Leschik.")

interface.launch()
