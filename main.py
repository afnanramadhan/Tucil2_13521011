from fungsii import *
import time

def main():
    showASCIIART()
    print("\n---------------------------------------------------")
    print("Masukkan jumlah titik: ")
    n = int(input())
    print("Masukkan dimensi: ")
    d = int(input())

    lll = createDots(n,d)
    lll.sort()

    

    startd = time.time()
    b,t1,t2 = findMinDivideConquer(lll)
    endd = time.time()
    print("---------------------------------------------------")
    print("div n con \t:", end=" ")
    print(b)
    print("time\t\t:", endd-startd, "second")
    print("---------------------------------------------------")

    startb = time.time()
    a,titik1,titik2 = findMinBruteForce(lll)
    endb = time.time()
    print("brute force \t:", end=" ")
    print(a)
    print("time\t\t:", endb-startb, "second")
    print("---------------------------------------------------")


    vis = input("Mau nampilin visual? (y/n) ")
    if(vis == 'y' or vis == 'Y'):
        if(d<=3):
            if(n>=1000):
                vis = input("Yakin mau nampilin visual?(ngelag banget ntar) (y/n) ")
                if(vis == 'y' or vis == 'Y'):
                    print("SIAPPPPP")
                    print("Resiko ditanggung sendiri")
                    showVisual(d,lll,t1,t2,b)
            else:
                showVisual(d,lll,t1,t2,b)
        else:
            print("MAAF VISUALISASI TIDAK DAPAT DITAMPILKAN")
            print("KARENA DIMENSI MELEBIHI 3")
    
    print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")    
        
    
if __name__ == "__main__":
    main()