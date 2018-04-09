from tkinter import *

def icalc(source,side):
    storeobj = Frame(source,borderwidth=4,bd=4,bg='powder blue')
    storeobj.pack(side=side,expand=YES,fill=BOTH)
    return storeobj

def button(source,side,text,command=None):
    storeobj = Button(source,text=text,command=command)
    storeobj.pack(side=side,expand=YES,fill=BOTH)
    return storeobj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font','arial 20 bold')
        self.pack(expand=YES,fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self,relief=GROOVE,textvariable=display,justify='right',bd=30,bg='powder blue').pack(side=TOP,expand=YES,fill=BOTH)
        for clearbut in (['CE'],['C']):
            erase = icalc(self,TOP)
            for ichar in clearbut:
                button(erase,LEFT,ichar,lambda storeobj=display,q=ichar: storeobj.set(''))

        for numbut in ("789/","456*","123-","0.+"):
            functionnum = icalc(self,TOP)
            for iequals in numbut:
                button(functionnum,LEFT,iequals,lambda storeobj=display,q=iequals:storeobj.set(storeobj.get()+q))

        Equalsbutton = icalc(self,TOP)
        for iequals in "=":
            if iequals == '=':
                btniequals = button(Equalsbutton,LEFT,iequals)
                btniequals.bind('<ButtonRelease-1>',lambda e,s=self,storeobj=display:s.calc(storeobj),'+')
            else:
                btniequals = button(Equalsbutton,LEFT,iequals,lambda storeobj=display,s=' %s '%iequals: storeobj.set(storeobj.get()+s))

    def calc(self,display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("Error")

if __name__ == '__main__':
    app().mainloop()
