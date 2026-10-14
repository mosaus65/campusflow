import unittest
from campusflow.tickets import calculate_priority, create_ticket


class TestTickets(unittest.TestCase):
    def test_critical_priority(self):
        self.assertEqual(calculate_priority("high", 15), "critical")

    def test_high_priority(self):
        self.assertEqual(calculate_priority("high", 2), "high")

    def test_medium_priority(self):
        self.assertEqual(calculate_priority("medium", 1), "medium")

    def test_low_priority(self):
        self.assertEqual(calculate_priority("low", 1), "low")

    def test_create_ticket(self):
        ticket = create_ticket(
            "T001", "Wi-Fi problem", "Network", "high", 15
        )
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            create_ticket("T002", "", "Network", "high", 15)

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            create_ticket("T003", "Wi-Fi problem", "Electricity", "high", 15)

    def test_invalid_urgency(self):
        with self.assertRaises(ValueError):
            create_ticket("T004", "Wi-Fi problem", "Network", "urgent", 15)

    def test_invalid_affected_users(self):
        with self.assertRaises(ValueError):
            create_ticket("T005", "Wi-Fi problem", "Network", "high", 0)


if __name__ == "__main__":
    unittest.main()
