from turtledemo.penrose import start
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    head_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN*60
    break_secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN*60

    if reps%8 == 0:
        head_label.config(text="Long Break", fg=RED, font=(FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
        count_down(long_break_secs)
    elif reps%2 == 0 :
        head_label.config(text="Break", fg=PINK, font=(FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
        count_down(break_secs)
    else:
        head_label.config(text="Work",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW,highlightthickness=0)
        count_down(work_secs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = math.floor(count%60)
    if count_min < 10:
        count_min = "0" + str(count_min)
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range (work_session):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

head_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW,highlightthickness=0)
head_label.grid(column=1,row=0)

canvas = Canvas(width=200 , height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomoto_img)
timer_text =canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,28,"bold"))
canvas.grid(column= 1, row = 1)

start_button = Button(text = "Start",highlightthickness=0,command=start_timer)
start_button.grid(column = 0,row = 2)

reset_button = Button(text = "Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column = 2,row = 2)

check_mark = Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)



window.mainloop()






