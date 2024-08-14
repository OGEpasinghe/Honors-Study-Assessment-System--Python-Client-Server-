from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


#proxy created to communicate with the database server
#please change the IP address to the IP address of the database server machine.
dbServer =xmlrpc.client.ServerProxy("http://localhost:8000")

#function to calculate average and assess for NON OUST user inputs
def calculateNonOust(unitMarks):
    if len(unitMarks) <= 15:
        return "Completed less than 16 units! DOES NOT QUALIFY FOR HONORS"

    unitFails = sum(1 for _, unitMark in unitMarks if int(unitMark) < 50)

    if unitFails >= 6:
        return "With 6 or more Fails! DOES NOT QUALIFY FOR HONORS STUDY"

    totalMarks = sum(int(unitMark) for _, unitMark in unitMarks)
    courseAvg = round((totalMarks / len(unitMarks)),2)

    sortMarks = sorted(unitMarks, key = lambda x: int(x[1]), reverse = True)
    topEightMarks = sortMarks[:8]
    topEightAvg = sum(int(unitMark) for _, unitMark in topEightMarks) /8

    if courseAvg >= 70:
    
        return f"Average: {courseAvg} \nQUALIFIES FOR HONORS STUDY!"
    elif courseAvg >= 65 and courseAvg < 70:
        if topEightAvg >= 80:
            return f"Average: {courseAvg} \nTop Eight Average: {topEightAvg} \nQUALIFIES FOR HONORS STUDY"
        else:
            return f"Average: {courseAvg} \nTop Eight Average: {topEightAvg} \nMAY HAVE A GOOD CHANCE! Needs further assessment!"
    elif courseAvg >= 60 and courseAvg <65:
        if topEightAvg >= 80:
            return f"Average: {courseAvg} \nTop Eight Average: {topEightAvg} \nMAY HAVE A GOOD CHANCE! Must be carefully reassessed and get the coordinator's permission"
        else:
            return f"Average: {courseAvg} \nDOES NOT QUALIFY FOR HONORS!"
    else:
        return f"Average: {courseAvg} \nDOES NOT QUALIFY FOR HONORS!"
    


#function to authenticate user, this checks against the database for authetication            
def userAuthenticationwDB(studentID, studentEmail, studentFname, studentLname):
        
    #this runs the function in the database server and returns it output here
    response = dbServer.userAuthentication(studentID, studentEmail, studentFname, studentLname)
    #return response
    if response != "User Authenticated!":
        return "\nAuthentication Failed, Please try with correct details!"
    print("User Authenticated")
    
#once user is authenticated, they will be evaluated according to their unit marks in the database
    #the following logic is similar to the non OUST calcualtion
    studentMarks = dbServer.retrieveMarks(studentID)

    

    if len(studentMarks) <= 15:
        return "Completed less than 16 units! DOES NOT QUALIFY FOR HONOURS"

    unitFails2 = sum(1 for _, mark in studentMarks if mark < 50)
    if unitFails2 >= 6:
        return "More than 6 fails, not qualified"

    totalMarks2 = sum(mark for _, mark in studentMarks)
    courseAvg2 = round((totalMarks2 / len(studentMarks)),2)

    sortMarks2 = sorted(studentMarks, key = lambda x: (x[1]), reverse = True)
    topEightMarks2 = sortMarks2[:8]
    topEightAvg2 = sum(mark for _, mark in topEightMarks2) /8

    if courseAvg2 >= 70:
        return f"\nStudent ID: {studentID} \nAverage: {courseAvg2} \nQUALIFIES FOR HONORS STUDY!"
    elif courseAvg2 >= 65 and courseAvg2 < 70:
        if topEightAvg2 >= 80:
            return f"\nStudent ID: {studentID} \nAverage: {courseAvg2} \nTop Eight Average: {topEightAvg2} \nASSESSMENT: QUALIFIES FOR HONORS STUDY"
        else:
            return f"\nStudent ID: {studentID} \nAverage: {courseAvg2} \nTop Eight Average: {topEightAvg2} \nASSESSMENT: MAY HAVE A GOOD CHANCE! Needs further assessment!"
    elif courseAvg2 >= 60 and courseAvg2 <65:
        if topEightAvg2 >= 80:
            return f"\nStudent ID: {studentID} \nAverage: {courseAvg2} \nTop Eight Average: {topEightAvg2} \nASSESSMENT: MAY HAVE A GOOD CHANCE! Must be carefully reassessed and get the coordinator's permission"
        else:
            return f"\nStudent ID: {studentID} \nAverage: {courseAvg2} \nDOES NOT QUALIFY FOR HONORS!"
    else:
        return f"\nStudent ID: {studentID} \nAverage: {courseAvg2} \nDOES NOT QUALIFY FOR HONORS!"



#simplexmlrpc server created that listens to all network interfaces on port 6789    
server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0", 6789))

print ("Server Online...")
#registering functions so they can be called remotely from client
server.register_function(calculateNonOust, "calculateNonOust")
server.register_function(userAuthenticationwDB, "userAuthenticationwDB")

server.serve_forever()


