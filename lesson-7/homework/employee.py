class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:

    def get_last_employee_id(self):
   
        try:
            with open("employees.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    return 1000  # If there is no any records it will start from 1000

            
            employee_ids = [int(line.split(",")[0]) for line in lines]
            return max(employee_ids)

        except (FileNotFoundError, ValueError):
            return 1000

    def add_new_employee(self, employee):
        with open("employees.txt", "a") as file:
            file.write(f"{employee.employee_id},{employee.name},{employee.position},{employee.salary}\n")
        print(f"{employee} added successfully!")

    def view_all_employees(self):
        try:
            with open("employees.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    print("No employees found.")
                    return

            employees = [line.strip().split(",") for line in lines]
            
            print("Sort employees by:")
            print("1. Name")
            print("2. Salary")
            choice = input("Enter choice (1/2): ").strip()

            if choice == "1":
                employees.sort(key=lambda x: x[1].lower())  # Sort by name
            elif choice == "2":
                employees.sort(key=lambda x: int(x[3]))  # Sort by salary
            else:
                print("Invalid choice! Displaying unsorted data.")

            print("\nAll Employee Records:")
            for emp in employees:
                print(", ".join(emp))

        except FileNotFoundError:
            print("No employee records found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def find_employee_by_id(self):
        employee_id = input("Enter Employee ID to search: ")
        found = False
        with open("employees.txt", "r") as file:
            for line in file:
                info = line.strip().split(",")
                if info[0].strip() == employee_id:
                    print(f"Employee found: {line.strip()}")
                    found = True
                    break
        if not found:
            print("No such employee found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        updated_records = []
        found = False

        with open("employees.txt", "r") as file:
            for line in file:
                info = line.strip().split(",")
                if info[0].strip() == employee_id:
                    found = True
                    print(f"Employee found: {line.strip()}")

                    new_name = input(f"Enter new name ({info[1]}): ").strip() or info[1]
                    new_position = input(f"Enter new position ({info[2]}): ").strip() or info[2]
                    new_salary = input(f"Enter new salary ({info[3]}): ").strip() or info[3]

                    updated_line = f"{employee_id},{new_name},{new_position},{new_salary}\n"
                    updated_records.append(updated_line)
                else:
                    updated_records.append(line)

        if not found:
            print("Employee not found.")
            return

        with open("employees.txt", "w") as file:
            file.writelines(updated_records)

        print("Employee information updated successfully.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        updated_records = []
        found = False

        with open("employees.txt", "r") as file:
            for line in file:
                info = line.strip().split(",")
                if info[0].strip() == employee_id:
                    found = True
                    print(f"Employee deleted: {line.strip()}")
                else:
                    updated_records.append(line)

        if not found:
            print("Employee not found.")
            return

        with open("employees.txt", "w") as file:
            file.writelines(updated_records)

        print(f"Employee record with ID {employee_id} deleted successfully.")


def main():
    manager = EmployeeManager()

    while True:
        print("""
Welcome to the Employee Records Manager !
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
""")
        try:
            option = int(input("Enter your choice: "))

            if option == 1:
                last_employee_id  = manager.get_last_employee_id()
                new_employee_id = last_employee_id + 1
                new_employee = Employee(
                    new_employee_id,
                    input("Enter name: "), 
                    input("Enter position: "), 
                    input("Enter salary: ")
                )
                manager.add_new_employee(new_employee)

            elif option == 2:
                manager.view_all_employees()

            elif option == 3:
                manager.find_employee_by_id()

            elif option == 4:
                manager.update_employee()

            elif option == 5:
                manager.delete_employee()

            elif option == 6:
                print("Goodbye!")
                break

            else:
                print("Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input. Enter only numbers between 1 and 6.")


if __name__ == "__main__":
    main()
