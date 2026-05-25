import sqlite3
from datetime import datetime

# Database setup aur tables create karne ka function
def init_db():
    conn = sqlite3.connect('it_support.db')
    cursor = conn.cursor()
    
    # Tickets Table (IT Support issues save karne ke liye)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            issue_description TEXT NOT NULL,
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Open',
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Naya IT ticket add karne ka function
def create_ticket(client, issue, priority):
    conn = sqlite3.connect('it_support.db')
    cursor = conn.cursor()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO tickets (client_name, issue_description, priority, created_at)
        VALUES (?, ?, ?, ?)
    ''', (client, issue, priority, time_now))
    
    conn.commit()
    conn.close()
    print(f"\n✅ Ticket successfully created for {client}!")

# Saare active tickets database se nikal kar dikhane ka function
def view_tickets():
    conn = sqlite3.connect('it_support.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tickets')
    rows = cursor.fetchall()
    conn.close()
    
    print("\n=== CURRENT IT SUPPORT TICKETS ===")
    if not rows:
        print("No active tickets found.")
    for row in rows:
        print(f"ID: {row[0]} | Client: {row[1]} | Issue: {row[2]} | Priority: {row[3]} | Status: {row[4]} | Date: {row[5]}")

# Ticket ka status update karne ka function (Open se Resolved)
def resolve_ticket(ticket_id):
    conn = sqlite3.connect('it_support.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tickets SET status = "Resolved" WHERE ticket_id = ?', (ticket_id,))
    conn.commit()
    conn.close()
    print(f"\n⚙️ Ticket ID {ticket_id} has been marked as RESOLVED.")

# Main Application Menu Interface
def main():
    init_db()
    while True:
        print("\n--- ENTERPRISE IT SUPPORT DATABASE SYSTEM ---")
        print("1. Log New IT Ticket")
        print("2. View All Database Tickets")
        print("3. Resolve an Active Ticket")
        print("4. Exit System")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            client = input("Enter Client/Employee Name: ")
            issue = input("Enter IT Issue Description: ")
            priority = input("Enter Priority (Low/Medium/High): ")
            create_ticket(client, issue, priority)
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            t_id = int(input("Enter Ticket ID to resolve: "))
            resolve_ticket(t_id)
        elif choice == '4':
            print("Shutting down IT Database Management System. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == '__main__':
    main()
