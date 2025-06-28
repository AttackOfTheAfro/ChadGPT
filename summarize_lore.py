import openai, json, requests
from bs4 import BeautifulSoup

with open("config.json") as f:
    config = json.load(f)

openai.api_key = config["openai_key"]

with open("lore_links.txt") as f:
    links = [line.strip() for line in f if line.strip()]

for link in links:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    text = soup.get_text()[:4000]

    prompt = f"Summarize this NoPixel lore into 3-5 bullet points:\n{text}"
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    bullets = response.choices[0].message.content.strip().split("\n")

    filename = link.split("/")[-1].lower().replace(" ", "_") + ".json"
    with open(f"lore_data/{filename}", "w") as out:
        json.dump(bullets, out, indent=2)
