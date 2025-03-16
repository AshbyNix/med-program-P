patients = [
    {
        "Name": "Tony Tony Chopper",
        "Age": 17,
        "Blood Type": "X",
        "Floor and Room": "1A001",
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
            print("Adding new patient... (Coming soon)")
        elif choice == "2":
            print("Viewing all patients... (coming soon)")
        elif choice == "3":
            print("Searching for patient... (coming soon)")
        elif choice == "4":
            print("Updating patient information... (Coming soon)")
        elif choice == "5":
            print("Saving and Exiting program (save function coming soon)")
            break