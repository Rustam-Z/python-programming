import os
def closeFile():
    try:
        os.system('TASKKILL /F /IM excel.exe')

    except Exception:
        print("KU")

closeFile()