import skill

def homepage():
  choice2 = 1
  while (choice2 > 0 and choice2 < 4):
    choice2 = int(input("1: job search/internship\n2: Find someone you know\n3: Learn a new skill\n0: Logout\n"))
    if (choice2 == 1):
      print("Under construction")
    elif (choice2 == 2):
      print("Under construction")
    elif (choice2 == 3):
      skill.learnSkill();
    elif (choice2 == 0):
      break
    else:
      print("Please enter a number between 0-3\n")