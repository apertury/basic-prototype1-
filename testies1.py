import time
import threading
from datetime import datetime

def logs():
    log_counter = 1
    logs = []

    while True:
        log_entry = input(f"Enter your log (LOG {log_counter}): ")
        formatted_log = f"LOG {log_counter}: {log_entry}"
        logs.append(formatted_log)
        log_counter += 1

        continue_logging = input("Add another? (yes/no): ").strip().lower()
        if continue_logging != 'yes':
            break
        
    tab = input("Show All Logs? (Y/N): ").strip().lower()
    if tab in ['yes', 'y', 'Y']:
        print("\nALL LOGS")
        for log in logs:
            print(log)

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d / %H:%M:%S")

while True:
  time.sleep(0.5)
  usr1 = input("Input New Username: ")
  time.sleep(0.2)
  pswrd1 = input("Input New Password: ")
  time.sleep(0.5)
  print(""), print("")
  time.sleep(1)
  entry = input("Input Username: ")
  if entry in [usr1]:
    entry2 = input("Input Password: ")
    if entry2 in [pswrd1]:
      print("Welcome! " + usr1.capitalize())
      print("Entry Date/Time:", formatted_datetime)
      print("\n")
      time.sleep(1)
      print("Options:"), time.sleep(1)
      print("1. Log Life, 2. Exit")
      print("3. U/C, 4. U/C")
      kee = input(">: ")
      if kee.lower() in ["1", "one", "log"]:
        logs(), print("\n"), time.sleep(1)
        print("\n")
      elif kee.lower() in ["2", ]
      
    else:
      print("Incorrect Password / Username")
      print("\n"), print("\n"), time.sleep(.5)
  else:
      print ("Incorrect Password / Username")
      print("\n"), print("\n"), time.sleep (1)
      print("\n")
