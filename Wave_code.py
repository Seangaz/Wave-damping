from statistics import mean
import numpy as np
from scipy.optimize import curve_fit
f=open("Desktop/sample-data2.txt", "r")
f2=open("Desktop/times.txt", "w")
f3=open("Desktop/amplitudes.txt", "w")
list1 = []
list_wave = []
list_wave_max = []
list_amp = []
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
    f2.write(str(x[0])+"\n")
    f3.write(str(x[1])+"\n")
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
f4=open("Desktop/ave_time.txt", "w")
f5=open("Desktop/ave_amp.txt", "w")
num=0.05
for i in range(10):
    f4.write(str(num)+"\n")
    f5.write(str(l[i])+"\n")
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
print("The 'a' value of best fit function is: "+str(round(popt[0], 6)))
f.close()
f2.close()
f3.close()
f4.close()
f5.close()
