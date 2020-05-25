import os, os.path
import time
import shutil
print("Generating folders...")
yearList = []
cwd = os.getcwd()
os.chdir("test files")
listItems = [name for name in os.listdir('.') if os.path.isfile(name)]
for check in listItems:
    year = time.ctime(os.path.getmtime(check))[20:]
    year = int(year)
    if year in yearList:
        continue
    yearList.append(year)
os.chdir(cwd)
for year in yearList:
    try:
        os.mkdir(f"{year}")
    except:
        print("Folder already exists")
os.chdir("test files")
for item in listItems:
    year = time.ctime(os.path.getmtime(item))[20:]
    print(f"Moving {item} to folder {year}")
    shutil.move(os.path.realpath(item),f'../{year}/{item}')


