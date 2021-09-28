from tkinter import*


win=Tk()
win.title('Calculator')

def click(number):
    global operator
    operator = operator + str(number)
    variable.set(operator)
def clear():
    global operator
    operator = " "
    variable.set(operator)
def result():
        global operator
        operator = str(eval(operator))
        variable.set(operator)
operator = " "
variable = StringVar()
Display = Entry(win, font=('arial',20,'bold'),bd=24,textvariable=variable,justify='right')
Display.grid(columnspan=5)

button7 = Button(win,text='7',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(7))
button7.grid(row=2,column=0)
button8 = Button(win,text='8',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(8))
button8.grid(row=2,column=1)
button9 = Button(win,text='9',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(9))
button9.grid(row=2,column=2)
button6 = Button(win,text='6',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(6))
button6.grid(row=3,column=0)
button5 = Button(win,text='5',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(5))
button5.grid(row=3,column=1)
button4= Button(win,text='4',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(4))
button4.grid(row=3,column=2)
button3 = Button(win,text='3',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(3))
button3.grid(row=4,column=0)
button2 = Button(win,text='2',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(2))
button2.grid(row=4,column=1)
button1 = Button(win,text='1',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(1))
button1.grid(row=4,column=2)
button0 = Button(win,text='0',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(0))
button0.grid(row=5,column=0)
pnt_button = Button(win,text='.',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('.'))
pnt_button.grid(row=5,column=1)
del_button = Button(win,text='C',font=('arial',20,'bold'),bd=5,padx=10,command = clear)
del_button.grid(row=5,column=2)
addbutton = Button(win,text='+',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('+'))
addbutton.grid(row=1,column=0)
subbutton = Button(win,text='-',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('-'))
subbutton.grid(row=1,column=1)
perbutton = Button(win,text='%',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('%'))
perbutton.grid(row=1,column=2)
mulbutton = Button(win,text='*',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click('*'))
mulbutton.grid(row=1,column=3)
rtbutton = Button(win,text='root',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(''))
rtbutton.grid(row=2,column=3)
rbutton = Button(win,text='=',font=('arial',20,'bold'),bd=5,padx=10,command = lambda : click(result))
rbutton.grid(row=3,column=3)

mainloop()
   
