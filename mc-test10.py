import mcpi.minecraft as minecraft,time as t
mc = minecraft.Minecraft.create()#sets up instance

mc.setBlocks(-30,-5,-30,60,60,60,0)#sets a large cube of air

for b in range (4,20,5):#sets up a finite loop
