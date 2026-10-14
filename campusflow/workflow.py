def assign_ticket(ticket, staff_name):
    if not staff_name.strip():
        raise ValueError("Staff name cannot be empty")

    if ticket["status"] == "resolved":
        raise ValueError("Reopen the ticket before assigning it")

    ticket["assigned_to"] = staff_name
    return ticket


def start_ticket(ticket):
    if ticket["status"] != "open":
        raise ValueError("Only open tickets can be started")

    if not ticket["assigned_to"]:
        raise ValueError("Assign the ticket before starting work")

    ticket["status"] = "in_progress"
    return ticket


def resolve_ticket(ticket):
    if ticket["status"] != "in_progress":
        raise ValueError("Only in-progress tickets can be resolved")

    ticket["status"] = "resolved"
    return ticket


def reopen_ticket(ticket):
    if ticket["status"] != "resolved":
        raise ValueError("Only resolved tickets can be reopened")

    ticket["status"] = "open"
    return ticket
