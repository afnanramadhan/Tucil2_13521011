
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
        
def show2dAll(list):
    for i in range(len(list)):
        x = list[i][0]
        y = list[i][1]
        plt.scatter(x, y, color='blue')
    
def showNearestDots2D(list,i,j):
    x1 = list[i][0]
    x2 = list[j][0]
    y1 = list[i][1]
    y2 = list[j][1]
    plt.scatter(x1, y1, color='red')
    plt.scatter(x2, y2, color='red')
    
def drawLine2D(list,i,j):
    x = np.array([list[i][0], list[j][0]])
    y = np.array([list[i][1], list[j][1]])
    plt.plot(x, y, color='red')
    
    

def show3dAll(list,ax):
    for i in range(len(list)):
        xs = list[i][0]
        ys = list[i][1]
        zs = list[i][2]
        ax.scatter(xs, ys, zs, color='blue')
       
def showNearestDots3D(list,i,j,ax):
    xs = list[i][0]
    ys = list[i][1]
    zs = list[i][2]
    xx = list[j][0]
    yy = list[j][1]
    zz = list[j][2]
    ax.scatter(xs, ys, zs, color='red')
    ax.scatter(xx, yy, zz, color='red')
        
        
def drawLine3D(list,i,j,ax):
    x = np.array([list[i][0], list[j][0]])
    y = np.array([list[i][1], list[j][1]])
    z = np.array([list[i][2], list[j][2]])
    ax.plot3D(x, y, z, color='red')
    
def hitungJarak(list,i,j):
    #i dan j indeks di list
    sum = 0
    for k in range(len(list[0])):
        sum+= (list[i][k]-list[j][k])**2
    jarak = math.sqrt(sum)
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

def findMinDivideConquer(list):
    #pembagian terkecil sisa 2 titik
    if(len(list)==2):
        return hitungJarak(list,0,1)
    elif(len(list)==3):
        return findMinBruteForce(list)[0]
    else:
        l1,l2 = splitList(list)
        d1 = findMinDivideConquer(l1)
        d2 = findMinDivideConquer(l2)
        d = min(d1,d2)
        
        tengah = len(list)//2
        if(len(list)%2==0):
            avg = (list[tengah][0]+list[tengah+1][0])/2
        else:
            avg = (list[tengah-1][0]+list[tengah+1][0])/2
        #cek apakah ada titik yang ada di daerah -d dan +d
        #sekalian dimasukkin ke list temporary
        temp = []
        for i in list:
            if(i[0]>= avg-d and i[0]<= avg+d):
                temp.append(i)
                
        #cari minimum jarak yang ada di daerah -d dan +d
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                for k in range(1,len(temp[0])):
                    ##abs(temp[i][0]-temp[j][0])>d or abs(temp[i][1]-temp[j][1])>d or abs(temp[i][2]-temp[j][2])>
                    if(temp[i][k]-temp[j][k]>d):
                        flag = False
                        break
                    else:
                        flag = True
                if(flag):
                    d3 = hitungJarak(temp,i,j)
                    if(d3<d):
                        d = d3                 
        return d
    
def showVisual(dim,list,titik1,titik2,distance):
    #d dimensi
    #titik1 dan titik2 indeks di list
    if(dim==2):
        print("2D")
        show2dAll(list)
        showNearestDots2D(list,titik1,titik2)
        drawLine2D(list,titik1,titik2)
        plt.annotate(round(distance), xy=((list[titik1][0]+list[titik2][0])/2, (list[titik1][1]+list[titik2][1])/2))
        plt.xlabel("Sumbu X")
        plt.ylabel("Sumbu Y")
        plt.show()
        
    elif(dim==3):
        print("3D")
        ax = plt.axes(projection='3d')
        show3dAll(list,ax)
        showNearestDots3D(list,titik1,titik2,ax)
        drawLine3D(list,titik1,titik2,ax)
        ax.set_xlabel('Sumbu X')
        ax.set_ylabel('Sumbu Y')
        ax.set_zlabel('Sumbu Z')
        plt.show()
    else:
        print("MAAF TIDAK DAPAT DITAMPILKAN")
        
def showASCIIART(): 
    print("       ___       _     __        ___    ")
    print("  ____/ (_)   __(_)___/ /__     ( _ )")
    print(" / __  / / | / / / __  / _ \   / __ \/|")
    print("/ /_/ / /| |/ / / /_/ /  __/  / /_/  <")
    print("\__,_/_/ |___/_/\__,_/\___/   \____/\/")
    print("  _________  ____  ____ ___  _____  _____")
    print(" / ___/ __ \/ __ \/ __ `/ / / / _ \/ ___/")
    print("/ /__/ /_/ / / / / /_/ / /_/ /  __/ /")
    print("\___/\____/_/ /_/\__, /\__,_/\___/_/")
    print("                   /_/")