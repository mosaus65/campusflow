import json


def save_tickets(tickets, filename="tickets.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)


def load_tickets(filename="tickets.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
