import time as t,mcpi.minecraft as minecraft,random
mc = minecraft.Minecraft.create()
while True:
	pos = mc.player.getPos()
	x = int(pos.x)
	y = pos.y
	z = int(pos.z)
	gravel = 13
	xg = random.randint(x-10,x+10)
	yg = y+50
	zg = random.randint(z-10,z+10)
	mc.setBlock(xg ,yg ,zg ,gravel)
	

