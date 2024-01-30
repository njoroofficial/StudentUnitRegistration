import tkinter
import tkinter.messagebox
from tkinter.ttk import Combobox
from tkinter import *
import re
from datetime import date
from tkcalendar import Calendar

# SQL
import mysql.connector

mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12960',
        port='3306',
        database='studentRecord'
    )

mycursor = mydb.cursor()


window = Tk()
window.geometry('700x500')
window.config(background='light grey')
window.title('Student Registration')

# get current date
TodayDate = StringVar()
DOBDate = StringVar()
today = date.today()
dat = today.strftime("%d/%m/%y")


# this will receive value from the Gender radioButton
x = IntVar()

# check user gender
if(x.get() == 0):
    gender = 'Male'
elif(x.get() == 1):
    gender = 'Female'

# method to get user details

def getDetails():

    global firstName,lastName,admission,school,course,contact,email,dob,home,courseID

    firstName = fnameField.get()
    lastName = lnameField.get()
    admission = adminField.get()
    school = schoolField.get()
    course = courseField.get()
    contact = contactField.get()
    email = emailField.get()
    dob = dobField.get()
    home = homeField.get()

    courseID = None
    if (course == 'Computer Science'):
        courseID = 'SCO'
    elif (course == 'Information Technology'):
        courseID = 'ISO'
    elif (course == 'Statistics'):
        courseID = 'STI'
    elif (course == 'Law'):
        courseID = 'LLB'

    if(firstName == "" or lastName == "" or admission == "" or course == "" or school == "" or contact == "" or email == ""
        or dob == "" or home == ""):
        tkinter.messagebox.showerror('Error!!','Fill All The Fields')
    else:
        tkinter.messagebox.showinfo('Success','Uploaded Successfully \nThankyou')

    checkContact()
    checkEmail()
    checkAdmin()
    disableEntries()
    databaseConnection()
    callClass()

def callClass():

     window.destroy()
     import mainFrame as mf
     mf.maindata.frame()


def checkContact():

    try:
        # attempt to convert the input string to an integer
        value = int(contactField.get())
        print('Valid Contact value '+str(value))

    except ValueError:
        # if the input string cannot be converted to an integer, show an error message
        print('Invalid Contact')
        tkinter.messagebox.showerror('Error','Input must be an integer.')

def checkEmail():

    emailPattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # match the input against the email pattern using regex

    if re.match(emailPattern,emailField.get()):
        print('Valid Email Address')
    else:
        print('Invalid Email')
        tkinter.messagebox.showerror('Error','Input Valid Email Address')

def checkAdmin():

    adminPattern = r"^[A-Z][0-9]{2}[A-Z]?/([0-9]{5})/[0-9]{4}$"

    match = re.match(adminPattern, adminField.get())

    global uniqueNumber

    uniqueNumber = match.group(1)
    print('The Unique value is '+str(uniqueNumber))

    if match:
        print('Valid Registration Number')
        uniqueNumber = match.group(1)
        print()
        print('The Unique value is ',uniqueNumber)

    else:
        print('Invalid Registration Number')
        tkinter.messagebox.showerror('Error','Input Valid Registration Number')

def disableEntries():

    fnameField.config(state=DISABLED)
    lnameField.config(state=DISABLED)
    adminField.config(state=DISABLED)
    schoolField.config(state=DISABLED)
    courseField.config(state=DISABLED)
    contactField.config(state=DISABLED)
    emailField.config(state=DISABLED)
    dobField.config(state=DISABLED)
    homeField.config(state=DISABLED)
    maleGender.config(state=DISABLED)
    femaleGender.config(state=DISABLED)


