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

    startb = time.time()
    a,titik1,titik2 = findMinBruteForce(lll)
    endb = time.time()

    startd = time.time()
    b = (findMinDivideConquer(lll,2))
    endd = time.time()

    

    print("---------------------------------------------------")
    print("brute force \t:", end=" ")
    print(a)
    print("time\t\t:", endb-startb, "second")
    print("---------------------------------------------------")
    print("div n con \t:", end=" ")
    print(b)
    print("time\t\t:", endd-startd, "second")
    print("---------------------------------------------------")

    vis = input("Mau nampilin visual? (y/n) ")
    if(vis == 'y' or vis == 'Y'):
        if(n>=1000):
            vis = input("Yakin mau nampilin visual?(ngelag banget ntar) (y/n) ")
            if(vis == 'y' or vis == 'Y'):
                print("SIAPPPPP")
                print("Resiko ditanggung sendiri")
                showVisual(d,lll,titik1,titik2,b)
        else:
            showVisual(d,lll,titik1,titik2,b)
    else:
        print("TERIMAKASIH")
    
if __name__ == "__main__":
    main()