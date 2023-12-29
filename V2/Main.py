import pathlib
import os, shutil
import sys, time
def GetTempFolder():
    return os.environ['TEMP' or 'TMP'] 
def GetChEngineTEMPFolder():
    return GetTempFolder() + "\\Cheat Engine" #Folder for Cht Engine
def GetChEngineSymbolsTempFolder():
    return GetTempFolder() + "\\Cheat Engine Symbols" # Symbols Folder for Cht Engine
def Main():
    path = pathlib.Path(GetChEngineTEMPFolder())
    anotherpath = pathlib.Path(GetChEngineSymbolsTempFolder())
    if path.exists():
        print("This Temp Folder is Founded!!!")
        shutil.rmtree(GetChEngineTEMPFolder())
        print("Temp Folder for Cheat Engine Successfully Deleted")
    elif anotherpath.exists():
        print("This Symbols Folder Is Existing... Deleting Now....")
        shutil.rmtree(GetChEngineSymbolsTempFolder())
        print("Symbols for Cheat Engine Successfully Deleted!!!")
    else:
        print("This Directories Is Now Deleted... Thank you for Choosing This Bypass!!!")
        time.sleep(5)
        sys.exit(2039)
if __name__ == "__main__":
    print("This is My First Bypass To Preventing Showing Japanese Message Box in Game HoloEarth... \nMade By DarknessSoulOfficial!!!")
    while True:
        Main()
        time.sleep(3)
