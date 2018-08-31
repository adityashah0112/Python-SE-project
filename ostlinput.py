from tkinter import *
import MySQLdb

root = Tk()
root.title("ID Information Form")
root.geometry('550x600')

photolabel = Label(root)
photo = PhotoImage(file="sakecheader2.png")
photolabel.config(image=photo)
photolabel.place(x=0, y=20)

label_0 = Label(root, text="ID Details", width=20, font=("bold", 20), fg='brown')
label_0.place(x=90, y=80)

label_1 = Label(root, text="Name (First/Last)", anchor = W, width=20, font=("bold", 10), fg='brown')
label_1.place(x=80, y=130)

entry_1_1 = Entry(root, bg='brown', fg='white', width=8)
entry_1_1.place(x=290, y=130)

entry_1_2 = Entry(root, bg='brown', fg='white', width=8)
entry_1_2.place(x=360, y=130)


label_2 = Label(root, text="D.O.B (DD/MM/YYYY)", width=20, anchor = W, font=("bold", 10), fg='brown')
label_2.place(x=80, y=180)

vald = IntVar()
sd=Spinbox(root, from_=1, to=31, textvariable=vald,  bg='brown', fg='white', width=3, font=('Arial', 10)).place(x=290, y=180)
vald.set('dd')

valm = IntVar()
sm=Spinbox(root, from_=1, to=12, textvariable=valm,  bg='brown', fg='white', width=3, font=('Arial', 10)).place(x=330, y=180)
valm.set('mm')

valy = IntVar()
sy=Spinbox(root, from_=1990, to=2000, textvariable=valy,  bg='brown', fg='white', width=6, font=('Arial', 10)).place(x=370, y=180)
valy.set('yyyy')

label_3 = Label(root, text="Gender", width=20, font=("bold", 10), anchor = W, fg='brown')
label_3.place(x=80, y=230)

var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var, value=1, fg='brown').place(x=285, y=230)
Radiobutton(root, text="Female", padx=5, variable=var, value=2, fg='brown').place(x=340, y=230)


label_4 = Label(root, text="Department", width=20, font=("bold", 10), anchor = W, fg='brown')
label_4.place(x=80, y=280)

list1 = ['Computers', 'Electronics', 'Information Technology', 'Electronics and Communications']
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width=15, bg='brown', fg='white')
c.set('Department')
droplist.place(x=290, y=280)

label_5 = Label(root, text="Reg. No.", anchor = W, width=20, font=("bold", 10), fg='brown')
label_5.place(x=80, y=330)

entry_3 = Entry(root, bg='brown', fg='white')
entry_3.place(x=290, y=330)


label_6 = Label(root, text="Year", width=20, anchor = W, font=("bold", 10), fg='brown')
label_6.place(x=80, y=380)

var1 = IntVar()
Radiobutton(root, text="First", padx=5, variable=var1, value=1, fg='brown').place(x=235, y=380)
Radiobutton(root, text="Second", padx=5, variable=var1, value=2, fg='brown').place(x=290, y=380)
Radiobutton(root, text="Third", padx=5, variable=var1, value=3, fg='brown').place(x=355, y=380)
Radiobutton(root, text="Fourth", padx=5, variable=var1, value=4, fg='brown').place(x=420, y=380)

label_7 = Label(root, text="Phone Number", width=20, anchor = W, font=("bold", 10), fg='brown')
label_7.place(x=80, y=430)

entry_4 = Entry(root, bg='brown', fg='white')
entry_4.place(x=290, y=430)

def getAttributes():
    fname = entry_1_1.get()
    lname = entry_1_2.get()
    
    d = vald.get()
    m = valm.get()
    y = valy.get()

    g = var.get()

    if g == 1:
        gender = "M"
    else:
        gender = "F"

    dept =  c.get()

    reg = entry_3.get()
    
    ye =  var1.get()
    if ye == 1:
        year = int(1)
    elif ye == 2:
        year = int(2)
    elif ye == 3:
        year = int(3)
    else:
        year = int(4)

    phn = entry_4.get()
    
    print("Name:\t",fname,lname,"\nD.O.B.:\t",d,m,y,"\nGender:\t",gender,"\nDepartment:\t",dept,"\nReg. No.:\t",reg,"\nYear:\t",year,"\nPhone Number:\t",phn)
    insert_rows(fname, lname, d, m, y, gender, dept, reg, year, phn)

def insert_rows(fname, lname, d, m, y, gender, dept, reg, year, phn):

    conn=MySQLdb.connect(host='localhost', database='world', user='root', password='aditya')

    cursor=conn.cursor()

    str="insert into student(fname, lname, d, m, y, gender, dept, reg, year, phn) values('%s', '%s', '%s', '%s', '%s', '%c', '%s', '%s', '%d', '%s')"
    args = (fname, lname, d, m, y, gender, dept, reg, year, phn)

    try:
        cursor.execute(str % args)

        conn.commit()
        print('row inserted...')

    except:
        conn.rollback()
        print("Try Again")

    finally:
        cursor.close()
        conn.close()
    Button(root, text='Exit', width=20, bg='brown', fg='white', command=destroy).place(x=180, y=530)

def destroy():
    root.destroy()

   
Button(root, text='Submit', width=20, bg='brown', fg='white', command=getAttributes).place(x=180, y=480)

root.mainloop()
