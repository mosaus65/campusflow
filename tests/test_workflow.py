def assign_ticket(ticket, staff_name):
    if not staff_name.strip():
        raise ValueError("Staff name cannot be empty")

    if ticket["status"] == "resolved":
        raise ValueError("Reopen the ticket before assigning it")

    ticket["assigned_to"] = staff_name
    return ticket

import unittest
from campusflow.tickets import create_ticket
from campusflow.workflow import (
    assign_ticket,
    start_ticket,
    resolve_ticket,
    reopen_ticket,
)


class TestWorkflow(unittest.TestCase):
    def setUp(self):
        self.ticket = create_ticket(
            "T001", "Wi-Fi problem", "Network", "high", 15
        )

    def test_assign_ticket(self):
        assign_ticket(self.ticket, "Amina")
        self.assertEqual(self.ticket["assigned_to"], "Amina")

    def test_cannot_start_unassigned_ticket(self):
        with self.assertRaises(ValueError):
            start_ticket(self.ticket)

    def test_start_ticket(self):
        assign_ticket(self.ticket, "Amina")
        start_ticket(self.ticket)
        self.assertEqual(self.ticket["status"], "in_progress")

    def test_resolve_ticket(self):
        assign_ticket(self.ticket, "Amina")
        start_ticket(self.ticket)
        resolve_ticket(self.ticket)
        self.assertEqual(self.ticket["status"], "resolved")

    def test_reopen_ticket(self):
        assign_ticket(self.ticket, "Amina")
        start_ticket(self.ticket)
        resolve_ticket(self.ticket)
        reopen_ticket(self.ticket)
        self.assertEqual(self.ticket["status"], "open")

    def test_empty_staff_name(self):
        with self.assertRaises(ValueError):
            assign_ticket(self.ticket, "   ")


if __name__ == "__main__":
    unittest.main()
