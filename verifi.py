# Verifies if input'd string follows all guidelines. Return 0 if it follows all criteria and returns 1 if an error occurs.

def verifiPass(validate):
  if (len(validate) < 8 or len(validate) > 12):
    print("Invalid length of name. ")
    return 1
  if (validate.isalpha()):
    print("Password requires a number ")
    return 1
  if (validate == validate.lower()):
    print("Require an uppercase letter. ")
    return 1
  if validate.isalnum():
    print("Password requires a special character")
    return 1
  print("Good password, nice job.")
  return 0