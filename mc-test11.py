import time as t,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

wood = 5
bricks = 45
stone = 1
air = 0
torch = 50

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def build_house(x,y,z) : 
    mc.setBlock(x,y-1,z,stone)
    mc.setBlocks(x+1,y,z+1,x+20,y+10,z+20,air)
    mc.setBlocks(x-1,y,z-1,x+22,y,z+22,bricks)
    mc.setBlocks(x+1,y+1,z+1,x+20,y+10,z+20,stone)
    mc.setBlocks(x+2,y+1,z+2,x+19,y+10,z+19,air)
    mc.setBlocks(x+1,y+11,z+1,x+20,y+11,z+20,wood)


def build_village(x,y,z):
    build_house(x+50,y,z+50)
    build_house(x+27,y,z+27)
    build_house(x+50,y,z+27)
    build_house(x+27,y,z+50)
    
t.sleep(1)
build_village(x,y,z)

