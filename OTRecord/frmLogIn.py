import sqlite3
import tkinter as tk
from tkinter import *
from screeninfo import get_monitors
from tkinter import messagebox
import bcrypt
from frmMain import MainFrm
from dBOTRecord import *

class frmLogIn:

    def __init__(self,master):
        self.master = master
        self.scale = self.get_screen_width()/1600
        self.FONT1 = ('Tahoma',int(12*self.scale))  # กำหนด font เริ่มต้น
    #    self.f = open("FileLocation.text", "r")
    #    self.dbLocation = self.f.readline()
    #    self.f.close()
        super().__init__()
        master.title('ลงชื่อเข้าใช้')
        master.geometry(str(int(480*self.scale))+'x'+str(int(90*self.scale))+'+'+str(int(400*self.scale))+'+'+str(int(200*self.scale)))
        master.grid_rowconfigure(4, weight=1)
        master.grid_columnconfigure(3, weight=1)
        master.resizable(False, False)

        lblUserName = tk.Label(master, text='User Name : ',font=self.FONT1)
        lblPassword = tk.Label(master, text='Password : ',font=self.FONT1)
        lblNewPassword = tk.Label(master, text='New Password : ',font=self.FONT1)
        lblConfirmPassword = tk.Label(master, text='Confirm Password : ',font=self.FONT1)

        self.vUserName = StringVar()
        entUserName = tk.Entry(master, textvariable=self.vUserName,font=self.FONT1)
        self.vPassword = StringVar()
        entPassword = tk.Entry(master,show='*', textvariable=self.vPassword,font=self.FONT1)
        self.vNewPassword = StringVar()
        entNewPassword = tk.Entry(master,show='*',textvariable=self.vNewPassword ,font=self.FONT1)
        self.vConfirmPassword = StringVar()
        entConfirmPassword = tk.Entry(master,show='*',textvariable= self.vConfirmPassword, font=self.FONT1)

        btnLogIn = tk.Button(master,text='เข้าสู่ระบบ',font=self.FONT1,command=self.UserLogIn)
        btnChangePassword = tk.Button(master,text='เปลี่ยนรหัสผ่าน',font=self.FONT1,command= self.ChangePassword)
        btnConfirmChangePassword = tk.Button(master,text='ยืนยัน',font=self.FONT1,command= self.SaveNewPassword)

        lblUserName.grid (row=0, column=0,padx= int(5*self.scale),pady= int(5*self.scale),sticky='ne')
        lblPassword.grid (row=1, column=0,padx= int(5*self.scale),pady= int(5*self.scale),sticky='ne')
        lblNewPassword.grid (row=2, column=0,padx= int(5*self.scale),pady= int(5*self.scale),sticky='ne')
        lblConfirmPassword.grid (row=3, column=0,padx= int(5*self.scale),pady= int(5*self.scale),sticky='ne')
        entUserName.grid(row=0, column=1,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nw')
        entPassword.grid(row=1, column=1,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nw')
        entNewPassword.grid(row=2, column=1,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nw')
        entConfirmPassword.grid(row=3, column=1,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nw')
        btnLogIn.grid(row=0, column=2,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nsew')
        btnChangePassword.grid(row=1, column=2,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nsew')
        btnConfirmChangePassword.grid(row=3, column=2,padx= int(5*self.scale),pady= int(5*self.scale),sticky='nsew')

        
    #    master.geometry(str(int(normalpositionX*self.scale))+'x'+str(int(normalpositiony*self.scale)))

    def get_screen_width(self):
    # ดึงความกว้างของหน้าจอหลัก
        for m in get_monitors():
            if m.is_primary:
                return m.width  
            
    def UserLogIn(self):
    #    conn = sqlite3.connect(self.dbLocation)
        conn = ConnectDb()
        cursor = conn.cursor()
        username = self.vUserName.get()
        password_str = self.vPassword.get()
        password_byte = password_str.encode()
        cursor.execute("SELECT Password_Hash, Salt FROM tblPerson WHERE UserName =?",(username,))
        result = cursor.fetchone()
        conn.close()
        if result:
            stored_password_hash, stored_salt = result
            hashed_password = bcrypt.hashpw(password_byte, stored_salt)
            if stored_password_hash == hashed_password:
            #    print('Login success')
            #    messagebox.showinfo("Success","เข้าระบบสำเร็จ")
                self.master.update()  # อัปเดตหน้าต่างก่อนปิด
                self.master.destroy() 
                MainFrm(tk.Tk(),username)   
            else:
            #    print('Password ไม่ถูกต้อง')
                messagebox.showinfo("Incorrecr Password","รหัสผ่านไม่ถูกต้อง")
        else:
        #    print("User not found")
            messagebox.showinfo("User not found","ไม่มีบัญชีผู้ใช้ในระบบ")             

    def ChangePassword(self):
        self.master.geometry(str(int(320*self.scale))+'x'+str(int(120*self.scale)))    

    def SaveNewPassword(self):
    #    conn = sqlite3.connect(self.dbLocation)
        conn = ConnectDb()
        cursor = conn.cursor()
        username = self.vUserName.get()
        newpassword_str = self.vNewPassword.get()
        newpassword_byte = newpassword_str.encode()
        confirmpassword = self.vConfirmPassword.get()
        password_str = self.vPassword.get()
        password_byte = password_str.encode()
        cursor.execute("SELECT Password_Hash, Salt FROM tblPerson WHERE UserName =?",(username,))
        result = cursor.fetchone()
        conn.close()
        print(result)
        if result:
            stored_password_hash, stored_salt = result
            hashed_password = bcrypt.hashpw(password_byte, stored_salt)
            if stored_password_hash == hashed_password:
                if newpassword_str==confirmpassword:
                    Salt = bcrypt.gensalt()
                    Hashed_Password = bcrypt.hashpw(newpassword_byte, Salt)
                #    conn = sqlite3.connect(self.dbLocation)
                    conn = ConnectDb()
                    cursor = conn.cursor()
                    try:
                        cursor.execute("UPDATE tblPerson SET Password_Hash =?,Salt =? WHERE UserName =?",(Hashed_Password,Salt,username))
                        conn.commit()
                        conn.close()                        
                        messagebox.showinfo("Success","เปลี่ยนรหัสผ่านเรียบร้อยแล้ว")
                        self.master.geometry(str(int(320*self.scale))+'x'+str(int(65*self.scale)))                        
                    except sqlite3.Error:
                        messagebox.showerror("ผิดพลาด", "ไม่สามารถเปลี่ยนรหัสผ่านได้")                   
                else:
                    messagebox.showwarning("Error","New Password และ Confirm Password ไม่ตรงกัน")
            else:
            #    print('password ไม่ถูกต้อง')
                messagebox.showinfo("Incorrect Old Password","รหัสผ่านเดิมไม่ถูกต้อง")
        else:
        #    print("User not found")
            messagebox.showinfo("User not found","ไม่มีบัญชีผู้ใช้ในระบบ") 

        
     

def main():
    root = tk.Tk()
    app = frmLogIn(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    