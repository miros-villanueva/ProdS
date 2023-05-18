import math
import numpy as np
from TypeofStimuli import *
import matplotlib.pyplot as plot

Sample_freq = 200000
Time_interval = 1/Sample_freq
Frequency = 7000
Period = 1/Frequency
Duty_cycle = 0.25
Time_frame = np.arange(0, Period, Time_interval)
Pulse_width = Duty_cycle * Period
Dots_per_cycle = Sample_freq/Frequency
time = np.arange(0, (Period+Time_interval), (Time_interval))

Amplitude = np.arange(1E-6, 15E-6, 0.05E-6)
Electrode_radius = np.arange(1E-6, 15E-6, 0.1E-6)
#CONSTANTS, RESISTANCE, CAPACITANCE, TAO

RM = 30000
Rm = 10000
Cm = 10E-9
tao = Rm/Cm 

#x = ExpWave(Pulse_width, Period, Amplitude[0], Time_interval)
#plot.plot(time, x)
#plot.show()

#Select Type of Stimulus for Simulation
#Sine = 1, Rectangular = 2, LinealIncrease = 3, Exponential = 4
Type_of_stimulus = 1
Array1 = []

for i in range(len(Electrode_radius)):
    
    for j in range(len(Amplitude)):
        
        if Type_of_stimulus == 1:
            x = SineWave(Amplitude[j], Frequency, Period, Time_interval, Pulse_width)
        elif Type_of_stimulus ==2:
            x = RectWave(Pulse_width, Period, Amplitude[j], Time_interval)
        elif Type_of_stimulus == 3:
            x = LinWave(Pulse_width, Period, Amplitude[j], Time_interval)
        elif Type_of_stimulus == 4:
            x = ExpWave(Pulse_width, Period, Amplitude[j], Time_interval)
        else:
            print("Not a valid option")
        Array1.append(x)




print(len(Array1))