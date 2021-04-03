from tkinter import *
import time
import webbrowser
import datetime
root = Tk()
root.configure(background='#bd00ff')
root.geometry("500x300")
from threading import *
def Threading():
    t1=Thread(target=alarm)
    t1.start()
def alarm():
    while 1:
        al_time=f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        curr_time=datetime.datetime.now().strftime("%H:%M:%S")
        if curr_time==al_time:
            Label(root,text='Wake the fuck up, Samurai',font='Cyberpunk 20 bold',fg='#fcec0c',bg='#bd00ff').pack()
            webbrowser.open(str(url.get()))
Label(root,text="Alarm Clock",font=("Cyberpunk 20 bold"),fg='#fcec0c',bg='#bd00ff').pack(pady=10)
Label(root,text="Set Time",font=("Cyberpunk 15 bold"),fg='#fcec0c',bg='#bd00ff').pack()
frame = Frame(root)
frame.pack()
  
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
  
hrs=OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
  
minute=StringVar(root)
minutes=('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
  
mins=OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
  
second=StringVar(root)
seconds=('00','01','02','03','04','05','06','07',
           '08','09','10','11','12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
  
secs=OptionMenu(frame,second,*seconds)
secs.pack(side=LEFT)
Label(root,text='Website Link Here',font='Cyberpunk 15 bold italic',fg='#fcec0c',bg='#bd00ff').pack()
url=StringVar()
url_ent=Entry(root,width=70,textvariable=url).pack()

Button(root,text="Set Alarm",font=("Cyberpunk 15"),fg='#fcec0c',bg='#3a243b',command=Threading).pack(pady=20)
root.mainloop()           
