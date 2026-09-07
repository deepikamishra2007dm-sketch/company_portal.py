import datetime

# --- DATA STORAGE (Simulating a Database) ---
# Format: { emp_id: { "name": ..., "password": ..., "contact": ..., "specialization": ..., "attendance": {date_str: bool} } }
employees_db = {
    "E101": {
        "name": "Aman Sharma",
        "password": "emp1",
        "contact": "9876543210",
        "specialization": "Python Developer",
        "attendance": {}
    },
    "E102": {
        "name": "Priya Verma",
        "password": "emp2",
        "contact": "8765432109",
        "specialization": "UI/UX Designer",
        "attendance": {}
    }
}

BOSS_PASSWORD = "boss123"

def get_today_string():
    return datetime.date.today().strftime("%Y-%m-%d")

# --- LOGIN PORTAL ---
def main_portal():
    while True:
        print("\n" + "="*35)
        print(" WELCOME TO EMPLOYEE-BOSS PORTAL ")
        print("="*35)
        print("1. Login as Boss")
        print("2. Login as Employee")
        print("3. Exit")
        
        choice = input("Choose your role (1-3): ").strip()
        
        if choice == "1":
            boss_login()
        elif choice == "2":
            employee_login()
        elif choice == "3":
            print("\nThank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

# --- BOSS SECTION ---
def boss_login():
    print("\n--- BOSS LOGIN ---")
    password = input("Enter Boss Password: ").strip()
    
    if password == BOSS_PASSWORD:
        print("\nLogin Successful! Welcome, Boss.")
        boss_menu()
    else:
        print("❌ Incorrect Boss Password!")

def boss_menu():
    while True:
        print("\n" + "-"*30)
        print("       BOSS DASHBOARD       ")
        print("-"*30)
        print("1. View All Employees Profiles")
        print("2. Mark Today's Attendance")
        print("3. View Attendance Report")
        print("4. Add New Employee")
        print("5. Logout")
        
        choice = input("Enter your choice (1-5): ").strip()
        today = get_today_string()
        
        if choice == "1":
            print("\n--- EMPLOYEE PROFILES ---")
            for emp_id, info in employees_db.items():
                print(f"\nID: {emp_id} | Name: {info['name']}")
                print(f"Contact: {info['contact']} | Specialization: {info['specialization']}")
                
        elif choice == "2":
            print(f"\n--- MARK ATTENDANCE FOR TODAY ({today}) ---")
            for emp_id, info in employees_db.items():
                status = input(f"Is {info['name']} ({emp_id}) Present? (y/n): ").strip().lower()
                if status == 'y':
                    info['attendance'][today] = True
                    print(f"-> Marked True (Present)")
                else:
                    info['attendance'][today] = False
                    print(f"-> Marked False (Absent)")
                    
        elif choice == "3":
            print("\n--- ATTENDANCE REPORT ---")
            for emp_id, info in employees_db.items():
                print(f"\nEmployee: {info['name']} ({emp_id})")
                if not info['attendance']:
                    print("  No attendance recorded yet.")
                for date, present in info['attendance'].items():
                    status_str = "🟢 True (Present)" if present else "🔴 False (Absent)"
                    print(f"  Date {date}: {status_str}")
                    
        elif choice == "4":
            print("\n--- ADD NEW EMPLOYEE ---")
            new_id = input("Enter New Employee ID (e.g., E103): ").strip()
            if new_id in employees_db:
                print("❌ This ID already exists!")
                continue
            name = input("Enter Name: ").strip()
            pwd = input("Set Password: ").strip()
            contact = input("Enter Contact Number: ").strip()
            spec = input("Enter Specialization: ").strip()
            
            employees_db[new_id] = {
                "name": name,
                "password": pwd,
                "contact": contact,
                "specialization": spec,
                "attendance": {}
            }
            print(f"✅ Employee {name} added successfully!")
            
        elif choice == "5":
            print("Logging out from Boss Dashboard...")
            break
        else:
            print("Invalid choice!")

# --- EMPLOYEE SECTION ---
def employee_login():
    print("\n--- EMPLOYEE LOGIN ---")
    emp_id = input("Enter your Employee ID: ").strip()
    password = input("Enter your Password: ").strip()
    
    if emp_id in employees_db and employees_db[emp_id]['password'] == password:
        print(f"\nLogin Successful! Welcome, {employees_db[emp_id]['name']}.")
        employee_menu(emp_id)
    else:
        print("❌ Invalid Employee ID or Password!")

def employee_menu(emp_id):
    while True:
        info = employees_db[emp_id]
        print("\n" + "-"*30)
        print(f"    EMPLOYEE DASHBOARD ({info['name']})    ")
        print("-"*30)
        print("1. View My Profile Details")
        print("2. Check My Attendance History")
        print("3. Logout")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\n--- MY PROFILE ---")
            print(f"ID: {emp_id}")
            print(f"Name: {info['name']}")
            print(f"Contact: {info['contact']}")
            print(f"Specialization: {info['specialization']}")
            
        elif choice == "2":
            print("\n--- MY ATTENDANCE LOGS ---")
            if not info['attendance']:
                print("No attendance marked yet.")
            for date, present in info['attendance'].items():
                status_str = "🟢 True (Present)" if present else "🔴 False (Absent)"
                print(f"Date {date}: {status_str}")
                
        elif choice == "3":
            print("Logging out from Employee Dashboard...")
            break
        else:
            print("Invalid choice!")

# --- START THE PROGRAM ---
if __name__ == "__main__":
    main_portal