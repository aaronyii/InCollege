import newaccount, homepage,login, video


choice = "0"
#log_in = False
while(choice != "1" or choice != "2"):
  print("A college student success story\nThere was a college student called Beau. He joined InCollege in 2000 and he became successful on the next year. Impressive and motivative story from Beau\n-Beau Gate\n\n")

  video.playVideo()
  
  
  choice = input("1: Login\n2: Create new account\n ")
  if(choice=="2"):
    choice = "3"

    name = input("Please create a unique username: ")
    password = input("Please create a strong password: ")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    newaccount.newaccount(name, password,first,last)
    print("Congrats on your new account!")
    #Continue from here.
    break
  elif(choice=="1"):
      username = input("Type a username: ")
      password = input("Type a password: ")
      result = login.login_page(username,password)
      if result == 0:
          homepage.homepage()







  