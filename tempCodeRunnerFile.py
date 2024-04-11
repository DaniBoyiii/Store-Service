from tkinter import *
from tkinter import messagebox, Label
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import csv

w = Tk()
w.geometry('1500x800')
w.resizable(False, False)
w.title('ACHARYAKULAM Store Service')
'''def about():
    file=open('about.txt','r')
    labout=Label(w,text=file.read())
    labout.pack()
    btnback=Button(w,image=image2,width=75,command=lambda:[btnback.place_forget(),labout.pack_forget(),step1()])
    btnback.place(x=0,y=0)'''
w.wm_iconbitmap('icon.ico')


#w.configure(bg='light blue')


def openaccount(admn):
    members.seek(0)
    stu = list(read_mem)[1:]
    members.seek(0)
    requirement.seek(0)
    for i in stu:
        try:
            if str(i[0]) == str(int(admn)):
                descr = [str(int(admn)), i[1]]
                info = 'Adm. no. : '+i[0]+'\tName : ' + i[1] + '\tClass : ' + i[2]
                content = Label(w, text=info, font='Arial 20 bold')
                content.place(x=400, y=50)
                grade = i[2]
                '''f = opens('class'+grade+'.csv')
                write_val = csv.writer(f[0])
                if f[1] == 0:
                    write_val.writerow(['Admn. no.', 'Name']+items)'''
                req = list(read_req)
                jn = 0
                reqs = dict()
                desc = dict()
                vals = dict()
                for j in req:
                    lj = Label(w, text=j[0]+'.  '+str(j[1]), font='helevetika 16')
                    reqs[jn] = lj
                    if req.index(j) == 0:
                        ld = Label(w, text='  '+str(j[2])+'\t\t'+str(j[3]), font='helevetika 16')
                        ldem = Label(w, text='Your Order', font='helevetika 16')
                    else:
                        ld = Label(w, text='\t'+str(j[2])+'\t\t  '+str(j[3]), font='helevetika 16')
                        maxm = list()
                        for val in range(int(str(j[2]))+1):
                            maxm.append(val)
                        ldem = Combobox(w, width=5, values=maxm, font='helevetika 20')
                        ldem.current(0)
                    vals[jn] = ldem
                    ldem.place(x=640, y=100+jn*50)
                    desc[jn] = ld
                    ld.place(x=800, y=100+jn*50)
                    lj.place(x=340, y=100+jn*50)
                    jn += 1
                btnhome = Button(w, text = "Logout", width=6, font=('arial 18 bold'),
                                 command=lambda: [btnhome.place_forget(), content.place_forget(), forget(reqs),
                                                  forget(desc), forget(vals), btnplace.place_forget(), step1()]) #image=image2, border=2
                btnhome.place(x=0, y=0)
                btnplace = Button(w, text='Place Order', border=2, bg='blue', fg='white', font='helevetika 20',
                                  command=lambda: [btnhome.place_forget(), content.place_forget(), forget(reqs),
                                                   forget(desc), forget(vals), btnplace.place_forget(),
                                                   order(descr, vals, grade, maxm)])
                btnplace.place(x=1100, y=710)
            else:
                continue
        except IndexError:
            continue


def order(info, dic, grade, maxm):
    f = opens('class' + grade + '.csv')
    write_val = csv.writer(f[0])
    f[0].seek(0, 2)
    if f[1] == 0:
        write_val.writerow(['Admn. no.', 'Name'] + items)
    req = list(info)
    for i in range(1, len(dic)):
        req.append(dic[i].get())
    write_val.writerow(req)
    f[0].close()
    messagebox.showinfo('VA Technologies', 'Order Placed and logged out Successfully')
    step1()


def forget(dic):
    for j in range(len(dic)):
        dic[j].place_forget()

        
