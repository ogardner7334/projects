import time as t, picamera
def camcaptuser():
    opin = ""
    try:
        with picamera.PiCamera() as cam:
            print ("setup camera")
            while opin != "yes":
                name = ""
                while name == "":
                    name = input("Name?")
                t.sleep(2)
                print("saving name")
                cam.start_preview()
                print("started the preview")
                t.sleep(2)
                cam.capture("{0}.jpg".format(name))
                print("captured the image")
                cam.stop_preview()
                opin = input("is the image ok? yes/no")
                if opin == "yes":
                    t.sleep (1)
                    print ("This account will be called {0}".format(name))
    except picamera.exc.PiCameraError:
        print ("there is a problem with the camera.")

                    
def profile():
    camcaptuser()
    t.sleep(1)
    haircolor = ""
    eyecolor = ""
    skincolor =""
    glasses =""
    while haircolor == "":
        haircolor = input ("Hair color? (brown/black/blonde/ginger)")
    while eyecolor == "":
        eyecolor = input ("Eye color? (blue/brown/grey/green)")
    while skincolor == "":
        skincolor = input ("Skin color? (white/black)")
    while glasses == "":
        glasses = input ("Glasses? (yes/no)")
    print ("You have {0} hair, {1} eyes, {2} skin and {3} to glasses".format(haircolor,eyecolor,skincolor,glasses))

