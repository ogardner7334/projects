import time as t, picamera

with picamera.PiCamera() as cam:
    cam.start_preview()
    t.sleep(2)
    for filename in cam.capture_continuous("ing{counter:03d}.jpg"):
        print('Captured %sw' % filename)
        t.sleep(5)
