from tkinter import *
from tkinter.ttk import *
import sys, os, re, time, random
import threading
from datetime import datetime

def setdone(val):
    global done
    done = val
    
def starttimer(x):
    try:
        global done
        timeinput.config(state="disabled")
        done = False
        timerange = int(timeamount.get())
        go.config(text="Stop")
        go.config(command=lambda:setdone(True))
    except:
        pass
        timerange = 0
    for i in range(timerange):
        try:
            if done == False:
                if timemeasure.get() == "Seconds":
                    time.sleep(1)
                elif timemeasure.get() == "Minutes":
                    time.sleep(1 * 60)
                elif timemeasure.get() == "Hours":
                    time.sleep(1 * 60 * 60)
                else:
                    timeamount.set("0")
                    i = 0
                timerange -= 1
                timeamount.set(str(timerange))
            else:
                timeinput.config(state="normal")
                go.config(text="Start")
                go.config(command=lambda:threading.Thread(target=starttimer, args=(1,)).start())
                done = False
                break
        except:
          done = False
          break  
    timeinput.config(state="normal")
    go.config(text="Start")
    go.config(command=lambda:threading.Thread(target=starttimer, args=(1,)).start())


def update():
    global other, clock
    if len(str(datetime.now().time().minute)) == 1:
        curtime = str(datetime.now().time().hour) + ":0" + str(datetime.now().time().minute)
    else:
        curtime = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)
    clock["text"] = curtime
    root.after(1000, update)


root = Tk()

root.title("Clock")

curtime = datetime.now()

root.geometry("500x500")

root.resizable(False, False)

timeamount = StringVar(root)
timeinput = Entry(root, textvariable=timeamount)
timeinput.place(x=20, y=20, width=360, height=30)
go = Button(root, text="Start", command=lambda:threading.Thread(target=starttimer, args=(1,)).start())
go.place(x=390, y=20, width=90, height=30)

timemeasure = StringVar(root)
timemeasure.set("Seconds")
dropdown = OptionMenu(root, timemeasure, "Choose a Measurement", "Hours", "Minutes", "Seconds")
dropdown.place(x=20, y=70, width=460, height=30)

clock = Label(root, font=("Arial", 25))
clock.place(x=180, y=120, width=460, height=40)

update()

root.mainloop()

done = True

