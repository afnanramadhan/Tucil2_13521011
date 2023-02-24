
import random
import matplotlib.pyplot as plt
import numpy as np
import math
import sys

def createDots(n,d):
    #n jumlah titik
    #d dimensi
    listt = []
    for i in range(n):
        temp = []
        for j in range(d):
            a = random.randint(0,99999)
            temp.append(a)
        listt.append(temp)
    return listt

def printList(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end=" ")
        print("")

def show3dAll(list,ax):
    for i in range(len(list)):
        xs = list[i][0]
        ys = list[i][1]
        zs = list[i][2]
        ax.scatter(xs, ys, zs, color='blue')
       
def showNearestDots(list,i,j,ax):
    xs = list[i][0]
    ys = list[i][1]
    zs = list[i][2]
    xx = list[j][0]
    yy = list[j][1]
    zz = list[j][2]
    ax.scatter(xs, ys, zs, color='red')
    ax.scatter(xx, yy, zz, color='red')
        
        
def drawLine(list,i,j,ax):
    x = np.array([list[i][0], list[j][0]])
    y = np.array([list[i][1], list[j][1]])
    z = np.array([list[i][2], list[j][2]])
    ax.plot3D(x, y, z, color='red')
    
def hitungJarak(list,i,j):
    #i dan j indeks di list
    x1 = list[i][0]
    x2 = list[j][0]
    y1 = list[i][1]
    y2 = list[j][1]
    z1 = list[i][2]
    z2 = list[j][2]
    jarak = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return jarak

def findMinBruteForce(list):
    min = sys.maxsize
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            # print(i,j,hitungJarak(list,i,j))
            temp = hitungJarak(list,i,j)
            if temp < min:
                min = temp
                titik1 = i
                titik2 = j
    return min,titik1,titik2

def splitList(list):
    n = len(list)//2
    if(n%2==0):
        return list[:n],list[n:]
    else:
        return list[:n],list[n+1:]

def findMinDivideConquer(list,n):
    #n paling
    if(len(list)==n):
        return hitungJarak(list,0,1)
    elif(len(list)==n+1):
        return findMinBruteForce(list)[0]
    else:
        l1,l2 = splitList(list)
        d1 = findMinDivideConquer(l1,n)
        d2 = findMinDivideConquer(l2,n)
        d = min(d1,d2)
        
        #cek apakah ada titik yang ada di daerah -d dan +d
        #sekalian dimasukkin ke list temporary
        temp = []
        for i in list:
            if(i[0]>= len(list)/2-d and i[0]<= len(list)/2+d):
                temp.append(i)
                
        #cari minimum jarak yang ada di daerah -d dan +d
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                if(abs(temp[i][0]-temp[j][0])>d or abs(temp[i][1]-temp[j][1])>d or abs(temp[i][2]-temp[j][2])>d):
                    continue
                else:
                    d3 = hitungJarak(temp,i,j)
                    if(d3<d):
                        d = d3                 
        return d
    
def jalan():
    print("Masukkan jumlah titik: ")
    n = int(input())

    lll = createDots(n,3)
    printList(lll)
    print("")
    lll.sort()
    printList(lll)
    print("")

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    print("-----------------------")
    min,titik1,titik2 = findMinBruteForce(lll)
    print("-----------------------")
    print("Jarak terdekat: ")
    print(min)
    print(titik1)
    print(titik2)

    show3dAll(lll,ax)
    showNearestDots(lll,titik1,titik2,ax)
    drawLine(lll,titik1,titik2,ax)

    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.set_zlabel('Sumbu Z')
    plt.show()
    

