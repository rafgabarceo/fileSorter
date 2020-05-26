import os, os.path
import time
import sys
import shutil
yearList = []
cwd = os.getcwd()
while True:
    toSort = input("Please input the folder to sort: ")
    try:
        os.chdir(f"{toSort}")
        break
    except FileNotFoundError:
        userChoice = input("Folder to sort does not exist. Press enter to retype. If you want to exit, please type 'exit'.")
        if "exit" in userChoice:
            sys.exit("User closed the program.")
        else:
            continue
print("Generating folders...")
listItems = [name for name in os.listdir('.') if os.path.isfile(name)]
for check in listItems:
    year = time.ctime(os.path.getmtime(check))[20:]
    year = int(year)
    if year in yearList:
        continue
    yearList.append(year)
for year in yearList:
    try:
        os.mkdir(f"{year}")
    except:
        print("Folder already exists")
for item in listItems:
    year = time.ctime(os.path.getmtime(item))[20:]
    print(f"Moving {item} to folder {year}")
    shutil.move(os.path.realpath(item),f'{year}/{item}')


