import openai
import pyttsx3
import speech_recognition as sr
import json
from chad.lore import load_lore
from chad.logger import log

def generate_reply():
    with open("config.json") as f:
        config = json.load(f)

    openai.api_key = config["openai_key"]
    voice = config.get("voice_token", "Guy")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
    except:
        return "Sorry, I didn't catch that."

    lore_data = load_lore()
    messages = [{"role": "system", "content": f"You are Chad, a crime-obsessed, rude GTA RP character. Use this lore: {lore_data}"},
                {"role": "user", "content": text}]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = response.choices[0].message.content.strip()

    engine = pyttsx3.init()
    engine.setProperty('voice', voice)
    engine.say(reply)
    engine.runAndWait()
    return reply
