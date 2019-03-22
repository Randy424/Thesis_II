import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from load_dataset import load_data_custom, load_data



flags, atmospheric_pressure = load_data()
sst = load_data_custom('TS')
at = load_data_custom('T')
#print(at)
pressure_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 10]

sst_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 13]

at_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 11]

side_by_side = list(zip(at, atmospheric_pressure, at_flags, pressure_flags))

#print(side_by_side)
#Z cleared data
cleared_p_data = []
cleared_at_data = []

#K flagged data
flagged_p_data = []
flagged_at_data = []
data_good = []
data_both_sus = []
t_sus = []
p_sus = []


for i in side_by_side:
    if i[2] == b'K' and i[3] == b'Z':
        cleared_p_data.append(i[1])
        flagged_at_data.append(i[0])
        t_sus.append((i[0], i[1]))
    elif i[3] == b'K' and i[2] == b'Z':
        cleared_at_data.append(i[0])
        flagged_p_data.append(i[1])
        p_sus.append((i[0], i[1]))
    elif i[2] == b'Z' and i[3] == b'Z':
        data_good.append((i[0], i[1]))
        cleared_at_data.append(i[0])
        cleared_p_data.append(i[1])
    elif i[2] == b'K' and i[3] == b'K':
        data_both_sus.append((i[0], i[1]))
        flagged_p_data.append(i[1])
        flagged_at_data.append(i[0])
        p_sus.append((i[0], i[1]))
        t_sus.append((i[0], i[1]))

print("good air temp data (Z)", len(cleared_at_data))
print("suspicous air temp data (K)", len(flagged_at_data))

print("good pressure data (Z)", len(cleared_p_data))
print("suspicous pressure data (K)", len(flagged_p_data))
"""
#data_good = zip(cleared_at_data, cleared_p_data)
#bad_data = zip(flagged_at_data, flagged_p_data)

data = (data_good, data_both_sus, p_sus)

colors = ("green", "red", "orange")
groups = ("good data", "both data points suspicious",
"pressure suspicious")

colors = (0,0,0)
area = np.pi*3
 
x, y = zip(*data_good)

# Plot
plt.scatter(x, y, s=area, c="green", alpha=0.5)
plt.title('Good pressure x temputure reading')
plt.xlabel('temperature')
plt.ylabel('pressure')
plt.show()
"""