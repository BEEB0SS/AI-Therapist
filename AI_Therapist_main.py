import openai
import gradio
import os


openai.api_key = os.environ["api_key"]

therapist_data = os.environ["therapist_data"]
messages = [{"role": "system", "content": therapist_data}]



def Therapist(patient):
    messages.append({"role": "user", "content": patient})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

therapist = gradio.Interface(fn=Therapist, inputs = "text", outputs = "text", title = "Albert The AI Therapist")

#therapist.launch(share=True)
therapist.launch()
