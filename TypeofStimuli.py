
import numpy as np
import math

array = []

#Biphasic Sine Wave Generator Function
def SineWave(Amplitude, Frequency, Period, Time_interval, Pulse_width):
    time = np.arange(0, (Period+Time_interval), (Time_interval))
    for i in range(len(time)):
        if time[i] < Pulse_width:
            y = Amplitude * np.sin(4*np.pi*Frequency*time[i])
            array.append(y)
        elif time[i] >= Pulse_width and time[i] <= Pulse_width * 2:
            y = Amplitude * np.sin(4*np.pi*Frequency*time[i])
            array.append(y)
        elif time[i] >= Pulse_width * 2:
            y = 0
            array.append(y)
    return array

#Biphasic Rectangular Wave Generator Function
def RectWave(Pulse_width, Period, Amplitude, Time_interval):
    time = np.arange(0, (Period+Time_interval), (Time_interval))
    for i in range(len(time)):
        if time[i] <= Pulse_width:
            y = Amplitude
            array.append(y)
        elif time[i] > Pulse_width and time[i] <= Pulse_width*2:
            y = -Amplitude
            array.append(y)
        elif time[i] > Pulse_width*2:
            y = 0
            array.append(y)
    return array

#Biphasic Linear Wave Generator Function
def LinWave(Pulse_width, Period, Amplitude, Time_interval):
    time = np.arange(0, (Period+Time_interval), (Time_interval))
    for i in range(len(time)):
        if time[i] <= Pulse_width:
            y = (Amplitude/Pulse_width)*time[i]
            array.append(y)
        elif time[i] > Pulse_width and time[i] <= Pulse_width*2:
            y = ((-Amplitude/Pulse_width)*time[i]) + Amplitude
            array.append(y)
        elif time[i] > Pulse_width*2:
            y = 0
            array.append(y)
    return array

#Biphasic Exponential Wave Generator Function
def ExpWave(Pulse_width, Period, Amplitude, Time_interval):
    time = np.arange(0, (Period+Time_interval), (Time_interval))
    for i in range(len(time)):
        if time[i] <= Pulse_width:
            y = Amplitude * (math.e**(-5*(Pulse_width-time[i])/Pulse_width))
            array.append(y)
        elif time[i] > Pulse_width and time[i] <= Pulse_width*2:
            y = -Amplitude * (0.00666 * math.e**(-5*(Pulse_width-time[i])/Pulse_width))
            array.append(y)
        elif time[i] > Pulse_width*2:
            y = 0
            array.append(y)
    return array