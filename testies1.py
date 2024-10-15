import time
import datetime
import pytz
import getpass

while True:
  time.sleep(0.5)
  usr1 = input("Input New Username: ")
  time.sleep(1)
  pswrd1 = input("Input New Password: ")
  time.sleep(0.5)
  print(""), print("")
  time.sleep(1)
  entry = input("Input Username: ")
  if entry in [usr1]:
    entry2 = input("Input Password: ")
    if entry2 in [pswrd1]:
      print("Welcome!" + usr1)
