def generate_report(tickets):
    """Return ticket counts and resolution statistics."""

    statuses = ("open", "in_progress", "resolved")
    priorities = ("critical", "high", "medium", "low")
    categories = ("Network", "Hardware", "Software", "Other")

    total = len(tickets)

    by_status = {
        status: sum(
            1 for ticket in tickets
            if ticket.get("status") == status
        )
        for status in statuses
    }

    by_priority = {
        priority: sum(
            1 for ticket in tickets
            if ticket.get("priority") == priority
        )
        for priority in priorities
    }

    by_category = {
        category: sum(
            1 for ticket in tickets
            if ticket.get("category") == category
        )
        for category in categories
    }

    resolved_count = by_status["resolved"]
    unresolved_count = (
        by_status["open"] + by_status["in_progress"]
    )

    resolution_percentage = (
        resolved_count / total * 100
        if total > 0
        else 0.0
    )

    return {
        "total_tickets": total,
        "by_status": by_status,
        "by_priority": by_priority,
        "by_category": by_category,
        "unresolved_count": unresolved_count,
        "resolved_count": resolved_count,
        "resolution_percentage": resolution_percentage,
    }
