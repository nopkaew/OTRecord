import tkinter as tk
from tkinter import ttk
from tkinter import *
from screeninfo import get_monitors
from dBOTRecord import *
from tkinter import messagebox
import bcrypt

class frmAdUser:
    def get_screen_width(self):
    # ดึงความกว้างของหน้าจอหลัก
        for m in get_monitors():
            if m.is_primary:
                return m.width 
            
    def __init__(self,MainWindow,UserName):
        self.MainWindow = MainWindow
        self.UserName = UserName
        self.scale = self.get_screen_width()/1600
        self.FONT1 = ('Tahoma',int(11*self.scale))  # กำหนด font เริ่มต้น 
        self.Window = tk.Toplevel(MainWindow.master)
        self.Window.title('บัญชีผู้ใช้ User : ' + self.UserName)
        self.Window.geometry(str(int(1000*self.scale))+'x'+str(int(500*self.scale))+'+'+str(int(400*self.scale))+'+'+str(int(200*self.scale)))
        # create all of the main containers
        #top_frame = tk.Frame(self, bg='cyan', width=450, height=50, pady=3)
        top_frame = tk.Frame(self.Window , background='pink',width=450, height=50, pady=3)
        center_frame = tk.Frame(self.Window , bg='gray2', width=50, height=40)
        btm_frame = tk.Frame(self.Window , bg='white', width=450, height=10, pady=3)
        btm_frame2 = tk.Frame(self.Window , bg='lavender', width=450, height=10, pady=3)

        # layout all of the main containers
        self.Window .grid_rowconfigure(1, weight=1)
        self.Window .grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center_frame.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ew")
        btm_frame2.grid(row=4, sticky="ew")

        # create the widgets for the top frame
        lblPersonNo = tk.Label(top_frame, background='pink', text='หมายเลข :',font=self.FONT1)
        self.vPersonNo = StringVar()
        entPersonNo = tk.Entry(top_frame, textvariable=self.vPersonNo,font=self.FONT1)    
        lblPersonName = tk.Label(top_frame, background='pink',text='ชื่อ :',font=self.FONT1)
        self.vPersonName = StringVar()
        entPersonName = tk.Entry(top_frame, textvariable=self.vPersonName,font=self.FONT1)
        lblUserName = tk.Label(top_frame, background='pink', text='User Name :',font=self.FONT1)
        self.vUserName = StringVar()
        entUserName = tk.Entry(top_frame, textvariable=self.vUserName,font=self.FONT1)
        lblUserLevel = tk.Label(top_frame, background='pink', text='User Level :',font=self.FONT1)
    #    cmbUserLevel = ttk.Combobox(top_frame,font=self.FONT1,values=['Manager','Supervisor','Engineer','Foreman','Fitter'])
        self.cmbUserLevel = ttk.Combobox(top_frame,font=self.FONT1,values=self.UserLevelItems())
        self.vActive = IntVar()
        chkActive = tk.Checkbutton(top_frame, background='pink',text='ยังคงปฏิบัติงานอยู่',variable=self.vActive,font=self.FONT1)
        btnSave = tk.Button(top_frame,text='บันทึก/ปรับปรุงข้อมูล',font=self.FONT1,command=self.SaveOrUpdateUser)
        btnDelete = tk.Button(top_frame,text='ลบข้อมูล',command=self.DeleteUser,font=self.FONT1)
        btnResetPassword= tk.Button(top_frame,text='รีเซ็ท รหัสผ่าน',command=self.ResetPassword,font=self.FONT1)

        self.treeScrollY = ttk.Scrollbar(center_frame)
    #    self.treeScrollx = ttk.Scrollbar(center_frame,orient="horizontal")

        header = ['รหัสพนักงาน', 'ชื่อ','UserName','User Level','สถานะปัจจุบัน']
        headerw = [50,100,50,50,50]
        self.tbl = ttk.Treeview(center_frame, columns=header,yscrollcommand=self.treeScrollY.set, show='headings')
        self.treeScrollY.config(command=self.tbl.yview)
    #    self.treeScrollx.config(command=self.tbl.xview)

        # layout the widgets in the top frame
        lblPersonNo.grid(row=0, column=0,padx= 5,pady= 5,sticky='ne')       
        entPersonNo.grid(row=0, column=1,padx= 5,pady= 5,sticky='nw')
        lblPersonName.grid(row=0, column=2,padx= 5,pady= 5,sticky='ne')
        entPersonName.grid(row=0, column=3,padx= 5,pady= 5,sticky='nw')
        lblUserName.grid(row=1, column=0,padx= 5,pady= 5,sticky='ne')
        entUserName.grid(row=1, column=1,padx= 5,pady= 5,sticky='nw')
        lblUserLevel.grid(row=1, column=2,padx= 5,pady= 5,sticky='ne')
        self.cmbUserLevel.grid(row=1, column=3,padx= 5,pady= 5,sticky='nw')
        chkActive.grid(row=0, column=4,padx= 5,pady= 5,sticky='nw')
        btnSave.grid(row=1, column=4,padx= 5,pady= 5,sticky='nsew')
        btnDelete.grid(row=0, column=5,padx= 5,pady= 5,sticky='nsew')
        btnResetPassword.grid(row=1, column=5,padx= 5,pady= 5,sticky='nsew')
        
        # create the center widgets
        center_frame.grid_rowconfigure(0, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)

        ctr_left = tk.Frame(center_frame, width=2, height=190)
        ctr_mid = tk.Frame(center_frame, bg='yellow', width=250, height=190, padx=3, pady=3)
        ctr_right = tk.Frame(center_frame, width=2, height=190)

    #    ctr_left.grid(row=0, column=0, sticky="ns")
    #    ctr_mid.grid(row=0, column=1, sticky="nsew")
        self.treeScrollY.grid(row=0, column=1,padx=(0,5) ,pady= 2,sticky='ns')
    #    self.treeScrollx.grid(row=1, column=0,padx= 5,pady= 5,sticky='ew')
        self.tbl.grid(row=0, column=0,padx= (5,0),pady= 5,sticky='nsew')
    #    ctr_right.grid(row=0, column=2, sticky="ns")

        style = ttk.Style()
        style.configure('Treeview.Heading',padding= (10,10),font=('Tahoma',int(12*self.scale),'bold'))
        style.configure('Treeview',rowheight=25,font=('Tahoma',int(12*self.scale),'bold'))
        for h,w in zip(header,headerw):
            self.tbl.heading(h,text=h)
            self.tbl.column(h,width=w)

        self.tbl.bind("<<TreeviewSelect>>",self.OnTblSelect)
        self.vActive.set(1)
        self.ShowTbl()

    def ResetPassword(self):
        if self.tbl.selection():
            selected = self.tbl.selection()
            output = self.tbl.item(selected)
            data = output['values']
            personno =data[0]
            personname =data[1]
            check = messagebox.askyesno("ยืนยันการรีเซ็ทรหัสผ่าน",f'รหัสผ่านของ {personno} : {personname} จะถูกตั้งค่าใหม่เป็น : 1234 \nยืนยันการดำเนินการหรือไม่?',parent=self.Window)
            if check:
                password_bypt = b'1234'
                Salt = bcrypt.gensalt()
                Hashed_Password = bcrypt.hashpw(password_bypt, Salt)
                conn = ConnectDb()
                with con:
                    sql = "UPDATE tblPerson SET Password_Hash=?, Salt = ? WHERE ID =?"
                    c.execute(sql,(Hashed_Password,Salt,personno))
                conn.commit()
                conn.close()

    def DeleteUser(self):
        if self.tbl.selection():
            selected = self.tbl.selection()
            output = self.tbl.item(selected)
            data = output['values']
            personno =data[0]
            personname =data[1]
            check = messagebox.askyesno("ยืนยันการลบข้อมูล",f'ยืนยันการลบข้อมูลของ {personno} : {personname} หรือไม่?',parent=self.Window)
            if check:
                conn = ConnectDb()
                curcor = conn.cursor()
                curcor.execute("DELETE FROM tblPerson WHERE ID =?",(personno,))
                conn.commit()
                conn.close()
                self.ShowTbl()
        
    def OnTblSelect(self,event):
        selected = self.tbl.selection()
        output = self.tbl.item(selected)
    #    print(output)
        data = output['values']
        if not data:
            return
        
        self.vPersonNo.set(data[0])
        self.vPersonName.set(data[1])
        self.vUserName.set(data[2])
        self.cmbUserLevel.set(data[3])
        if data[4] =='A':
            self.vActive.set(1)
        else:
            self.vActive.set(0)
        pass

    def UserLevelItems(self):
        conn = ConnectDb()
        cursor = conn.cursor()
        cursor.execute("SELECT Name FROM tblUserLevel WHERE ID <=4 AND ID >0")
        rows = cursor.fetchall()
        items = [row[0] for row in rows]
        conn.close()
        return items
    
    def FindUserLevelID(self):
        selected = self.cmbUserLevel.get()
        if selected:
            conn = ConnectDb()
            cursor = conn.cursor()
            cursor.execute("SELECT ID FROM tblUserLevel WHERE Name =?",(selected,))
            result =cursor.fetchone()
            conn.close()
            if result:
                userlevelid = result[0]
            #    print(f"Selected User Level ID: {userlevelid} : {selected}")
                return userlevelid
            else:
                return -1
            
    def IsAlreadyHavePersonNo(self,PersonNo):
        conn = ConnectDb()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tblPerson WHERE ID =?",(PersonNo,))
        result = cursor.fetchone()
        if result:
            return TRUE
        else:
            return FALSE
        

    def SaveOrUpdateUser(self):
        personno= self.vPersonNo.get()
        if not personno:
            messagebox.showwarning("No Data","โปรดใส่รหัสประจำตัว",parent=self.Window)
            return
        if self.IsAlreadyHavePersonNo(personno):
            self.UpdateUser()
        else:
            self.AddUser()

    def UpdateUser(self):
        personno= self.vPersonNo.get()
        personname = self.vPersonName.get()
        username = self.vUserName.get()
        levelid= self.FindUserLevelID()
        if self.vActive.get()==1:
            active ='A'   
        else:
            active ='I' 

        conn = ConnectDb()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE tblPerson SET Name = ?, UserName =?, Active =?, UserLevelID =? WHERE ID =?",(personname,username,active,levelid,personno))
            conn.commit()
            conn.close()
            self.ShowTbl()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error",f'มี User Name : {username} อยู่แล้ว',parent=self.Window)
            pass
        

    def AddUser(self):
        personno= self.vPersonNo.get()
        personname = self.vPersonName.get()
        username = self.vUserName.get()
        levelid= self.FindUserLevelID()
        if self.vActive.get()==1:
            active ='A'   
        else:
            active ='I' 
        
        if not personno:
            messagebox.showwarning("No Data","โปรดใส่รหัสประจำตัว",parent=self.Window)
            return
        if not personname:
            messagebox.showwarning("No Data","โปรดใส่ชื่อ",parent=self.Window)
            return
        if not username:
            messagebox.showwarning("No Data","โปรดใส่ User Name",parent=self.Window)
            return
        if levelid<0:
            messagebox.showwarning("No Data","โปรดเลือก User Level",parent=self.Window)
            return
        password_bypt = b'1234'
        Salt = bcrypt.gensalt()
        Hashed_Password = bcrypt.hashpw(password_bypt, Salt)
        conn = ConnectDb()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tblPerson (ID, Name,UserName,Password_Hash,Salt,Active,UserLevelID)"+ 
                           " VALUES (?, ?,?,?,?,?,?)", (personno, personname,username,Hashed_Password,Salt,active,levelid))
        conn.commit()
        conn.close()
        self.ShowTbl()



    def ShowTbl(self):
        conn =ConnectDb()
        cursor = conn.cursor()
        cursor.execute("SELECT tblPerson.ID, tblPerson.Name, tblPerson.UserName, tblUserLevel.Name, tblPerson.Active FROM tblPerson INNER JOIN tblUserLevel " +
                       "ON tblPerson.UserLevelID = tblUserLevel.ID")
        rows = cursor.fetchall()     
        self.tbl.delete(*self.tbl.get_children())
        for row in rows:
            self.tbl.insert('','end',values=row)


def main():
    root = tk.Tk()
    app = frmAdUser(root)
    root.mainloop()

if __name__ == "__main__":
    main()