import json
import csv
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/applications.json")

STATUSES = ["Applied", "Phone Screen", "Interview", "Offer", "Rejected", "Withdrawn"]


def load_data():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save_data(applications):
    with open(DATA_FILE, "w") as f:
        json.dump(applications, f, indent=2)


def next_id(applications):
    return max((a["id"] for a in applications), default=0) + 1


def add_application(applications):
    print("\n--- Add Application ---")
    app = {
        "id": next_id(applications),
        "company": input("Company: ").strip(),
        "title": input("Job Title: ").strip(),
        "location": input("Location: ").strip(),
        "link": input("Job Link: ").strip(),
        "salary": input("Salary (optional): ").strip(),
        "recruiter_name": input("Recruiter Name (optional): ").strip(),
        "recruiter_email": input("Recruiter Email (optional): ").strip(),
        "status": "Applied",
        "date_applied": datetime.today().strftime("%Y-%m-%d"),
        "follow_up_date": input("Follow-up Date (YYYY-MM-DD, optional): ").strip(),
        "notes": input("Notes (optional): ").strip(),
    }
    applications.append(app)
    save_data(applications)
    print(f"\n✓ Added: {app['title']} at {app['company']} (ID: {app['id']})")


def list_applications(applications):
    print("\n--- Applications ---")
    if not applications:
        print("No applications found.")
        return
    print(f"{'ID':<5} {'Company':<25} {'Title':<30} {'Status':<15} {'Date Applied'}")
    print("-" * 90)
    for a in applications:
        print(f"{a['id']:<5} {a['company']:<25} {a['title']:<30} {a['status']:<15} {a['date_applied']}")


def update_status(applications):
    print("\n--- Update Status ---")
    list_applications(applications)
    try:
        app_id = int(input("\nEnter Application ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    app = next((a for a in applications if a["id"] == app_id), None)
    if not app:
        print("Application not found.")
        return
    print(f"\nCurrent status: {app['status']}")
    for i, s in enumerate(STATUSES, 1):
        print(f"  {i}. {s}")
    try:
        choice = int(input("Select new status: ")) - 1
        app["status"] = STATUSES[choice]
        notes = input("Add a note (optional): ").strip()
        if notes:
            app["notes"] = (app.get("notes", "") + f"\n[{datetime.today().strftime('%Y-%m-%d')}] {notes}").strip()
        save_data(applications)
        print(f"✓ Status updated to: {app['status']}")
    except (ValueError, IndexError):
        print("Invalid choice.")


def delete_application(applications):
    print("\n--- Delete Application ---")
    list_applications(applications)
    try:
        app_id = int(input("\nEnter Application ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    app = next((a for a in applications if a["id"] == app_id), None)
    if not app:
        print("Application not found.")
        return
    confirm = input(f"Delete '{app['title']}' at '{app['company']}'? (y/n): ").strip().lower()
    if confirm == "y":
        applications.remove(app)
        save_data(applications)
        print("✓ Application deleted.")
    else:
        print("Cancelled.")


def search_applications(applications):
    print("\n--- Search Applications ---")
    query = input("Search (company, title, status, location): ").strip().lower()
    results = [
        a for a in applications
        if query in a["company"].lower()
        or query in a["title"].lower()
        or query in a["status"].lower()
        or query in a["location"].lower()
    ]
    if not results:
        print("No matches found.")
    else:
        print(f"\n{len(results)} result(s):")
        list_applications(results)


def export_applications(applications):
    print("\n--- Export Applications ---")
    if not applications:
        print("No applications to export.")
        return
    export_path = os.path.join(os.path.dirname(__file__), "../data/applications_export.csv")
    fields = ["id", "company", "title", "location", "link", "salary",
              "recruiter_name", "recruiter_email", "status", "date_applied",
              "follow_up_date", "notes"]
    with open(export_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(applications)
    print(f"✓ Exported {len(applications)} application(s) to:\n  {os.path.abspath(export_path)}")


def main():
    print("=== Job Application Tracker ===")
    while True:
        print("\n1. Add application")
        print("2. List all applications")
        print("3. Update status")
        print("4. Delete application")
        print("5. Search applications")
        print("6. Export to CSV")
        print("0. Exit")
        choice = input("\nSelect an option: ").strip()

        applications = load_data()

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            list_applications(applications)
        elif choice == "3":
            update_status(applications)
        elif choice == "4":
            delete_application(applications)
        elif choice == "5":
            search_applications(applications)
        elif choice == "6":
            export_applications(applications)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
