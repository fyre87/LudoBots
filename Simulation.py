import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import time



#Create world
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#Get rid of sidebars
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

#Add gravity
p.setGravity(0,0,-9.8)

#Read files::
planeId = p.loadURDF("plane.urdf") #Floor
robotId = p.loadURDF("body.urdf") #Robot

#Add a box
p.loadSDF("world.sdf")

#Prepare to use sensors
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000) #Store sensor values
frontLegSensorValues = np.zeros(1000)


#Run the simulation
for i in range(0, 1000):
    print(i)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/120)

#Disconnect world
p.disconnect()

#Print results
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
