#Module packages

from tkinter import *
import winsound
from tkinter import font
from PIL import ImageTk,Image
import time
from tkinter import ttk as ttk
import random

#window configuration
tk = Tk()
backg_pic = ImageTk.PhotoImage(Image.open("background.jpg"))
tk.title("Learning is Fun")
w=backg_pic.width()
h=backg_pic.height()
backg_label = Label(tk,image=backg_pic)
backg_label.place(x=0,y=0,relwidth=1,relheight=1)
tk.geometry("712x503")

#Labels and Button configuration
l_font_all=font.Font(family="Comic Sans MS",slant="roman",weight="normal",size=14)
b_font_all=font.Font(family="Open Sans",slant="italic",weight="bold",size=10)
num_font_all = font.Font(family="IrisUPC",slant="italic",weight="bold",size=50)
check_font_all = font.Font(family="Comic Sans MS",slant="roman",weight="bold",size=15)
swap_font_all = font.Font(family="Open Sans",slant="roman",weight="bold",size=20)
def A_sound():
    winsound.PlaySound("audio-alphabet\A.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def B_sound():
    winsound.PlaySound("audio-alphabet\B.wav",winsound.SND_ASYNC|winsound.SND_ALIAS)
def C_sound():
    winsound.PlaySound("audio-alphabet\C.wav",winsound.SND_ASYNC|winsound.SND_ALIAS)
def D_sound():
    winsound.PlaySound("audio-alphabet\D.wav",winsound.SND_ASYNC|winsound.SND_ALIAS)
def E_sound():
    winsound.PlaySound("audio-alphabet\E.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def F_sound():
    winsound.PlaySound("audio-alphabet\F.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def G_sound():
    winsound.PlaySound("audio-alphabet\G.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def H_sound():
    winsound.PlaySound("audio-alphabet\H.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def I_sound():
    winsound.PlaySound("audio-alphabet\I.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def J_sound():
    winsound.PlaySound("audio-alphabet\J.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def K_sound():
    winsound.PlaySound("audio-alphabet\K.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def L_sound():
    winsound.PlaySound("audio-alphabet\L.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def M_sound():
    winsound.PlaySound("audio-alphabet\M.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def N_sound():
    winsound.PlaySound(r"audio-alphabet\N.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def O_sound():
    winsound.PlaySound("audio-alphabet\O.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def P_sound():
    winsound.PlaySound("audio-alphabet\P.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def Q_sound():
    winsound.PlaySound("audio-alphabet\Q.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def R_sound():
    winsound.PlaySound("audio-alphabet\R.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def S_sound():
    winsound.PlaySound("audio-alphabet\S.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def T_sound():
    winsound.PlaySound("audio-alphabet\T.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def U_sound():
    winsound.PlaySound(r"audio-alphabet\U.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def V_sound():
    winsound.PlaySound("audio-alphabet\V.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def W_sound():
    winsound.PlaySound("audio-alphabet\W.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def X_sound():
    winsound.PlaySound("audio-alphabet\X.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def Y_sound():
    winsound.PlaySound("audio-alphabet\Y.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def Z_sound():
    winsound.PlaySound("audio-alphabet\Z.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def zero_sound():
    winsound.PlaySound(r"audio-numbers\0.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def one_sound():
    winsound.PlaySound(r"audio-numbers\1.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def two_sound():
    winsound.PlaySound(r"audio-numbers\2.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def three_sound():
    winsound.PlaySound(r"audio-numbers\3.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def four_sound():
    winsound.PlaySound(r"audio-numbers\4.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def five_sound():
    winsound.PlaySound(r"audio-numbers\5.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def six_sound():
    winsound.PlaySound(r"audio-numbers\6.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def seven_sound():
    winsound.PlaySound(r"audio-numbers\7.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def eight_sound():
    winsound.PlaySound(r"audio-numbers\8.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def nine_sound():
    winsound.PlaySound(r"audio-numbers\9.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_abc():
    winsound.PlaySound(r"Rhymes\abcsong.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_baa():
    winsound.PlaySound(r"Rhymes\Baa_Baa.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_hickory():
    winsound.PlaySound(r"Rhymes\Hickory.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_humpty():
    winsound.PlaySound(r"Rhymes\Humpty_Dumpty.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_incy():
    winsound.PlaySound(r"Rhymes\Incy_Wincy.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_jack():
    winsound.PlaySound(r"Rhymes\Jack_and_Jill.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_london():
    winsound.PlaySound(r"Rhymes\London_Bridge.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_old():
    winsound.PlaySound(r"Rhymes\Old_MC.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_rain():
    winsound.PlaySound(r"Rhymes\Rain_Rain.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
def rhy_twinkle():
    winsound.PlaySound(r"Rhymes\twinkle.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
i=0
def c_swap():
    global frame_10
    global i
    global label_175
    f_color = ["pink","red","yellow","green","black","violet","blue"]
    c_color = ["deep pink","red","DarkGoldenrod1","green","black","purple4","blue"]
    f_choosen = random.choice(f_color)
    c_choosen = random.choice(c_color)
    if i>=1:
        label_175.place_forget()
    label_175 = Label(frame_10,text=f_choosen,bg="white",fg=c_choosen,font=swap_font_all)
    label_175.place(x=85, y=25)
    i+=1

j=[]
sum=0
def g_cal_sub():
    global j
    number = random.randint(0,9)
    label_177 = Label(frame_11,text=str(number),font=swap_font_all,bg="white",fg="black")
    label_177.place(x=20,y=10)
    j.append(number)
def g_cal_ans():
    global sum
    for a in j:
        sum+=a
    entry_2.delete(0,END)
    entry_2.insert(0,sum)












def swap():
    global frame_10
    winsound.PlaySound("btn_snd.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
    mainframe_14 = Toplevel()
    mainframe_14.geometry("800x500")
    mainframe_14.title("Color game")
    mainframe_14.resizable(False,False)
    mainframe_14.config(bg="lawn green")
    frame_10 = Frame(mainframe_14,height=100,width=250,bg="white")
    frame_10.place(x=250,y=100)
    button_68 = Button(mainframe_14,text="NEXT",bg="black",fg="cyan",font=b_font_all,borderwidth=5,relief=RIDGE,height=5,width=15,command=lambda :c_swap())
    button_68.place(x=300,y=350)

def g_cal():
    winsound.PlaySound("btn_snd.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
    global frame_11
    global entry_2
    mainframe_15 = Toplevel()
    mainframe_15.geometry("800x500")
    mainframe_15.resizable(False,False)
    mainframe_15.config(bg="lawn green")
    mainframe_15.title("Mind Cal")
    stat_143 = "Ready to calculate !!!"
    label_176 = Label(mainframe_15,text=stat_143,font=l_font_all,bg="lawn green",fg="black")
    label_176.place(x=10,y=10)
    frame_11 = Frame(mainframe_15,height=50,width=100,bg="white")
    frame_11.place(x=350,y=190)
    button_69 = Button(mainframe_15,text="NEXT",bg="black",fg="lawn green",activebackground="cyan",borderwidth=5,relief=RIDGE,font=b_font_all,command=lambda :g_cal_sub())
    button_69.place(x=350,y=290)
    button_70 = Button(mainframe_15,text="ANSWER",bg="cyan",fg="black",borderwidth=5,relief=RIDGE,activebackground="cyan",font=b_font_all,command=lambda :g_cal_ans(),width=98)

    button_70.place(x=0,y=345)
    entry_2 = Entry(mainframe_15,bg="black",fg="lawn green",font=l_font_all,width=97,borderwidth=5,relief=RIDGE)
    entry_2.place(x=0,y=385)


def g_0():
    entry_3.delete(0,END)
    entry_3.insert(0,0)
def g_1():
    entry_3.delete(0,END)
    entry_3.insert(0,1)
def g_2():
    entry_3.delete(0, END)
    entry_3.insert(0, 2)
def g_3():
    entry_3.delete(0, END)
    entry_3.insert(0, 3)
def g_4():
    entry_3.delete(0, END)
    entry_3.insert(0, 4)
def g_5():
    entry_3.delete(0, END)
    entry_3.insert(0, 5)
def g_6():
    entry_3.delete(0, END)
    entry_3.insert(0, 6)
def g_7():
    entry_3.delete(0, END)
    entry_3.insert(0, 7)
def g_8():
    entry_3.delete(0, END)
    entry_3.insert(0, 8)
def g_9():
    entry_3.delete(0, END)
    entry_3.insert(0, 9)

count=0

def g_start():
    global count
    count=0
    global g_random_number
    g_random_number = random.randint(0,9)


    button_71.config(state=ACTIVE)
    button_72.config(state=ACTIVE)
    button_73.config(state=ACTIVE)
    button_74.config(state=ACTIVE)
    button_75.config(state=ACTIVE)
    button_76.config(state=ACTIVE)
    button_77.config(state=ACTIVE)
    button_78.config(state=ACTIVE)
    button_79.config(state=ACTIVE)
    button_80.config(state=ACTIVE)
    button_81.config(state=ACTIVE)






def g_submit():
    global count
    count+=1
    winsound.PlaySound("btn_snd.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)

    g_answer = entry_3.get()
    if count == 3:
        Label(mainframe_17,text="SORRY !!!YOU DID NOT PREDICT IT CORRECTLY TRY ONCE AGAIN\nBEST OF LUCK                          ").place(x=0,y=0)
        time.sleep(3)
        mainframe_16.destroy()
    if int(g_random_number) == int(g_answer) :
        Label(mainframe_17,text="CORRECT!!!                                                                                       ").place(x=0, y=0)
        time.sleep(3)
        mainframe_16.destroy()
    if int(g_answer) != int(g_random_number):
        if int(g_answer)>int(g_random_number):
            Label(mainframe_17,text="TOO HIGH!!!! TRY AGAIN                                                                               ").place(x=0,y=0)
        elif int(g_answer)<int(g_random_number):
            Label(mainframe_17,text="TOO LOW!!!!! TRY AGAIN                                                                               ").place(x=0,y=0)













def g_guess():
    global entry_3
    global button_71
    global button_72
    global button_73
    global button_74
    global button_75
    global button_76
    global button_77
    global button_78
    global button_79
    global button_80
    global button_81
    global mainframe_17
    global mainframe_16
    winsound.PlaySound("btn_snd.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)


    mainframe_16 = Toplevel()
    mainframe_16.geometry("800x500")
    mainframe_16.resizable(False,False)
    mainframe_16.config(bg="lawn green")
    mainframe_16.title("Guess the Number")
    mainframe_17 = Toplevel()
    mainframe_17.geometry("100x100")
    mainframe_17.title("SCORE")
    stat_144 = "HAI !!!GUESS THE NUMBER BETWEEN 0 TO 9\nYOU HAVE 2 CHANCES GUESS THE NUMBER CORRECTLY"
    label_177 = Label(mainframe_16,text=stat_144,font=l_font_all,bg="lawn green",fg="black")
    label_177.place(x=20,y=30)
    stat_145 = "                                                                                                                                                                                                                                                                                                                                 "
    label_178 = Label(mainframe_16,text=stat_145,bg="black")
    label_178.place(x=0,y=85)
    label_179 = Label(mainframe_16,text=stat_145,bg="black")
    label_179.place(x=0,y=10)
    entry_3 = Entry(mainframe_16,bg="black",fg="lawn green",font=l_font_all,borderwidth=10)
    entry_3.config(width=35)
    entry_3.place(x=155,y=195)
    button_71 = Button(mainframe_16,text="0",relief=SUNKEN,font=b_font_all,borderwidth=7,width=4,height=2,command=lambda :g_0(),state=DISABLED)
    button_72 = Button(mainframe_16, text="1", relief=SUNKEN, font=b_font_all, borderwidth=7,width=4,height=2,command=lambda :g_1(),state=DISABLED)
    button_73 = Button(mainframe_16, text="2", relief=SUNKEN, font=b_font_all, borderwidth=7,width=4,height=2,command=lambda :g_2(),state=DISABLED)
    button_74 = Button(mainframe_16, text="3", relief=SUNKEN, font=b_font_all, borderwidth=7,width=4,height=2,command=lambda :g_3(),state=DISABLED)
    button_75 = Button(mainframe_16, text="4", relief=SUNKEN, font=b_font_all, borderwidth=7,width=4,height=2,command=lambda :g_4(),state=DISABLED)
    button_76 = Button(mainframe_16, text="5", relief=SUNKEN, font=b_font_all, borderwidth=7,width=4,height=2,command=lambda :g_5(),state=DISABLED)
    button_77 = Button(mainframe_16, text="6", relief=SUNKEN, font=b_font_all, borderwidth=7,width=4,height=2,command=lambda :g_6(),state=DISABLED)
    button_78 = Button(mainframe_16, text="7", relief=SUNKEN, font=b_font_all, borderwidth=7,width=4,height=2,command=lambda :g_7(),state=DISABLED)
    button_79 = Button(mainframe_16, text="8", relief=SUNKEN, font=b_font_all, borderwidth=7,width=4,height=2,command=lambda :g_8(),state=DISABLED)
    button_80 = Button(mainframe_16, text="9", relief=SUNKEN, font=b_font_all, borderwidth=7,width=4,height=2,command=lambda :g_9(),state=DISABLED)
    button_71.place(x=195, y=245)
    button_72.place(x=255, y=245)
    button_73.place(x=315, y=245)
    button_74.place(x=375, y=245)
    button_75.place(x=435, y=245)
    button_76.place(x=495, y=245)
    button_77.place(x=255, y=315)
    button_78.place(x=315, y=315)
    button_79.place(x=375, y=315)
    button_80.place(x=435, y=315)
    button_81 = Button(mainframe_16,text="SUBMIT",borderwidth=7,relief=RIDGE,state=DISABLED,command=lambda :g_submit())
    button_81.config(width=20)
    button_81.place(x=275,y=395)
    button_82 = Button(mainframe_16,text="START",borderwidth=7,relief=RIDGE,command=lambda :g_start())
    button_82.config(height=7,width=7)
    button_82.place(x=515,y=355)







def A_F():
    winsound.PlaySound("btn_snd.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    mainframe_2 = Toplevel()
    mainframe_2.geometry("800x500")
    mainframe_2.title("A - F")
    note_0= ttk.Notebook(mainframe_2)
    tab_0 = Frame(note_0,bg="black")
    tab_1 = Frame(note_0,bg="black")
    tab_2 = Frame(note_0,bg="black")
    tab_3 = Frame(note_0,bg="black")
    tab_4 = Frame(note_0,bg="black")
    tab_5 = Frame(note_0,bg="black")
    note_0.add(tab_0, text="Letter-A")
    note_0.add(tab_1, text="Letter-B")
    note_0.add(tab_2, text="Letter-C")
    note_0.add(tab_3, text="Letter-D")
    note_0.add(tab_4, text="Letter-E")
    note_0.add(tab_5, text="Letter-F")
    note_0.pack(fill=BOTH,expand=1)
    #Tab_0
    stat_2 = "Letter A "
    label_3 = Label(tab_0,text=stat_2,font=l_font_all,fg="cyan",bg="black")
    label_3.place(x=400,y=10)
    frame_pic_2 = ImageTk.PhotoImage(Image.open("Letter-A.png"))
    frame_2 = Frame(tab_0,height=260,width=372,border="0")
    label_4 = Label(frame_2,image=frame_pic_2,border="0")
    label_4.image=frame_pic_2
    label_4.pack(expand=1,fill=BOTH)
    frame_2.place(x=540,y=10)
    button_11 = Button(tab_0,height=136,width=136,command=lambda :A_sound(),borderwidth=5,relief=RIDGE)
    pic_1 = ImageTk.PhotoImage(Image.open("Play_Button.png"))
    button_11.config(image=pic_1)
    button_11.image=pic_1
    button_11.place(x=200,y=300)
    stat_3 = "\tSmall letter - a\n\tCapital letter - A"
    stat_4 = "WORDS :\n\t Apple\n\t Aeroplane\n\t Ant"
    label_5 = Label(tab_0,text=stat_3,bg="black",fg="cyan",font=l_font_all)
    label_5.place(x=2,y=60)
    label_6 = Label(tab_0,bg="black",fg="cyan",text=stat_4,font=l_font_all)
    label_6.place(x=2,y=150)
    #Tab_1
    stat_6 = "Letter B "
    label_12 = Label(tab_1, text=stat_6, font=l_font_all, fg="cyan", bg="black")
    label_12.place(x=400, y=10)
    frame_3 = Frame(tab_1,height=263,width=380)
    frame_3.place(x=555,y=0)
    frame_pic_3 = ImageTk.PhotoImage(Image.open("Letter-B.png"))
    label_7 = Label(frame_3,image=frame_pic_3,border="0")
    label_7.image=frame_pic_3
    label_7.pack(fill=BOTH ,expand=1)
    stat_5 = "\tCapital letter - B\n\tSmall letter - b"
    stat_6 = "WORDS\n\tBalloon\n\tBall\n\tBat"
    label_8 = Label(tab_1,text=stat_5,bg="black",fg="cyan",font=l_font_all)
    label_8.place(x=2,y=60)
    label_9 = Label(tab_1,text=stat_6,fg="cyan",bg="black",font=l_font_all)
    label_9.place(x=2,y=150)
    button_12 = Button(tab_1,bg="black",height=136,width=136,command=lambda :B_sound())
    button_12.config(image=pic_1)
    button_12.image = pic_1
    button_12.place(x=200,y=300)
    #tab_2
    stat_7 = "Letter-C"
    pic_2 = ImageTk.PhotoImage(Image.open("Letter-C.png"))
    label_13 = Label(tab_2,image=pic_2,border="0")
    label_13.image=pic_2
    label_13.place(x=556,y=0)
    label_14 = Label(tab_2,text=stat_7,fg="cyan",bg="black",font=l_font_all)
    label_14.place(x=400,y=10)
    stat_8 = "\tCapital Letter - C\n\tSmall Letter - c"
    label_15 = Label(tab_2,text=stat_8,fg="cyan",bg="black",font=l_font_all)
    label_15.place(x=2,y=60)
    stat_9 = "WORDS\n\tCat\n\tCarpet\n\tCalender"
    label_16 = Label(tab_2,text=stat_9,bg="black",fg="cyan",font=l_font_all)
    label_16.place(x=2,y=150)
    button_13 = Button(tab_2,image=pic_1,height=140,width=140,command =lambda :C_sound())
    button_13.config(image=pic_1)
    button_13.place(x=200,y=300)
    #tab_3
    stat_10 = "Letter - D"
    pic_3 = ImageTk.PhotoImage(Image.open("Letter-D.png"))
    label_17 = Label(tab_3,image=pic_3,border="0")
    label_17.image = pic_3
    label_17.place(x=537,y=0)
    label_18 = Label(tab_3,text=stat_10,font=l_font_all,bg="black",fg="cyan")
    label_18.place(x=400,y=10)
    stat_10 = "\tCapital Letter - D\n\tSmall Letter - d"
    label_19 = Label(tab_3,text=stat_10,font=l_font_all,bg="black",fg="cyan")
    label_19.place(x=2,y=60)
    stat_11 = "WORDS\n\tDog\n\tDonkey\n\tDrums"
    label_20 = Label(tab_3,text=stat_11,fg="cyan",bg="black",font=l_font_all)
    label_20.place(x=2,y=150)
    button_14 = Button(tab_3,image=pic_1,height=140,width=140,command = lambda :D_sound())
    button_14.image=pic_1
    button_14.place(x=200,y=300)
    #tab_4
    stat_12 = "Letter - E"
    pic_4 = ImageTk.PhotoImage(Image.open("Letter-E.png"))
    label_21 = Label(tab_4,image=pic_4,border="0")
    label_21.image= pic_4
    label_21.place(x=532,y=0)
    label_22 = Label(tab_4,text=stat_12,font=l_font_all,bg="black",fg="cyan")
    label_22.place(x=400,y=10)
    stat_13 = "Capital letter  - E\nSmall Letter - e"
    label_23 = Label(tab_4,text=stat_13,font=l_font_all,bg="black",fg="cyan")
    label_23.place(x=2,y=60)
    stat_14 = "WORDS - \n\tEgg\n\tEagle\n\tEntry"
    label_24 = Label(tab_4,text=stat_14,bg="black",fg="cyan",font=l_font_all)
    label_24.place(x=2,y=150)
    button_15 = Button(tab_4,image=pic_1,height=140,width=140,command=lambda :E_sound())
    button_15.image = pic_1
    button_15.place(x=200,y=300)
    #tab_5
    stat_15 = "Letter - F"
    pic_5 = ImageTk.PhotoImage(Image.open("Letter-F.png"))
    label_25 = Label(tab_5,image=pic_5,border="0")
    label_25.image = pic_5
    label_25.place(x=535,y=0)
    label_26 = Label(tab_5,text=stat_15,fg="cyan",bg="black",font=l_font_all)
    stat_16 = "Capital Letter - F\nSmall Letter - f"
    label_27 = Label(tab_5,text=stat_16,font=l_font_all,bg="black",fg="cyan")
    label_27.place(x=2,y=60)
    label_26.place(x=400,y=10)
    stat_17 = "WORDS\n\tFlower\n\tFrog\n\tFruits"
    label_28 = Label(tab_5,text=stat_17,font=l_font_all,fg="cyan",bg="black")
    label_28.place(x=2,y=150)
    button_16 = Button(tab_5,image=pic_1,height=140,width=140,command= lambda :F_sound())
    button_16.image=pic_1
    button_16.place(x=200,y=300)
    #resize
    mainframe_2.resizable(False,False)

def G_L():
    winsound.PlaySound("btn_snd.wav",winsound.SND_ASYNC|winsound.SND_ALIAS)
    mainframe_3 = Toplevel()
    mainframe_3.geometry("800x500")
    mainframe_3.title("G - L")
    note_1 = ttk.Notebook(mainframe_3)
    tab_6 = Frame(note_1, bg="black")
    tab_7 = Frame(note_1, bg="black")
    tab_8 = Frame(note_1, bg="black")
    tab_9 = Frame(note_1, bg="black")
    tab_10 = Frame(note_1, bg="black")
    tab_11 = Frame(note_1, bg="black")
    note_1.add(tab_6, text="Letter-G")
    note_1.add(tab_7, text="Letter-H")
    note_1.add(tab_8, text="Letter-I")
    note_1.add(tab_9, text="Letter-J")
    note_1.add(tab_10, text="Letter-K")
    note_1.add(tab_11, text="Letter-L")
    #tab_6
    stat_18 = "Letter - G"
    label_29 = Label(tab_6,text=stat_18,font=l_font_all,fg="cyan",bg="black")
    label_29.place(x=400,y=10)
    pic_6 = ImageTk.PhotoImage(Image.open("Letter-G.png"))
    label_30 = Label(tab_6,image=pic_6,border="0")
    label_30.image = pic_6
    label_30.place(x=527,y=0)
    stat_19 = "Capital Letter - G\nSmall Letter - g"
    label_31 = Label(tab_6,text=stat_19,font=l_font_all,fg="cyan",bg="black")
    label_31.place(x=2,y=60)
    stat_20 = "WORDS :\n\tGoose\n\tGlue\n\tGirl"
    label_32 = Label(tab_6,text=stat_20,font=l_font_all,bg="black",fg="cyan")
    label_32.place(x=2,y=150)
    pic_1 = ImageTk.PhotoImage(Image.open("Play_Button.png"))
    button_17 = Button(tab_6,image=pic_1,command=lambda :G_sound(),height=140,width=140)
    button_17.image = pic_1
    button_17.place(x=200,y=300)
    #tab_7
    stat_21 = "Letter - H"
    label_33 = Label(tab_7,text=stat_21,font=l_font_all,fg="cyan",bg="black")
    label_33.place(x=400,y=10)
    pic_7 = ImageTk.PhotoImage(Image.open("Letter-H.png"))
    stat_22 = "Capital Letter - H\nSmall letter - h"
    label_34 = Label(tab_7,text=stat_22,fg="cyan",bg="black",font=l_font_all)
    label_34.place(x=2,y=60)
    label_35 = Label(tab_7,image=pic_7,border="0")
    label_35.image = pic_7
    label_35.place(x=538,y=0)
    stat_23 = "WORDS:\n\tHat\n\tHead\n\tHorse"
    label_36 = Label(tab_7,text=stat_23,fg="cyan",bg="black",font=l_font_all)
    label_36.place(x=0,y=150)
    button_18 = Button(tab_7,image=pic_1,height=140,width=140,command=lambda :H_sound())
    button_18.image = pic_1
    button_18.place(x=200,y=300)
    #tab_8
    stat_24 = "Letter - I"
    label_37 = Label(tab_8,text=stat_24,fg="cyan",bg="black",font=l_font_all)
    label_37.place(x=400,y=10)
    pic_8 = ImageTk.PhotoImage(Image.open("Letter-I.png"))
    label_38 = Label(tab_8,image=pic_8,border="0")
    label_38.image = pic_8
    label_38.place(x=(800-268),y=0)
    stat_25 = "WORDS:\n\tImage\n\tIce Cream\n\tIce"
    label_39 = Label(tab_8,text=stat_25,font=l_font_all,bg="black",fg="cyan")
    label_39.place(x=0,y=150)
    stat_26 = "Capital Letter - I\nSmall Letter -i"
    label_40 = Label(tab_8,text=stat_26,font=l_font_all,fg="cyan",bg="black")
    label_40.place(x=2,y=60)
    button_19 = Button(tab_8,image=pic_1,height=140,width=140,command=lambda :I_sound())
    button_19.image = pic_1
    button_19.place(x=200,y=300)
    #tab_9
    stat_27 = "Letter  - J"
    label_41 = Label(tab_9,text=stat_27,font=l_font_all,bg="black",fg="cyan")
    label_41.place(x=400,y=10)
    pic_9 = ImageTk.PhotoImage(Image.open("Letter-J.png"))
    label_41 = Label(tab_9,image=pic_9,border="0")
    label_41.image=pic_9
    label_41.place(x=535,y=0)
    stat_28 = "Capital Letter - J\nSmall Letter - j"
    label_42 = Label(tab_9,text=stat_28,font=l_font_all,bg="black",fg="cyan")
    label_42.place(x=2,y=60)
    stat_29 = "WORDS:\n\tJoker\n\tJelly\n\tJam"
    label_43 = Label(tab_9,text=stat_29,font=l_font_all,bg="black",fg="cyan")
    label_43.place(x=0,y=150)
    button_20 = Button(tab_9,image=pic_1,height=140,width=140,command=lambda :J_sound())
    button_20.image = pic_1
    button_20.place(x=200,y=300)

    #tab_10
    stat_30 = "Letter - K"
    label_44 = Label(tab_10,text=stat_30,font=l_font_all,bg="black",fg="cyan")
    label_44.place(x=400,y=10)
    pic_10 = ImageTk.PhotoImage(Image.open("Letter-K.png"))
    label_45 = Label(tab_10,image=pic_10,border="0")
    label_45.image = pic_10
    label_45.place(x=534,y=0)
    stat_31 = "Capital Letter - K\nSmall Letter - k"
    label_46 = Label(tab_10,text=stat_31,bg="black",fg="cyan",font=l_font_all)
    label_46.place(x=2,y=60)
    stat_32 = "WORDS:\n\tKite\n\tKing\n\tkangaroo"
    label_47 = Label(tab_10,text=stat_32,bg="black",fg="cyan",font=l_font_all)
    label_47.place(x=0,y=150)
    button_21 = Button(tab_10,image=pic_1,height=140,width=140,command= lambda :K_sound())
    button_21.place(x=200,y=300)

    #tab_11
    stat_33 = "Letter - L"
    label_48 = Label(tab_11, text=stat_33, font=l_font_all, bg="black", fg="cyan")
    label_48.place(x=400, y=10)
    pic_11 = ImageTk.PhotoImage(Image.open("Letter-L.png"))
    label_49 = Label(tab_11, image=pic_11, border="0")
    label_49.image = pic_11
    label_49.place(x=507, y=0)
    stat_34 = "Capital Letter - L\nSmall Letter - l"
    label_50 = Label(tab_11, text=stat_34, bg="black", fg="cyan", font=l_font_all)
    label_50.place(x=2, y=60)
    stat_35 = "WORDS:\n\tLion\n\tLoyal\n\tLaugh"
    label_51 = Label(tab_11, text=stat_35, bg="black", fg="cyan", font=l_font_all)
    label_51.place(x=0, y=150)
    button_22 = Button(tab_11, image=pic_1, height=140, width=140, command=lambda: L_sound())
    button_22.place(x=200, y=300)
    note_1.pack(fill=BOTH, expand=1)
    mainframe_3.resizable(False, False)


def M_R():
    winsound.PlaySound("btn_snd.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
    mainframe_4 = Toplevel()
    mainframe_4.geometry("800x500")
    mainframe_4.title("M - R")
    mainframe_4.resizable(False,False)
    note_2 = ttk.Notebook(mainframe_4)
    note_2.pack(fill=BOTH, expand=1)
    tab_12 = Frame(note_2, bg="black")
    tab_13 = Frame(note_2, bg="black")
    tab_14 = Frame(note_2, bg="black")
    tab_15 = Frame(note_2, bg="black")
    tab_16 = Frame(note_2, bg="black")
    tab_17 = Frame(note_2, bg="black")
    note_2.add(tab_12, text="Letter-M")
    note_2.add(tab_13, text="Letter-N")
    note_2.add(tab_14, text="Letter-O")
    note_2.add(tab_15, text="Letter-P")
    note_2.add(tab_16, text="Letter-Q")
    note_2.add(tab_17, text="Letter-R")
    #tab_12
    stat_36 = "Letter - M"
    label_52 = Label(tab_12,text=stat_36,font=l_font_all,bg="black",fg="cyan")
    label_52.place(x=400,y=0)
    pic_12 = ImageTk.PhotoImage(Image.open("Letter-M.png"))
    label_53 = Label(tab_12,image=pic_12,border="0")
    label_53.image = pic_12
    label_53.place(x=527,y=0)
    stat_37 = "WORDS:\n\tMonkey\n\tMouse\n\tMayor"
    label_54 = Label(tab_12,text=stat_37,font=l_font_all,bg="black",fg="cyan")
    label_54.place(x=0,y=150)
    stat_38 = "Capital Letter - M\nSmall Letter - m"
    label_55 = Label(tab_12,text=stat_38,fg="cyan",bg="black",font=l_font_all)
    label_55.place(x=2,y=60)
    pic_1 = ImageTk.PhotoImage(Image.open("Play_Button.png"))
    button_23 = Button(tab_12,image=pic_1,height=140,width=140,command = lambda :M_sound())
    button_23.image = pic_1
    button_23.place(x=200,y=300)
    #tab_13
    stat_39 = "Letter - N"
    label_56 = Label(tab_13,text=stat_39,font=l_font_all,bg="black",fg="cyan")
    label_56.place(x=400,y=0)
    pic_13 = ImageTk.PhotoImage(Image.open("Letter-N.png"))
    label_57 = Label(tab_13,image=pic_13,border="0")
    label_57.image = pic_13
    label_57.place(x=526,y=0)
    stat_40 = "Capital Letter - N\nSmall Letter - n"
    label_58 = Label(tab_13,text=stat_40,fg="cyan",bg="black",font=l_font_all)
    label_58.place(x=2,y=60)
    stat_41 = "WORDS :\n\tNest\n\tNuts\n\tNew"
    label_59 = Label(tab_13,text=stat_41,fg="cyan",bg="black",font=l_font_all)
    label_59.place(x=0,y=150)
    button_24 = Button(tab_13,image=pic_1,height=140,width=140,command=lambda :N_sound())
    button_24.place(x=200,y=300)
    #tab_14
    stat_42 = "Letter - O"
    label_60 = Label(tab_14,text=stat_42,font=l_font_all,bg="black",fg="cyan")
    label_60.place(x=400,y=0)
    pic_14 = ImageTk.PhotoImage(Image.open("Letter-O.png"))
    label_61 = Label(tab_14,image=pic_14,border="0")
    label_61.image  = pic_14
    label_61.place(x=537,y=0)
    stat_43 = "Capital Letter - O\nSmall Letter - o"
    label_62 = Label(tab_14,text=stat_43,fg="cyan",bg="black",font=l_font_all)
    label_62.place(x=2,y=60)
    stat_44 = "WORDS:\n\tOrange\n\tOpen]\n\tOctopus"
    label_63 = Label(tab_14,text=stat_44,bg="black",fg="cyan",font=l_font_all)
    label_63.place(x=0,y=150)
    button_25 = Button(tab_14,image=pic_1,height=140,width=140,command=lambda :O_sound())
    button_25.place(x=200,y=300)
    #tab_15
    stat_45 = "Letter - P"
    label_64 = Label(tab_15,text=stat_45,font=l_font_all,bg="black",fg="cyan")
    label_64.place(x=400,y=0)
    pic_15 = ImageTk.PhotoImage(Image.open("Letter-P.png"))
    label_65 = Label(tab_15,image=pic_15,border="0")
    label_65.image=pic_15
    label_65.place(x=534,y=0)
    stat_46 = "Capital Letter - P\nSmall Letter - p"
    label_66 = Label(tab_15,text=stat_46,fg="cyan",bg="black",font=l_font_all)
    label_66.place(x=2,y=60)
    stat_47 = "WORDS:\n\tPrince\n\tPencil\n\tPrincess"
    label_67 = Label(tab_15,text=stat_47,fg="cyan",bg="black",font=l_font_all)
    label_67.place(x=0,y=150)
    button_26 = Button(tab_15,image=pic_1,height=140,width=140,command=lambda :P_sound())
    button_26.image = pic_1
    button_26.place(x=200,y=300)
    #tab_16
    stat_48 = "Letter - Q"
    label_68 = Label(tab_16,text=stat_48,fg="cyan",bg="black",font=l_font_all)
    label_68.place(x=400,y=0)
    pic_16 = ImageTk.PhotoImage(Image.open("Letter-Q.png"))
    label_69 = Label(tab_16,image=pic_16,border="0")
    label_69.image=pic_16
    label_69.place(x=533,y=0)
    stat_49 = "Capital Letter - Q\nSmall Letter - q"
    label_70 = Label(tab_16,text=stat_49,font=l_font_all,bg="black",fg="cyan")
    label_70.place(x=2,y=60)
    stat_50 = "WORDS :\n\tQueen\n\tQuestion\n\tQuack"
    label_71 = Label(tab_16,text=stat_50,fg="cyan",bg="black",font=l_font_all)
    label_71.place(x=0,y=150)
    button_27 = Button(tab_16,image=pic_1,height=140,width=140,command=lambda :Q_sound())
    button_27.place(x=200,y=300)
    #tab_17
    stat_51 = "Letter - R"
    label_72 = Label(tab_17,text=stat_51,fg="cyan",bg="black",font=l_font_all)
    label_72.place(x=400,y=0)
    pic_17 = ImageTk.PhotoImage(Image.open("Letter-R.png"))
    label_73 = Label(tab_17,image=pic_17,border="0")
    label_73.image = pic_17
    label_73.place(x=537,y=0)
    stat_52 = "Capital Letter - R\nSmall Letter - r"
    label_74 = Label(tab_17,text=stat_52,fg="cyan",bg="black",font=l_font_all)
    label_74.place(x=2,y=60)
    stat_53 = "WORDS :\n\tRain\n\tRabbit\n\tRace"
    label_75 = Label(tab_17,text=stat_53,bg="black",fg="cyan",font=l_font_all)
    label_75.place(x=0,y=150)
    button_28 = Button(tab_17,image=pic_1,height=140,width=140,command=lambda :R_sound())
    button_28.image = pic_1
    button_28.place(x=200,y=300)


def S_Z():
    winsound.PlaySound("btn_snd.wav",winsound.SND_ALIAS|winsound.SND_ASYNC)
    mainframe_5 = Toplevel()
    mainframe_5.title("S - Z")
    mainframe_5.geometry("800x500")
    mainframe_5.resizable(False,False)
    note_3 = ttk.Notebook(mainframe_5)
    note_3.pack(fill=BOTH,expand=1)
    tab_18 = Frame(note_3, bg="black")
    tab_19 = Frame(note_3, bg="black")
    tab_20 = Frame(note_3, bg="black")
    tab_21 = Frame(note_3, bg="black")
    tab_22 = Frame(note_3, bg="black")
    tab_23 = Frame(note_3, bg="black")
    tab_24 = Frame(note_3, bg="black")
    tab_25 = Frame(note_3, bg="black")
    note_3.add(tab_18, text="Letter - S")
    note_3.add(tab_19, text="Letter - T")
    note_3.add(tab_20, text="Letter - U")
    note_3.add(tab_21, text="Letter - V")
    note_3.add(tab_22, text="Letter - W")
    note_3.add(tab_23, text="Letter - X")
    note_3.add(tab_24, text="Letter - Y")
    note_3.add(tab_25, text="Letter - Z")
    #tab_18
    stat_54 = "Letter - S"
    label_76 = Label(tab_18,text=stat_54,fg="cyan",bg="black",font=l_font_all)
    label_76.place(x=400,y=0)
    pic_18 = ImageTk.PhotoImage(Image.open("Letter-S.png"))
    label_77 = Label(tab_18,image=pic_18,border="0")
    label_77.image = pic_18
    label_77.place(x=541,y=0)
    stat_55 = "Capital Letter - S\nSmall Letter - s"
    label_78 = Label(tab_18,text=stat_55,fg="cyan",bg="black",font=l_font_all)
    label_78.place(x=2,y=60)
    stat_56 = "WORDS :\n\tSnail\n\tSnake\n\tSeed"
    label_79 = Label(tab_18,text=stat_56,fg="cyan",bg="black",font=l_font_all)
    label_79.place(x=0,y=150)
    pic_1 = ImageTk.PhotoImage(Image.open("Play_Button.png"))
    button_29 = Button(tab_18,image=pic_1,height=140,width=140,command=lambda :S_sound())
    button_29.image = pic_1
    button_29.place(x=200,y=300)
    #tab_19
    stat_57 = "Letter - T"
    label_80 = Label(tab_19,text=stat_57,fg="cyan",bg="black",font=l_font_all)
    label_80.place(x=400,y=0)
    pic_19 = ImageTk.PhotoImage(Image.open("Letter-T.png"))
    label_81 = Label(tab_19,image=pic_19,border="0")
    label_81.image = pic_19
    label_81.place(x=538,y=0)
    stat_58 = "Capital Letter - T\nSmall Letter - t"
    label_82 = Label(tab_19,text=stat_58,fg="cyan",bg="black",font=l_font_all)
    label_82.place(x=2,y=60)
    stat_59 = "WORDS :\n\tTrain\n\tTree\n\tTemperature"
    label_83 = Label(tab_19,text=stat_59,fg="cyan",bg="black",font=l_font_all)
    label_83.place(x=0,y=150)
    button_30 = Button(tab_19,image=pic_1,height=140,width=140,command=lambda :T_sound())
    button_30.image = pic_1
    button_30.place(x=200,y=300)
    #tab_20
    stat_60 = "Letter - U"
    label_84 = Label(tab_20,text=stat_60,fg="cyan",bg="black",font=l_font_all)
    label_84.place(x=400,y=0)
    pic_20 = ImageTk.PhotoImage(Image.open("Letter-U.png"))
    label_85 = Label(tab_20,image=pic_20,border="0")
    label_85.image = pic_20
    label_85.place(x=554,y=0)
    stat_61 = "Capital Letter - U\nSmall Letter - u"
    label_86 = Label(tab_20,text=stat_61,fg="cyan",bg="black",font=l_font_all)
    label_86.place(x=2,y=60)
    stat_62 = "WORDS :\n\tUmbrella\n\tUncle\n\tUgly"
    label_87 = Label(tab_20,text=stat_62,fg="cyan",bg="black",font=l_font_all)
    label_87.place(x=0,y=150)
    button_31 = Button(tab_20,image=pic_1,height=140,width=140,command=lambda :U_sound())
    button_31.image = pic_1
    button_31.place(x=200,y=300)
    #tab_21
    stat_63 = "Letter - V"
    label_88 = Label(tab_21,text=stat_63,fg="cyan",bg="black",font=l_font_all)
    label_88.place(x=400,y=0)
    pic_21 = ImageTk.PhotoImage(Image.open("Letter-V.png"))
    label_89 = Label(tab_21,image=pic_21,border="0")
    label_89.image = pic_21
    label_89.place(x=579,y=0)
    stat_64 = "Capital Letter - V\nSmall Letter - v"
    label_90 = Label(tab_21,text=stat_64,fg="cyan",bg="black",font=l_font_all)
    label_90.place(x=2,y=60)
    stat_65 = "WORDS :\n\tViolin\n\tVacation\n\tVan"
    label_91 = Label(tab_21,text=stat_65,fg="cyan",bg="black",font=l_font_all)
    label_91.place(x=0,y=150)
    button_32 = Button(tab_21,image=pic_1,height=140,width=140,command=lambda :V_sound())
    button_32.image = pic_1
    button_32.place(x=200,y=300)
    #tab_22
    stat_66 = "Letter - W"
    label_92 = Label(tab_22,text=stat_66,fg="cyan",bg="black",font=l_font_all)
    label_92.place(x=400,y=0)
    pic_22 = ImageTk.PhotoImage(Image.open("Letter-W.png"))
    label_93 = Label(tab_22,image=pic_22,border="0")
    label_93.image = pic_22
    label_93.place(x=576,y=0)
    stat_67 = "Capital Letter - W\nSmall Letter - w"
    label_94 = Label(tab_22,text=stat_67,fg="cyan",bg="black",font=l_font_all)
    label_94.place(x=2,y=60)
    stat_68 = "WORDS :\n\tWater\n\tWhale\n\tWhite"
    label_95 = Label(tab_22,text=stat_68,fg="cyan",bg="black",font=l_font_all)
    label_95.place(x=0,y=150)
    button_33 = Button(tab_22,image=pic_1,height=140,width=140,command=lambda :W_sound())
    button_33.image = pic_1
    button_33.place(x=200,y=300)
    #tab_23
    stat_69 = "Letter - X"
    label_96 = Label(tab_23,text=stat_69,fg="cyan",bg="black",font=l_font_all)
    label_96.place(x=400,y=0)
    pic_23 = ImageTk.PhotoImage(Image.open("Letter-X.png"))
    label_97 = Label(tab_23,image=pic_23,border="0")
    label_97.image = pic_23
    label_97.place(x=539,y=0)
    stat_70 = "Capital Letter - X\nSmall Letter - x"
    label_98 = Label(tab_23,text=stat_70,fg="cyan",bg="black",font=l_font_all)
    label_98.place(x=2,y=60)
    stat_71 = "WORDS :\n\tXylophone\n\tXmas\n\tXerox"
    label_99 = Label(tab_23,text=stat_71,fg="cyan",bg="black",font=l_font_all)
    label_99.place(x=0,y=150)
    button_34 = Button(tab_23,image=pic_1,height=140,width=140,command=lambda :X_sound())
    button_34.image = pic_1
    button_34.place(x=200,y=300)
    #tab_24
    stat_72 = "Letter - Y"
    label_100 = Label(tab_24,text=stat_72,fg="cyan",bg="black",font=l_font_all)
    label_100.place(x=400,y=0)
    pic_24 = ImageTk.PhotoImage(Image.open("Letter-Y.png"))
    label_101 = Label(tab_24,image=pic_24,border="0")
    label_101.image = pic_24
    label_101.place(x=536,y=0)
    stat_73 = "Capital Letter - Y\nSmall Letter - y"
    label_102 = Label(tab_24,text=stat_73,fg="cyan",bg="black",font=l_font_all)
    label_102.place(x=2,y=60)
    stat_74 = "WORDS :\n\tYacht\n\tYarn\n\tYak"
    label_103 = Label(tab_24,text=stat_74,fg="cyan",bg="black",font=l_font_all)
    label_103.place(x=0,y=150)
    button_35 = Button(tab_24,image=pic_1,height=140,width=140,command=lambda :Y_sound())
    button_35.image = pic_1
    button_35.place(x=200,y=300)
    #tab_25
    stat_75 = "Letter - Z"
    label_104 = Label(tab_25,text=stat_75,fg="cyan",bg="black",font=l_font_all)
    label_104.place(x=400,y=0)
    stat_76 = "Capital Letter - Z\nSmall Letter - z"
    label_105 = Label(tab_25,text=stat_76,fg="cyan",bg="black",font=l_font_all)
    label_105.place(x=2,y=60)
    stat_77 = "WORDS :\n\tZebra\n\tZip\n\tZero"
    label_106 = Label(tab_25,text=stat_77,bg="black",fg="cyan",font=l_font_all)
    label_106.place(x=0,y=150)
    pic_25 = ImageTk.PhotoImage(Image.open("Letter-Z.png"))
    label_107 = Label(tab_25,image=pic_25,border="0")
    label_107.image = pic_25
    label_107.place(x=540,y=0)
    button_36 = Button(tab_25,image=pic_1,height=140,width=140,command=lambda :Z_sound())
    button_36.place(x=200,y=300)









































def alpha():
    winsound.PlaySound("btn_snd.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    mainframe_1 = Toplevel()
    frame_pic_2 = ImageTk.PhotoImage(Image.open("Frame_pic.jpg"))
    backg_label_1 = Label(mainframe_1,image=frame_pic_2,border="0")
    backg_label_1.image = frame_pic_2
    backg_label_1.place(x=0,y=0)
    mainframe_1.title("Alphabets")
    mainframe_1.geometry("885x576")
    mainframe_1.resizable(False,False)
    stat_2 = "Hai children!!!!!! Ready to learn alphabets ........Which one you want to learn"
    label_3 = Label(mainframe_1,text=stat_2,bg="black",font=l_font_all,fg="cyan")
    label_3.place(x=5,y=10)
    button_7 = Button(mainframe_1,text="A-F",relief=RIDGE,font=b_font_all,bg="cyan",fg="black",activebackground="yellow",height=10,width=10,borderwidth=10,command=lambda :A_F())
    button_7.place(x=87,y=150)
    button_8 = Button(mainframe_1,text="G-L",relief=RIDGE,font=b_font_all,bg="cyan",fg="black",activebackground="yellow",height=10,width=10,borderwidth=10,command=lambda :G_L())
    button_8.place(x=187,y=150)
    button_9 = Button(mainframe_1,text="M-R",relief=RIDGE,font=b_font_all,bg="cyan",fg="black",activebackground="yellow",height=10,width=10,borderwidth=10,command=lambda :M_R())
    button_9.place(x=287,y=150)
    button_10 = Button(mainframe_1,text="S-Z",relief=RIDGE,font=b_font_all,bg="cyan",fg="black",activebackground="yellow",height=10,width=10,borderwidth=10,command=lambda :S_Z())
    button_10.place(x=387,y=150)


def num():
    winsound.PlaySound("btn_snd.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
    mainframe_7 = Toplevel()
    mainframe_7.geometry("800x500")
    mainframe_7.title("Numbers")
    mainframe_7.resizable(False,False)
    note_4 = ttk.Notebook(mainframe_7)
    note_4.pack(fill=BOTH, expand=1)
    tab_26 = Frame(mainframe_7, bg="black")
    tab_27 = Frame(mainframe_7, bg="black")
    tab_28 = Frame(mainframe_7, bg="black")
    tab_29 = Frame(mainframe_7, bg="black")
    tab_30 = Frame(mainframe_7, bg="black")
    tab_31 = Frame(mainframe_7, bg="black")
    tab_32 = Frame(mainframe_7, bg="black")
    tab_33 = Frame(mainframe_7, bg="black")
    tab_34 = Frame(mainframe_7, bg="black")
    tab_35 = Frame(mainframe_7, bg="black")
    note_4.add(tab_26, text="Number - 0")
    note_4.add(tab_27, text="Number - 1")
    note_4.add(tab_28, text="Number - 2")
    note_4.add(tab_29, text="Number - 3")
    note_4.add(tab_30, text="Number - 4")
    note_4.add(tab_31, text="Number - 5")
    note_4.add(tab_32, text="Number - 6")
    note_4.add(tab_33, text="Number - 7")
    note_4.add(tab_34, text="Number - 8")
    note_4.add(tab_35, text="Number - 9")
    #tab_26
    stat_79 = "Number - Zero"
    label_110 = Label(tab_26,text=stat_79,bg="black",fg="cyan",font=l_font_all)
    label_110.place(x=350,y=0)
    stat_80 = "0"
    label_111 = Label(tab_26,text=stat_80,bg="cyan",fg="black",font=num_font_all)
    label_111.config(height=4,width=8)
    label_111.place(x=579,y=0)
    stat_81 = "   Zero"
    label_112 = Label(tab_26,text=stat_81,bg="cyan",fg="black",font=num_font_all)
    label_112.place(x=579,y=20)
    stat_82 = "NUMBER :\n\t0\nSPELLING :\n\tZero"
    label_113 = Label(tab_26,text=stat_82,bg="black",fg="cyan",font=l_font_all)
    label_113.place(x=30,y=40)
    stat_83 = "USES:\n\t0 cars\n\t0birds"
    label_114 = Label(tab_26,text=stat_83,bg="black",fg="cyan",font=l_font_all)
    label_114.place(x=30,y=240)
    pic_1 = ImageTk.PhotoImage(Image.open("Play_Button.png"))
    button_40 = Button(tab_26,image=pic_1,height=140,width=140,command=lambda :zero_sound())
    button_40.image = pic_1
    button_40.place(x=300,y=310)
    #tab_27
    stat_84 = "Number - One"
    label_115 = Label(tab_27,text=stat_84,bg="black",fg="cyan",font=l_font_all)
    label_115.place(x=350,y=0)
    stat_85 = "1"
    label_116 = Label(tab_27,text=stat_85,fg="black",bg="cyan",font=num_font_all)
    label_116.config(height=4,width=8)
    label_116.place(x=579,y=0)
    stat_86 = "   One"
    label_117 = Label(tab_27,text=stat_86,fg="black",bg="cyan",font=num_font_all)
    label_117.place(x=579,y=20)
    stat_87 = "NUMBER :\n\t1\nSPELLING :\n\tOne"
    label_118 = Label(tab_27,text=stat_87,fg="cyan",bg="black",font=l_font_all)
    label_118.place(x=30,y=40)
    stat_88 = "USES :\n\t1 Car\n\t1 man"
    label_119 = Label(tab_27,text=stat_88,fg="Cyan",bg="black",font=l_font_all)
    label_119.place(x=30,y=240)
    button_41 = Button(tab_27,image=pic_1,height=140,width=140,command=lambda :one_sound())
    button_41.image = pic_1
    button_41.place(x=300,y=310)
    #tab_28
    stat_89 = "Number - Two"
    label_120 = Label(tab_28,text=stat_89,fg="cyan",bg="black",font=l_font_all)
    label_120.place(x=350,y=0)
    stat_90 = "2"
    label_121 = Label(tab_28,text=stat_90,fg="black",bg="cyan",font=num_font_all)
    label_121.config(height=4,width=8)
    label_121.place(x=579,y=0)
    stat_91 = "  Two"
    label_122 = Label(tab_28,text=stat_91,fg="black",bg="cyan",font=num_font_all)
    label_122.place(x=579,y=20)
    stat_92 = "NUMBER :\n\t2\nSPELLING :\n\tTwo"
    label_123 = Label(tab_28,text=stat_92,fg="cyan",bg="black",font=l_font_all)
    label_123.place(x=30,y=40)
    stat_93 = "USES :\n\t2 Balls\n\t2 Cats"
    label_124 = Label(tab_28,text=stat_93,fg="cyan",bg="black",font=l_font_all)
    label_124.place(x=30,y=240)
    button_42 = Button(tab_28,image=pic_1,height=140,width=140,command=lambda :two_sound())
    button_42.place(x=300,y=310)
    #tab_29
    stat_94 = "Number - Three"
    label_125 = Label(tab_29,text=stat_94,fg="cyan",bg="black",font=l_font_all)
    label_125.place(x=350,y=0)
    stat_95 = "3"
    label_126 = Label(tab_29,text=stat_95,bg="cyan",fg="black",font=num_font_all)
    label_126.config(height=4,width=8)
    label_126.place(x=579,y=0)
    stat_96 = "  Three"
    label_127 = Label(tab_29,text=stat_96,bg="cyan",fg="black",font=num_font_all)
    label_127.place(x=579,y=20)
    stat_97 = "NUMBER :\n\t3\nSPELLING :\n\tThree"
    label_128 = Label(tab_29,text=stat_97,bg="black",fg="cyan",font=l_font_all)
    label_128.place(x=30,y=40)
    stat_98 = "USES :\n\t3 Cats\n\t3 Carpets"
    label_129 = Label(tab_29,text=stat_98,fg="cyan",bg="black",font=l_font_all)
    label_129.place(x=30,y=240)
    button_43 = Button(tab_29,image=pic_1,height=140,width=140,command=lambda :three_sound())
    button_43.place(x=300,y=310)
    #tab_30
    stat_99 = "Number - Four"
    label_130 = Label(tab_30,text=stat_99,fg="cyan",bg="black",font=l_font_all)
    label_130.place(x=350,y=0)
    stat_100 = "4"
    label_131 = Label(tab_30,text=stat_100,fg="black",bg="cyan",font=num_font_all)
    label_131.config(height=4,width=8)
    label_131.place(x=579,y=0)
    stat_101 = "  Four"
    label_132 = Label(tab_30,text=stat_101,fg="black",bg="cyan",font=num_font_all)
    label_132.place(x=579,y=20)
    stat_102 = "NUMBER :\n\t4\nSPELLING :Four"
    label_133 = Label(tab_30,text=stat_102,fg="cyan",bg="black",font=l_font_all)
    label_133.place(x=30,y=40)
    stat_103 = "USES :\n\t4 Cardboards\n\t4 Fans"
    label_134 = Label(tab_30,text=stat_103,fg="cyan",bg="black",font=l_font_all)
    label_134.place(x=30,y=240)
    button_44 = Button(tab_30,image=pic_1,height=140,width=140,command=lambda :four_sound())
    button_44.place(x=300,y=310)
    #tab_31
    stat_104 = "Number - Five"
    label_135 = Label(tab_31,text=stat_104,fg="cyan",bg="black",font=l_font_all)
    label_135.place(x=350,y=0)
    stat_105 = "5"
    label_136 = Label(tab_31,text=stat_105,fg="black",bg="cyan",font=num_font_all)
    label_136.config(height=4,width=8)
    label_136.place(x=579,y=0)
    stat_106 = "  Five"
    label_137 = Label(tab_31,text=stat_106,fg="black",bg="cyan",font=num_font_all)
    label_137.place(x=579,y=20)
    stat_107 = "NUMBER :\n\t5\nSPELLING :\n\tFive"
    label_138 = Label(tab_31,text=stat_107,fg="cyan",bg="black",font=l_font_all)
    label_138.place(x=30,y=40)
    stat_108 = "USES :\n\t5 Papers\n\t5 Kites"
    label_139 = Label(tab_31,text=stat_108,fg="cyan",bg="black",font=l_font_all)
    label_139.place(x=30,y=240)
    button_45 = Button(tab_31,image=pic_1,height=140,width=140,command=lambda :five_sound())
    button_45.image = pic_1
    button_45.place(x=300,y=310)
    #tab_32
    stat_109 = "Number - Six"
    label_140 = Label(tab_32,text=stat_109,fg="cyan",bg="black",font=l_font_all)
    label_140.place(x=350,y=0)
    stat_110 = "6"
    label_141 = Label(tab_32,text=stat_110,fg="black",bg="cyan",font=num_font_all)
    label_141.config(height=4,width=8)
    label_141.place(x=579,y=0)
    stat_111 = "  Six"
    label_142 = Label(tab_32,text=stat_111,bg="cyan",fg="black",font=num_font_all)
    label_142.place(x=579,y=20)
    stat_112 = "NUMBER :\n\t6\nSPELLING :\n\tSix"
    label_143 = Label(tab_32,text=stat_112,bg="black",fg="cyan",font=l_font_all)
    label_143.place(x=30,y=40)
    stat_113 = "USES :\n\t6 Aeroplanes\n\t6Cycles"
    label_144 = Label(tab_32,text=stat_113,fg="cyan",bg="black",font=l_font_all)
    label_144.place(x=30,y=240)
    button_46 = Button(tab_32,image=pic_1,height=140,width=140,command=lambda :six_sound())
    button_46.place(x=300,y=310)
    #tab_33
    stat_114 = "Number - Seven"
    label_145 = Label(tab_33,text=stat_114,font=l_font_all,bg="black",fg="cyan")
    label_145.place(x=350,y=0)
    stat_115 = "7"
    label_146 = Label(tab_33,text=stat_115,fg="black",bg="cyan",font=num_font_all)
    label_146.config(height=4,width=8)
    label_146.place(x=579,y=0)
    stat_116 = " Seven"
    label_147 = Label(tab_33,text=stat_116,fg="black",bg="cyan",font=num_font_all)
    label_147.place(x=579,y=20)
    stat_117 = "NUMBER :\n\t7\nSPELLING :\n\tSeven"
    label_148 = Label(tab_33,text=stat_117,fg="cyan",bg="black",font=l_font_all)
    label_148.place(x=30,y=40)
    stat_118 = "USES :\n\t7 Flowers\n\t7 hills"
    label_149 = Label(tab_33,text=stat_118,fg="cyan",bg="black",font=l_font_all)
    label_149.place(x=30,y=240)
    button_47 = Button(tab_33,image=pic_1,height=140,width=140,command=lambda :seven_sound())
    button_47.place(x=300,y=310)
    #tab_34
    stat_119 = "Number - Eight"
    label_150 = Label(tab_34,text=stat_119,fg="cyan",bg="black",font=l_font_all)
    label_150.place(x=350,y=0)
    stat_120 = "8"
    label_151 = Label(tab_34,text=stat_120,fg="black",bg="cyan",font=num_font_all)
    label_151.config(height=4,width=8)
    label_151.place(x=579,y=0)
    stat_121 = "  Eight"
    label_152 = Label(tab_34,text=stat_121,fg="black",bg="cyan",font=num_font_all)
    label_152.place(x=579,y=20)
    stat_122 = "NUMBER :\n\t8\nSPELLING :\n\tEight"
    label_153 = Label(tab_34,text=stat_122,fg="cyan",bg="black",font=l_font_all)
    label_153.place(x=30,y=40)
    stat_123 = "USES :\n\t8 Rivers\n\t8 Glasses"
    label_154 = Label(tab_34,text=stat_123,fg="cyan",bg="black",font=l_font_all)
    label_154.place(x=30,y=240)
    button_48 = Button(tab_34,image=pic_1,height=140,width=140,command=lambda :eight_sound())
    button_48.place(x=300,y=310)
    #tab_35
    stat_124 = "Number - Nine"
    label_155 = Label(tab_35,text=stat_124,fg="cyan",bg="black",font=l_font_all)
    label_155.place(x=350,y=0)
    stat_125 = "9"
    label_156 = Label(tab_35,text=stat_125,fg="black",bg="cyan",font=num_font_all)
    label_156.config(height=4,width=8)
    label_156.place(x=579,y=0)
    stat_126 = "   Nine"
    label_157 = Label(tab_35,text=stat_126,fg="black",bg="cyan",font=num_font_all)
    label_157.place(x=579,y=20)
    stat_127 = "NUMBER :\n\t9\nSPELLING :\n\tNine"
    label_158 = Label(tab_35,text=stat_127,fg="cyan",bg="black",font=l_font_all)
    label_158.place(x=30,y=40)
    stat_128 = "USES :\n\t9 Ships\n\t9 Bottles"
    label_159 = Label(tab_35,text=stat_128,fg="cyan",bg="black",font=l_font_all)
    label_159.place(x=30,y=240)
    button_49 = Button(tab_35,image=pic_1,height=140,width=140,command=lambda :nine_sound())
    button_49.place(x=300,y=310)








def help_():
    mainframe_10 = Toplevel()
    mainframe_10.geometry("800x500")
    mainframe_10.resizable(False,False)
    mainframe_10.title("help")
    mainframe_10.config(bg="black")
    label_165 = Label(mainframe_10,text="You can enter the numbers in the entry box and obtain the result\nUse the following symbols to perform the calculations :\n\t(+)  Addition\n\t(-) Subtraction\n\t(*) Multiplication\n\t(/) Division",font=l_font_all,bg="black",fg="cyan")
    label_165.place(x=0,y=0)
def cal():
    winsound.PlaySound("btn_snd.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
    mainframe_9 = Toplevel()
    mainframe_9.geometry("800x500")
    mainframe_9.resizable(False,False)
    mainframe_9.title("Learn to calculate")
    pic_27 = ImageTk.PhotoImage(Image.open("background_1.jpg"))
    label_162 = Label(mainframe_9,image=pic_27,border=0)
    label_162.image = pic_27
    label_162.place(x=0,y=0)
    stat_130 = "LEARN CALCULATION"
    label_163 = Label(mainframe_9,text=stat_130,fg="cyan",bg="black",font=l_font_all)
    label_163.place(x=10,y=10)
    stat_131 = "Enter the numbers in the box and learn to add, subtract, multiply, divide the numbers"
    label_164 = Label(mainframe_9,text=stat_131,fg="cyan",bg="black",font=l_font_all)
    label_164.place(x=30,y=40)
    entry_1 = Entry(mainframe_9,bg="lawn green",fg="black",font=l_font_all,borderwidth=5,relief=RIDGE)
    entry_1.place(x=215,y=110)
    button_54 = Button(mainframe_9,text="submit",borderwidth=8,relief=RIDGE,bg="lawn green",fg="black",font=b_font_all,command=lambda:cmd_cal(),width=9,height=3)
    button_54.place(x=290,y=175)
    entry_2 = Entry(mainframe_9,fg="black", bg="lawn green", font=l_font_all,relief=RIDGE,borderwidth=5)
    entry_2.place(x=215,y=315)
    button_55 = Button(mainframe_9,text="HELP",borderwidth=5,relief=RIDGE,bg="lawn green",fg="black",font=b_font_all,command=lambda :help_())
    button_55.place(x=750,y=0)

    def cmd_cal():
        val_1 = entry_1.get()
        ans_1 = eval(str(val_1))
        entry_2.delete(0,END)
        entry_2.insert(0,ans_1)

def shape():
    winsound.PlaySound("btn_snd.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
    mainframe_11 = Toplevel()
    mainframe_11.geometry("800x500")
    mainframe_11.resizable(False,False)
    mainframe_11.title("Shape")

    note_5 = ttk.Notebook(mainframe_11)
    tab_36 = Frame(note_5, bg="black")
    tab_37 = Frame(note_5, bg="black")
    tab_38 = Frame(note_5, bg="black")
    tab_39 = Frame(note_5, bg="black")
    tab_40 = Frame(note_5, bg="black")
    note_5.add(tab_36, text="SQUARE")
    note_5.add(tab_37, text="RECTANGLE")
    note_5.add(tab_38, text="TRIANGLE")
    note_5.add(tab_39, text="CIRCLE")
    note_5.add(tab_40, text="OVAL")

    #tab_36
    stat_132 = "SQUARE"
    label_166 = Label(tab_36,text=stat_132,fg="cyan",bg="black",font=l_font_all)
    label_166.place(x=400,y=0)
    frame_2 = Frame(tab_36,height=300,width=500)
    frame_2.place(x=200,y=50)
    canvas_1 = Canvas(frame_2)
    canvas_1.config(bg="lawn green")
    canvas_1.create_rectangle(100,100,200,200,fill="orange")
    canvas_1.pack()
    stat_133 = "EDGES : 4\nVERTICES : 4"
    label_167 = Label(tab_36,text=stat_133,font=l_font_all,bg="black",fg="cyan")
    label_167.place(x=600,y=350)
    #tab_37
    stat_134 = "RECTANGLE"
    label_168 = Label(tab_37,text=stat_134,bg="black",fg="cyan",font=l_font_all)
    label_168.place(x=400,y=0)
    frame_3 = Frame(tab_37,height=300,width=500)
    frame_3.place(x=200,y=50)
    canvas_2 = Canvas(frame_3)
    canvas_2.config(bg="lawn green")
    canvas_2.create_rectangle(100,100,310,190,fill="orange")
    canvas_2.pack()
    stat_135 = "EDGES : 4\nVERTICES : 4"
    label_169 = Label(tab_37,text=stat_135,bg="black",fg="cyan",font=l_font_all)
    label_169.place(x=600,y=350)
    #tab_38
    stat_136 = "TRIANGLE"
    label_170 = Label(tab_38,text=stat_136,fg="cyan",bg="black",font=l_font_all)
    label_170.place(x=400,y=0)
    frame_4 = Frame(tab_38,height=300,width=500)
    frame_4.place(x=200,y=50)
    canvas_3 = Canvas(frame_4)
    canvas_3.config(bg="lawn green")
    canvas_3.create_polygon(170,50,50,230,290,230,fill="orange",outline="black")
    canvas_3.pack()
    stat_137 = "EDGES : 3\nVERTICES : 3"
    label_171 = Label(tab_38,text=stat_137,fg="cyan",bg="black",font=l_font_all)
    label_171.place(x=600,y=350)
    #tab_39
    stat_138 = "CIRCLE"
    label_172 = Label(tab_39,text=stat_138,fg="cyan",bg="black",font=l_font_all)
    label_172.place(x=400,y=0)
    frame_5 = Frame(tab_39,height=200,width=500)
    frame_5.place(x=200,y=50)
    canvas_4 = Canvas(frame_5)
    canvas_4.config(bg="lawn green")
    canvas_4.create_oval(60,60,250,250,fill="orange",outline="black")
    canvas_4.pack()
    stat_139 = "EDGES : 0\nVERTICES : 0"
    label_173 = Label(tab_39,text=stat_139,bg="black",fg="cyan",font=l_font_all)
    label_173.place(x=600,y=350)
    #tab_40
    stat_140 = "OVAL"
    label_174 = Label(tab_40,text=stat_140,fg="cyan",bg="black",font=l_font_all)
    label_174.place(x=400,y=0)
    frame_6 = Frame(tab_40,height=200,width=500)
    frame_6.place(x=200,y=50)
    canvas_5 = Canvas(frame_6)
    canvas_5.config(bg="lawn green")
    canvas_5.create_oval(45,15,180,250,fill="orange")
    canvas_5.pack()
    stat_141 = "VERTICES : 0\nEDGES : 0"
    label_175 = Label(tab_40,text=stat_141,bg="black",fg="cyan",font=l_font_all)
    label_175.place(x=600,y=350)


    note_5.pack(fill=BOTH, expand=1)




















def math():
    winsound.PlaySound("btn_snd.wav",winsound.SND_ASYNC|winsound.SND_ALIAS)
    mainframe_6 = Toplevel()
    mainframe_6.geometry("788x444")
    mainframe_6.resizable(False,False)
    pic_26 = ImageTk.PhotoImage(Image.open("Frame_Pic_2.jpg"))
    label_108 = Label(mainframe_6,image=pic_26,border="0")
    label_108.image = pic_26
    label_108.place(x=0,y=0)
    stat_78 = "Hai Children!!!! Shall we learn maths .....Which one of these you like"
    label_109 = Label(mainframe_6,text=stat_78,bg="black",fg="cyan",font=l_font_all)
    label_109.place(x=10,y=10)
    button_37 = Button(mainframe_6,relief=RIDGE,text="Numbers",bg="cyan",fg="black",font=b_font_all,activebackground="yellow",height=10,width=10,borderwidth=10,command=lambda :num())
    button_37.place(x=150,y=150)
    button_38 = Button(mainframe_6,relief=RIDGE,text="  Arithemetic\nOperation",fg="black",bg="cyan",font=b_font_all,activebackground="yellow",height=10,width=15,borderwidth=10,command=lambda :cal())
    button_38.place(x=255,y=150)
    button_39 = Button(mainframe_6,text="shapes",relief=RIDGE,activebackground="yellow",borderwidth=10,height=10,width=10,fg="black",bg="cyan",font=b_font_all,command=lambda :shape())
    button_39.place(x=400,y=150)



def rhymes():
    winsound.PlaySound("btn_snd.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
    mainframe_12 = Toplevel()
    mainframe_12.geometry("1000x700")
    mainframe_12.resizable(False,False)
    mainframe_12.config(bg="red")
    mainframe_12.title("Rhymes")

    label_176 = Label(mainframe_12,text="Hai Children!!! ready for learning rhymes\n\tWhich one you like",bg="red",fg="white",font=l_font_all)
    label_176.place(x=0,y=3)
    button_56 = Button(mainframe_12,text="ABCD rhymes",bg="black",fg="white",font=b_font_all,borderwidth=5,relief=RIDGE,height=5,width=10,command=lambda:rhy_abc())
    button_56.place(x=30,y=70)
    button_57 = Button(mainframe_12,text="Baa\nBaa\nBlack Sheep",bg="black",fg="white",font=b_font_all,borderwidth=5,relief=RIDGE,height=5,width=10,command=lambda :rhy_baa())
    button_57.place(x=130,y=70)
    button_58 = Button(mainframe_12,text="Hickory\nDickory\nDock",bg="black",fg="white",font=b_font_all,borderwidth=5,relief=RIDGE,height=5,width=10,command=lambda :rhy_hickory())
    button_58.place(x=230,y=70)
    button_59 = Button(mainframe_12,text="Humpty\nDumpty",bg="black",fg="white",font=b_font_all,height=5,width=10,borderwidth=5,relief=RIDGE,command=lambda :rhy_humpty())
    button_59.place(x=330,y=70)
    button_60 = Button(mainframe_12,text="Incy\nwincy\nspider",bg="black",fg="white",font=b_font_all,height=5,width=10,borderwidth=5,relief=RIDGE,command=lambda:rhy_incy())
    button_60.place(x=30,y=190)
    button_61 = Button(mainframe_12,text="Jack\nand\nJill",bg="black",fg="white",font=b_font_all,height=5,width=10,borderwidth=5,relief=RIDGE,command=lambda :rhy_jack())
    button_61.place(x=130,y=190)
    button_62 = Button(mainframe_12,text="Old\nMC Donald",bg="black",fg="white",borderwidth=5,font=b_font_all,height=5,width=10,relief=RIDGE,command=lambda :rhy_old())
    button_62.place(x=230,y=190)
    button_63 = Button(mainframe_12,text="Rain\nRain",bg="black",fg="white",borderwidth=5,relief=RIDGE,font=b_font_all,height=5,width=10,command=lambda :rhy_rain())
    button_63.place(x=330,y=190)
    button_64 = Button(mainframe_12,text="Twinkle\nTwinkle",bg="black",fg="white",borderwidth=5,relief=RIDGE,font=b_font_all,height=5,width=48,command=lambda: rhy_twinkle() )
    button_64.place(x=30,y=310)

def games():
    winsound.PlaySound("btn_snd.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
    mainframe_13 = Toplevel()
    mainframe_13.geometry("800x500")
    mainframe_13.resizable(False,False)
    mainframe_13.title("Games")
    mainframe_13.config(bg="lawn green")
    stat_142 = "Excited to play!!!!\nStart playing kids we have a some games\nwhich one you like the most"
    label_177 = Label(mainframe_13,text=stat_142,font=l_font_all,bg="lawn green",fg="black")
    label_177.place(x=20,y=30)
    button_65 = Button(mainframe_13,text="SWAP\nCOLOR",bg="black",fg="lawn green",height=7,width=10,borderwidth=5,font=b_font_all,relief=RIDGE,command=lambda :swap())
    button_65.place(x=150,y=150)
    button_66 = Button(mainframe_13,text="MIND\nCAL",bg="black",fg="lawn green",height=7,width=10,borderwidth=5,font=b_font_all,relief=RIDGE,command=lambda :g_cal())
    button_66.place(x=250,y=150)
    button_67 = Button(mainframe_13,text="GUESS\nTHE\nNUMBER",bg="black",fg="lawn green",height=7,width=10,borderwidth=5,font=b_font_all,relief=RIDGE,command=lambda :g_guess())
    button_67.place(x=350,y=150)







#Base_1 button
stat_1 = "Hai Children!!!! Ready for learning.\nwhat topic do you want?"
label_1 = Label(tk,text=stat_1,bg="black",borderwidth=0,font=l_font_all,fg="cyan")
label_1.place(x=5,y=10)
button_1 = Button(tk,text="Alphabets",relief=RIDGE,borderwidth=5,bg="cyan",activebackground="yellow",fg="black",font=b_font_all,command=lambda :alpha(),width=14,height=3)
button_1.place(x=240,y=210)
button_2 = Button(tk,text="Maths",relief=RIDGE,borderwidth=5,bg="cyan",fg="black",activebackground="yellow",font=b_font_all,width=14,height=3,command=lambda  :math())
button_2.place(x=369,y=210)
button_3 = Button(tk,text="Rhymes",relief=RIDGE,borderwidth=5,bg="cyan",fg="black",activebackground="yellow",font=b_font_all,width=30,height=3,command=lambda :rhymes())
button_3.place(x=240,y=135)
button_4 = Button(tk,text="Games",relief=RIDGE,borderwidth=5,bg="cyan",fg="black",activebackground="yellow",font=b_font_all,width=30,height=3,command=lambda :games())
button_4.place(x=240,y=285)





tk.resizable(False,False)










tk.mainloop()

