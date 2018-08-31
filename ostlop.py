from tkinter import *
import MySQLdb

root = Tk()
root.title("ID Generation Form")
root.geometry('600x600')

label_0 = Label(root, text="Enter ID Details", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Reg.No.", width=20, anchor=W, font=("bold", 10), fg='brown')
label_1.place(x=80, y=130)

entry_1_1 = Entry(root, bg='brown', fg='white', width=15)
entry_1_1.place(x=290, y=130)

label_2 = Label(root, text="OR", width=20, font=("bold", 10), fg='brown')
label_2.place(x=150, y=180)

label_3 = Label(root, text="Phone no.", width=20, anchor=W, font=("bold", 10), fg='brown')
label_3.place(x=70, y=230)

entry_3 = Entry(root, bg='brown', fg='white', width=15)
entry_3.place(x=290, y=230)

def getAttributes():
    reg = '0'
    phn = '0'
    reg = entry_1_1.get()
    
    phn = entry_3.get()
         
    get_row(reg, phn)

def get_row(reg, phn):

    conn=MySQLdb.connect(host='localhost', database='world', user='root', password='aditya')

    cur=conn.cursor()

    str="select * from student where reg = '%s' or  phn = '%s'"
    args = (reg, phn)

    try:
        cur.execute(str % args)
        row = cur.fetchone()
        print(row)
        conn.commit()
        print('row recieved...')

        root1 = Tk()
        root1.title("ID Generator")
        c = Canvas(root1, height=400, width=300, cursor='pencil')
        #file1 = PhotoImage(file="sakeclogo.gif")
        #c.create_image(150,200, image=file1)

        name = row[0]+" "+row[1]

        dob = row[2]+"/"+row[3]+"/"+row[4]

        gender = row[5]

        dept = row[6]

        reg = row[7]

        year = row[8]

        phn = row[9]

        c.create_text(130,100, text='Name:', anchor=E, font=('Arial',17,'bold'), fill='grey')
        c.create_text(150,100, text=name, anchor=W, font=('Arial',17,'bold'), fill='brown')

        c.create_text(130,135, text='D.O.B.:', anchor=E, font=('Arial',17,'bold'), fill='brown')
        c.create_text(150,135, text=dob, font=('Arial',17,'bold'), anchor=W, fill='brown')

        c.create_text(130,170, text='Gender:', font=('Arial',17,'bold'), anchor=E, fill='red')
        c.create_text(150,170, text=gender, font=('Arial',17,'bold'), anchor=W, fill='brown')

        c.create_text(130,205, text='Dept.:', font=('Arial',17,'bold'), anchor=E, fill='brown')
        c.create_text(150,205, text=dept, font=('Arial',17,'bold'), anchor=W, fill='brown')

        c.create_text(130,240, text='Reg No.:', font=('Arial',17,'bold'), anchor=E, fill='brown')
        c.create_text(150,240, text=reg, font=('Arial',17,'bold'), anchor=W, fill='brown')

        c.create_text(130,275, text='Year:', font=('Arial',17,'bold'), anchor=E, fill='brown')
        c.create_text(150,275, text=year, font=('Arial',17,'bold'), anchor=W, fill='brown')

        c.create_text(130,310, text='Phone No.:', font=('Arial',17,'bold'), anchor=E, fill='brown')
        c.create_text(150,310, text=phn, font=('Arial',17,'bold'), fill='brown', anchor=W)

        c.pack()
        root1.mainloop()

    except Exception as e:
        conn.rollback()
        print(e)

    finally:
        cur.close()
        conn.close()
    root.destroy()

Button(root, text='Submit', width=20, bg='brown', fg='white', command=getAttributes).place(x=180, y=480)

root.mainloop()
