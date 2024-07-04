import sqlite3
import os

con = sqlite3.connect('OTRecord.sqlite3')
c = con.cursor()

def ConnectDb():
    f = open("FileLocation.text", "r")
    dbLocation = f.readline()
    f.close()
    conn = sqlite3.connect(dbLocation)
    return conn

def IsDBExist():
    folder_path = r"H:\PythonGUI\OTRecord"
    file_name = "OTRecord.sqlite3"
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        print(f"ไฟล์ {file_name} พบในโฟลเดอร์ {folder_path}")
        
    else:
        print(f"ไม่พบไฟล์ {file_name} ในโฟลเดอร์ {folder_path}")

IsDBExist()