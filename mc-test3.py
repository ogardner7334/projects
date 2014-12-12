import time as t,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

black=7
red=14
orange=1
green=5

for num in (0,1,2,3,4,5,6):
    mc.setBlock(25,num,25,35,black)

for num in (0,1,2,3,4,5,6):
    mc.setBlock(20,num,25,35,black)

for num in (0,1,2,3,4,5,6):
    mc.setBlock(20,num,24,35,black)

while True:
    t.sleep(4)
    mc.setBlock(25,4,25,35,black)
    mc.setBlock(25,5,25,35,black)
    mc.setBlock(25,6,25,35,black)
    mc.setBlock(25,6,25,35,red)
    mc.setBlock(20,4,25,35,black)
    mc.setBlock(20,5,25,35,black)
    mc.setBlock(20,6,25,35,black)
    mc.setBlock(20,6,25,35,red)
    mc.postToChat("Red")
    t.sleep(10)
    mc.setBlock(25,5,25,35,orange)
    mc.setBlock(20,5,25,35,orange)
    mc.postToChat("Red Amber")
    t.sleep(2)
    mc.setBlock(25,5,25,35,black)
    mc.setBlock(25,6,25,35,black)
    mc.setBlock(25,4,25,35,green)
    mc.setBlock(20,5,25,35,black)
    mc.setBlock(20,6,25,35,black)
    mc.setBlock(20,4,25,35,green)
    mc.postToChat("Green")
    t.sleep(10)
    mc.setBlock(25,4,25,35,black)
    mc.setBlock(25,5,25,35,orange)
    mc.setBlock(20,4,25,35,black)
    mc.setBlock(20,5,25,35,orange)
    mc.postToChat("Amber")
