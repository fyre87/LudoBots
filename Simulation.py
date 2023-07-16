import pybullet as p
import time

#Create world
physicsClient = p.connect(p.GUI)
#Get rid of sidebars
#åp.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

#Add a box
p.loadSDF("box.sdf")
for i in range(0, 1000):
    print(i)
    p.stepSimulation()
    time.sleep(1/60)

#Disconnect world
p.disconnect()
