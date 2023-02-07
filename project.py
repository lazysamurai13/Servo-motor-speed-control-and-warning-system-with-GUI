from pyfirmata import Arduino, SERVO
from time import sleep #to create delay in rotations
import pyttsx3 #Text to speech
import tkinter as tk #GUI
#--------------------------------Text to Speech----------------------------
engine = pyttsx3.init() ## init function to get an engine instance for the speech synthesis
#---------------------------------Arduino----------------------------------
board = Arduino('COM11') #serial port number of pc where arduino is connected
pin = 8 #Digital output pin of arduino which allows communication between servo motor and arduino
board.digital[pin].mode = SERVO #Indicates arduino pin 8 has servo connected to it
def main():
    angle = int(rotation_Angle.get()) #Taking angle of rotation from user
    speed = int(rotation_Speed.get()) #Taking speed from user
    delay = delay_select(speed) #setting to current delay
    if safety(delay) == True: #checking speed is within speed_limit
        motion(delay, angle)
    else:
        raise ValueError
#-------------------------------Motor motion------------------------------

def motion(delay,angle):
    for i in range(0,angle): #for loop provides rotation between 0 and specified angle
        board.digital[pin].write(i)
        sleep(delay)

#----------------------Selecting appropriate Delay------------------------
def delay_select(speed): #reducing delay implies increasing duty cycle which inturn increases speed of sero motor
    if speed ==1:
        current_delay =0.12
    elif speed ==2:
        current_delay =0.09
    elif speed ==3:
        current_delay =0.06
    elif speed ==4:
        current_delay =0.03
    elif speed ==5:
        current_delay =0.01
    else:
        raise ValueError("Wrong speed")
    return current_delay
#-------------------------------Speed Limit-------------------------------
def safety(delay):
    speed_limit = 0.03 #Setting Speed Limit
    if delay == speed_limit :
        engine.say("YOU ARE ABOUT TO CROSS THE SPEED LIMIT") #say method on the engine that passing input text to be spoken
        engine.runAndWait() # run and wait method
        return True
    if delay >speed_limit:
        return True
    if delay < speed_limit:
        engine.say("YOU HAVE CROSSED THE SPEED LIMIT")
        engine.runAndWait()
        return False
#----------------------------Quiting GUI----------------------------------
def quit():
    engine.say('THIS IS CS50 GOODBYE')
    engine.runAndWait()
    gui.destroy() #closes gui

# ---------------------------GUI design ----------------------------------
gui = tk.Tk() #creates a window
gui.title("SERVO MOTOR CONTROLLER") #Title of dialogue box
gui.minsize(300,300) #Size of dialogue box

rotation_Angle = tk.Scale(gui, bd=10, from_=0, to=360, orient=tk.HORIZONTAL) #Scaler Design
rotation_Angle.grid(column=2, row=1) #Scalar Postion
tk.Label(gui, text="Angle (0 to 180) ").grid(column=3, row=1) #Text box

rotation_Speed = tk.Entry(gui, bd=10, width=10,) #Input box design
rotation_Speed.grid(column=2, row=2)
tk.Label(gui, text=" Speed (1 to 5) ").grid(column=3, row=2)

start_btn = tk.Button(gui, bd=10, bg='#097969', text="START", activebackground= "yellow", command=main) #Button Design
start_btn.grid(column=2, row=10)

quit_btn = tk.Button(gui, bg='red', text="QUIT",activebackground= "yellow",command=quit)
quit_btn.grid(column=10, row=10)

gui.mainloop()

if __name__=="__main__":
    main()
