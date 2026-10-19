def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10:
        return "high"
    elif urgency == "medium" or affected_users >= 3:
        return "medium"
    else:
        return "low"


def create_ticket(ticket_id, title, category, urgency, affected_users):
    if not title.strip():
        raise ValueError("Title cannot be empty")

    if category not in ["Network", "Hardware", "Software", "Other"]:
        raise ValueError("Invalid category")

    if urgency not in ["low", "medium", "high"]:
        raise ValueError("Invalid urgency")

    if not isinstance(affected_users, int) or isinstance(affected_users, bool) or affected_users < 1:
        raise ValueError("Affected users must be a positive integer")

    priority = calculate_priority(urgency, affected_users)

    ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None,
        "notes": []
    }

    return ticket

