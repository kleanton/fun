
from tkinter import *
import random

def catch_me():
    x=random.choice(range(50,800,50))
    y=random.choice(range(50,800,50))
    new='100x100+'+str(x)+'+'+str(y)
    root.geometry(new)
    counter()
    

def counter():
    global i
    i+=1
    label1.configure(text=str(i))

def tick():
    global temp,after_id
    after_id = root1.after(1000,tick)
    if temp > 0:
        label2.configure(text=str(temp))
        temp-=1
    else:    
        label2.grid_forget()
        label1.configure(font=("Arial",80),text=str(i)+"\n очков")
        label1.grid(rowspan=2, columnspan=2)
        
        
   
i=0
temp=20  
after_id=''

    
root=Tk()
root1=Tk()
root1.title('Игра «Поймай меня»')
root.title('Поймай и кликни')
root.geometry('100x100+0+0') # ширина=500, высота=400, x=300, y=200
root1.geometry('300x300+0+0')
#root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна
#root.overrideredirect(False)
#root1.overrideredirect(False)
root.resizable(False, False) # размер окна может быть изменён только по горизонтали
root1.resizable(False, False) 

button = Button (root,text='Поймай меня',command=catch_me,width=25,height=5,bg='black',fg='red',font='arial 14')
label1= Label (root1, width=5, font=("Arial",40),text="0")
label1.grid(row=1, columnspan=1)

label2= Label (root1, width=5, font=("Arial",100),text="20")
label2.grid(row=0, columnspan=2)



button.pack()
tick()
root.mainloop()