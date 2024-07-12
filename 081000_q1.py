def add_P(patients):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    illness = input("Enter type of illness: ")
    patient = {
                 'name': name, 
                 'age': age, 
                 'illness': illness
              }
    patients.append(patient)
    print(f" New Patient {name} added Successfully. ")

def display_P(patients):
    if not patients:
        print("No patients currently listed.")
    else:
        for patient in patients:
            print(f"Name: {patient['name']}, 
                    \nAge: {patient['age']}, 
                    \nIllness: {patient['illness']}")

def search_P(patients):
    name = input("Search Patient's 1Name: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Name: {patient['name']}, 
                    Age: {patient['age']}, 
                    Illness: {patient['illness']}")
            return
    print(f" Patient '{name}' not found.")

def remove_P(patients):
    name = input("Type Name to delete: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print(f"{name} deleted!")
            return
    print(f"Patient name '{name}' does not exist.")

def main():
    patients = []
    
    while True:
        print("\nHospital Patient Management System")
        print("1. Add new patient")
        print("2. Display patients")
        print("3. Patient Search")
        print("4. Remove patient")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_P(patients)
        elif choice == '2':
            display_P(patients)
        elif choice == '3':
            search_P(patients)
        elif choice == '4':
            remove_P(patients)
        elif choice == '5':
            print("Exited")
            break
        else:
            print(f"Invalid choice. 
                    Enter a number between 1 and 5.")

if __name__ == "__main__":
    main()