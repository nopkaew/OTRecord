import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from screeninfo import get_monitors
import os
#from frmLogIn import frmLogIn
import bcrypt
#from dBOTRecord import *

class frmCreateDb:

    def __init__(self,master):
        self.master = master
        f = open("FileLocation.text", "r")
        self.dbLocation = f.readline()
        f.close()
        self.scale = self.get_screen_width() / 1600
        self.FONT1 = ('Tahoma',int(8*self.scale))  # กำหนด font เริ่มต้น
        if self.IsDBExist():       
           self.master.update()  # อัปเดตหน้าต่างก่อนปิด
           self.master.destroy() 
           from frmLogIn import frmLogIn
           frmLogIn(tk.Tk())
        else:
            self.CreateGUI(master)

    def get_screen_width(self):
    # ดึงความกว้างของหน้าจอหลัก
        for m in get_monitors():
            if m.is_primary:
                return m.width    
    
    def IsDBExist(self):
    #    f = open("FileLocation.text", "r")
    #    fileLocation = f.readline()
        folder_path = r"H:\PythonGUI\OTRecord"
        file_name = "OTRecord.sqlite3"
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(self.dbLocation):
            print(f"ไฟล์ {file_path} พบในโฟลเดอร์ {folder_path}")
            return True      
        else:
            print(f"ไม่พบไฟล์ {file_path} ในโฟลเดอร์ {folder_path}")
            return False

    def CloseForm(self):
        self.master.destroy()
        return False
    
    def CreateGUI(self,master):
        master.title('สร้างฐานข้อมูลสำหรับเริ่มต้นใช้งาน')
        master.geometry(str(int(380*self.scale))+'x'+str(int(230*self.scale))+'+'+str(int(400*self.scale))+'+'+str(int(200*self.scale)))
        master.grid_rowconfigure(6, weight=1)
        master.grid_columnconfigure(3, weight=1)
        master.resizable(False, False)

        lblInform = tk.Label(master, text='กำลังสร้างฐานข้อมูลสำหรับเริ่มต้นใช้งาน \nกรุณาระบุุ User Name และ Password สำหรับการเข้าระบบครั้งแรก',font=self.FONT1)
        lblPersonID = tk.Label(master, text='หมายเลขประจำตัว : ',font=self.FONT1)
        lblPersonName = tk.Label(master, text='ชื่อ : ',font=self.FONT1)
        lblUserName = tk.Label(master, text='User Name : ',font=self.FONT1)
        lblPassword = tk.Label(master, text='Password : ',font=self.FONT1)
        lblConfirm = tk.Label(master, text='Confirm Password : ',font=self.FONT1)

        self.vPersonID = StringVar()
        entPersonID = tk.Entry(master,textvariable=self.vPersonID ,font=self.FONT1)
        self.vPersonName = StringVar()
        entPersonName = tk.Entry(master,textvariable=self.vPersonName ,font=self.FONT1)
        self.vUserName = StringVar()
        entUserName = tk.Entry(master,textvariable=self.vUserName ,font=self.FONT1)
        self.vPassword = StringVar()
        entPassword = tk.Entry(master,show='*',textvariable=self.vPassword, font=self.FONT1)
        self.vConfirm = StringVar()
        entConfirm = tk.Entry(master,show='*',textvariable=self.vConfirm, font=self.FONT1)

        btnOK = tk.Button(master,text='ตกลง',font=self.FONT1,command= self.CreateDb)
        btnCancel = tk.Button(master,text='ยกเลิก',font=self.FONT1,command=self.CloseForm)

        lblInform.grid(row=0, column=0,columnspan=3,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nsew')
        lblPersonID.grid (row=1, column=0,padx= int(5*self.scale),pady= int(5*self.scale),sticky='ne')
        lblPersonName.grid (row=2, column=0,padx= int(5*self.scale),pady= int(5*self.scale),sticky='ne')
        lblUserName.grid (row=3, column=0,padx= int(5*self.scale),pady= int(5*self.scale),sticky='ne')
        lblPassword.grid (row=4, column=0,padx= int(5*self.scale),pady= int(5*self.scale),sticky='ne')
        lblConfirm.grid (row=5, column=0,padx= int(5*self.scale),pady= int(5*self.scale),sticky='ne')
        entPersonID.grid(row=1, column=1,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nw')
        entPersonName.grid(row=2, column=1,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nw')
        entUserName.grid(row=3, column=1,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nw')
        entPassword.grid(row=4, column=1,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nw')
        entConfirm.grid(row=5, column=1,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nw')
        btnOK.grid(row=4, column=2,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nsew')
        btnCancel.grid(row=5, column=2,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nsew')

    def CreateDb(self):
        personid = self.vPersonID.get()
        personname = self.vPersonName.get()
        username = self.vUserName.get()
        password_str = self.vPassword.get()
        password_bypt = password_str.encode()
        confirm_password = self.vConfirm.get()

        if password_str != confirm_password:
            # Show error message if passwords don't match
            messagebox.showerror("เกิดข้อผิดพลากลด", "รหัสผ่านไม่ตรงกัน")
            return
        
        Salt = bcrypt.gensalt()
        Hashed_Password = bcrypt.hashpw(password_bypt, Salt)
        conn = sqlite3.connect(self.dbLocation)
        cursor = conn.cursor()

        # Create users table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        #tbl 1
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblHrOTCode (
                Code TEXT PRIMARY KEY NOT NULL,
                Detail TEXT
            )
        ''')
        #tbl 2
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblUserLevel (
                ID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT
            )
        ''')
        #tbl 3
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblPerson (
                ID TEXT PRIMARY KEY NOT NULL,
                Name TEXT,
                UserName TEXT UNIQUE NOT NULL,
                Password_Hash BLOB NOT NULL,
                Salt BLOB NOT NULL,
                Active TEXT,                       
                UserLevelID INTEGER,
                FOREIGN KEY (UserLevelID)  REFERENCES tblUserLevel(ID)            
            )
        ''')
        #tbl 4
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblOTType (
                ID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT,
                Multify NUMERIC         
            )
        ''')
        #tbl 5
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblSalary (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                PersonID TEXT,
                Salary REAL,
                FOREIGN KEY (PersonID)  REFERENCES tblPerson(ID)   
            )
        ''')
        #tbl 6
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblOTBudget (
                YearID INTEGER NOT NULL,
                MonthID INTEGER NOT NULL,
                Budget NUMERIC,
                PRIMARY KEY(YearID,MonthID)
            )
        ''')
        #tbl 7
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblTeam (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                PersonID TEXT,
                MasterPerson TEXT,
                BigBoss TEXT,
                FullMasterPerson TEXT,
                Active TEXT,
                Note TEXT,
                FullPathPerson TEXT,
                FOREIGN KEY (PersonID)  REFERENCES tblPerson(ID)  
            )
        ''')
        #tbl 8
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblReason (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Detail TEXT,
                ShortDetail TEXT,
                HrOTCode TEXT,
                Active TEXT,
                FOREIGN KEY (HrOTCode)  REFERENCES tblHrOTCode(Code)  
            )
        ''')
        #tbl 9
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblReasonGroup (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                ReasonID INTEGER,
                MasterReason INTEGER,
                FullMasterReason TEXT,
                Active TEXT,
                FullPathReason TEXT,
                FOREIGN KEY (ReasonID)  REFERENCES tblReason(ID)  
            )
        ''')
        #tbl 10
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblOT (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                OTDate INTEGER,
                OTTime INTEGER,
                Detail TEXT,
                CheckByBoss TEXT,
                PersonID TEXT,
                ReasonGroupID INTEGER,
                OTTypeID INTEGER,
                RecordDate INTEGER,
                FOREIGN KEY (OTTypeID)  REFERENCES tblOTType(ID),
                FOREIGN KEY (ReasonGroupID)  REFERENCES tblReasonGroup(ID)
            )
        ''')

        # Insert user
        try:
            cursor.execute("INSERT INTO tblUserLevel (ID,Name) VALUES (?,?)",(0,'Guest'))
            cursor.execute("INSERT INTO tblUserLevel (ID,Name) VALUES (?,?)",(1,'Fitter'))
            cursor.execute("INSERT INTO tblUserLevel (ID,Name) VALUES (?,?)",(2,'Foreman'))
            cursor.execute("INSERT INTO tblUserLevel (ID,Name) VALUES (?,?)",(3,'Engineer'))
            cursor.execute("INSERT INTO tblUserLevel (ID,Name) VALUES (?,?)",(4,'Supervisor'))
            cursor.execute("INSERT INTO tblUserLevel (ID,Name) VALUES (?,?)",(5,'Admin'))
            cursor.execute("INSERT INTO tblUserLevel (ID,Name) VALUES (?,?)",(6,'Object'))
            cursor.execute("INSERT INTO tblHrOTCode (Code,Detail) VALUES (?,?)",('000','MM Reserve'))            
            cursor.execute("INSERT INTO tblHrOTCode (Code,Detail) VALUES (?,?)",('1000','เหตุฉุกเฉิน (ไฟไหม้/ไฟฟ้าดับ/เตารั่ว)'))
            cursor.execute("INSERT INTO tblHrOTCode (Code,Detail) VALUES (?,?)",('1500','การฝึกอบรมต่างๆ(จากส่วนกลาง)'))
            cursor.execute("INSERT INTO tblHrOTCode (Code,Detail) VALUES (?,?)",('200','อัตรากำลังคนไม่ครบตามโครงสร้าง'))
            cursor.execute("INSERT INTO tblHrOTCode (Code,Detail) VALUES (?,?)",('300','การประชุมและกิจกรรมต่างๆ '))
            cursor.execute("INSERT INTO tblHrOTCode (Code,Detail) VALUES (?,?)",('600','เกิดจากเครื่องจักร/อุปกรณ์มีปัญหา'))
            cursor.execute("INSERT INTO tblHrOTCode (Code,Detail) VALUES (?,?)",('700','เกิดจากผลิตภัณฑ์มีปัญหา'))
            cursor.execute("INSERT INTO tblHrOTCode (Code,Detail) VALUES (?,?)",('800','งานโครงการพิเศษ'))
            cursor.execute("INSERT INTO tblHrOTCode (Code,Detail) VALUES (?,?)",('900','ปฏิบัติงานตามที่ได้รับมอบหมาย'))
            cursor.execute("INSERT INTO tblOTType (ID,Name,Multify) VALUES (?,?,?)",(1,'X 1.5',1.5))
            cursor.execute("INSERT INTO tblOTType (ID,Name,Multify) VALUES (?,?,?)",(2,'X 3',3))
            cursor.execute("INSERT INTO tblOTType (ID,Name,Multify) VALUES (?,?,?)",(3,'X Call In',4))

            conn.commit()

            cursor.execute("INSERT INTO tblPerson (ID, Name,UserName,Password_Hash,Salt,Active,UserLevelID)"+ 
                           " VALUES (?, ?,?,?,?,?,?)", (personid, personname,username,Hashed_Password,Salt,'A',5))
            conn.commit()

            messagebox.showinfo("Success", "สร้างฐานข้อมูล และข้อมูลผู้ใช้งานสำเร็จ")
            self.CloseForm()
            from frmLogIn import frmLogIn
            frmLogIn(tk.Tk())
        except sqlite3.IntegrityError:
            messagebox.showerror("ผิดพลาด", "มีผู้ใช้งานบัญชีนี้อยู่แล้ว")

        conn.close()

def main():
    root = tk.Tk()
    app = frmCreateDb(root)
    root.mainloop()

if __name__ == "__main__":
    main()