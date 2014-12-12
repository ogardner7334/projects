import time as t,mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()
mc.postToChat("activating fall protection...")
while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    if y < -10:
        mc.player.setPos(x, y+20, z)
    
