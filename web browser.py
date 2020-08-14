import  tkinter as tk
from tkinter import *
import webbrowser
win = tk.Tk()
win.title('web browser')
win.geometry('675x320')

label0 = Label(win,text = 'GOOGLE',font = ('Arial Bold',50))
label0.grid(row=1,column=0, padx=20,pady=0)
label1 = Label(win,text = 'CHROME',font = ('Arial Bold',50))
label1.grid(row=1,column=1)

def google():
    webbrowser.open('www.google.com')

def crome():
    webbrowser.open('www.chrome.com')
    
igoogle = PhotoImage(file='google.png')
google =  tk.Button(win,image=igoogle,command=google)
google.grid(row=0,column=0)

icrome = PhotoImage(file='crome.png')
crome =  tk.Button(win,image=icrome,command=crome)
crome.grid(row=0,column=1)

win.mainloop()
