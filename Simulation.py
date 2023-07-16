import pybullet as p
import pybullet_data
import time



#Create world
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#Get rid of sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

#Add gravity
p.setGravity(0,0,-9.8)

#Add a floor
planeId = p.loadURDF("plane.urdf")

#Add a box
p.loadSDF("boxes.sdf")

#Run the simulation
for i in range(0, 1000):
    print(i)
    p.stepSimulation()
    time.sleep(1/60)

#Disconnect world
p.disconnect()
