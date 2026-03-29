import numpy as np
import tempfile

#creating the data structure
weather_structure=np.dtype([('day',np.int64),('temperature',np.float64),('humidity',np.float64)])
fname=tempfile.mkstemp()[1]
#creating the data 
data=np.array([(1,22.5,60.0),(2,19.3,75.5),(3,19.3,75.5),(4,25.1,55.2),(5,17.8,80.0),(6,23.0,65.3)],dtype=weather_structure)
#storing the data
data.tofile(fname)
np.fromfile(fname,dtype=weather_structure)
np.save(fname,data)
#loading the data
load=np.load(fname + ".npy")
#showing off the AVG,min,max temperature in these 6 days
max_day=np.argmax(load['temperature'])+1
max_temperature=load['temperature'][max_day]
min_day=np.argmin(load['temperature'])+1
min_temperature=load['temperature'][min_day]
avg_temperature=np.mean(load['temperature'])
#showing the stats of the  temperature
print("AVG temperature from the 6 collected days was: ",avg_temperature)
print("maximun temperature was: ",max_temperature," on day ",max_day)
print("minimun temperature was: ",min_temperature,"on day",min_day)


