import time as t, picamera, camcaptuser
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
    print ("You have {0} hair, {1} eyes, {2} skin and {4} to glasses".format(haircolor,eyecolor,skincolor,glasses))
    
