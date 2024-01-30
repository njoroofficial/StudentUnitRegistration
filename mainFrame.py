from tkinter import *
import tkinter.messagebox
# SQL
import mysql.connector


# the login frame class
class MainData():

    root = Tk()
    root.geometry("400x300")
    root.title('Student Login')
    root.config(bg='light grey')


    def frame(self):

        panel = LabelFrame(maindata.root, text='Student Login',
                           font=('Times New Roman', 14, 'bold'),
                           bd=2, relief=GROOVE,
                           bg='Lavender',
                           width=380,
                           height=280)
        panel.place(x=10, y=10)

        email = Label(panel, text='Email:', font=('Times New Roman', 14, 'bold'), anchor=W, bg='Lavender', fg='Indigo')
        email.place(x=20,y=50,width=100)

        global emailEntry
        emailEntry = Entry(panel, font=('Aerial', 14, 'bold'))
        emailEntry.place(x=140,y=50,width=230,height=30)

        password = Label(panel, text='Password:', font=('Times New Roman', 14, 'bold'), anchor=W, bg='Lavender',
                         fg='Indigo')
        password.place(x=20,y=130,width=100)

        global passwordEntry
        passwordEntry = Entry(panel, font=('Aerial', 14, 'bold'))
        passwordEntry.place(x=140,y=130,width=230,height=30)

        registerbtn = Button(panel, text='Register',
                             fg='black', bg='#708090',
                             font=('Times New Roman', 14),
                             command=maindata.callClass)
        registerbtn.place(x=30, y=200, width=150)

        Loginbtn = Button(panel, text='Login',
                          bg='#708090', fg='blue',
                          font=('Times New Roman', 14),
                          command=database.databaseRetrieve)
        Loginbtn.place(x=200, y=200, width=150)

        maindata.root.mainloop()

        # when register button is clicked
    def callClass(self):

        maindata.root.destroy()
        import registerFrame as rf
        rf.studentDetails()

    def callMainDetails(self):
        maindetails.displayDetails()


# the database class
class dataBase():

    dictStore = {'id': None,
                 'admin': None,
                 'fname': None,
                 'lname': None,
                 'gender': None,
                 'school': None,
                 'course': None,
                 'contact': None,
                 'email': None,
                 'dob': None,
                 'home': None,
                 'regDate': None}

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12960',
        port='3306',
        database='studentRecord'
    )

    mycursor = mydb.cursor()

    def databaseRetrieve(self):

        sql = "SELECT Email, RegNumber FROM studentrecord.studentdetails WHERE Email=%s AND RegNumber=%s"
        val = (emailEntry.get(), passwordEntry.get())
        database.mycursor.execute(sql, val)
        # mycursor.fetchall()

        if (emailEntry == "" or passwordEntry == ""):
            tkinter.messagebox.showerror('Error!!', 'Please Fill All The Field')

        if database.mycursor.fetchall():
            tkinter.messagebox.showinfo('Success', 'Successfull Login')
            emailEntry.config(state=DISABLED)
            passwordEntry.config(state=DISABLED)

            maindata.callMainDetails()

        else:
            tkinter.messagebox.showerror('Error!!', 'Wrong Login Information \nPlease Register')


