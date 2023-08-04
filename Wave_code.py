from statistics import mean
import numpy as np
from scipy.optimize import curve_fit
import math
f=open("Desktop/sample-data.txt", "r")
list1 = []
list_wave = []
list_wave_max = []
list_amp = []
list_pos_amp = []
for line in f:
    line=line.strip()
    nums=line.split()
    list1.append(nums)
if float(list1[0][1])<0:
    while len(list1) != 0:
        for x in list1:
            if float(x[1])<=0:
                list_wave.append(x)
            else:
                break
        for x in list_wave:
            list_wave_max.append(abs(float(x[1])))
        maxi = max(list_wave_max)
        for x in list_wave:
            if abs(float(x[1])) == maxi:
                x[0] = float(x[0])
                x[1] = abs(float(x[1]))
                list_amp.append(x)
        for x in list_wave:
            list1.remove(x)
        list_wave.clear()
        list_wave_max.clear()
        if len(list1) == 0:
            break
        for x in list1:
            if float(x[1])>=0:
                list_wave.append(x)
            else:
                break
        for x in list_wave:
            list_wave_max.append(abs(float(x[1])))
        maxi = max(list_wave_max)
        for x in list_wave:
            if abs(float(x[1])) == maxi:
                x[0] = float(x[0])
                x[1] = abs(float(x[1]))
                list_amp.append(x)
                list_pos_amp.append(x)
        for x in list_wave:
            list1.remove(x)
        list_wave.clear()
        list_wave_max.clear()
else:
    while len(list1) != 0:
        for x in list1:
            if float(x[1])>=0:
                list_wave.append(x)
            else:
                break
        for x in list_wave:
            list_wave_max.append(abs(float(x[1])))
        maxi = max(list_wave_max)
        for x in list_wave:
            if abs(float(x[1])) == maxi:
                x[0] = float(x[0])
                x[1] = abs(float(x[1]))
                list_amp.append(x)
                list_pos_amp.append(x)
        for x in list_wave:
            list1.remove(x)
        list_wave.clear()
        list_wave_max.clear()
        if len(list1) == 0:
            break
        for x in list1:
            if float(x[1])<=0:
                list_wave.append(x)
            else:
                break
        for x in list_wave:
            list_wave_max.append(abs(float(x[1])))
        maxi = max(list_wave_max)
        for x in list_wave:
            if abs(float(x[1])) == maxi:
                x[0] = float(x[0])
                x[1] = abs(float(x[1]))
                list_amp.append(x)
        for x in list_wave:
            list1.remove(x)
        list_wave.clear()
        list_wave_max.clear()
for x in list_amp:
    x[1]="{:f}".format(x[1])
def ave(num1, num2):
    list_=[]
    for x in list_amp:
        if num1 < float(x[0]) <= num2:
            list_.append(float(x[1]))
    ave = mean(list_)
    return ave
ave1 = ave(0, 0.1)
ave2 = ave(0.1, 0.2)
ave3 = ave(0.2, 0.3)
ave4 = ave(0.3, 0.4)
ave5 = ave(0.4, 0.5)
ave6 = ave(0.5, 0.6)
ave7 = ave(0.6, 0.7)
ave8 = ave(0.7, 0.8)
ave9 = ave(0.8, 0.9)
ave10 = ave(0.9, 1)
l=[ave1, ave2, ave3, ave4, ave5, ave6, ave7, ave8, ave9, ave10]
x_data=[]
num=0.05
for i in range(10):
    x_data.append(num)
    num+=0.10
x_data=np.array(x_data)
y_data=[]
for obj in l:
    y_data.append(obj)
y_data=np.array(y_data)
def func(x, a):
    return a/x
popt, pcov=curve_fit(func, x_data, y_data)
print("Average 'a' value of best fit function: "+str(round(popt[0], 6)))
for x in list_pos_amp:
    x[1]=float(x[1])
    x[1]="{:f}".format(x[1])
def log_dec(min, max):
    l_range_amps=[]
    l_log_dec=[]
    for x in list_pos_amp:
        if x[0]>min and x[0]<=max:
            l_range_amps.append(x[1])
    for i in range(len(l_range_amps)-1):
        if l_range_amps[i]>l_range_amps[i+1]:
            l_log_dec.append(math.log(float(l_range_amps[i])/float(l_range_amps[i+1])))
    return mean(l_log_dec)
log_dec_1=log_dec(0, 0.1)
log_dec_2=log_dec(0.1, 0.2)
log_dec_3=log_dec(0.2, 0.3)
log_dec_4=log_dec(0.3, 0.4)
log_dec_5=log_dec(0.4, 0.5)
log_dec_6=log_dec(0.5, 0.6)
log_dec_7=log_dec(0.6, 0.7)
log_dec_8=log_dec(0.7, 0.8)
log_dec_9=log_dec(0.8, 0.9)
log_dec_10=log_dec(0.9, 1)
l_log_decs=[log_dec_1, log_dec_2, log_dec_3, log_dec_4, log_dec_5, log_dec_6, log_dec_7, log_dec_8, log_dec_9, log_dec_10]
ave_log_dec=mean(l_log_decs)
print("Average δ: "+str(round(ave_log_dec, 6)))
def zeta(log_dec):
    zeta=log_dec/(math.sqrt(4*pow(math.pi, 2)+pow(log_dec, 2)))
    return zeta
ave_zeta=zeta(ave_log_dec)
print("Average ζ: "+str(round(ave_zeta, 6)))
f.close()
