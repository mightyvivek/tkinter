from tkinter import*
import webbrowser

win=Tk()
win.title('Search Bar')

def bt_on():
    url=entry.get()
    webbrowser.open(url)
    
label= Label(win,text='Enter url: ',font=('arial',14,'bold'))
label.grid(row=0,column=0)
    
entry = Entry(win,width=35)
entry.grid(row=0,column=1)

button =Button(win,text='Search',width = 10,height=1,command=bt_on)
button.grid(row=1,column=1,pady=5)


win.mainloop()
