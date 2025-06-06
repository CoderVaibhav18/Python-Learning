
# def log_decorator(func):
#   def greet():
#     print("printing started from here...")
#     result = func()
#     print("printing ended at here...")
#     return result
#   return greet

# @log_decorator
# def hello():
#   return "Hello world!!"

# print(hello())   

def requires_login(func):
  def wrapper(user):
    if user['isLogin']:
      return func(user)
    else:
      return "Plzz login first!!"
  return wrapper

@requires_login
def show_profile(user):
  return f"welcome {user['name']} This is your profile"

user1 = {"name": "Vaibhav", "isLogin": True}
user2 = {"name": "DM", "isLogin": False}

print(show_profile(user1))
print(show_profile(user2))