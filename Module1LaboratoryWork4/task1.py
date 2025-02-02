import json
def task() -> float:
    input_path = "input.json"
    with open(input_path, "r", encoding="utf-8") as infile:
        data = json.load(infile)
    total_sum = sum(item["score"] * item["weight"] for item in data)
    return round(total_sum, 3)
print(task())
