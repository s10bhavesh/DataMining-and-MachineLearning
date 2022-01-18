#Read data from data base
import math
import numpy as np
import matplotlib.pyplot as plt 
import dtw as dtw

def z_score(x=[],y=[]):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_std = []
    y_std = []
    x_norm = []
    y_norm = []
    sumX=0
    sumY=0
    
    for i in x:
        sumX = sumX + ((i-x_mean)**2)
        
    x_std = math.sqrt((sumX)/len(x))
        
    for j in y:
        sumY = sumY + ((j-y_mean)**2)
        
    y_std = math.sqrt((sumX)/len(y))
    

    for i in x:
        x_norm.append((i-x_mean)/x_std)
        
    for j in y:
        y_norm.append((j-y_mean)/y_std)
        
    return x_norm, y_norm

def return_array(data):
        plotX = []
        plotY = []
        for t in data:
            #print(t.split(' '))
            num = t.split(' ')
            plotX.append(int(num[0]))
            plotY.append(int(num[1]))
        normX, normY = z_score(plotX, plotY)
        npX = np.array(normX)
        npY = np.array(normY)
        return np.vstack((npX,npY)).T
           
username = input("Enter user name to test : ")
username.upper()
#username = "U1S1"
signatureDB = open(f"Shiv\\Task2\\Task2\\{username}.TXT","r")
count = signatureDB.readline()
content = signatureDB.readlines()
S1 =  return_array(content)

distGen = 0
distFake = 0
for i in range(1,6):
    username2 = f"U1S{i}"
    signatureDB2 = open(f"Shiv\\Task2\\Task2\\{username2}.TXT","r")
    count = signatureDB2.readline()
    content2 = signatureDB2.readlines()
    S2 =  return_array(content2)  
    euclidean_norm = lambda S1,S2: math.sqrt((S1[0]-S2[0])**2 + (S1[1]-S2[1])**2) 
    a,b,c,d = dtw.dtw(S1,S2,dist=euclidean_norm)
    distGen = distGen + a
    signatureDB2.close()

avgDistGen = distGen / 5

for i in range(21,26):
    username2 = f"U1S{i}"
    signatureDB2 = open(f"Shiv\\Task2\\Task2\\{username2}.TXT","r")
    count = signatureDB2.readline()
    content3 = signatureDB2.readlines()
    S3 =  return_array(content3)  
    euclidean_norm = lambda S1,S3: math.sqrt((S1[0]-S3[0])**2 + (S1[1]-S3[1])**2) 
    a1,b,c,d = dtw.dtw(S1,S2,dist=euclidean_norm)
    distFake = distFake + a1
    signatureDB2.close()

avgDistFake = distFake / 5

print(avgDistFake -  avgDistGen)

if((avgDistFake -  avgDistGen) < 0):
    print(f"{username} is genuine signature.")
else:
    print(f"{username} is forged signature.")
    

  




