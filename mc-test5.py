import time as t,mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()
mc.postToChat("Activating Tunnel God...")
while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    glass = 20
    water = 9
    mc.setBlocks(x-1, y, z-1, x+1, y+1 ,z+1, 0)
    t.sleep(0.1)
    
    

