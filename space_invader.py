#space invader by oskar gardner 
import time as t,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def si(x,y,z):#builds a space invader
    mc.setBlocks(x+1,y,z,x+13,y+10,z,35,15)
    mc.setBlocks(x+4,y+3,z,x+10,y+7,z,35,0)
    mc.setBlock(x+4,y+2,z,35,0)
    mc.setBlock(x+10,y+2,z,35,0)
    mc.setBlocks(x+5,y+1,z,x+6,y+1,z,35,0)
    mc.setBlocks(x+8,y+1,z,x+9,y+1,z,35,0)
    mc.setBlocks(x+2,y+3,z,x+2,y+5,z,35,0)
    mc.setBlocks(x+12,y+3,z,x+12,y+5,z,35,0)
    mc.setBlocks(x+3,y+5,z,x+3,y+6,z,35,0)
    mc.setBlocks(x+11,y+5,z,x+11,y+6,z,35,0)
    mc.setBlock(x+5,y+6,z,35,15)
    mc.setBlock(x+9,y+6,z,35,15)
    mc.setBlock(x+5,y+8,z,35,0)
    mc.setBlock(x+9,y+8,z,35,0)
    mc.setBlock(x+4,y+9,z,35,0)
    mc.setBlock(x+10,y+9,z,35,0)
def si_a(x,y,z):#animates the space invader
    while True:
        mc.setBlocks(x+2,y+5,z,x+2,y+8,z,35,15)
        mc.setBlocks(x+12,y+5,z,x+12,y+8,z,35,15)
        mc.setBlocks(x+2,y+3,z,x+2,y+5,z,35,0)
        mc.setBlocks(x+12,y+3,z,x+12,y+5,z,35,0)
        t.sleep(1)
        mc.setBlocks(x+2,y+3,z,x+2,y+5,z,35,15)
        mc.setBlocks(x+12,y+3,z,x+12,y+5,z,35,15)
        mc.setBlocks(x+2,y+5,z,x+2,y+8,z,35,0)
        mc.setBlocks(x+12,y+5,z,x+12,y+8,z,35,0)
        t.sleep(1)
def si_s(x,y,z):#failing to add extra functions
    mc.setBlocks(x+7,y+1,z,x+7,y,z,35,0)
def si_i(x,y,z):#builds 4 space invaders and animates them
    si(x,y,z)
    si(x+14,y,z)
    si(x,y+12,z)
    si(x+14,y+12,z)

def si_ia(x,y,z):#builds 16 space invaders
    si_i(x,y,z)
    si_i(x+28,y,z)
    si_i(x,y+24,z)
    si_i(x+28,y+24,z)
    
si_ia(x,y,z)#calls for the building of 16 space invaders
si_a(x,y,z)#calls for the animation of one of the space invaders


