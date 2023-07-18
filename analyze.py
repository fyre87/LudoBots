import numpy as np
import matplotlib.pyplot as plt

#Load stored data
backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

#Plot it
plt.plot(backLegSensorValues, label = "Back Leg Sensor")
plt.plot(frontLegSensorValues, label = "Front leg sensor")

plt.legend()
plt.show()
