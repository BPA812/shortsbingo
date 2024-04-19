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
window.geometry("500x500")
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
window.mainloop()