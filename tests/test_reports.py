import unittest

from campusflow.reports import generate_report


class TestReports(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            {
                "id": "T001",
                "title": "Wi-Fi problem",
                "category": "Network",
                "urgency": "high",
                "affected_users": 15,
                "priority": "critical",
                "status": "open",
                "assigned_to": None,
                "notes": [],
            },
            {
                "id": "T002",
                "title": "Laptop problem",
                "category": "Hardware",
                "urgency": "medium",
                "affected_users": 3,
                "priority": "medium",
                "status": "in_progress",
                "assigned_to": "Mentor A",
                "notes": [],
            },
            {
                "id": "T003",
                "title": "Software installation",
                "category": "Software",
                "urgency": "low",
                "affected_users": 1,
                "priority": "low",
                "status": "resolved",
                "assigned_to": "Mentor B",
                "notes": [],
            },
        ]

    def test_report_totals(self):
        report = generate_report(self.tickets)

        self.assertEqual(report["total_tickets"], 3)
        self.assertEqual(report["resolved_count"], 1)
        self.assertEqual(report["unresolved_count"], 2)

    def test_report_status_counts(self):
        report = generate_report(self.tickets)

        self.assertEqual(
            report["by_status"],
            {
                "open": 1,
                "in_progress": 1,
                "resolved": 1,
            },
        )

    def test_report_category_counts(self):
        report = generate_report(self.tickets)

        self.assertEqual(
            report["by_category"],
            {
                "Network": 1,
                "Hardware": 1,
                "Software": 1,
                "Other": 0,
            },
        )

    def test_resolution_percentage(self):
        report = generate_report(self.tickets)

        self.assertAlmostEqual(
            report["resolution_percentage"],
            100 / 3,
        )

    def test_empty_report(self):
        report = generate_report([])

        self.assertEqual(report["total_tickets"], 0)
        self.assertEqual(report["resolved_count"], 0)
        self.assertEqual(report["unresolved_count"], 0)
        self.assertEqual(report["resolution_percentage"], 0.0)


if __name__ == "__main__":
    unittest.main()
