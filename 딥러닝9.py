import numpy as np
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import winsound
from gtts import gTTS
import playsound
import os
import cv2

cnn=tf.keras.models.load_model("my_cnn_for_deploy.h5")

class_names_en=['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']
class_names_fr=['avion','voiture','oiseau','chatte','biche','chienne','grenouille','jument','navire','un camion']
class_names_de=['Flugzeug','Automobil','Vogel','Katze','Hirsch','Hund','Frosch','Pferd','Schiff','LKW']
class_names_ko=['비행기', '자동차', '새', '고양이', '사슴', '개', '개구리', '말', '배', '트럭']

class_id=0
tk_img=''

def process_image():
    global class_id, tk_img

    fname=filedialog.askopenfilename() # 사용자가 폴더에서 영상을 선택하게 함
    img=Image.open(fname)
    tk_img=img.resize([128,128])
    tk_img=ImageTk.PhotoImage(tk_img)
    canvas.create_image((canvas.winfo_width()/2,canvas.winfo_height()/2),image=tk_img,anchor='center')

    x_test=[]
    x=np.asarray(img.resize([32,32]))/255.0
    x_test.append(x)
    x_test=np.asarray(x_test)
    res=cnn.predict(x_test)
    class_id=np.argmax(res)
    label_en['text']='영어: '+class_names_en[class_id]
    label_fr['text']='프랑스어: '+class_names_fr[class_id]
    label_de['text']='독일어: '+class_names_de[class_id]
    label_ko['text']='한국어: '+class_names_ko[class_id]
    winsound.Beep(frequency=500,duration=250)

def tts_english():
    tts=gTTS(text=class_names_en[class_id],lang='en')
    if os.path.isfile('word.mp3'): os.remove('word.mp3')
    tts.save('word.mp3')
    playsound.playsound('word.mp3',True)

def tts_french():
    tts=gTTS(text=class_names_fr[class_id],lang='fr')
    if os.path.isfile('word.mp3'): os.remove('word.mp3')
    tts.save('word.mp3')
    playsound.playsound('word.mp3',True)

def tts_deutsch():
    tts=gTTS(text=class_names_de[class_id],lang='de')
    if os.path.isfile('word.mp3'): os.remove('word.mp3')
    tts.save('word.mp3')
    playsound.playsound('word.mp3',True)
    
def tts_korea():
    tts=gTTS(text=class_names_ko[class_id],lang='ko')
    if os.path.isfile('word.mp3'): os.remove('word.mp3')
    tts.save('word.mp3')
    playsound.playsound('word.mp3',True)

def quit_program():
    win.destroy()

win=tk.Tk()
win.title('다국어 단어 공부_2270005_권지현')
win.geometry('512x500')

process_button=tk.Button(win,text='영상 선택',command=process_image)
quit_button=tk.Button(win,text='끝내기',command=quit_program)
canvas=tk.Canvas(win,width=256,height=256,bg='cyan',bd=4)
label_en=tk.Label(win,width=16,height=1,bg='yellow',bd=4,text='영어',anchor='w')
label_fr=tk.Label(win,width=16,height=1,bg='yellow',bd=4,text='프랑스어',anchor='w')
label_de=tk.Label(win,width=16,height=1,bg='yellow',bd=4,text='독일어',anchor='w')
label_ko=tk.Label(win,width=16,height=1,bg='yellow',bd=4,text='한국어',anchor='w')
tts_en=tk.Button(win,text='듣기',command=tts_english)
tts_fr=tk.Button(win,text='듣기',command=tts_french)
tts_de=tk.Button(win,text='듣기',command=tts_deutsch)
tts_ko=tk.Button(win,text='듣기',command=tts_korea)

process_button.grid(row=0,column=0)
quit_button.grid(row=1,column=0)
canvas.grid(row=0,column=1)
label_en.grid(row=1,column=1,sticky='e')
label_fr.grid(row=2,column=1,sticky='e')
label_de.grid(row=3,column=1,sticky='e')
label_ko.grid(row=4,column=1,sticky='e')
tts_en.grid(row=1,column=2,sticky='w')
tts_fr.grid(row=2,column=2,sticky='w')
tts_de.grid(row=3,column=2,sticky='w')
tts_ko.grid(row=4,column=2,sticky='w')

win.mainloop()