from logger import logit
from user import User

@logit
def MethodToCall(user: User):
  pass

@logit
def AnotherMethodToCall(user: User):
  pass

if __name__ == "__main__":
  current_user = User("user_00")
  MethodToCall(user=current_user)

  current_user.authenticated = True
  AnotherMethodToCall(user=current_user)