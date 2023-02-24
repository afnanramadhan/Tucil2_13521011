from fungsii import *
import time

# jalan()
print("Masukkan jumlah titik: ")
n = int(input())
# # print("Masukkan dimensi: ")
# # d = int(input())

lll = createDots(n,3)
lll.sort()
# printList(lll)
# print("")

startb = time.time()
a = findMinBruteForce(lll)[0]
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