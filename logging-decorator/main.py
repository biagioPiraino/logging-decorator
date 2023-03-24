from logger import logit
from user import User

@logit
def MethodToCall(user: User):
  pass

if __name__ == "__main__":
  current_user = User("user_00")
  MethodToCall(current_user)

  current_user.authenticated = True
  MethodToCall(current_user)