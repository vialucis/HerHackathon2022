import os
import openai

def gpt3_answer(text):
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"I am a chatbot and my customer just asked me: \n \"\"\" {text} \n \"\"\" " \
             f"I am answering: \n\"\"\"\n"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )

    output_text = response['choices'][0]["text"]

    return output_text
