import json

def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        data = [json.loads(line) for line in f if line.strip()]
    return data


# example
# path1 = "/Users/pelinsutopaloglu/Thesis/Thesis-Project/data/raw/en_unspecific.jsonl"
# print(load_data(path1)[7])

