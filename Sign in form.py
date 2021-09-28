from tkinter import*

win=Tk()
win.title('SIGN UP')
win.geometry('500x200+0+0')

def lo_in():
    if entry.get()==vivek and entry1.get()==123:
        def bt_on():
            window=Toplevel()
            window.geometry('500x200+0+0')
            label2=Label(window,text='You are signed In!',font=('arial',20,'bold'))
            label2.grid(row=0,column=0,ipadx=100,ipady=30)
            button1=Button(window,text='Close',width=10,command=window.destroy)
            button1.grid(row=1,column=0)
    else:
        def bt_on1():
            window=Toplevel()
            window.geometry('500x200+0+0')
            label0=Label(window,text='Wrong password!',font=('arial',20,'bold'))
            label0.grid(row=0,column=0,ipadx=100,ipady=30)
            button2=Button(window,text='Close',width=10,command=window.destroy)
            button2.grid(row=1,column=0)

label=Label(text='SIGN UP',font=('arial',14,'bold'))
label.grid(row=0,column=1,ipady=10)
label1=Label(text='Enter your user_name:',font=('Arial',8,'bold'))
label1.grid(row=2,column=0,ipadx=10)
label1=Label(text='Enter your user_password:',font=('Arial',8,'bold'))
label1.grid(row=3,column=0,ipadx=10)

entry=Entry(win,width=40)
entry.grid(row=2,column=1,ipady=3,pady=5)
entry1=Entry(win,width=40)
entry1.grid(row=3,column=1,ipady=3,pady=5)

button0=Button(win,text='sign up',width=10,command=lo_in)
button0.grid(row=4,column=1,pady=30)


mainloop()




