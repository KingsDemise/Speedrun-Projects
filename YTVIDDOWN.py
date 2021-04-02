import tkinter as tk
import pytube
from pytube import YouTube
from tkinter import *
root=Tk()
root.geometry('500x300')
root.resizable(0,1)
root.title("EZ YouTube Video Downloader by K13")
Label(root,text='Youtube Video Downloader',font='"Billy Ohio" 25 bold').pack()
link = StringVar()
Label(root,text='PASTE LINK HERE',font='Futura 15 bold italic').place(x= 160,y=60)
link_enter=Entry(root, width=70,textvariable=link).place(x=32,y=90)
def Downloader():     
    url=YouTube(str(link.get()))
    video=url.streams.filter(progressive=True,res="720p").first()
    video.download()
    Label(root,text='Done!', font = 'Futura 15 bold italic').place(x=200,y=210)  

Button(root,text='DOWNLOAD <3', font='Futura 15 bold italic',bg='#a83eb8',padx=2,command=Downloader).place(x=160,y=150)

root.mainloop()
