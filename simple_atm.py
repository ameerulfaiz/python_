from email.utils import localtime
from lzma import FILTER_LZMA2
from tkinter import *
from random import randint
import time
import _tkinter
from tkinter.tix import Balloon
from tokenize import String

root = Tk()
root.geometry("900x650")
root.title("ATM MACHINE") #bank of ameerulfaiz_x8841_projectX
root.configure(bg="black")

Tops = Frame(root, bd="white", width=800, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

fl = Frame(root, bg="black", width=300, height=700, relief=SUNKEN)
fl.pack(side=LEFT)

f2 = Frame(root, bg="black", width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lbl1 = Label(Tops,font= ('aria',30, 'bold'), text="ATM MACHICE", fg="Powder Blue", bg="black", bd=10, anchor='w')
lbl1.grid(row=0, column=0)
lbl2 = Label(Tops, ('aria',20, 'bold'), text=localtime,fg="Powder Blue", bg="black", bd=10, anchor='w')
lbl2.grid(row=1, column=0)

number = StringVar()
amount = StringVar()
withd = StringVar()
acca = " "

def bank():
    global acca
    accno = ["0092","27833","78364"]
    account = number.get()
    if account in accno:
        Label.config(text="Registered User")
        bank = {"0092":10000,"27833":20000,"78364":30000}
        balance = bank[account]
        acca = balance
    else:
        Label.config(text+"Non Registered User")

def deposit():
    global acca
    amo = float(amount.get())
    bal = acca+amo
    label3.config(text=("Net Balance:",str(bal)))

def withdrawn():
    global acca
    wd = float(withd.get())
    if acca>=wd:
        ace = acca-wd
        label4.configur(text=("Net Balance :",str(ace)))

    else:
        label4.config(text+"Insufficient Balance")

def bal():
    global acca
    label5.config(text=("Net Balance",str(acca)))

def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")


lbl = Label(fl, font=('aria' ,16, 'bold' ),text="Enter the account number:              ",bg = "black",fg="Powder Blue",bd=10,anchor='w')
lbl.grid(row=0,column=3)
text = Entry(fl,font=('aria',16,'bold'), textvariable=number , bd=6,insertwidth=4,bg="Powder Blue" ,justify='right')
text.grid(row=0,column=4)
label = Label(fl, fg="white", bg = "black",font=( 'aria' ,16, 'bold') )
label.grid(row=1, column=4)
btnsubmit = Button(f2, padx=16, pady=4, bd=10, fg="black",font=('aria',16,'bold'),width=7,text="SUBMIT", bg="Powder Blue", command=bank)
btnsubmit.grid(row=0, column=4)

lblTotal = Label(fl, text="                                          ",fg="white", bg = "black")
lblTotal.grid(row=3,columnspan=10)

lbl = Label(fl, font=( 'aria' ,16, 'bold' ), text="Enter the amount to be deposited:",fg="Powder Blue",bg = "black",bd=10,anchor='w')
lbl.grid(row=4,column=3)
txt = Entry(fl,font=( 'aria' ,16, 'bold' ),textvariable=amount , bd=6,insertwidth=4,bg="Powder Blue" ,justify='right')
txt.grid(row=4,column=4)
label3 = Label(fl, fg="white",bg = "black",font=( 'aria' ,16, 'bold' ) )
label3.grid(row=5, column=4)
btndeposit =Button(f2,padx=16,pady=4, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=7, text="DEPOSIT", bg="Powder Blue", command=deposit)
btndeposit.grid(row=4, column=4)

lblTotal = Label(fl,text="                                          ",fg="white",bg = "black")
lblTotal.grid(row=7,column=10)

lbl = Label(fl, font=( 'aria' ,16, 'bold' ),text="Enter the amount to be withdrawn:",fg="Powder Blue",bg = "black",bd=10,anchor='w')
lbl.grid(row=8,column=3)
txt = Entry(fl,font=( 'aria' ,16, 'bold' ),textvariable=withd , bd=6,insertwidth=4,bg="Powder Blue" ,justify='right')
txt.grid(row=8,column=4)
label4 = Label(fl, fg="white",bg = "black",font=( 'aria' ,16, 'bold' ) )
label4.grid(row=9, column=4)
label5 = Label(fl, fg="white",bg = "black",font=( 'aria' ,16, 'bold' ) )
label5.grid(row=10, column=4)

btnwithdraw =Button(f2,padx=16,pady=4, bd=10 ,fg="black",font=('ariel' ,16, 'bold'),width=7, text="WITHDRAWL", bg="Powder Blue", command=withdrawn)
btnwithdraw.grid(row=8, column=4)
btnbal =Button(f2,padx=16,pady=4, bd=10 ,fg="black",font=('ariel' ,16, 'bold'),width=7, text="BALANCE", bg="Powder Blue",command=bal)
btnbal.grid(row=10,column=4)
btnreset =Button(f2,padx=16,pady=4, bd=10 ,fg="black",font=('ariel' ,16, 'bold'),width=7, text="RESET", bg="Powder Blue",command=reset)
btnreset.grid(row=11,column=4)
btnexit =Button(f2,padx=16,pady=4, bd=10 ,fg="black",font=('ariel' ,16, 'bold'),width=7, text="EXIT", bg="Powder Blue",command=root.destroy)
btnexit.grid(row=12, column=4)




root.mainloop()