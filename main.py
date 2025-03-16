from symbol import return_stmt

patients = [
    {
        "Name": "Tony Tony Chopper",
        "Age": 17,
        "Blood Type": "X",
        "Condition": "Excellent",
        "Allergies": ["None"]
    }
]



def add_patient():
    print("\n--- Add New Patient ---")

    while True:
        name = input("Enter patient's name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")

    while True:
        try:
            age = int(input("Enter patient's age: "))
            if age > 0:
                break
            print("Age must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    valid_blood_types = ["A", "B", "AB","O"]
    while True:
        blood_type = input("Enter patient's blood type (A, B, AB, or O): ").upper().strip()
        if blood_type in valid_blood_types:
            break
        print("Invalid blood type. Please choose from A, B, AB, or O.")

    condition = input("Enter patient's current condition (e.g., stable, critical): ").strip()

    allergies = input("Enter any allergies (comma-separated): ").strip().split(',')

    new_patient = {
        "Name": name,
        "Age": age,
        "Blood Type": blood_type,
        "Condition": condition,
        "Allergies": [allergy.strip() for allergy in allergies]
    }

    patients.append(new_patient)
    print(f"\nPatient '{name}' has been successfully added!")



# Function to display patients with sorting and detailed options
def view_patients():
    if not patients:
        print("\nNo patients found in the system.")
        return  # Exit the function if the list is empty

    # Sorting Options
    print("\n--- Display Options ---")
    print("1. Sort by Name")
    print("2. Sort by Age")
    print("3. Sort by Condition")
    print("4. Display Detailed Patient Info")
    print("5. Back to Main Menu")

    choice = input("Choose an option: ")

    # Sorting Logic
    if choice == "1":
        sorted_patients = sorted(patients, key=lambda p: p["Name"])
        print("\n--- Patients (Sorted by Name) ---")
    elif choice == "2":
        sorted_patients = sorted(patients, key=lambda p: p["Age"])
        print("\n--- Patients (Sorted by Age) ---")
    elif choice == "3":
        sorted_patients = sorted(patients, key=lambda p: p["Condition"])
        print("\n--- Patients (Sorted by Condition) ---")
    elif choice == "4":
        print("\n--- Detailed Patient Information ---")
        for patient in patients:
            print(f"\nName: {patient['Name']}")
            print(f"Age: {patient['Age']}")
            print(f"Blood Type: {patient['Blood Type']}")
            print(f"Condition: {patient['Condition']}")
            print(f"Allergies: {', '.join(patient['Allergies']) if patient['Allergies'] else 'None'}")
        return
    elif choice == "5":
        return
    else:
        print("Invalid choice. Returning to menu.")
        return

    # Display Sorted Patients (Summary View)
    for patient in sorted_patients:
        print(f"{patient['Name']} (Age: {patient['Age']})")

# Function to search for a patient.
def search_patient():
    if not patients:
        print("\nNo patients found in the system.")
        return

    search_query = input("\nEnter the patient's name to search for: ").strip().lower()

    # Find matches (case-insensitive search)
    matches = [p for p in patients if search_query in p['Name'].lower()]

    if matches:
        print(f"\n--- Search results for '{search_query}' ---")
        for patient in matches:
            print(f"\nName: {patient['Name']}")
            print(f"Age: {patient['Age']}")
            print(f"Blood Type: {patient['Blood Type']}")
            print(f"Condition: {patient['Condition']}")
            print(f"Allergies: {', '.join(patient['Allergies']) if patient['Allergies'] else 'None'}")
    else:
        print(f"\nNo patients found matching '{search_query}'.")




### Keep at bottom of code.
# Update main menu to include this feature
def main_menu():
    while True:
        print("\n--- Medical Program Menu ---")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Search for Patient")
        print("4. Update Patient Information")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            print("Updating patient information... (Coming Soon)")
        elif choice == "5":
            print("Saving data and exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()