import tkinter as tk
from frmAddUser import frmAdUser
from frmCreateTeam import frmCreateTeam
from screeninfo import get_monitors

class MainFrm:       
   
    def get_screen_width(self):
    # ดึงความกว้างของหน้าจอหลัก
        for m in get_monitors():
            if m.is_primary:
                return m.width                     
    
    def RunFrmAddUser(self):
        frmAdUser(self.master,self.UserName)

    def RunFrmCreateTeam(self):
        frmCreateTeam(self.master,self.UserName)


    def __init__(self,master,UserName):
        self.master = master
        self.UserName = UserName
        self.scale = self.get_screen_width()/1600
        self.FONT1 = ('Tahoma',int(15*self.scale))  # กำหนด font เริ่มต้น
        super().__init__()          
        master.title("บันทึกการทำงานล่วงเวลา User : " + self.UserName)
    #    self.geometry('500x200+400+200')
        master.geometry(str(int(500*self.scale))+'x'+str(int(300*self.scale))+'+'+str(int(400*self.scale))+'+'+str(int(200*self.scale)))
        master.columnconfigure([0,1,2],weight=1,minsize=int(100*self.scale))
        master.rowconfigure([0,1,2],weight=1,minsize=int(100*self.scale))

        btn_open_adduser = tk.Button(master, text="บัญชีผู้ใช้",font=self.FONT1,command=self.RunFrmAddUser)
        btn_open_otrecord = tk.Button(master, text="บันทึก OT",font=self.FONT1,command=self.RunFrmAddUser)
        btn_open_createteam = tk.Button(master, text="สร้างทีม",font=self.FONT1,command=self.RunFrmCreateTeam)
        btn_open_summary= tk.Button(master, text="รายงานสรุป",font=self.FONT1,command=self.RunFrmAddUser)
        btn_open_sql = tk.Button(master, text="SQL",font=self.FONT1,command=self.RunFrmAddUser)
        btn_open_reason= tk.Button(master, text="สร้างเหตุผล",font=self.FONT1,command=self.RunFrmAddUser)
        btn_open_reasoncatagory = tk.Button(master, text="จัดกลุ่มเหตุผล",font=self.FONT1,command=self.RunFrmAddUser)
        btn_open_budget = tk.Button(master, text="งบประมาณ",font=self.FONT1,command=self.RunFrmAddUser)
        btn_open_sarary = tk.Button(master, text="เงินเดือน",font=self.FONT1,command=self.RunFrmAddUser)

        btn_open_otrecord.grid(column=0,row=0,padx=int(5*self.scale),pady=int(5*self.scale),sticky='nsew')
        btn_open_reasoncatagory.grid(column=1,row=0,padx=int(5*self.scale),pady=int(5*self.scale),sticky='nsew')
        btn_open_reason.grid(column=2,row=0,padx=int(5*self.scale),pady=int(5*self.scale),sticky='nsew')
        btn_open_summary.grid(column=0,row=1,padx=int(5*self.scale),pady=int(5*self.scale),sticky='nsew')
        btn_open_createteam.grid(column=1,row=1,padx=int(5*self.scale),pady=int(5*self.scale),sticky='nsew')
        btn_open_adduser.grid(column=2,row=1,padx=int(5*self.scale),pady=int(5*self.scale),sticky='nsew')
        btn_open_budget.grid(column=0,row=2,padx=int(5*self.scale),pady=int(5*self.scale),sticky='nsew')
        btn_open_sql.grid(column=1,row=2,padx=int(5*self.scale),pady=int(5*self.scale),sticky='nsew')
        btn_open_sarary.grid(column=2,row=2,padx=int(5*self.scale),pady=int(5*self.scale),sticky='nsew')

'''         
def main():
#    app = frmCreateDb()
    root = tk.Tk()
    app = MainFrm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    '''
