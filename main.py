import verifi, newaccount


choice = "0"
while(choice != "1" or choice != "2"):
  choice = input("1: Login\n2: Create new account\n ")
  if(choice=="1"):
    username = input("Type a username: ")
    password = input("Type a password: ")
  if(choice=="2"):
    newaccount.newaccount()
    print("Congrats on your new account!")
    #Continue from here.
  print("Invalid choice. Please choose between 1 or 2.\n")





  