import picamera,time as t

with picamera.PiCamera() as cam:
    cam.resolution = (1024,768)
    cam.start_preview()

    t.sleep(2)
    cam.capture("a.gif")
