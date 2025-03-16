patients = [
    {
        "Name": "Tony Tony Chopper",
        "Age": 17,
        "Blood Type": "X",
        "Condition": "Excellent",
        "Allergies": ["None"]
    }
]

def main_menu():
    while True:
        print("\n--- Medical Program Menu P ---")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Search for Patient")
        print("4. Update Patient Information")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            print("Viewing all patients... (coming soon)")
        elif choice == "3":
            print("Searching for patient... (coming soon)")
        elif choice == "4":
            print("Updating patient information... (Coming soon)")
        elif choice == "5":
            print("Saving and Exiting program (save function coming soon)")
            break
        else:
            print("Invalid choice. Please try Again.")

if __name__ == "__main__":
    main_menu()

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