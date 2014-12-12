import time as t,mcpi.minecraft as minecraft,random as ran
mc = minecraft.Minecraft.create()
while True:
    t.sleep(1)
    mc.postToChat("3")
    t.sleep(1)
    mc.postToChat("2")
    t.sleep(1)
    mc.postToChat("1")
    t.sleep(1)
    mc.postToChat("Teleporting...")
    mc.player.getPos(
    t.sleep(0.5)
    mc.postToChat("Teleported")
