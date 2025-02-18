stopping = {"quit", "stop", "exit"}
while True:
    options = input("1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\nEnter your option: ")

    if options.lower() in stopping or options == "6" or options == 6:
            print("Program Finished !")
            break
    else:
        try:
            options = int(options)
        except ValueError:
            print("Invalid input. Please enter a number or Stop/Quit/Exit.")
            continue
        
    def add_new(func):
        def wrapper():
            if options == 1:
                info = input("Enter data as following (Employee ID, Name, Position, Salary): ")
                with open("employees.txt", "a") as file: 
                    func(file.write(f"{info}\n"))
                
            elif options == 2:
                with open("employees.txt") as file:
                    content = func(file.read())
                
                
                    lines = content.split("\n")
                for line in lines:
                    print(line)
            
            elif options == 3:
                employee_id = int(input("Enter employee's id number: "))
                employee_id = str(employee_id)
                with open("employees.txt") as file:
                    lines = file.readlines()
                
                
                for line in lines:
                    if employee_id in line:
                        print(f"Employee found: {line.strip()}")
                        
                        break

                if line not in lines:
                    print("Employee not found")

            elif options == 4:
                employee_id_to_update = input("Enter Employee ID to update: ")
                new_info = input("Enter new information: ")

                with open("employees.txt", "r") as file:
                    lines = file.readlines()  

                with open("employees.txt", "w") as file:
                    for line in lines:
                        if line.startswith(employee_id_to_update + ","): 
                            file.write(new_info + "\n")  
                        else:
                            file.write(line)  


            elif options == 5:
                emp_id = input("Enter Employee ID to delete: ")  
                with open("employees.txt", "r") as f: 
                    data = f.readlines() 

                with open("employees.txt", "w") as f: 
                    for index, line in enumerate(data): 
                        if emp_id not in line.strip(): 
                            f.write(line)
            
            

            elif options > 6 or options < 1:
                print("Please enter only numbers between 1 to 6")


        return wrapper
    
    

            
                

        

    @add_new

    def finish(fin):
        return fin  

    finish()

