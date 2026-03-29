import numpy as np
import tempfile

#creating the data structure
weather_structure=np.dtype([('day',np.int64),('temperature',np.float64),('humidity',np.float64)])
fname=tempfile.mkstemp()[1]
#creating the data 
data=np.array([(1,22.5,60.0),(2,19.3,75.5),(3,19.3,75.5),(3,25.1,55.2),(4,17.8,80.0),(5,23.0,65.3)],dtype=weather_structure)
#storing the data
data.tofile(fname)
np.fromfile(fname,dtype=weather_structure)
np.save(fname,data)
#loading the data
load=np.load(fname + ".npy")
#showing off the AVG temperature in these 6 days
total=0
for row in load:
    total+=row['temperature']
avg_temperature=total/len(load)
#showing the avg temperature
print("AVG temperature from the 6 collected days was ",avg_temperature)



