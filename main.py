from colorama import Fore, Style
import etc._funct_ as fnct
import os
from config import clean_cmd

#Header
fnct.header("S I S")
print(Fore.GREEN + "STUDENT INFORMATION SYSTEM")
Style.RESET_ALL

program_state = "Active"
while program_state == "Active":
#Menu
  menu = ["1. Add New Record", "2. Change Existing Record", "3. Search A Record", "4. Delete Record", "5. Settings", "0. Exit"]
  print("\n")
  for data in menu:
    print(Fore.YELLOW + data)
  user_input = int(input("\n>> "))
  if user_input == 0:
    program_state = "Deactive"

os.system(clean_cmd)
print(Fore.GREEN + "\nThanks For Using This Program")