def checkmember(dob_l, dob_d, dob_m, dob_y, btncontinue, ladmn, lclass, lnamef, lnames, admnentry, classbox, namefentry,
                namesentry, btnback):
    if classbox.get() not in grades:
        messagebox.showerror('VA Technologies', 'Enter valid value for Class')
    elif int(dob_d.get()) not in dates:
        messagebox.showerror('VA Technologies', 'Enter valid value for Date')
    elif dob_m.get() not in months:
        messagebox.showerror('VA Technologies', 'Enter valid value for Month')
    elif int(dob_y.get()) not in years:
        messagebox.showerror('VA Technologies', 'Enter valid value for Year')
    else:
        try:
            admn = int(admnentry.get())
        except ValueError:
            admn = -1
        classentry = classbox.get()
        namef = namefentry.get()
        names = namesentry.get()
        btncontinue.place(x=980, y=650)
        month = (months.index(dob_m.get())) + 1
        if month < 10:
            month = ('0' + str(month))
        dob = str(dob_d.get() + str(month) + dob_y.get())
        if len(names) == 0:
            names = ' '
        members.seek(0)
        iss = []
        flag = False
        for ij in list(read_mem)[1:]:
            iss.append(ij[0])
        try:
            if admn < 1 or admn > 1500:
                messagebox.showinfo('VA Technologies', 'Admission Number is not Valid')
                admnentry.configure(bg='red')
            else:
                for nos in iss:
                    if admn == int(nos):
                        flag = True
                if not flag:
                    if len(namef) == 0:
                        messagebox.showinfo('VA Technologies', 'You can\'t Leave \'Name\' field empty !')
                        namefentry.configure(bg='red')
                    else:
                        dob_l.place_forget()
                        dob_d.place_forget()
                        dob_m.place_forget()
                        dob_y.place_forget()
                        btncontinue.place_forget()
                        ladmn.place_forget()
                        lclass.place_forget()
                        lnamef.place_forget()
                        lnames.place_forget()
                        admnentry.place_forget()
                        classbox.place_forget()
                        namefentry.place_forget()
                        namesentry.place_forget()
                        btnback.place_forget()
                        write_mem.writerow([str(int(admn)), namef + ' ' + names, classentry, dob])
                        members.flush()
                        messagebox.showinfo('VA Technologies', 'Registered Succesfully !')
                        step1()
                else:
                    messagebox.showinfo('VA Technologies', 'This Admission Number is Already Registered !')
                    admnentry.configure(bg='red')
        except ValueError:
            messagebox.showinfo('VA Technologies', 'Please Enter A Valid Number for Admission number!')
            admnentry.configure(bg='red')


def step22():
    btnback = Button(w, image=image2, border=2, width=75,
                     command=lambda: [btnback.place_forget(), usr.place_forget(), usrentry.place_forget(),
                                      btnenter.place_forget(), psd.place_forget(), psdentry.place_forget(), step1()])
    btnback.place(x=0, y=0)
    usr = Label(w, border=5, text='Username (Admn. no.):', font=('Agency FB', 22, ' bold'), fg='black')
    psd = Label(w, border=5, text='Password (DOB in DDMMYYYY):', font=('Agency FB', 22, ' bold'), fg='black')
    usrentry = Entry(w, border=5, font='helevetika 22', fg='blue', bg='light yellow', width=25)
    psdentry = Entry(w, border=5, font='helevetika 22', fg='blue', show='X', bg='light yellow', width=25)
    btnenter = Button(w, image=image3, command=lambda: [logincheck(btnback, usr, usrentry, btnenter, psd, psdentry)])
    usr.place(x=350, y=280)
    psd.place(x=350, y=380)
    usrentry.place(x=650, y=280)
    psdentry.place(x=650, y=380)
    btnenter.place(x=1100, y=380)


def logincheck(btnback, usr, usrentry, btnenter, psd, psdentry):
    members.seek(0)
    adm = 0
    pswd = 0
    stu = list(read_mem)[1:]
    members.seek(0)
    for i in stu:
        try:
            if int(usrentry.get()) == int(i[0]):
                adm = 1
                if int(psdentry.get()) == int(i[3]):
                    pswd = 1
            else:
                continue
        except ValueError:
            messagebox.showinfo('VA Technologies', 'Username and password shoud be in numeric form!')
        except IndexError:
            continue
    if adm == 1:
        if pswd == 1:
            btnback.place_forget()
            usr.place_forget()
            usrentry.place_forget()
            btnenter.place_forget()
            openaccount(usrentry.get())
            psd.place_forget()
            psdentry.place_forget()
        else:
            messagebox.showinfo('VA Technologies', 'Incorrect Password!')
            psdentry.configure(bg='red')
    else:
        messagebox.showinfo('VA Technologies', 'You are not Registerd yet !')
        usrentry.configure(bg='red')


