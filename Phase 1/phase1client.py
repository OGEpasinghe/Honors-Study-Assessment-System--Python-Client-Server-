#import client module to communicate with xmlrpc server
import xmlrpc.client



#function to get marks (takes in only 5 marks)
def get_marks():
    marks = []
    for i in range(5): #set to 5 to make it easier during testing
        while True:
            try:
                unitCode = input(f"Enter unit {i+1} code: ")
                input_marks = int(input(f"Enter marks for unit {i+1}: "))
                if input_marks >= 0 and input_marks <= 100: #validation to only have marks within proper range
                    marks.append((unitCode, input_marks)) #if in range it appends to the list
                    break
                else:
                    print("Please enter valid marks (0 - 100)") 
            except ValueError:
                print("Please enter a valid number.")
        
    return marks

def main():
    

    #proxy created to communicate with the server located at the sepcified IP and port
    #please include the IP address of the machine which the server is on
    client = xmlrpc.client.ServerProxy(f'http://192.168.152.128:6789/')
    print("* * * WELCOME TO HEPaS - Phase 1 * * *")
    print()

    while True:
        
        is_oust = input("Are you an OUST student? (yes/no): ").lower()
        while is_oust not in ["yes", "no"]:
            print("Please enter 'Yes' or 'No'.")
            is_oust = input("Are you an OUST student? (yes/no): ").lower()
        if is_oust == "yes":
            studentName = input("Enter your student Name: ")
            studentID = input("Enter your student ID: ")
            while not studentID.isdigit() or len(studentID) != 8:
                print("Please enter validID... 8 digits only")
                personID = input("Enter your student ID: ")

            user_ID = studentID
            break
        elif is_oust == "no":
            
            user_ID = input("Enter your person ID number: ")
            while not user_ID.isdigit() or len(user_ID) != 8:
                print("Please enter valid ID... 8 digits only")
                personID = input("Enter your person ID: ")
            break
        else:
            print("Invalid Input!")
    marks = get_marks()

    #function called from the server, User ID and marks are passed as arguements
    #the result from the server is captured in result variable
    result = client.averageCalc(user_ID, marks)
    avg, message, marks = result
    print()
    print("ENTERED MARKS: ", marks)
    print("Your Average: ", avg)
    print(message)
    input("\n* * * Press ENTER to exit... * * *")
    

if __name__== "__main__":
    main()
    
