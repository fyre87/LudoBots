import pybullet as p
import time

#Create world
physicsClient = p.connect(p.GUI)
#Get rid of sidebars
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

for i in range(0, 1000):
    print(i)
    p.stepSimulation()
    time.sleep(1/60)

#Disconnect world
p.disconnect()
