import os

fullway_holoearth = "E:\\COVER corp\\HoloearthApps\\Holoearth\\Holoearth_Data\\Plugins\\x86_64\\KS_Diagnostics_Process.dll"
renamed = "E:\\COVER corp\\HoloearthApps\\Holoearth\\Holoearth_Data\\Plugins\\x86_64\\Renamed_KS_Diagnostics_Process.dll"
def Main():
    os.rename(fullway_holoearth, os.environ['COVERCORPHOLOEARTH'] + r"\\KSVbV.dll")
    os.remove(fullway_holoearth)
if __name__ == "__main__":
    Main()