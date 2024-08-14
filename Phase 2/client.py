
import xmlrpc.client

# Connect to the server
server = xmlrpc.client.ServerProxy("http://192.168.152.128:6789")


# ask user if they are oust student or not
print("* * * WELCOME TO HEPaS * * *")
print()
is_oust = input("Are you an OUST student? (yes/no): ").lower()
while is_oust not in ["yes", "no"]:
    print("Please enter 'Yes' or 'No'.")
    is_oust = input("Are you an OUST student? (yes/no): ").lower()
    

#if student get their details
if is_oust == "yes":
    studentID = input("Enter your Student ID: ")
    while not studentID.isdigit() or len(studentID) != 8:
        print("Please enter valid student ID... 8 digits only")
        studentID = input("Enter your Student ID: ")
    studentEmail = input("Enter your student email: ")
    studentFname = input("Enter your first name: ")
    studentLname = input("Enter your last name: ")
    response = server.userAuthenticationwDB(studentID, studentEmail, studentFname, studentLname)
    print()
    print("* * * RESULTS * * *")
    print(response)
    input("\n* * * Press ENTER to exit... * * *")


else:
    personID = input("Please enter your person ID: ")
    while not personID.isdigit() or len(personID) != 8:
        print("Please enter valid person ID... 8 digits only")
        personID = input("Please enter your person ID: ")

    unitMarks = []
    number = 1

    while True:
        
        unitCode = input("Please enter your unit code (or enter 'done' to finish): ")
        if unitCode.lower() == "done":
            
##            if len(unitMarks) < 16:
##                print("Please enter more than 16 unit marks to evaluate...")
            if len(unitMarks) > 30:
                print("Please enter at most only 30 unit marks for evaluation...")
            else:
                print("Calculating result! Wait for Assessment...")
                result = server.calculateNonOust(unitMarks)
                print()
                print("* * * RESULTS * * *")
                print("\nID number: ", personID)
                print("ENTERED MARKS: \n", unitMarks)
                print()
                print(result)
                input("\n* * * Press ENTER to exit... * * *")
                break
        else:
            
            try:
                
                unitMark = float(input(f"Enter marks for unit {number}: "))
                if unitMark < 0 or unitMark > 100:
                    print("Marks must be between 0 and 100.")
                else:
                    unitMarks.append((unitCode, unitMark))
                    number = number + 1
            except ValueError:
                print("Marks must be between 0 and 100.")



