import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time

flag = True
# put your test video path here
stream = cv2.VideoCapture("clip.mp4")
def play(speed):
    global flag
    print(f"You Clicked on play. Speed is {speed}")
    frame1= stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+ speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width= SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134,26,fill="green", font="Times 26 bold", text="Decision Pending")
    flag = not flag
def pending(decision):
    # 1 Display decision pending image
    frame = cv2.cvtColor(cv2.imread("Dpendings.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor= tkinter.NW)
    # 2 wait for 1 second
    time.sleep(1)
    # 3 Display Sponser
    frame = cv2.cvtColor(cv2.imread("sponsorss.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor= tkinter.NW)
   
    # 4 wait for 1.5 seconds
    time.sleep(1.5)
    # 5 Display out/notout image
    if decision == "out":
        decisionImg = "outtt.png"
    else:
        decisionImg = "notoutt.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor= tkinter.NW)
   

def out():
    thread =threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread =threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

#width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

#tkinter GUI
window = tkinter.Tk()
window.title("vishal Third Umpire Decision Review")
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
cv_img = cv2.cvtColor(cv2.imread("welcomeee.png"), cv2.COLOR_BGR2RGB)      #front page interface
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, ancho=tkinter.NW, image=photo)
canvas.pack()

# buttons to control;
btn = tkinter.Button(window, text="<< Previous (Fast)", width = 50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<< Previous (Slow)", width = 50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text=" Next (Fast) >>", width = 50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text=" Next (Slow) >>", width = 50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text=" Give Out", width = 50, command=out)
btn.pack()
btn = tkinter.Button(window, text=" Give Not Out", width = 50,command=not_out)
btn.pack()


window.mainloop()