# CLASS WHERE THE STUDENT DETAILS ARE DISPLAYED
class MainDetails(MainData,dataBase):


    def displayDetails(self):

        window = Tk()
        window.geometry('650x515')
        window.config(bg='#c0c0c0')

        sql = "SELECT * FROM studentrecord.studentdetails WHERE Email=%s AND RegNumber=%s"
        val = (emailEntry.get(), passwordEntry.get())
        database.mycursor.execute(sql, val)

        i = 0

        for x in database.mycursor.fetchall():
            for key, values in database.dictStore.items():
                database.dictStore.update({key: x[i]})
                i = i + 1

        global schoolName

        schoolName = database.dictStore.get('school')
        fullName = database.dictStore.get('fname')+" "+database.dictStore.get('lname')
        admin = database.dictStore.get('admin')
        courseName = database.dictStore.get('course')
        emailInfor = database.dictStore.get('email')
        contactInfor = database.dictStore.get('contact')
        dob = database.dictStore.get('dob')
        home = database.dictStore.get('home')
        regdate = database.dictStore.get('regDate')


        title = Label(window, text='STUDENT PORTAL', font=('Rockwell', 16, 'bold'),bg='brown',width=10,height=2)
        title.pack(side=TOP,fill=X)

        panel = LabelFrame(window, text='Personal Details', font=('Times New Roman', 14), borderwidth=5, relief=GROOVE)
        panel.place(x=50, y=70, width=550, height=370)

        nameLabel = Label(panel, text='Name:', font=('Times New Roman', 14,'bold'), anchor=W,fg='#dc143c')
        nameLabel.place(x=5, y=10,width=90)

        name = Label(panel,text=""+str(fullName),font=('Times New Roman', 14),anchor=W)
        name.place(x=70,y=10)

        adminLabel = Label(panel,text='Admin:',font=('Times New Roman', 14,'bold'), anchor=W,fg='#dc143c')
        adminLabel.place(x=260,y=10)

        admin = Label(panel,text=""+str(admin),font=('Times New Roman', 14), anchor=W)
        admin.place(x=350,y=10)

        schoolLabel = Label(panel, text='School:', font=('Times New Roman', 14, 'bold'), anchor=W, fg='#dc143c')
        schoolLabel.place(x=5, y=70, width=90)

        school = Label(panel, text="" + str(schoolName), font=('Times New Roman', 14), anchor=W)
        school.place(x=70, y=70)

        courseLabel = Label(panel, text='Course:', font=('Times New Roman', 14, 'bold'), anchor=W, fg='#dc143c')
        courseLabel.place(x=260, y=70, width=90)

        course = Label(panel, text="" + str(courseName), font=('Times New Roman', 14), anchor=W)
        course.place(x=350, y=70)

        emailLabel = Label(panel, text='Email:', font=('Times New Roman', 14, 'bold'), anchor=W, fg='#dc143c')
        emailLabel.place(x=5, y=130, width=90)

        email = Label(panel, text="" + str(emailInfor), font=('Times New Roman', 14), anchor=W)
        email.place(x=70, y=130)

        contactLabel = Label(panel, text='Contact:', font=('Times New Roman', 14, 'bold'), anchor=W, fg='#dc143c')
        contactLabel.place(x=260, y=130, width=90)

        contact = Label(panel, text="" + str(contactInfor), font=('Times New Roman', 14), anchor=W)
        contact.place(x=350, y=130)

        dobLabel = Label(panel, text='DOB:', font=('Times New Roman', 14, 'bold'), anchor=W, fg='#dc143c')
        dobLabel.place(x=5, y=200, width=90)

        dob = Label(panel, text="" + str(dob), font=('Times New Roman', 14), anchor=W)
        dob.place(x=70, y=200)

        homeLabel = Label(panel, text='Home:', font=('Times New Roman', 14, 'bold'), anchor=W, fg='#dc143c')
        homeLabel.place(x=260, y=200, width=90)

        homeArea = Label(panel, text="" + str(home), font=('Times New Roman', 14), anchor=W)
        homeArea.place(x=350, y=200)

        regDateLabel = Label(panel, text='RegDate:', font=('Times New Roman', 14, 'bold'), anchor=W, fg='#dc143c')
        regDateLabel.place(x=5, y=270, width=140)

        regDate = Label(panel, text="" + str(regdate), font=('Times New Roman', 14), anchor=W)
        regDate.place(x=100, y=270)

        unitBtn = Button(window,text='RegUnits',bg='#708090',fg='blue',
                         font=('Times New Roman',14),command=unitregistrationclass.unitregistration_Frame)
        unitBtn.place(x=300,y=450)

        maindata.root.destroy()

        window.mainloop()

    def callUnitClass(self):

        unitregistrationclass.unitregistration_Frame()


