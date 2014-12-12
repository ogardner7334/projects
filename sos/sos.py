#morse flasher by Oskar Gardner
import RPi.GPIO as GPIO,time as t
GPIO.setmode(GPIO.BOARD) #set the pin numbering system
GPIO.setup(11,GPIO.OUT)
def Dot():
        GPIO.output(11,True)
        t.sleep (0.5)
        GPIO.output(11,False)
        t.sleep (1.5)
def Dash():
        GPIO.output(11,True)
        t.sleep (1.5)
        GPIO.output(11,False)
        t.sleep (1.5)
GPIO.output(11,False)
def morse(letter):
        if morse == "a":
                Dot()
                Dash()
        elif morse == "b":
                Dash()
                Dot()
                Dot()
                Dot()
        elif morse == "c":
                Dash()
                Dot()
                Dash()
                Dot()
        elif morse == "d":
                Dash()
                Dot()
                Dot()
        elif morse == "e":
                Dot()
        elif morse == "f":
                Dot()
                Dot()
                Dash()
                Dot()
        elif morse == "g":
                Dash()
                Dash()
                Dot()
        elif morse == "h":
                Dot()
                Dot()
                Dot()
                Dot()
        elif morse == "i":
                Dot()
                Dot()
        elif morse == "j":
                Dot()
                Dash()
                Dash()
                Dash()
        elif morse == "k":
                Dash()
                Dot()
                Dash()
        elif morse == "l":
                Dot()
                Dash()
                Dot()
                Dot()
        elif morse == "m":
                Dash()
                Dash()
        elif morse == "n":
                Dash()
                Dot()
        elif morse == "o":
                Dash()
                Dash()
                Dash()
        elif morse == "p":
                Dot()
                Dash()
                Dash()
                Dot()
        elif morse == "q":
                Dash()
                Dash()
                Dot()
                Dash()
        elif morse == "r":
                Dot()
                Dash()
                Dot()
        elif morse == "s":
                Dot()
                Dot()
                Dot()
        elif morse == "t":
                Dash()
        elif morse == "u":
                Dot()
                Dot()
                Dash()
        elif morse == "v":
                Dot()
                Dot()
                Dot()
                Dash()
        elif morse == "w":
                Dot()
                Dash()
                Dash()
        elif morse == "x":
                Dash()
                Dot()
                Dot()
                Dash()
        elif morse == "y":
                Dash()
                Dot()
                Dash()
                Dash()
        elif morse == "z":
                Dash()
                Dash()
                Dot()
                Dot()
                
        
                
        else:
                print ("sorry not finished")    