def studentDetails():

    title = Label(window,text='Student Registration Form',font=('Algerian',17,'bold'),bg='brown',width=10,height=2)
    title.pack(side=TOP,fill=X)

    todayLabel = Label(window,text='Date:',font=('Times New Roman',13,'bold'),bg='grey')
    todayLabel.place(x=500,y=59)

    global todayEntry
    todayEntry = Entry(window,textvariable=TodayDate,font=('Times New Roman',14))
    todayEntry.place(x=550,y=59,width=120,height=22)
    TodayDate.set(dat)

    frame = LabelFrame(window,text='Student Details',font=('Times New Roman',16,'bold'),bd=2,
                       relief=GROOVE,
                       bg='Lavender',
                       width=650,
                       height=360)
    frame.place(x=20,y=85)

    fname = Label(frame,text='First Name:',font=('Times New Roman',14),bg='Lavender',anchor=W)
    fname.place(x=10,y=20,width=100)

    global fnameField
    fnameField = Entry(frame,font=('Calibri (Body)',13))
    fnameField.place(x=120,y=20,width=150,height=25)

    lname = Label(frame,text='Last Name:',font=('Times New Roman',14),bg='Lavender',anchor=W)
    lname.place(x=300,y=20,width=100)

    global lnameField
    lnameField = Entry(frame,font=('Calibri (Body)',13))
    lnameField.place(x=410, y=20, width=160, height=25)

    admin = Label(frame,text='Reg Number:',font=('Times New Roman',14),bg='Lavender',anchor=W)
    admin.place(x=10,y=80,width=100)

    global adminField
    adminField = Entry(frame,font=('Calibri (Body)',13))
    adminField.place(x=120,y=80,width=150,height=25)

    gender = Label(frame,text='Gender:',font=('Times New Roman',14),bg='Lavender',anchor=W)
    gender.place(x=300,y=80,width=100)

    global maleGender,femaleGender
    maleGender = Radiobutton(frame,text='Male',font=('Times New Roman',10),variable=x,value=0,bg='Lavender')
    maleGender.place(x=380,y=80)
    femaleGender = Radiobutton(frame,text='Female',font=('Times New Roman',10),variable=x,value=1,bg='Lavender')
    femaleGender.place(x=450,y=80)

    school = Label(frame,text='School:',font=('Times New Roman',14),bg='Lavender',anchor=W)
    school.place(x=10,y=140,width=100)

    global schoolField
    schoolField = Entry(frame,font=('Calibri (Body)',13))
    schoolField.place(x=120,y=140,width=150,height=25)

    course = Label(frame,text='Course:',font=('Times New Roman',14),bg='Lavender',anchor=W)
    course.place(x=300,y=140,width=100)

    global courseField
    courseField = Entry(frame,font=('Calibri (Body)',13))
    courseField.place(x=380,y=140,width=190,height=25)

    contact = Label(frame,text='Contact:',font=('Times New Roman',14),bg='Lavender',anchor=W)
    contact.place(x=10,y=200,width=100)

    global contactField
    contactField = Entry(frame,font=('Calibri (Body)',13))
    contactField.place(x=120,y=200,width=150,height=25)

    email = Label(frame,text='Email:',font=('Times New Roman',14),bg='Lavender',anchor=W)
    email.place(x=300,y=200,width=100)

    global emailField
    emailField = Entry(frame,font=('Calibri (Body)',13))
    emailField.place(x=380,y=200,width=190,height=25)

    dob = Label(frame,text='Date Of Birth:',font=('Times New Roman',12),bg='Lavender',anchor=W)
    dob.place(x=10,y=260,width=100)

    global dobField
    dobField = Entry(frame,font=('Times New Roman',13),textvariable=DOBDate)
    dobField.place(x=120,y=260,width=150,height=25)
    DOBDate.set(dat)

    homeTown = Label(frame,text='Home Area:',font=('Times New Roman',14),bg='Lavender',anchor=W)
    homeTown.place(x=300,y=260,width=100)

    global homeField
    homeField = Entry(frame,font=('Calibri (Body)',13))
    homeField.place(x=400,y=260,width=180,height=25)

    inforLabel = Label(window,text="Please Confirm The Details Before Submitting",font=('Times New Roman',14),
                       bg='light grey',fg='red')
    inforLabel.place(x=5,y=450,width=380)


    btn = Button(window,text='Submit',font=('Times New Roman',14),bg='Grey',command=getDetails)
    btn.place(x=500,y=450,width=150)

    # dob = Button(window, text='select date of birth', font=('Times New Roman', 12))
    # dob.place(x=15, y=330, width=200)

    # global cal
    # cal = Calendar(window,selectmode='day',year=2023,month=4,day=22)
    # cal.place(x=135,y=330)


def databaseConnection():

    sql = "INSERT INTO studentdetails(stID,RegNumber,FirstName,LastName,Gender,School,Course,Contact,Email,DOB,Town,RegDate,corID)" \
          " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (int(uniqueNumber),admission,firstName,lastName,gender,school,course,contact,email,dob,home,dat,courseID)
    mycursor.execute(sql,val)

    mydb.commit()

    tkinter.messagebox.showinfo(str(mycursor.rowcount),'Record Inserted Successfully')

    print(mycursor.rowcount, 'record inserted')


studentDetails()

window.mainloop()

