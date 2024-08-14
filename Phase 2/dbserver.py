import xmlrpc.server

#using arrays to mimic database
#contains student details
#CONTAINS ONLY 5 STUDENTS
studentDetails =[
    ["20241201", "j.max@our.oust.edu.au", "Jim", "MAX", "U65"],
    ["20241202", "jt.max@our.oust.edu.au", "Jit", "MAX", "U65"],
    ["20241203", "l.max@our.oust.edu.au", "Late", "MAX", "U65"],
    ["20241204", "r.smith@our.oust.edu.au", "Rep", "SMITH", "U65"],
    ["20241205", "p.landan@our.oust.edu.au", "Paul", "Landan", "U67"]
##    [],
##    [],
##    []
    ]

#contains marks and unit codes of all units attempted by all students mentioned above
studentMarks =[
    ["20241201", "Unit_01", 100],
    ["20241201", "Unit_02", 67.6],
    ["20241201", "Unit_03", 64.6],
    ["20241201", "Unit_04", 80.2],
    ["20241201", "Unit_05", 90],
    ["20241201", "Unit_06", 55],
    ["20241201", "Unit_07", 60.8],
    ["20241201", "Unit_08", 85.2],
    ["20241201", "Unit_09", 68.2],
    ["20241201", "Unit_10", 68.3],
    ["20241201", "Unit_11", 56.7],
    ["20241201", "Unit_12", 38.9],
    ["20241201", "Unit_12", 77.5],
    ["20241201", "Unit_14", 76.2],
    ["20241201", "Unit_15", 81.3],
    ["20241201", "Unit_16", 46.2],
    ["20241201", "Unit_16", 81.7],
    ["20241201", "Unit_18", 43.3],
    ["20241201", "Unit_18", 77.3],
    ["20241201", "Unit_20", 42.8],
    ["20241201", "Unit_20", 45.4],
    ["20241201", "Unit_20", 90.9],
    ["20241201", "Unit_23", 71.1],
    ["20241201", "Unit_24", 92.6],
    ["20241201", "Unit_25", 74.1],
    ["20241201", "Unit_26", 94.6],
    ["20241201", "Unit_27", 56.9],
    ["20241201", "Unit_28", 40.6],
    ["20241201", "Unit_28", 82.7],
    ["20241201", "Unit_30", 99.9],
    ["20241202", "Unit_01", 74],
    ["20241202", "Unit_02", 95.3],
    ["20241202", "Unit_03", 92.3],
    ["20241202", "Unit_04", 67.3],
    ["20241202", "Unit_06", 90.9],
    ["20241202", "Unit_07", 71.1],
    ["20241202", "Unit_08", 52.6],
    ["20241202", "Unit_09", 74.1],
    ["20241202", "Unit_10", 94.6],
    ["20241202", "Unit_11", 56.9],
    ["20241202", "Unit_12", 56.6],
    ["20241202", "Unit_13", 76.4],
    ["20241202", "Unit_14", 58.5],
    ["20241202", "Unit_16", 62.4],
    ["20241202", "Unit_18", 67],
    ["20241202", "Unit_19", 74.4],
    ["20241202", "Unit_20", 74.9],
    ["20241202", "Unit_21", 53],
    ["20241202", "Unit_23", 52.8],
    ["20241202", "Unit_24", 65.7],
    ["20241202", "Unit_25", 84.3],
    ["20241202", "Unit_26", 87.7],
    ["20241202", "Unit_27", 72.9],
    ["20241202", "Unit_30", 93],
    ["20241203", "Unit_01", 22.2],
    ["20241203", "Unit_01", 83.8],
    ["20241203", "Unit_03", 75.8],
    ["20241203", "Unit_04", 92.1],
    ["20241203", "Unit_05", 64.6],
    ["20241203", "Unit_06", 80.3],
    ["20241203", "Unit_07", 56.3],
    ["20241203", "Unit_08", 82.8],
    ["20241203", "Unit_09", 33.6],
    ["20241203", "Unit_09", 75.9],
    ["20241203", "Unit_11", 80.1],
    ["20241203", "Unit_12", 69.8],
    ["20241203", "Unit_12", 26.5],
    ["20241203", "Unit_12", 57.8],
    ["20241203", "Unit_14", 87.8],
    ["20241203", "Unit_16", 11.5],
    ["20241203", "Unit_16", 79],
    ["20241203", "Unit_18", 73],
    ["20241203", "Unit_19", 75],
    ["20241203", "Unit_20", 89],
    ["20241203", "Unit_21", 50.6],
    ["20241203", "Unit_22", 71.7],
    ["20241203", "Unit_23", 77.8],
    ["20241203", "Unit_24", 75.7],
    ["20241203", "Unit_25", 52],
    ["20241203", "Unit_26", 67.7],
    ["20241203", "Unit_27", 75.9],
    ["20241203", "Unit_30", 71.7],
    ["20241204", "Unit_01", 71.6],
    ["20241204", "Unit_02", 65.2],
    ["20241204", "Unit_03", 72.8],
    ["20241204", "Unit_04", 75.9],
    ["20241204", "Unit_05", 65.4],
    ["20241204", "Unit_06", 70.8],
    ["20241204", "Unit_07", 81.7],
    ["20241204", "Unit_08", 72.7],
    ["20241204", "Unit_09", 58.9],
    ["20241204", "Unit_10", 53.5],
    ["20241204", "Unit_11", 59],
    ["20241204", "Unit_13", 68.7],
    ["20241204", "Unit_14", 83.1],
    ["20241204", "Unit_15", 52],
    ["20241204", "Unit_16", 55.5],
    ["20241204", "Unit_18", 56.9],
    ["20241204", "Unit_19", 67],
    ["20241204", "Unit_21", 68],
    ["20241204", "Unit_22", 55.3],
    ["20241204", "Unit_23", 78.1],
    ["20241204", "Unit_25", 46.5],
    ["20241204", "Unit_25", 50.7],
    ["20241204", "Unit_27", 45],
    ["20241204", "Unit_27", 75.4],
    ["20241204", "Unit_29", 68.3],
    ["20241204", "Unit_30", 76.9],
    ["20241205", "Unit_01", 70],
    ["20241205", "Unit_02", 80.5],
    ["20241205", "Unit_03", 60.1],
    ["20241205", "Unit_04", 54.9],
    ["20241205", "Unit_05", 23.6],
    ["20241205", "Unit_05", 51.6],
    ["20241205", "Unit_07", 42.3],
    ["20241205", "Unit_07", 86.3],
    ["20241205", "Unit_49", 60.9],
    ["20241205", "Unit_50", 53.2],
    ["20241205", "Unit_51", 81.9],
    ["20241205", "Unit_52", 52.1],
    ["20241205", "Unit_53", 86.9],
    ["20241205", "Unit_54", 55.3],
    ["20241205", "Unit_55", 55.9],
    ["20241205", "Unit_56", 55.7],
    ["20241205", "Unit_58", 62.9],
    ["20241205", "Unit_59", 84],
    ["20241205", "Unit_61", 76.1],
    ["20241205", "Unit_62", 65],
    ["20241205", "Unit_63", 74.9],
    ["20241205", "Unit_64", 83.8],
    ["20241205", "Unit_65", 74.3],
    ["20241205", "Unit_66", 56.8],
    ["20241205", "Unit_67", 53.7],
    ["20241205", "Unit_68", 42.8],
    ["20241205", "Unit_68", 76.8]
    ]


#function to authenticate users.
def userAuthentication(studentID, studentEmail, studentFname, studentLname):
    for student in studentDetails:
        if student[0] == studentID and student[1] == studentEmail and student[2] == studentFname and student[3] == studentLname:
            return "User Authenticated!"#True
    return "User not found!"#False

#fuction to retrieev marks
#used by the server to get the marks of selected users if authetnicated
def retrieveMarks(studentID):
    return [(studScore[1], studScore[2]) for studScore in studentMarks if studScore[0] == studentID]

#simplexmlrpc server created that listens to all network interfaces on port 8000 
dbServer = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0", 8000))

#registering functions so they can be called remotely from server
dbServer.register_function(retrieveMarks, "retrieveMarks")
dbServer.register_function(userAuthentication, "userAuthentication")
print("Database Online...")
dbServer.serve_forever()
