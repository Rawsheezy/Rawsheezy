from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random
import time

class DataEntryForm:
    def __init__(self,root):
        self.root = root
        self.root.title("MySQL Data Entry Form")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background="gainsboro")

        
        RefNo = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Telephone = StringVar()
        RegDate = StringVar()
        Prove = StringVar()
        CurrentDate = StringVar()
        MemberType = StringVar()
        MemberFee = StringVar()
        Search = StringVar()
        DateDay = StringVar()
        DateToDay = StringVar()

        MainFrame = Frame(self.root, bd =10, width=1350, height =700 , relief=RIDGE)
        MainFrame.grid()
        MainFrame.pack()

        TopFrame1 = Frame(MainFrame, bd =5, width=1340, height =200 , relief=RIDGE, bg= 'cadet blue')
        TopFrame1.grid(row=0, column=0)
        TopFrame2 = Frame(MainFrame, bd =5, width=1340, height =50 , relief=RIDGE, bg= 'cadet blue')
        TopFrame2.grid(row=1, column=0)
        TopFrame3 = Frame(MainFrame, bd =5, width=1340, height =300 , relief=RIDGE, bg= 'cadet blue')
        TopFrame3.grid(row=2, column=0)

        InnerTopFrame1 = Frame(TopFrame1, bd =5, width=1330, height =190 , relief=RIDGE)
        InnerTopFrame1.grid()
        InnerTopFrame2 = Frame(TopFrame2, bd =5, width=1330, height =48 , relief=RIDGE)
        InnerTopFrame2.grid()
        InnerTopFrame3 = Frame(TopFrame3, bd =5, width=1330, height =280 , relief=RIDGE)
        InnerTopFrame3.grid()
        
        RegDate.set(time.strftime("%m/%d/%Y"))
        DateToDay.set(time.strftime("%m/%d/%Y"))

        def Reset():
            RefNo.set("")
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Telephone.set("")
            RegDate.set("")
            Prove.set("")
            CurrentDate.set("")
            MemberType.set("")
            MemberFee.set("")
            Search.set("")
            DateDay.set("")
            DateToDay.set("")
             
            RegDate.set(time.strftime("%m/%d/%Y"))
            DateToDay.set(time.strftime("%m/%d/%Y"))

        def iExit():
            iExit = tkinter.messagebox.askyesno("Data Entry Form","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def addData():
            if RefNo.get()=="" or Firstname.get()=="" or Surname.get()=="":
                tkinter.messagebox.showerror("Data Entry Form","Enter Correct Details")
            else:
                sqlCon =pymysql.connect(host="localhost", user="root", password="T3chnician", database="dataentry") #python pip install pymyql
                cur = sqlCon.cursor()
                cur.execute("insert into dataentry values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                RefNo.get(),
                Firstname.get(),
                Surname.get(),
                Address.get(),
                Telephone.get(),
                RegDate.get(),
                Prove.get(),
                CurrentDate.get(),
                MemberType.get(),
                MemberFee.get()
                ))

                sqlCon.commit()
                DisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")
        
        
        def DisplayData():
            sqlCon =pymysql.connect(host="localhost", user="root", password="T3chnician", database="dataentry") #python pip install pymyql
            cur = sqlCon.cursor()
            cur.execute("select * from dataentry")
            result = cur.fetchall()
            if len(result) !=0:
                tree_records.delete(*tree_records.get_children())
                for row in result:
                    tree_records.insert('',END,values = row)
                    
                sqlCon.commit()
                sqlCon.close
        
        def LearnersInfo(ev):
            viewInfo = tree_records.focus()
            learnerData = tree_records.item(viewInfo)
            row = learnerData ['values']
            RefNo.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            Telephone.set(row[4])
            RegDate.set(row[5])
            Prove.set(row[6])
            DateDay.set(row[7])
            MemberType.set(row[8])
            MemberFee.set(row[9])

        def update():
            sqlCon =pymysql.connect(host="localhost", user="root", password="T3chnician", database="dataentry") #python pip install pymyql
            cur = sqlCon.cursor()
            cur.execute("update dataentry set Firstname=%s,Surname=%s,Address=%s,Telephone=%s,RegDate=%s,ProveID=%s,CurrentDate=%s,MemberType=%s,MemberFee=%s where RefNo=%s",(
                  
            Firstname.get(),
            Surname.get(),
            Address.get(),
            Telephone.get(),
            RegDate.get(),
            Prove.get(),
            DateDay.get(),
            MemberType.get(),
            MemberFee.get(),
            RefNo.get()
            ))

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Updated Successfully")

        def deleteDB():
            sqlCon =pymysql.connect(host="localhost", user="root", password="T3chnician", database="dataentry") #python pip install pymyql
            cur = sqlCon.cursor()
            cur.execute("delete from dataentry where RefNo=%s", RefNo.get())

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Deleted Successfully")

        def searchDB():
            try:
                sqlCon =pymysql.connect(host="localhost", user="root", password="T3chnician", database="dataentry") #python pip install pymyql
                cur = sqlCon.cursor()
                cur.execute("select * from dataentry where RefNo=%s", Search.get())

                row = cur.fetchone()

                RefNo.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                Address.set(row[3])
                Telephone.set(row[4])
                RegDate.set(row[5])
                Prove.set(row[6])
                DateDay.set(row[7])
                MemberType.set(row[8])
                MemberFee.set(row[9])

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form","No Such Record Found")
                Reset()
            sqlCon.close()
            Search.set("")


        #========================================Widget==============================================
        lblReference = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Reference No", bd=10)
        lblReference.grid(row=0, column=0, sticky=W) 
        txtReference = Entry(InnerTopFrame1, font =('arial',12, 'bold'), bd=5, width=32, justify='left', textvariable=RefNo)
        txtReference.grid(row=0, column=1) 
        
        lblFirstname = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="First Name", bd=10)
        lblFirstname.grid(row=1, column=0, sticky=W) 
        txtFirstname = Entry(InnerTopFrame1, font =('arial',12, 'bold'), bd=5, width=32, justify='left', textvariable=Firstname)
        txtFirstname.grid(row=1, column=1) 

        lblSurname = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Surname", bd=10)
        lblSurname.grid(row=2, column=0, sticky=W) 
        txtSurname = Entry(InnerTopFrame1, font =('arial',12, 'bold'), bd=5, width=33, justify='left', textvariable=Surname)
        txtSurname.grid(row=2, column=1)
        
        self.lblTelephone = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Telephone", bd=10)
        self.lblTelephone.grid(row=0, column=2, sticky=W) 
        self.txtTelephone = Entry(InnerTopFrame1, font =('arial',12, 'bold'), bd=5, width=32, justify='left', textvariable=Telephone)
        self.txtTelephone.grid(row=0, column=3) 
         
        self.lblRegistrationDate = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Registration Date", bd=10)
        self.lblRegistrationDate.grid(row=1, column=2, sticky=W) 
        self.txtRegistrationDate = Entry(InnerTopFrame1, font =('arial',12, 'bold'), bd=5, width=32, justify='left', textvariable=RegDate)
        self.txtRegistrationDate.grid(row=1, column=3) 
        
        self.lblProveOfID = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Prove Of Id", bd=10)
        self.lblProveOfID.grid(row=2, column=2, sticky=W) 
        
        self.cboProveOfID = ttk.Combobox(InnerTopFrame1,font=('font',12, 'bold'), width=31, textvariable=Prove)
        self.cboProveOfID['value'] = ('Select an option','Pilot License','Driving License','Student ID','Passport') 
        self.cboProveOfID.current(0)
        self.cboProveOfID.grid(row=2, column=3)

        self.lblSearch = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Search", bd=10)
        self.lblSearch.grid(row=0, column=4, sticky=W) 
        self.txtSearch = Entry(InnerTopFrame1, font =('arial',12, 'bold'), bd=5, width=32, justify='left', textvariable=Search)
        self.txtSearch.grid(row=0, column=5)
        
        self.lblDate = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Date", bd=10)
        self.lblDate.grid(row=1, column=4, sticky=W) 
        self.txtDate = Entry(InnerTopFrame1, font =('arial',12, 'bold'), bd=5, width=33, justify='left', textvariable=DateToDay)
        self.txtDate.grid(row=1, column=5)
        
        self.lblMemberType = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Member Type", bd=10)
        self.lblMemberType.grid(row=2, column=4, sticky=W) 
        
        self.cboMemberType = ttk.Combobox(InnerTopFrame1,font=('font',12, 'bold'), width=31, textvariable=MemberType)
        self.cboMemberType['value'] = ('Select an option','Annual','Quarterly','Monthly','Weekly') 
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=2, column=5)
        
        self.lblMemberFee = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Member Fee", bd=10)
        self.lblMemberFee.grid(row=3, column=4, sticky=W) 
        
        self.cboMemberFee = ttk.Combobox(InnerTopFrame1,font=('font',12, 'bold'), width=31, textvariable=MemberFee)
        self.cboMemberFee['value'] = ('Select an option','$150.00','$37.00','$12.50','$2.89') 
        self.cboMemberFee.current(0)
        self.cboMemberFee.grid(row=3, column=5)
        
        self.lblAddress = Label(InnerTopFrame1, font =('arial',12, 'bold'),text="Address", bd=10)
        self.lblAddress.grid(row=3, column=0, sticky=W) 
        self.txtAddress = Entry(InnerTopFrame1, font =('arial',12, 'bold'), bd=5, width=83, justify='left', textvariable=Address)
        self.txtAddress.grid(row=3, column=1,columnspan=3) 
        #============================================SCROLL BARS=================================================

        scroll_x=Scrollbar(InnerTopFrame3, orient = HORIZONTAL)
        scroll_y=Scrollbar(InnerTopFrame3, orient = VERTICAL)
        #============================================TABLES=================================================

        tree_records = ttk.Treeview(InnerTopFrame3, height =13, columns=("RefNo","Firstname","Surname","Address","Telephone",
        "RegDate","ProveID","CurrentDate","MemberType","MemberFee"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side =BOTTOM, fill=X)
        scroll_y.pack(side =RIGHT, fill=Y)
        #============================================TABLE HEADINGS=================================================

        tree_records.heading("RefNo", text="Reference No")
        tree_records.heading("Firstname", text="First Name")
        tree_records.heading("Surname", text="Surname")
        tree_records.heading("Address", text="Address")
        tree_records.heading("Telephone", text="Telephone")
        tree_records.heading("RegDate", text="Registration Date")
        tree_records.heading("ProveID", text="Proof Of ID")
        tree_records.heading("CurrentDate", text="Current Date")
        tree_records.heading("MemberType", text="Member Type")
        tree_records.heading("MemberFee", text="Member Fee")

        tree_records['show']='headings'

        tree_records.column("RefNo", width=100)
        tree_records.column("Firstname", width=150)
        tree_records.column("Surname", width=150)
        tree_records.column("Address", width=252)
        tree_records.column("Telephone", width=100)
        tree_records.column("RegDate", width=100)
        tree_records.column("ProveID", width=100)
        tree_records.column("CurrentDate", width=100)
        tree_records.column("MemberType", width=150)
        tree_records.column("MemberFee", width=100)

        tree_records.pack(fill =BOTH, expand=1)
        tree_records.bind("<ButtonRelease-1>",LearnersInfo)
        DisplayData()
        #=============================================================================================
        self.btnAddNew = Button(InnerTopFrame2, pady=1, bd=4, font=('arial',16, 'bold'), width=13,text="Add New",command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=3)

        self.Display = Button(InnerTopFrame2, pady=1, bd=4, font=('arial',16, 'bold'), width=13,text="Display",command=DisplayData)
        self.Display.grid(row=0, column=1, padx=3)
        
        self.btnUpdate = Button(InnerTopFrame2, pady=1, bd=4, font=('arial',16, 'bold'), width=13,text="Update",command=update)
        self.btnUpdate.grid(row=0, column=2, padx=3)

        self.btnDelete = Button(InnerTopFrame2, pady=1, bd=4, font=('arial',16, 'bold'), width=13,text="Delete",command=deleteDB)
        self.btnDelete.grid(row=0, column=3, padx=3)
        
        self.btnReset = Button(InnerTopFrame2, pady=1, bd=4, font=('arial',16, 'bold'), width=13,text="Reset",command=Reset)
        self.btnReset.grid(row=0, column=4, padx=3)

        self.btnExit = Button(InnerTopFrame2, pady=1, bd=4, font=('arial',16, 'bold'), width=13,text="Exit",command=iExit)
        self.btnExit.grid(row=0, column=5, padx=3)

        self.btnSearch = Button(InnerTopFrame2, pady=1, bd=4, font=('arial',16, 'bold'), width=13,text="Search",command=searchDB)
        self.btnSearch.grid(row=0, column=6, padx=3)


if __name__=='__main__':
    root = Tk()
    application =  DataEntryForm(root)
    root.mainloop()
