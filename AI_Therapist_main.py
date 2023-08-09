import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a psychologist and therapist with 40+ years of experience. Your job is to utilize the techniques you've learnt over the years to make your patients feel better. These techniques include but are not limited to appropriate use of silence, rephrasing or paraphrasing, reflection, summarizing, and acknowledgement"}]



def Therapist(patient):
    messages.append({"role": "user", "content": patient})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

therapist = gradio.Interface(fn=Therapist, inputs = "text", outputs = "text", title = "Albert The AI Therapy Advisor")

therapist.launch(share=True)