# another class for Unit Registration

class UnitRegistration_Class(MainDetails,dataBase):

    def unitregistration_Frame(self):

        window = Tk()
        window.geometry('580x520')
        window.config(bg='#c0c0c0')

        # GETTING STUDENT DETAILS
        schoolName = database.dictStore.get('school')
        admin = database.dictStore.get('admin')
        courseName = database.dictStore.get('course')
        department = None
        if (courseName == 'Computer Science' or courseName == 'Information Technology'):
            department = 'CIT'
        elif (courseName == 'Pharmacy' or courseName == 'Biochemestry' or courseName == 'Nursing'):
            department = 'Pharmacy'
        elif (courseName == 'Neurosergion'):
            department = 'Sergical'
        elif (courseName == 'Law'):
            department = 'Law'
        elif (courseName == 'Statistics'):
            department = 'Mathematics'


        title = Label(window, text='Unit Registration', font=('Times New Roman', 17, 'bold'), bg='#BBEBEA',
                      fg='#941A44', width=10, height=1)
        title.pack(side=TOP, fill=X)

        # admin design
        adminLabel = Label(window, text='Admin:-', font=('Times New Roman', 15, 'bold'), fg='#AD1F35',
                           bg='#c0c0c0',anchor=W)
        adminLabel.place(x=5, y=40)

        admin = Label(window,text=""+str(admin),font=('Times New Roman',16,'bold'),
                      bg='#c0c0c0',
                      anchor=W,
                      fg='#500554')
        admin.place(x=100,y=40)

        # school design
        schoolLabel = Label(window, text='School:-', font=('Times New Roman', 15, 'bold'),
                            bg='#c0c0c0',fg='#AD1F35',anchor=W)
        schoolLabel.place(x=300, y=40)

        school = Label(window,text=""+str(schoolName),font=('Times New Roman',16,'bold'),fg='#500554',
                       bg='#c0c0c0',anchor=W)
        school.place(x=395,y=40)

        # department design
        deptLabel = Label(window, text='Department:-', font=('Times New Roman', 15, 'bold'),
                          fg='#AD1F35', bg='#c0c0c0',anchor=W)
        deptLabel.place(x=5, y=100)

        dept = Label(window, text="" + str(department), font=('Times New Roman', 16, 'bold'),
                      bg='#c0c0c0',fg='#500554',anchor=W)
        dept.place(x=140, y=100)

        # course design
        courseLabel = Label(window, text='Course:-', font=('Times New Roman', 15, 'bold'), fg='#AD1F35',
                            bg='#c0c0c0',anchor=W)
        courseLabel.place(x=300, y=100)

        course = Label(window, text="" + str(courseName), font=('Times New Roman', 16, 'bold'),
                       bg='#c0c0c0',fg='#500554',anchor=W)
        course.place(x=395, y=100)

        # academic year design
        acadYearLabel = Label(window, text='Academic Year:-', font=('Times New Roman', 15, 'bold'), fg='#AD1F35',
                              bg='#c0c0c0',anchor=W)
        acadYearLabel.place(x=5, y=160)

        acadYear = Label(window,text='2023/2024',font=('Times New Roman', 16, 'bold'),
                         bg='#c0c0c0',fg='#500554',anchor=W)
        acadYear.place(x=140, y=160)


        # semester design
        semesterLabel = Label(window, text='Semester:-', font=('Times New Roman', 15, 'bold'),
                              fg='#AD1F35', bg='#c0c0c0',anchor=W)
        semesterLabel.place(x=300, y=160)

        semester = Label(window,text='2',font=('Times New Roman', 16, 'bold'),
                         bg='#c0c0c0',fg='#500554',anchor=W)
        semester.place(x=395, y=160)

        frame = LabelFrame(window, text='Units', font=('Times New Roman', 16, 'bold'), bd=2,
                           relief=GROOVE,
                           bg='#F2E7E9',
                           fg='#000000',
                           width=540,
                           height=250
                           )
        frame.place(x=15, y=210)

        #DATABASE CONNECTION

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12960',
            port='3306',
            database='studentRecord'
        )

        mycursor = mydb.cursor()

        # a list to hold the courses
        course = []

        sql = "SELECT * FROM studentrecord.unittable WHERE courseid IN " \
              "( SELECT courseID FROM studentrecord.coursetable WHERE courseName IN " \
              "( SELECT Course from studentrecord.studentdetails where Course=%s))"

        val = [courseName]
        mycursor.execute(sql,val)

        for x in mycursor.fetchall():
            course.append(x[1])

        # frame details
        unit1_Label = Label(frame, text='Unit 1:',bg='#F2E7E9',font=('Times New Roman', 14, 'bold'),fg='#216663')
        unit1_Label.place(x=5, y=10)

        unit1 = Label(frame,text=""+course[0],bg='#F2E7E9',font=('Times New Roman', 16),fg='#635C09')
        unit1.place(x=70,y=10)

        unit2_Label = Label(frame, text='Unit 2:',bg='#F2E7E9',font=('Times New Roman', 14, 'bold'),fg='#216663')
        unit2_Label.place(x=5, y=60)

        unit2 = Label(frame, text="" + course[1], bg='#F2E7E9',font=('Times New Roman', 16),fg='#635C09')
        unit2.place(x=70, y=60)

        unit3_Label = Label(frame, text='Unit 3:',bg='#F2E7E9',font=('Times New Roman', 14, 'bold'),fg='#216663')
        unit3_Label.place(x=5, y=110)

        unit3 = Label(frame, text="" + course[2], bg='#F2E7E9',font=('Times New Roman', 16),fg='#635C09')
        unit3.place(x=70, y=110)

        unit4_Label = Label(frame, text='Unit 4:',bg='#F2E7E9',font=('Times New Roman', 14, 'bold'),fg='#216663')
        unit4_Label.place(x=5, y=160)

        unit4 = Label(frame, text="" + course[3], bg='#F2E7E9',font=('Times New Roman', 16),fg='#635C09')
        unit4.place(x=70, y=160)

        unit5_Label = Label(frame, text='Unit 5:',bg='#F2E7E9',font=('Times New Roman', 14, 'bold'),fg='#216663')
        unit5_Label.place(x=290, y=10)

        unit5 = Label(frame, text="" + course[4], bg='#F2E7E9',font=('Times New Roman', 16),fg='#635C09')
        unit5.place(x=350, y=10)

        unit6_Label = Label(frame, text='Unit 6:',bg='#F2E7E9',font=('Times New Roman', 14, 'bold'),fg='#216663')
        unit6_Label.place(x=290, y=60)

        unit6 = Label(frame, text="" + course[5], bg='#F2E7E9',font=('Times New Roman', 16),fg='#635C09')
        unit6.place(x=350, y=60)

        unit7_Label = Label(frame, text='Unit 7:',bg='#F2E7E9',font=('Times New Roman', 14, 'bold'),fg='#216663')
        unit7_Label.place(x=290, y=110)

        unit7 = Label(frame, text="" + course[6], bg='#F2E7E9',font=('Times New Roman', 16),fg='#635C09')
        unit7.place(x=350, y=110)

        # file design
        homeBtn = Button(window, text='Submit', font=('Times New Roman', 14))
        homeBtn.place(x=200, y=470)

        window.mainloop()



# creating objects of this classes
maindata = MainData()
database = dataBase()
maindetails = MainDetails()
unitregistrationclass = UnitRegistration_Class()

maindata.frame()
