from tkinter import*

firstnum=secondnum=None

def operator(op):
    global firstnum,operate
    firstnum=int(lb['text'])
    operate=op
    lb.config(text='')

    
def get(digit):
    current=lb['text']
    new=current+str(digit)
    lb.config(text=new)

def point(dig):
    current=lb['text']
    new=current+(dig)
    lb.config(text=new)

def clear():
    lb.config(text='')

def result():
    global firstnum,secondnum,operate
    secondnum=int(lb['text'])

    if (operate=="+"):
        lb.config(text=str(firstnum + secondnum))
    elif (operate=="-"):
        lb.config(text=str(firstnum - secondnum))
    elif (operate=="*"):
        lb.config(text=str(firstnum * secondnum))
    else:
        if (secondnum==0):
            lb.config(text='error')
        else:
            lb.config(text=str(round(firstnum / secondnum,2)))
win=Tk()
win.geometry('380x480')
win.title('calculator')
win['bg']='black'

lb=Label(win,text='',font='ariel 40 bold',bg='black',fg='white')
lb.grid(column=0,row=0,pady=60,padx=10,columnspan=15)

btn7=Button(win,text='7',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(7))
btn7.grid(column=0,row=1)

btn8=Button(win,text='8',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(8))
btn8.grid(column=1,row=1)

btn9=Button(win,text='9',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(9))
btn9.grid(column=2,row=1)

btnadd=Button(win,text='+',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :operator("+"))    
btnadd.grid(column=3,row=1)

btn4=Button(win,text='4',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(4))
btn4.grid(column=0,row=2)

btn5=Button(win,text='5',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(5))
btn5.grid(column=1,row=2)

btn6=Button(win,text='6',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(6))
btn6.grid(column=2,row=2)

btnsub=Button(win,text='-',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :operator("-"))
btnsub.grid(column=3,row=2)

btn1=Button(win,text='1',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(1))
btn1.grid(column=0,row=3)

btn2=Button(win,text='2',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(2))
btn2.grid(column=1,row=3)

btn3=Button(win,text='3',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(3))
btn3.grid(column=2,row=3)

btnmul=Button(win,text='*',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :operator("*"))
btnmul.grid(column=3,row=3)

btnc=Button(win,text='C',font='ariel 20 bold',bg='black',fg='white',width=5,command=clear)
btnc.grid(column=0,row=4)

btn0=Button(win,text='0',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :get(0))
btn0.grid(column=1,row=4)

btnp=Button(win,text='.',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :point("."))
btnp.grid(column=2,row=4)

btndiv=Button(win,text='/',font='ariel 20 bold',bg='black',fg='white',width=5,command=lambda :operator("/"))
btndiv.grid(column=3,row=4)

btneq=Button(win,text='=',font='ariel 20 bold',bg='black',fg='white',width=15,command=result)
btneq.grid(column=0,row=5,ipady=5,columnspan=5)


win.mainloop()
