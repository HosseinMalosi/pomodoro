from tkinter import *
import math
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
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text ="00:00")
    label_timer.config(text='Timer', fg=GREEN)
    label_check.config(text = "")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec  =SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN *  60
    
    if reps % 8 == 0:
        counter(long_sec)
        label_timer.config(text= "break",fg=RED)
    elif reps % 2 == 0 :
        counter(short_sec)
        label_timer.config(text="break",fg=PINK)
    else:
        counter(work_sec)
        label_timer.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    global checkmark
    global timer
    count_min=math.floor(count/60)
    count_sec= count % 60
    if count_min < 10 :
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,counter,count - 1)
    if count == 0:
        
        start_timer()
        mark = ""
        for n in range(math.floor(reps/2)):
            mark += "✔"
        label_check.config(text=mark)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg =YELLOW)


canvas = Canvas(width=250,height=225,bg=YELLOW,highlightthickness=0)
img =PhotoImage(file="tomato.png")
canvas.create_image(125,112,image=img)
timer_text = canvas.create_text(125,130,text ="00:00" , fill="white" ,font = (FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# Labels
label_timer = Label(text="Timer",font=(FONT_NAME,50,"bold"),bg=YELLOW,fg=GREEN)
label_timer.grid(column=1,row=0)
label_check = Label(text="",bg=YELLOW,fg=GREEN,font=(20))
label_check.grid(column=1,row=3)

# Buttons
start_btn = Button(text="Start",command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn = Button(text="Reset",command=reset_timer)
reset_btn.grid(column=2,row=2)




window.mainloop()