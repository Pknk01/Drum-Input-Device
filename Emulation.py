from time import sleep
import serial as SRL
import re 
from pynput import keyboard

# --- Keyboard Emulation and Reading ---

msdelay = 10 #time to wait in ms

def SimKeypress(KeytoPress):

    keyboard.press(KeytoPress)
    sleep(msdelay / 1000) 
    keyboard.release(KeytoPress)

RecursionCheck = True

def Press_Callback(key):
    if key == keyboard.Key.esc:
        RecursionCheck = False
        return False

listener = keyboard.Listener( on_press=Press_Callback )     #binds event callback
listener.start()                                            #starts event listening


# --- Serial Communication ---

arduino = SRL.Serial(port='/dev/tty.usbmodem14201', baudrate=9600, timeout=1) #Instantiates Arduino Object

while (RecursionCheck):
    Raw_Val = arduino.readline()                                #Reads from the serial line
    Filtered_Val = re.findall(r'[ABCD]', str(Raw_Val))          #Returns filtered value from serial line

    #Attemtps to press all inputs from line
    for x in Filtered_Val:
        try:
            SimKeypress(Filtered_Val)
        except:
            print("Value is null")
            continue


