
import random
import matplotlib.pyplot as plt
import numpy as np
import math

def createDots(n):
    listt = []
    for i in range(n):
        temp = []
        for j in range(3):
            a = random.randint(0,99)
            temp.append(a)
        listt.append(temp)
    return listt

def printList(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end=" ")
        print("")

def show3dAll(list):
    for i in range(n):
        xs = lll[i][0]
        ys = lll[i][1]
        zs = lll[i][2]
        ax.scatter(xs, ys, zs, color='blue')
       
def showNearestDots(list,i,j):
    xs = lll[i][0]
    ys = lll[i][1]
    zs = lll[i][2]
    xx = lll[j][0]
    yy = lll[j][1]
    zz = lll[j][2]
    ax.scatter(xs, ys, zs, color='red')
    ax.scatter(xx, yy, zz, color='red')
        
        
def drawLine(list,i,j):
    x = np.array([lll[i][0], lll[j][0]])
    y = np.array([lll[i][1], lll[j][1]])
    z = np.array([lll[i][2], lll[j][2]])
    ax.plot3D(x, y, z, color='red')
    
def hitungJarak(list,i,j):
    x1 = list[i][0]
    x2 = list[j][0]
    y1 = list[i][1]
    y2 = list[j][1]
    z1 = list[i][2]
    z2 = list[j][2]
    jarak = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return jarak

def findMin(list):
    min = hitungJarak(list,0,1)
    titik1 = 0
    titik2 = 1
    for i in range(n):
        for j in range(n):
            if(i!=j):
                print(i,j,hitungJarak(list,i,j))
                if hitungJarak(list,i,j) < min:
                    min = hitungJarak(list,i,j)
                    titik1 = i
                    titik2 = j
    return min,titik1,titik2

print("Masukkan jumlah titik: ")
n = int(input())

lll = createDots(n)
printList(lll)

fig = plt.figure()
ax = plt.axes(projection='3d')

print("-----------------------")
min,titik1,titik2 = findMin(lll)
print("-----------------------")
print("Jarak terdekat: ")
print(min)
print(titik1)
print(titik2)

show3dAll(lll)
showNearestDots(lll,titik1,titik2)
drawLine(lll,titik1,titik2)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()