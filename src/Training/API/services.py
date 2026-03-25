import json


def load_report():
    with open("report.json") as f:
        return json.load(f)
