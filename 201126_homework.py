#1
'''
from tkinter import * 

window = Tk()

label1 = Label(window,text="화씨")
label2 = Label(window,text="섭씨")
entry1 = Entry(window)
entry2 = Entry(window)
button1 = Button(window,text="화씨->섭씨")
button2 = Button(window,text="섭씨->화씨")

label1.pack()
label2.pack()
entry1.pack()
entry2.pack()
button1.pack()
button2.pack()

window.mainloop()
'''
#2
'''
from tkinter import *

def process() :
    inch = int(entry.get())
    cm = inch*2.54
    label4["text"]=str(cm)+"센티미터"
window=Tk()
label1 = Label(window,text="인치를 센티미터로 변환하는 프로그램")
label2 = Label(window,text="인치를 입력하시오 : ")
label3 = Label(window,text="변환결과 : ")
label4 = Label(window,text="결과값이 출력됩니다.")
entry = Entry(window)
button = Button(window,text="변환",command=process)

label1.grid(row=0,column=0,columnspan=2)
label2.grid(row=1,column=0)
entry.grid(row=1,column=1)
label3.grid(row=2,column=0)
label4.grid(row=2,column=1)
button.grid(row=3,column=1)

window.mainloop()
'''
#3
'''
from tkinter import *
from PIL import ImageTk, Image

window = Tk()

def change_img() :
    path = inputBox.get()
    img = ImageTk.PhotoImage(Image.open(path))
    imageLabel.configure(image = img)
    imageLabel.image = img

photo = ImageTk.PhotoImage(Image.open("wl.gif"))
imageLabel = Label(window, image = photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button = Button(window, text = "Submit", command = change_img)
button.pack()

window.mainloop()
'''
#4
'''
from tkinter import *

mycolor = 'blue'

def paint(event) :
    x1, y1 = (event.x-1),(event.y+1)
    x2, y2 = (event.x-1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2,fill = mycolor)

def change_color() :
    global mycolor
    mycl=olor = 'red'

window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

button = Button(window, text="빨간색", command = change_color)
button.pack()
window.mainloop()
'''
#5 1. 숫자를 입력하고, 더하기(+)버튼은 더하기, 빼기(-)버튼은 뺄셈, 초기화는 초기화
'''
from tkinter import *

def sum() :
    global total
    a = int(entry.get())
    total += a
    label2["text"] = total

def minus() :
    global total
    a = int(entry.get())
    total -= a
    label2["text"] = total

def new() :
    entry.delete(0,END)
    total = 0
    label2["text"] = 0

window=Tk()

total = 0
label1 = Label(window,text="현재 합계")
label2 = Label(window,text=total)
entry = Entry(window)
button1 = Button(window,text="더하기(+)",command=sum)
button2 = Button(window,text="빼기(-)",command=minus)
button3 = Button(window,text="초기화",command=new)

label1.grid(row=0,column=0)
label2.grid(row=0,column=1,columnspan=2)
entry.grid(row=1,column=0,columnspan=3)
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)

window.mainloop()
'''


