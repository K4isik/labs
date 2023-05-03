# from tkinter.constants import YES
# import tkinter
from tkinter import *
import tkinter
from PIL import ImageTk, Image
from tkinter.constants import CENTER
from pygame import mixer
from tkinter import Tk, font 
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from os import listdir
from os.path import isfile, join
import pygame
current_song=0
mypath=""
current_volume = float(0.5)
onlyfiles=""
mysongs=[]
mypictures=[]
#Функции
def shuffle():
    global mypictures, current_song, panel, img
    img = ImageTk.PhotoImage(Image.open('C:/Users/user/Desktop/progging/python/pictures/{}.png'.format(current_song)).resize((300,300), Image.ANTIALIAS))
    panel = Label(project, image=img)
    panel.place(X=400, y=250, anchor=CENTER)
def current_picture():
    global mypictures, current_song,panel,img
    img = ImageTk.PhotoImage(Image.open('C:/Users/user/Desktop/progging/python/pictures/{}.png'.format(current_song)).resize((300,300), Image.ANTIALIAS))
    panel = Label(project, image = img)
    panel.place(x=400, y=250, anchor=CENTER)

    print('C:/Users/user/Desktop/progging/python/pictures/{}.png'.format(current_song))
    # if current_picture<len(mypictures):
    #     current_picture+=1
    #     current_song+=1
    # else:
    #     current_picture=0
    #     current_song=0
    # try:
    #     # img = str('C:/Users/user/Desktop/python/pictures'+'/'+str(current_song))
    #     # print(img)
    #     img = PhotoImage(file=('C:/Users/user/Desktop/python/pictures/0.png'))
    #     # print(img)
        
        # picture_title_label = Label(project, image=img).pack()
        # picture_title_label.place(x=400, y=300, anchor=CENTER)

    # except Exception as e:
    #     print(e)
    #     song_title_label.config(fg='red', text = 'Error playing music')
    #     btn.place(x=400, y=300, anchor=CENTER)
        

def previous_song():
    global mysongs,current_song,onlyfiles
    if current_song.key == pygame.K_DOWN or current_song.key == pygame.K_LEFT:
        if current_song !=0:
            current_song-=1
        else:
            current_song=len(mysongs)-1
            
        try:
            mixer.init()
            # mixer.music.load(current_song)
            print(mysongs)
            print(current_song)
            mixer.music.load(mysongs[current_song])
            mixer.music.set_volume(current_volume)
            mixer.music.play()
            song_title = onlyfiles[current_song]
            song_title_label.config(text='Now playing:' + str(song_title))
            # volume_label.config(text='Volume :' + str(current_volume))
            current_picture()
        except Exception as e:
            print(e)
            song_title_label.config(fg='red', text = 'Error playing music')
            btn.place(x=400, y=300, anchor=CENTER)


def next_song():
    global mysongs,current_song,onlyfiles
    if current_song<len(mysongs)-1:
        current_song+=1
    else:
        current_song=0
    try:
        mixer.init()
        # mixer.music.load(current_song)
        print(mysongs)
        print(current_song)
        mixer.music.load(mysongs[current_song])
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title = onlyfiles[current_song]
        song_title_label.config(text='Now playing:' + str(song_title))
        # volume_label.config(text='Volume :' + str(current_volume))
        current_picture()

    except Exception as e:
        print(e)
        song_title_label.config(fg='red', text = 'Error playing music')
        btn.place(x=400, y=300, anchor=CENTER)
       


def play_song():
    global btn,current_song,mypath,onlyfiles,mysongs
    btn.place(y=-100,x=-500)
    # filename = filedialog.askopenfilename(initialdir='C:/', title = 'Please select a song')
    mypath=filedialog.askdirectory()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    mysongs=[]
    current_song=0
    for music in onlyfiles:
        mysongs.append(mypath+"/"+music)


    # current_song = filename
    song_title = onlyfiles[current_song]
    
    
    try:
        mixer.init()
        # mixer.music.load(current_song)
        mixer.music.load(mysongs[0])
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(text='Now playing:' + str(song_title))
        volume_label.config(text='Volume :' + str(current_volume))
        current_picture()
    except Exception as e:
        print(e)
        song_title_label.config(fg='red', text = 'Error playing music')
        btn.place(x=400, y=300, anchor=CENTER)
       

def stop_music():
    mixer.music.pause()
   
def resume_music():
    mixer.music.unpause()

def volume_up():
    try:
        global current_volume
        if current_volume>=1:
            volume_label.config(text='Volume : Max')
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(text='Volume:' +str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(text="Track hasn't been selected yet")


def volume_down():
    try:
        global current_volume
        if current_volume<=0:
            volume_label.config(text='Volume : Muted')
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(text='Volume:'+str(current_volume))
        # loudness_bar_label.config((current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(text="Track hasn't been selected yet")

#Главный экран
project = Tk()
project['bg']='#a60d3b'
project.title('Music Player')
project.geometry('800x600')


#Заголовки
name_label = Label(project, bg='#e6493e', fg='white', text='Kaisar Music', font=('Harrier Bold Expanded', 32))
name_label.place(x=400, y=50, anchor=CENTER)

# loudness_bar_label=Label(project, fg='red')
# loudness_bar_label.place(x=400, y=550, anchor=CENTER)

song_title_label = Label(project, bg='#a60d3b', fg='white', font=('Agency FB',14))
song_title_label.place(x=400, y=500, anchor=CENTER)

volume_label = Label(project, bg='#a60d3b', fg='white', font=('Agency FB', 14))
volume_label.place(x=400, y=550, anchor=CENTER)

# #Кнопки
img = ImageTk.PhotoImage(Image.open('C:/Users/user/Desktop/progging/python/pictures/0.png').resize((300,200), Image.ANTIALIAS))
panel = Label(project, image = img)
# panel.place(x=400, y=200, anchor=CENTER)

btn = Button(project, text='Select song', bg='#de6712', fg='white', font=('Agency FB', 12), command=play_song)
btn.place(x=400, y=300, anchor=CENTER)

pause_btn = Button(project, text='Pause', bg='#de6712', fg='white', font=('agency FB', 12), command=stop_music)
pause_btn.place(x=300, y=450, anchor=CENTER)

resume_btn = Button(project, text='Resume', bg='#de6712', fg='white', font=('agency FB', 12), command=resume_music)
resume_btn.place(x=500, y=450, anchor=CENTER)

volume_down_btn = Button(project, text='-', bg='#de6712', fg='white', font=('agency FB', 12), command=volume_down)
volume_down_btn.place(x=200, y=550, anchor=CENTER)

volume_up_btn = Button(project, text='+', bg='#de6712', fg='white', font=('agency FB', 12), command=volume_up)
volume_up_btn.place(x=600, y=550, anchor=CENTER)

next_music_btn = Button(project, text='NEXT', bg='#de6712', fg='white', font=('Agency FB', 12), command=next_song)
next_music_btn.place(x=600, y=300, anchor=CENTER)

previous_music_btn = Button(project, text='PREV', bg='#de6712', fg='white', font=('Agency FB', 12), command=previous_song)
previous_music_btn.place(x=200, y=300, anchor=CENTER)

project.mainloop()