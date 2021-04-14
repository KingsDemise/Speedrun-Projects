from tkinter import *
import tkinter.font as font
calc=Tk()
calc.geometry("350x350")
calc.resizable(0,0)
calc.title("Calcy")
calc.configure(bg="#fcec0c")
def clck(item):
    global exp
    exp=exp+str(item)
    input_text.set(exp)
def clr(): 
    global exp 
    exp="" 
    input_text.set("")
def res():
    global exp
    result=str(eval(exp))
    input_text.set(result)
    exp="" 
exp=""
input_text=StringVar()
input_frame=Frame(calc,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=2) 
input_frame.pack(side=TOP)
input_field=Entry(input_frame,font=('Nexa Light',18,'bold'),textvariable=input_text,width=50,bg="#fcec0c",fg="#136377",bd=0,justify=RIGHT) 
input_field.grid(row=0,column=0) 
input_field.pack(ipady=10) 
btns_frame=Frame(calc,width=312,height=272.5,bg="grey") 
btns_frame.pack()
clear=Button(btns_frame,text="C",fg="#136377",width=32,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clr()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide=Button(btns_frame,text="/",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck("/")).grid(row=0,column=3,padx=1,pady=1)
seven=Button(btns_frame,text="7",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(7)).grid(row=1,column=0,padx=1,pady=1)
eight=Button(btns_frame,text="8",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(8)).grid(row=1,column=1,padx=1,pady=1)
nine=Button(btns_frame,text="9",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(9)).grid(row=1,column=2,padx=1,pady=1)
multiply=Button(btns_frame,text="*",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck("*")).grid(row=1,column=3,padx=1,pady=1)
four=Button(btns_frame,text="4",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(4)).grid(row=2,column=0,padx=1,pady=1)
five=Button(btns_frame,text="5",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(5)).grid(row=2,column=1,padx=1,pady=1)
six=Button(btns_frame,text="6",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(6)).grid(row=2,column=2,padx=1,pady=1)
minus=Button(btns_frame,text="-",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck("-")).grid(row=2,column=3,padx=1,pady=1)
one=Button(btns_frame,text="1",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(1)).grid(row=3,column=0,padx=1,pady=1)
two=Button(btns_frame,text="2",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(2)).grid(row=3,column=1,padx=1,pady=1)
three=Button(btns_frame,text="3",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(3)).grid(row=3,column=2,padx=1,pady=1)
plus=Button(btns_frame,text="+",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck("+")).grid(row=3,column=3,padx=1,pady=1)
zero=Button(btns_frame,text="0",fg="#136377",width=21,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(0)).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
point=Button(btns_frame,text=".",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:clck(".")).grid(row=4,column=2,padx=1,pady=1)
equals=Button(btns_frame,text="=",fg="#136377",width=10,height=3,bd=0,bg="#fcec0c",cursor="hand2",command=lambda:res()).grid(row=4,column=3,padx=1,pady=1)
calc.mainloop()

