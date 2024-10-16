import time
import math
from datetime import datetime

def epsilon8():
    while True:
        

def mathmod():
    print("Math Module!")
    time.sleep(0.5)
    print("1. Multiply // 2. Divide")
    print("3. Addition // 4. minnus")
    trs = input(">: ")
    if trs.lower() in ["1", "one", "multiply"]:
        numa1 = int(input("Number 1: "))
        numb1 = int(input("Number 2: "))
        time.sleep(0.5), print("\n")
        print(f"Answer: {numa1 * numb1}")
        
    elif trs.lower() in ["2", "two", "divide"]:
        numa2 = int(input("Number 1: "))
        numb2 = int(input("Number 2: "))
        time.sleep(0.5), print("\n")
        print(f"Answer: {numa2 / numb2}")
        
    elif trs.lower() in ["3", "three", "addition"]:
        numa3 = int(input("Number 1: "))
        numb3 = int(input("Number 2: "))
        time.sleep(0.5), print("\n")
        print(f"Answer: {numa3 + numb3}")
        
    elif trs.lower() in ["4", "four", "minus"]:
        numa4 = int(input("Number 1: "))
        numb4 = int(input("Number 1: "))
        time.sleep(0.5), print("\n")
        print(f"Answer; {numa4 - numb4}")

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
      print("\n")
      print("Welcome! " + usr1.capitalize())
      print("\n")
      print("Entry Date/Time:", formatted_datetime)
      print("\n")
      time.sleep(1)
      print("Options:"), time.sleep(1)
      print("1. Log Life, 2. Exit")
      print("3. Math, 4. Search the web")
      print("5. Epislon - 8")
      kee = input(">: ")
        
      if kee.lower() in ["1", "one", "log"]:
        logs(), print("\n"), time.sleep(1)
        print("\n")
          
      elif kee.lower() in ["2", "two", "exit"]:
          print("Exiting..")
          time.sleep(0.5)
          break
          
      elif kee.lower() in ["3", "three", "math"]:
          print("swithching to math module")
          time.sleep(0.3)
          mathmod()
          
      elif kee.lower() in ["4", "four", "web"]:
        print("U/C")

      elif kee.lower() in ["5", "five", "epsilon"]:
          print("1. Proceed, 2. Go to Main Menu, 3. Leave Program Entirely")
          epentry = input("\> ")
          if epentry 
        
    else:
      print("Incorrect Password / Username")
      print("\n"), print("\n"), time.sleep(.5)
  else:
      print ("Incorrect Password / Username")
      print("\n"), print("\n"), time.sleep (1)
      print("\n")
