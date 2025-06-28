import os, json

def load_lore():
    lore_folder = "lore_data"
    summaries = []
    for file in os.listdir(lore_folder):
        if file.endswith(".json"):
            with open(os.path.join(lore_folder, file)) as f:
                data = json.load(f)
                summaries.extend(data)
    return "\n".join(summaries)
