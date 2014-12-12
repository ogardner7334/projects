import time as t, picamera
opin = ""
with picamera.PiCamera() as cam:
    while opin != "y":
        cam.start_preview()
        t.sleep(2)
        for filename in cam.capture("a(counter:03d).jpg"):
            opin = input("is the image ok? y/n")
