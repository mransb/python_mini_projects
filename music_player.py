from tkinter  import *
from tkinter.filedialog import askdirectory
import os
import pygame
class MyPlayer:
    def __init__(self):
        frame=Tk()
        frame.geometry("500x500")
        frame.title("MyPlayer")
        self.vr=StringVar()
        songtitle=Label(frame,textvariable=self.vr, font="aerial 14 bold")
        self.play_btn   =Button(frame,text="PLAY",width=5, height=3, font="aerial 14 bold",fg="red",bg="white",command=self.play_func)
        self.pause_btn  =Button(frame,state="disabled",text="PAUSE",width=5, height=3, font="aerial 14 bold",fg="red",bg="white",command=self.pause_func)
        self.stop_btn   =Button(frame,state="disabled",text="STOP",width=5, height=3, font="aerial 14 bold",fg="red",bg="white",command=self.stop_func)
        self.resume_btn  =Button(frame,state="disabled",text="RESUME",width=5, height=3, font="aerial 14 bold",fg="red",bg="white",command=self.resume_func)
        self.song_listbox=Listbox(frame, font="aerial 14 bold",fg="red",bg="white")
        songtitle.pack()
        self.play_btn.pack(fill="x")
        self.pause_btn.pack(fill="x")
        self.stop_btn.pack(fill="x")
        self.resume_btn.pack(fill="x")
        self.song_listbox.pack(fill="both", expand="yes")
        ad=askdirectory()       #opens the open dialog box
        os.chdir(ad)            #changes the current folder to the folder you selected
        all_songs=os.listdir()  #get all the files from the selected folder
        pos=0
        for song in all_songs:
            self.song_listbox.insert(pos,song)
            pos=pos+1
        pygame.init()
        pygame.mixer.init()
    def play_func(self):
        pygame.mixer.music.load(self.song_listbox.get(ACTIVE))
        self.vr.set(self.song_listbox.get(ACTIVE))
        pygame.mixer.music.play()
        self.pause_btn['state']='normal'
        self.stop_btn['state']='normal'
        
    def pause_func(self):
        pygame.mixer.music.pause()
        self.pause_btn['state']='disabled'
        self.resume_btn['state']='normal'
    def stop_func(self):
        pygame.mixer.music.stop()
    def resume_func(self):
        self.pause_btn['state']='normal'
        pygame.mixer.music.unpause()
        self.resume_btn['state']='disabled'
       

MP=MyPlayer()
