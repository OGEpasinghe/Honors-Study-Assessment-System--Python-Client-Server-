# ssimplexmlrpcserver class imported from xmlrpcserver module
from xmlrpc.server import SimpleXMLRPCServer

#this function calculates the average from the user input
#then using if/else provides if the user is qualified or not acc to the avg
def averageCalc(user_ID, marks):
    avg = round(sum(mark for _, mark in marks) / len(marks),2)
    sortMarks = sorted(marks, key = lambda x: x[1], reverse = True)
    topEightMarks = sortMarks [:3] #sorts top 3 marks (for easier testing because input is 5 marks)
                                    #value will be top 8 in real case.
    topEightAvg = round(sum(int(mark) for _, mark in topEightMarks) /3,2)
    
    unitFails = sum(1 for _, mark in marks if mark < 50)
    if unitFails >= 2: #lowered unit fails for testing purposes only (as input takes only 5 values)
                        #value will be upto 6 in real case
        message = "With 6 or more Fails! DOES NOT QUALIFY FOR HONORS STUDY"

    elif avg >= 70:
        message = "QUALIFIES FOR HONORS STUDY"

    elif avg >=65 and avg < 70:
        if topEightAvg >= 80:
            message = f"TOP EIGHT AVG: {topEightAvg} \nASSESSMENT: QUALIFIES FOR HONORS STUDY"
        else:
            message = f"TOP EIGHT AVG: {topEightAvg} \nASSESSMENT: MAY HAVE A GOOD CHANCE! Needs further assessment!"
    elif avg >= 60 and avg <65:
        if topEightAvg >= 80:
            message = f"Top Eight Average: {topEightAvg} \nASSESSMENT: MAY HAVE A GOOD CHANCE! Must be carefully reassessed and get the coordinator's permission"

        else:
            message = "DOES NOT QUALIFY FOR HONORS STUDY!"
    else:
        message = "DOES NOT QUALIFY FOR HONORS STUDY"
    return avg, message, marks

#simplexmlrpc server created that listens to all network interfaces on port 6789
server = SimpleXMLRPCServer(("0.0.0.0",6789), logRequests=True)

#registering function averagecalc that  can be called remotely from client
server.register_function(averageCalc)
print("Serving... ")

server.serve_forever()