def step21():
    btnback = Button(w, image=image2, width=75,
                     command=lambda: [btnback.place_forget(), btncontinue.place_forget(), ladmn.place_forget(),
                                      lclass.place_forget(), lnamef.place_forget(), lnames.place_forget(),
                                      admnentry.place_forget(), classbox.place_forget(), namefentry.place_forget(),
                                      namesentry.place_forget(), ldob.place_forget(), dob_d.place_forget(),
                                      dob_m.place_forget(), dob_y.place_forget(), step1()])
    btnback.place(x=0, y=0)
    ladmn = Label(w, text='Admission no. (Username)', font=('arial', 20))
    lnamef = Label(w, text='First name', font=('arial', 20))
    lnames = Label(w, text='Second name', font=('arial', 20))
    lclass = Label(w, text='Class', font=('arial', 20))
    admnentry = Entry(w, fg='blue', bg='light yellow', border=5, font='helevetika 16', width=7)
    classbox = Combobox(w, width=7, values=grades, font='helevetika 20')
    ldob = Label(w, text='Date Of Birth', font='helevetika 20')
    dob_d = Combobox(w, width=2, values=dates, font='helevetika 20')
    dob_m = Combobox(w, width=10, values=months, font='helevetika 20')
    dob_y = Combobox(w, width=4, values=years, font='helevetika 20')
    classbox.current(0)
    dob_d.current(0)
    dob_m.current(0)
    dob_y.current(0)
    w.option_add('*TCombobox*Listbox.font', 20)
    namefentry = Entry(w, fg='blue', bg='light yellow', border=5, font='helevetika 20', width=20)
    namesentry = Entry(w, fg='blue', bg='light yellow', border=5, font='helevetika 20', width=20)
    ladmn.place(x=400, y=100)
    lclass.place(x=400, y=200)
    lnamef.place(x=400, y=300)
    lnames.place(x=400, y=400)
    admnentry.place(x=800, y=100)
    classbox.place(x=800, y=200)
    namefentry.place(x=800, y=300)
    namesentry.place(x=800, y=400)
    ldob.place(x=400, y=500)
    dob_d.place(x=800, y=500)
    dob_m.place(x=860, y=500)
    dob_y.place(x=1050, y=500)
    btncontinue = Button(w, text='Continue', font='arial 18', bg='blue', fg='white', width=10, border=5,
                         command=lambda: [checkmember(ldob, dob_d, dob_m, dob_y, btncontinue, ladmn, lclass, lnamef,
                                                      lnames, admnentry, classbox, namefentry, namesentry, btnback)])
    btncontinue.place(x=980, y=600)


def step1():
    l1 = Label(w, image=image1, bg='light yellow')
    l1.pack(ipadx=1000)
    l2 = Label(w, text='ACHARYAKULAM STORE SERVICE\nWelcomes You', font=('Bradley Hand ITC', 55, ' bold'),
               bg='light yellow', fg='red')
    l2.pack(ipady=20, ipadx=1000, side=TOP)
    body = Label(w, text='', bg='light yellow')
    body.pack(ipadx=900, ipady=200)
    btnlogin = Button(w, text='Login', font=('arial', 20, 'bold'), border=5, bg='blue', fg='white',
                      command=lambda: [l1.pack_forget(), l2.pack_forget(), btnlogin.place_forget(),
                                       btnsignup.place_forget(), body.pack_forget(), step22()])
    btnlogin.place(x=800, y=600)
    btnsignup = Button(w, text='Signup', font=('arial', 20, 'bold'), border=5, bg='blue', fg='white',
                       command=lambda: [l1.pack_forget(), l2.pack_forget(), btnlogin.place_forget(),
                                        btnsignup.place_forget(), body.pack_forget(), step21()])
    btnsignup.place(x=600, y=600)


def opens(a):
    try:
        f = open(a, 'r+', newline='')
        lives = 1
    except FileNotFoundError:
        f = open(a, 'a+', newline='')
        lives = 0
    return f, lives


# __Main__

file = opens('members.csv')
members, exist = file[0], file[1]
file = opens('requirement.csv')
requirement, exist2 = file[0], file[1]
write_mem = csv.writer(members)
members.seek(0)
read_mem = csv.reader(members)
img = Image.open("logo.png")
image1 = ImageTk.PhotoImage(img)
img2 = Image.open('home.jpg')
image2 = ImageTk.PhotoImage(img2)

img3 = Image.open('next.jpg')
image3 = ImageTk.PhotoImage(img3)
img4 = Image.open('background.jpg')
imgback = ImageTk.PhotoImage(img4)
lback = Label(w, image=imgback).place(x=0, y=0)
l3 = Label(w, text='A software by VA Technologies {Anmol & Vilakshan}', font=('Monotype Corsiva', 18, 'bold'),
           bg='orange', fg='black', border=5).pack(fill=X, side='bottom')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
read_req = csv.reader(requirement)
write_req = csv.writer(requirement)
if exist2 == 0:
    write_req.writerow(['Sr no.', 'Item name', 'Maximum Quantity', 'Cost'])
    requirement.flush()
if exist == 0:
    write_mem.writerow(['Admission no.', 'Name', 'Class', 'Date Of Birth'])
    members.flush()
items = list()
for q in list(read_req)[1:]:
    items.append(str(q[1]))
years = []
for year in range(1999, 2020):
    years.append(year)
dates = []
for date in range(1, 31):
    dates.append(date)
grades = ('V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII')
members.seek(0)
requirement.seek(0)
opened = 0
step1()
w.mainloop()
