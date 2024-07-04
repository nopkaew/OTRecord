import tkinter as tk
from tkinter import ttk
from tkinter import *
from screeninfo import get_monitors
from dBOTRecord import *
from tkinter import messagebox

class frmCreateTeam:
    def get_screen_width(self):
    # ดึงความกว้างของหน้าจอหลัก
        for m in get_monitors():
            if m.is_primary:
                return m.width 

    def __init__(self,MainWindow,UserName):
        self.MainWindow = MainWindow
        self.UserName = UserName
        self.SelectPathID_tree = None
        self.SelectNodeID_tree = None
        self.SelectBigBossID_tree = None
        self.scale = self.get_screen_width()/1600
        self.FONT1 = ('Tahoma',int(11*self.scale))  # กำหนด font เริ่มต้น 
        self.Window = tk.Toplevel(MainWindow.master)
        self.Window.title('สร้างทีม User : ' + self.UserName)
        self.Window.geometry(str(int(1000*self.scale))+'x'+str(int(500*self.scale))+'+'+str(int(400*self.scale))+'+'+str(int(200*self.scale)))

        top_frame = tk.Frame(self.Window , bg='red',width=400, height=50, pady=3)
        left_frame = tk.Frame(self.Window , bg='yellow', width=450, height=400, pady=3)
        right_frame = tk.Frame(self.Window , bg='blue', width=450, height=400, pady=3)
        right_bottom_frame = tk.Frame(right_frame , bg='pink', width=450, height=100, pady=3)
        bottom_frame = tk.Frame(self.Window , bg='gray', width=400, height=40, pady=3)

        # layout all of the main containers
        self.Window .grid_rowconfigure(1, weight=1)
        self.Window .grid_columnconfigure(0, weight=1)
        self.Window .grid_columnconfigure(1, weight=1)

        top_frame.grid(row=0,column=0,columnspan=2,sticky="nsew")
        left_frame.grid(row=1,column=0,sticky="nsew")
        right_frame.grid(row=1,column=1,sticky="nsew")
        right_bottom_frame.grid(row=2,column=0, columnspan=3,sticky="nsew")
        bottom_frame.grid(row=2,column=0,columnspan=2,sticky="nsew")
        
        left_frame.grid_rowconfigure(1, weight=1)
        left_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_rowconfigure(1, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        

        lblInfo = tk.Label(top_frame,background='red',foreground='white' ,text='สร้างทีมโดยเลือกทีมงานจากตารางด้านขวา',font=self.FONT1)
        self.lblTeam = tk.Label(left_frame,background='yellow',text='ทีมทั้งหมด',font=self.FONT1)
        lblPerson = tk.Label(right_frame,background='blue', foreground='white' , text='รายชื่อพนักงาน',font=self.FONT1)
        lblฺBottom = tk.Label(bottom_frame,background='gray', text='Bottom Frame',font=self.FONT1)
        self.vActive = IntVar()
        chkActive = tk.Checkbutton(right_frame,text='ยังคงปฏิบัติงานอยู่',variable=self.vActive,font=self.FONT1)
        self.vlblTreeSelected = StringVar()
        lblTreeSelected = tk.Label(right_bottom_frame,textvariable=self.vlblTreeSelected,background='pink', text='Tree Selected',font=self.FONT1)
        self.vlblTblSelected = StringVar()
        lblTblSelected = tk.Label(right_bottom_frame, textvariable=self.vlblTblSelected ,background='pink',text='Table Selected',font=self.FONT1)
        btnCreateTeam = tk.Button(right_bottom_frame,text='    สร้างทีม    ',font=self.FONT1,command=self.OnCreateTeam)
        btnAddMember = tk.Button(right_bottom_frame,text='  เพิ่มสมาชิก  ',font=self.FONT1,command=self.OnAddMember)
        btnDeleteMomber = tk.Button(right_bottom_frame,text='นำสมาชิกออก',font=self.FONT1, command= self.OnDeleteMember)

        self.YScrollTbl = ttk.Scrollbar(right_frame)
        self.YScrollTree = ttk.Scrollbar(left_frame)

        header = ['รหัสพนักงาน', 'ชื่อ','User Level','สถานะปัจจุบัน']
        # กำหนดหัวตารางและความกว้าง
        column_widths = {  # กำหนดความกว้างของแต่ละคอลัมน์
            "รหัสพนักงาน": 80,
            "ชื่อ": 150,
            "User Level": 100,
            "สถานะปัจจุบัน": 80
        }
        
        self.tree = ttk.Treeview(left_frame,yscrollcommand=self.YScrollTree.set)
        self.tbl= ttk.Treeview(right_frame, columns=header, yscrollcommand=self.YScrollTbl.set ,show='headings')
        self.YScrollTbl.config(command=self.tbl.yview)
        self.YScrollTree.config(command=self.tree.yview)

        for col, heading in zip(("รหัสพนักงาน", "ชื่อ", "User Level", "สถานะปัจจุบัน"), ("รหัสพนักงาน", "ชื่อ", "User Level", "สถานะปัจจุบัน")):
            self.tbl.heading(col, text=heading, anchor="center")
            self.tbl.column(col, anchor="w", width=column_widths.get(col, 100))  # กำหนดความกว้าง หรือใช้ค่า default 100
        #    self.tree.heading(col, text=heading, anchor="center")
        #    self.tree.column(col, anchor="w", width=column_widths.get(col, 100))  # กำหนดความกว้าง หรือใช้ค่า default 100
        self.tree.heading("#0", text="รายชื่อสมาชิกทีม")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Tahoma", 11,"bold"))
        style.configure("Treeview", font=("Tahoma", 11))

        lblInfo.grid(row=0, column=0,padx= 5,pady= 5,sticky='nsew')  
        self.lblTeam .grid(row=0, column=0,padx= 5,pady= 5,sticky='nw')
        lblPerson.grid(row=0, column=0,padx= 5,pady= 5,sticky='nw')
        lblฺBottom.grid(row=0, column=0,padx= 5,pady= 5,sticky='nsew')
        chkActive.grid(row=0, column=1,padx= 5,pady= 5,sticky='nw')
        self.YScrollTree.grid(row=1, column=1,padx= (0,5),pady= 2,sticky='ns')
        self.tree.grid(row=1, column=0,padx= (5,0),pady= 3,sticky='nsew')
        self.YScrollTbl.grid(row=1, column=2,padx= (0,5),pady= 2,sticky='ns')
        self.tbl.grid(row=1, column=0,columnspan=2,padx= (5,0),pady= 3,sticky='nsew')
        lblTreeSelected.grid(row=0, column=0,columnspan=3,padx= 5,pady= 5,sticky='nw')
        lblTblSelected.grid(row=1, column=0,columnspan=3,padx= 5,pady= 5,sticky='nw')
        btnCreateTeam.grid(row=2, column=0,padx= 5,pady= 5,sticky='nsew') 
        btnAddMember.grid(row=2, column=1,padx= 5,pady= 5,sticky='nsew') 
        btnDeleteMomber.grid(row=2, column=2,padx= 5,pady= 5,sticky='nsew')

        self.tbl.bind("<<TreeviewSelect>>",self.OnTblSelect)
        self.tree.bind("<<TreeviewSelect>>",self.OnTreeSelect)
        self.vActive.set(1)
        self.ShowTbl()
        self.ShowTeam()
    #    self.DisplayTeam()

    def OnCreateTeam(self):
        selected = self.tbl.selection()
        if not selected:
            print('no selection')
            return
        output = self.tbl.item(selected)
    #    print(output)
        data = output['values']
        personid = data[0]
    #    print(personid)
        conn = ConnectDb()
        curror = conn.cursor()
        try:
            sql = 'INSERT INTO tblTeam (PersonID,MasterPerson,BigBoss,FullMasterPerson,Active,FullPathPerson) VALUES (?,?,?,?,?,?)'
            curror.execute(sql,(personid,None,personid,None,'Active',personid))
            conn.commit()
        except sqlite3.Error as e:
                print(f'error : {e}')  
        finally:       
            conn.close()
        self.ShowTeam()
    #    self.DisplayTeam()

    def ShowTeam(self):
        conn = ConnectDb()
        cursor = conn.cursor()
        sql = 'SELECT tblTeam.PersonID,tblPerson.Name,tblTeam.MasterPerson,tblTeam.BigBoss FROM tblTeam INNER JOIN tblPerson ON tblTeam.PersonID = tblPerson.ID'
        cursor.execute(sql)
        rows  = cursor.fetchall()
        if self.tree.get_children():
            self.tree.delete(*self.tree.get_children())

        bigboss_nodes = {}

        # สร้าง node ของ BigBoss และ node ลูกน้องทั้งหมด
        for row in rows:
            id, name, manager_id, bigboss_id = row
            if manager_id is None:  # ถ้าเป็น root node (BigBoss)
                if bigboss_id not in bigboss_nodes:
                    parent_text = self.tree.insert('', 'end', text=name, values=(id, name, bigboss_id))
                    bigboss_nodes[bigboss_id] = parent_text
                else:
                    parent_text = bigboss_nodes[bigboss_id]
                self.insert_employee(id, parent_text, rows, bigboss_nodes)  # เรียกฟังก์ชัน insert_employee ซ้ำ

        conn.close()

    def insert_employee(self, parent_id, parent_text, rows, bigboss_nodes={}):
        for row in rows:
            id, name, manager_id, bigboss_id = row
            if manager_id == parent_id:
                if manager_id is None:  # ถ้าเป็น root node (BigBoss)
                    if bigboss_id not in bigboss_nodes:
                        parent_text = self.tree.insert('', 'end', text=name, values=(id, name, bigboss_id))
                        bigboss_nodes[bigboss_id] = parent_text
                    else:
                        parent_text = bigboss_nodes[bigboss_id]
                    node_values = (id, name, id)  # ใช้ id แทน None เมื่อเป็น BigBoss
                else:
                    parent_text = parent_text
                    node_values = (id, name, bigboss_id)
                    parent_bigboss_id = self.tree.item(parent_text)['values'][2]  # ดึงค่า BigBoss ของ parent
                    print('parent_bigboss_id :  bigboss_id : ')
                    print(parent_bigboss_id)
                    print(bigboss_id)
                if str(parent_bigboss_id) == str(bigboss_id):    
                    print('Equal')                
                    node_text = f"{name}"
                    node_id = self.tree.insert(parent_text, 'end', text=node_text, values=node_values)
                    self.insert_employee(id, node_id, rows, bigboss_nodes)
            '''
    def insert_employee(self, parent_id, parent_text, rows, bigboss_nodes={}):
        for row in rows:
            id, name, manager_id, bigboss_id = row
            if manager_id == parent_id:
                if manager_id is None:  # ถ้าเป็น root node (BigBoss)
                    if bigboss_id not in bigboss_nodes:
                        parent_text = self.tree.insert('', 'end', text=name, values=(id, name, bigboss_id))
                        bigboss_nodes[bigboss_id] = parent_text
                    else:
                        parent_text = bigboss_nodes[bigboss_id]
                    node_values = (id, name, id)  # ใช้ id แทน None เมื่อเป็น BigBoss
                else:
                    parent_text = parent_text
                    node_values = (id, name, bigboss_id)

                node_text = f"{name}"
                node_id = self.tree.insert(parent_text, 'end', text=node_text, values=node_values)
                self.insert_employee(id, node_id, rows, bigboss_nodes)
            '''

    def DisplayTeam(self):
        conn = ConnectDb()
        cursor = conn.cursor()
        sql = 'SELECT tblTeam.PersonID,tblPerson.Name,tblTeam.MasterPerson,tblTeam.BigBoss FROM tblTeam INNER JOIN tblPerson ON tblTeam.PersonID = tblPerson.ID'
        cursor.execute(sql)
        rows = cursor.fetchall()

        if self.tree.get_children():
            self.tree.delete(*self.tree.get_children())

        bigboss_nodes = {}  # เก็บ node ของ BigBoss
        nodes = {}          # เก็บ node ของพนักงานทั้งหมด

        # สร้าง node ของ BigBoss ก่อน
        for row in rows:
            id, name, manager_id, bigboss_id = row
            if manager_id is None:
                node_id = self.tree.insert('', 'end', text=name, values=(id, name, bigboss_id))
                bigboss_nodes[bigboss_id] = node_id
                nodes[id] = node_id

        # สร้าง node ของพนักงานที่เหลือ
        while True:
            changed = False  # flag เพื่อติดตามการเปลี่ยนแปลง
            for row in rows:
                id, name, manager_id, bigboss_id = row
                if manager_id is not None and manager_id in nodes and id not in nodes:
                    parent_text = bigboss_nodes.get(bigboss_id, '')
                    node_values = (id, name, bigboss_id if manager_id is None else None)
                    node_id = self.tree.insert(parent_text, 'end', text=name, values=node_values)
                    nodes[id] = node_id
                    changed = True
            if not changed:  # ถ้าไม่มีการเปลี่ยนแปลง แสดงว่าสร้าง node ครบแล้ว
                break

        conn.close()

    def OnDeleteMember(self):
        selected = self.tree.selection()
        check = messagebox.askyesno("ยืนยันการลบสมาชิกทีม",'กำลังนำรายชื่อสมาชิกออกจากทีม ยืนยันให้ดำเนินการหรือไม่?',parent=self.Window)
        if not  check:
            return
        if selected:
            # ตรวจสอบว่าเป็นสมาชิกที่อยู่ล่างสุดหรือไม่
            if not self.tree.get_children(selected):
                fullpathperson = self.SelectPathID_tree
                print(fullpathperson)
                conn = ConnectDb()
                cursor = conn.cursor()
                try:
                    cursor.execute('DELETE FROM tblTeam WHERE FullPathPerson = ?',(fullpathperson,))
                    conn.commit()
                    self.tree.delete(selected)
                    self.lblTeam.config(text="")
                except sqlite3.Error as e:
                    messagebox.showerror('Error',f'error : {e}',parent=self.Window)  
                finally:       
                    conn.close()
                

    def OnAddMember(self):
        selected = self.tbl.selection()
        if not selected:
            print('no selection')
            return
        output = self.tbl.item(selected)
    #    print(output)
        data = output['values']
        personid = data[0]
        personname = data[1]
        
        if self.SelectPathID_tree==None:
            return
        conn = ConnectDb()
        cursor = conn.cursor()
        try:
            sql = 'INSERT INTO tblTeam (PersonID,MasterPerson,BigBoss,FullMasterPerson,Active,FullPathPerson) VALUES (?,?,?,?,?,?)'
            cursor.execute(sql,(personid,self.SelectNodeID_tree,self.SelectBigBossID_tree,self.SelectPathID_tree,'Active',self.SelectPathID_tree+'/'+str(personid)))
            conn.commit()
            treeselected = self.tree.selection()
        #    FullMasterPerson = self.GetSelectionPathID()
            if treeselected:     
                new_member = self.tree.insert(treeselected,'end',text=personname,values=[personid,personname,self.SelectBigBossID_tree])
                self.tree.selection_set(new_member)  # เลือกสมาชิกที่เพิ่งเพิ่ม
                self.tree.see(new_member)  # ให้ treeview เลื่อนไปแสดงสมาชิกใหม่
        except sqlite3.Error as e:
                messagebox.showerror('Error',f'error : {e}',parent=self.Window)  
        finally:       
            conn.close()


    def GetSelectionPathID(self):
        selected = self.tree.selection()
        if selected:
            path = []
            while selected != "":
                nameitem = self.tree.item(selected)
                name = nameitem['values']
                path.insert(0,name[0])    #ต้องการนำค่าจาก values มาใช้ เพื่อประโยชน์ในการ Record ลง dB
            #    path.insert(0, self.tree.item(selected, 'text'))           #สามารถใช้ path.insert(0, self.tree.item(selected, 'text'))  ก็ได้
                selected = self.tree.parent(selected)
            txtPath="/".join(path)
        return str(txtPath)
      
    def OnTreeSelect(self,event):
        focused_item = self.tree.focus()
        if not focused_item:
            self.SelectPathID_tree =None
            self.SelectNodeID_tree = None
            self.SelectBigBossID_tree = None
            self.lblTeam.config(text="")
            return
        
        selected = self.tree.selection()
        print(selected)
        output = self.tree.item(selected)
        print(output)
        datatree = output['values']
        if not datatree:
            return
        self.vlblTreeSelected.set(f'Tree View กำลังเลือก หมายเลข {datatree[0]} : {datatree[1]}')
        self.SelectNodeID_tree = datatree[0]
        self.SelectBigBossID_tree = datatree[2]
             
        if selected:
            pathText = []
            pathID =[]
            while selected != "":
                nameitem = self.tree.item(selected)
                name = nameitem['values']
                pathText.insert(0,name[1])    #ต้องการนำค่าจาก values มาใช้ เพื่อประโยชน์ในการ Record ลง dB
                pathID.insert(0,str(name[0]))
            #    path.insert(0, self.tree.item(selected, 'text'))           #สามารถใช้ path.insert(0, self.tree.item(selected, 'text'))  ก็ได้
                selected = self.tree.parent(selected)
            self.SelectPathID_tree = "/".join(pathID)
            self.lblTeam.config(text= '/'.join(pathText))     


    def OnTblSelect(self,event):
        selected = self.tbl.selection()
        output = self.tbl.item(selected)
        data = output['values']
        if not data:
            return
        self.vlblTblSelected.set(f'Table View กำลังเลือก หมายเลข {data[0]} : {data[1]}')
        pass
       
    def ShowTbl(self):
        for item in self.tbl.get_children():
            self.tbl.delete(item)
        conn=ConnectDb()
        with conn:
            sql = "SELECT tblPerson.ID, tblPerson.Name, tblUserLevel.Name, tblPerson.Active FROM tblPerson INNER JOIN tblUserLevel ON tblPerson.UserLevelID = tblUserLevel.ID"
            c.execute(sql)
            rows = c.fetchall()
        conn.close()
        for row in rows:
            self.tbl.insert("", "end", values=row)

def main():
    root = tk.Tk()
    app = frmCreateTeam(root)
    root.mainloop()

if __name__ == "__main__":
    main()