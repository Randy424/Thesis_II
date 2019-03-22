import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
from load_dataset import load_data_custom, load_data
from sklearn.preprocessing import LabelEncoder


flags, atmospheric_pressure = load_data()
sst = load_data_custom('TS')
at = load_data_custom('T')
time = load_data_custom('time')



#print(at)
pressure_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 10]

sst_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 13]

at_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 11]

at_f = set(at_flags)
print(at_f)

#label encoding
le = LabelEncoder()
int_encoding_temp = le.fit_transform(at_flags)
print(le.classes_, "\n")



x = time
y = at
labels = int_encoding_temp
color = labels

df = pd.DataFrame(dict(time_x=time, temperature_y=at, color=color))

fig, ax = plt.subplots()

colors = {0:'yellow', 1:'orange', 2:'green'}

ax.scatter(df['time_x'], df['temperature_y'], c=df['color'].apply(lambda x: colors[x]))

plt.title('temperature x time' )
plt.show()
