import os
import unittest
from campusflow.storage import save_tickets, load_tickets


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.filename = "test_storage_data.json"
        self.tickets = [
            {"id": "T001", "title": "Wi-Fi problem"},
            {"id": "T002", "title": "Computer problem"}
        ]

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_load_tickets(self):
        save_tickets(self.tickets, self.filename)
        loaded_tickets = load_tickets(self.filename)
        self.assertEqual(loaded_tickets, self.tickets)

    def test_missing_file_returns_empty_list(self):
        self.assertEqual(load_tickets("missing_tickets.json"), [])


if __name__ == "__main__":
    unittest.main()
