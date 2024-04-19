import tkinter as tk
window = tk.Tk()
i = tk.PhotoImage(width=1,height=1)
def crossoff1():
    if button1['foreground'] == 'black':
        button1['foreground'] = 'red'
        button1['text'] = 'X'
        button1['font'] = ('Helvetica', 40, 'bold')
    else:
        button1['foreground'] = 'black'
        button1['text'] = 'Dead Meme'
        button1['font'] = ('Helvetica', 15, 'bold')
def crossoff2():
    if button2['foreground'] == 'black':
        button2['foreground'] = 'red'
        button2['text'] = 'X'
        button2['font'] = ('Helvetica', 40, 'bold')
    else:
        button2['foreground'] = 'black'
        button2['text'] = 'TikTok Video'
        button2['font'] = ('Helvetica', 15, 'bold')
def crossoff3():
    if button3['foreground'] == 'black':
        button3['foreground'] = 'red'
        button3['text'] = 'X'
        button3['font'] = ('Helvetica', 40, 'bold')
    else:
        button3['foreground'] = 'black'
        button3['text'] = 'Hard Edit🔥'
        button3['font'] = ('Helvetica', 15, 'bold')
def crossoff4():
    if button4['foreground'] == 'black':
        button4['foreground'] = 'red'
        button4['text'] = 'X'
        button4['font'] = ('Helvetica', 40, 'bold')
    else:
        button4['foreground'] = 'black'
        button4['text'] = 'Made For \n An 8 Year-Old'
        button4['font'] = ('Helvetica', 15, 'bold')
def crossoff5():
    if button5['foreground'] == 'black':
        button5['foreground'] = 'red'
        button5['text'] = 'X'
        button5['font'] = ('Helvetica', 40, 'bold')
    else:
        button5['foreground'] = 'black'
        button5['text'] = 'Satisfying'
        button5['font'] = ('Helvetica', 15, 'bold')
def crossoff6():
    if button6['foreground'] == 'black':
        button6['foreground'] = 'red'
        button6['text'] = 'X'
        button6['font'] = ('Helvetica', 40, 'bold')
    else:
        button6['foreground'] = 'black'
        button6['text'] = '\"this guy\"'
        button6['font'] = ('Helvetica', 15, 'bold')
def crossoff7():
    if button7['foreground'] == 'black':
        button7['foreground'] = 'red'
        button7['text'] = 'X'
        button7['font'] = ('Helvetica', 40, 'bold')
    else:
        button7['foreground'] = 'black'
        button7['text'] = 'Different \n Language'
        button7['font'] = ('Helvetica', 15, 'bold')
def crossoff8():
    if button8['foreground'] == 'black':
        button8['foreground'] = 'red'
        button8['text'] = 'X'
        button8['font'] = ('Helvetica', 40, 'bold')
    else:
        button8['foreground'] = 'black'
        button8['text'] = 'Fortnite'
        button8['font'] = ('Helvetica', 15, 'bold')
def crossoff9():
    if button9['foreground'] == 'black':
        button9['foreground'] = 'red'
        button9['text'] = 'X'
        button9['font'] = ('Helvetica', 40, 'bold')
    else:
        button9['foreground'] = 'black'
        button9['text'] = 'TV/Movie \n Clip'
        button9['font'] = ('Helvetica', 15, 'bold')
def crossoff10():
    if button10['foreground'] == 'black':
        button10['foreground'] = 'red'
        button10['text'] = 'X'
        button10['font'] = ('Helvetica', 40, 'bold')
    else:
        button10['foreground'] = 'black'
        button10['text'] = 'Sub Bait'
        button10['font'] = ('Helvetica', 15, 'bold')
def crossoff11():
    if button11['foreground'] == 'black':
        button11['foreground'] = 'red'
        button11['text'] = 'X'
        button11['font'] = ('Helvetica', 40, 'bold')
    else:
        button11['foreground'] = 'black'
        button11['text'] = 'TikTok Girl \n Voice'
        button11['font'] = ('Helvetica', 15, 'bold')
def crossoff12():
    if button12['foreground'] == 'black':
        button12['foreground'] = 'red'
        button12['text'] = 'X'
        button12['font'] = ('Helvetica', 40, 'bold')
    else:
        button12['foreground'] = 'black'
        button12['text'] = 'Actually \n Funny'
        button12['font'] = ('Helvetica', 15, 'bold')
def crossoff13():
    if button13['foreground'] == 'black':
        button13['foreground'] = 'red'
        button13['text'] = 'X'
        button13['font'] = ('Helvetica', 40, 'bold')
    else:
        button13['foreground'] = 'black'
        button13['text'] = 'Free!'
        button13['font'] = ('Helvetica', 40, 'bold')
def crossoff14():
    if button14['foreground'] == 'black':
        button14['foreground'] = 'red'
        button14['text'] = 'X'
        button14['font'] = ('Helvetica', 40, 'bold')
    else:
        button14['foreground'] = 'black'
        button14['text'] = 'Girls \n Dancing'
        button14['font'] = ('Helvetica', 15, 'bold')
window.geometry("546x546")
window.title("YT Shorts Bingo")
button1 = tk.Button(
    text='Dead Meme',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff1,
    font=('Helvetica', 15, 'bold')
)
button1.place(x=1,y=1)
button2 = tk.Button(
    text='TikTok Video',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff2,
    font=('Helvetica', 15, 'bold')
)
button2.place(x=110,y=1)
button3 = tk.Button(
    text='Hard Edit🔥',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff3,
    font=('Helvetica', 15, 'bold')
)
button3.place(x=219,y=1)
button4 = tk.Button(
    text='Made For \n An 8 Year-Old',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff4,
    font=('Helvetica', 15, 'bold')
)
button4.place(x=328,y=1)
button5 = tk.Button(
    text='Satisfying',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff5,
    font=('Helvetica', 15, 'bold')
)
button5.place(x=437,y=1)
button6 = tk.Button(
    text='\"this guy\"',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff6,
    font=('Helvetica', 15, 'bold')
)
button6.place(x=1,y=110)
button7 = tk.Button(
    text='Different \n Language',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff7,
    font=('Helvetica', 15, 'bold')
)
button7.place(x=110,y=110)
button8 = tk.Button(
    text='Fortnite',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff8,
    font=('Helvetica', 15, 'bold')
)
button8.place(x=219,y=110)
button9 = tk.Button(
    text='TV/Movie \n Clip',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff9,
    font=('Helvetica', 15, 'bold')
)
button9.place(x=328,y=110)
button10 = tk.Button(
    text='Sub Bait',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff10,
    font=('Helvetica', 15, 'bold')
)
button10.place(x=437,y=110)
button11 = tk.Button(
    text='TikTok Girl \n Voice',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff11,
    font=('Helvetica', 15, 'bold')
)
button11.place(x=1,y=219)
button12 = tk.Button(
    text='Actually \n Funny',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff12,
    font=('Helvetica', 15, 'bold')
)
button12.place(x=110,y=219)
button13 = tk.Button(
    text='Free!',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff13,
    font=('Helvetica', 40, 'bold')
)
button13.place(x=219,y=219)
button14 = tk.Button(
    text='Girls \n Dancing',
    image=i,
    compound='c',
    width=100, 
    height=100,
    foreground='black',
    command=crossoff14,
    font=('Helvetica', 15, 'bold')
)
button14.place(x=328,y=219)
window.mainloop()