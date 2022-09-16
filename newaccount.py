# This file is to create a new InCollege account

import verifi, json


def newaccount():
    username = input("Please create a unique username: ")
    
    with open('students.json') as f:
        data = json.load(f)
        for item in data['studentsLogin']: #going over each username
            if username == item['username']: #if username in system already
                print("Username already exists...")
                exit()
            if len(data['studentsLogin']) >= 5:
                print(
                    "All permitted accounts have been created, please come back later"
                )
                exit()
              
    newPassword = input("Please create a strong password: ")
    boolNum = verifi.verifiPass(newPassword) 
    while (boolNum != 0): # if invalid password, try again.
      print("Try again.\n")
      newPassword = input("Please create a strong password: ")
      boolNum = verifi.verifiPass(newPassword)
      
    tempDict = {"username":username,"password":newPassword}
    data['studentsLogin'].append(tempDict) # add new Info to database 
    
    with open('students.json', "w") as f:
        json.dump(data, f)

# Trying to figure out how to use GitHub