import sys
TryAgain = True
while TryAgain:
  try:
      value = int(input("type a number"))
  except ValueError:
      print("you must type a whole number")
      try:
          DoOver=input("Try again y/n")
      except:
                print("see you")
                TryAgain = False
      else:
                if(str.upper(DoOver)=="N"):
                    TryAgain = False
  except :
        print("see you next time")
        TryAgain = False
  else:
        print("you typed", value)
        TryAgain = False

class CustomExceptionClass(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args ={arg}
try:
    raise CustomExceptionClass("exception from custom class")
except CustomExceptionClass as c:
    print("exception is:", c.strerror)
    print("exception is:", c.args)
import sys
TryAgain = True
while TryAgain:
  try:
      value = int(input("type a number custom"))
  except CustomExceptionClass:
      print("you must type a whole number")
      try:
          DoOver=input("Try again y/n")
      except:
                print("see you")
                TryAgain = False
      else:
                if(str.upper(DoOver)=="N"):
                    TryAgain = False
  except :
        print("see you next time")
        TryAgain = False
  else:
        print("you typed", value)
        TryAgain = False