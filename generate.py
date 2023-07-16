import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("boxes.sdf")

scale = 1
for k in range(0, 5):
    for j in range(0, 5):
        for i in range(0, 10):
            pyrosim.Send_Cube(name="Box", pos=[x+j,y+k,z+i] , size=[length*scale,width*scale,height*scale])
            scale = scale * 0.9
        scale = 1
pyrosim.End()
