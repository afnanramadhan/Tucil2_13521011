from fungsi import *
import time

def main():
    showASCIIART()
    print("\n---------------------------------------------------")
    print("Masukkan jumlah titik: ")
    n = int(input())
    print("Masukkan dimensi: ")
    d = int(input())
    myList = createDots(n,d)
    myList.sort()
    
    startd = time.time()
    dnc,t1,t2 = findMinDivideConquer(myList)
    endd = time.time()
    
    print("---------------------------------------------------")
    print("div n con \t:", dnc)
    print("time\t\t:", endd-startd, "second")
    
    print("---------------------------------------------------")

    startb = time.time()
    bf = findMinBruteForce(myList)[0]
    endb = time.time()
    print("brute force \t:",bf)
    print("time\t\t:", endb-startb, "second")
    print("---------------------------------------------------")
    
    print("Euclidian count = ", countOperation())


    vis = input("Mau nampilin visual? (y/n) ")
    if(vis == 'y' or vis == 'Y'):
        if(d<=3):
            if(n>=1000):
                vis = input("Yakin mau nampilin visual?(ngelag banget ntar) (y/n) ")
                if(vis == 'y' or vis == 'Y'):
                    print("SIAPPPPP")
                    print("Resiko ditanggung sendiri")
                    showVisual(d,myList,t1,t2,dnc)
            else:
                showVisual(d,myList,t1,t2,dnc)
        else:
            print("MAAF VISUALISASI TIDAK DAPAT DITAMPILKAN")
            print("KARENA DIMENSI MELEBIHI 3")
    
    print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")    
        
    
if __name__ == "__main__":
    main()