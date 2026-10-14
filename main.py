
from campusflow.tickets import create_ticket
from campusflow.storage import save_tickets, load_tickets


def show_menu():
    print("\n=== CampusFlow Helpdesk System ===")
    print("1. Create a ticket")
    print("2. List all tickets")
    print("3. Assign a ticket")
    print("4. Start working on a ticket")
    print("5. Resolve a ticket")
    print("6. Reopen a ticket")
    print("7. View reports")
    print("0. Save and exit")


def main():
    tickets = load_tickets()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            ticket_id = f"T{len(tickets) + 1:03d}"
            title = input("Enter ticket title: ")
            category = input("Enter category (Network, Hardware, Software, Other): ")
            urgency = input("Enter urgency (low, medium, high): ")

            try:
                affected_users = int(input("Enter number of affected users: "))
                ticket = create_ticket(
                    ticket_id, title, category, urgency, affected_users
                )
                tickets.append(ticket)
                save_tickets(tickets)
                print(f"Ticket {ticket_id} created successfully!")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "0":
            save_tickets(tickets)
            print("Tickets saved. Thank you for using CampusFlow!")
            break

        else:
            print("This option is not available yet.")


if __name__ == "__main__":
    main()
