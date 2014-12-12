import mcpi.minecraft as minecraft,time as t
mc = minecraft.Minecraft.create()#sets up instance

mc.setBlocks(-60,-20,-60,60,60,60,0)#sets a large cube of air

for b in range (4,20,5):#sets up a finite loop
    mc.postToChat(b)#posts a number to chat
    mc.setBlock(0,b,0,35,b)#sets a block to varing materials
    t.sleep(2)
